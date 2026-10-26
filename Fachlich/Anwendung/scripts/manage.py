"""Run from Fachlich/Anwendung: python scripts/manage.py backup | restore BACKUP.zip"""
import argparse
import json
import os
import subprocess
import time
import uuid
from datetime import datetime, timezone
from pathlib import Path
from urllib.request import urlopen

ROOT = Path(__file__).resolve().parents[1]
BACKUPS = ROOT / 'backups'


def run(*args, capture=False, env=None):
    result = subprocess.run(list(args), cwd=ROOT, env=env, text=True,
                            stdout=subprocess.PIPE if capture else None, check=True, timeout=600)
    return result.stdout.strip() if capture else None


def compose(*args, **kwargs):
    return run('docker', 'compose', *args, **kwargs)


def health():
    for _ in range(40):
        try:
            with urlopen('http://127.0.0.1:8000/health', timeout=2) as response:
                if json.load(response) == {'status': 'ok'}:
                    return
        except OSError:
            pass
        time.sleep(1)
    raise RuntimeError('Neue App wurde nicht erreichbar')


def backup():
    BACKUPS.mkdir(exist_ok=True)
    filename = datetime.now(timezone.utc).strftime('archive-%Y%m%d-%H%M%S-') + uuid.uuid4().hex[:6] + '.zip'
    running = bool(compose('ps', '--status', 'running', '-q', 'app', capture=True))
    if running:
        compose('stop', 'app')
    try:
        compose('run', '--rm', '--no-deps', '-v', f'{BACKUPS.as_posix()}:/backups', 'app',
                'python', 'scripts/archive_backup.py', 'create', '--archive', '/backups/' + filename)
        compose('run', '--rm', '--no-deps', '-v', f'{BACKUPS.as_posix()}:/backups:ro', 'app',
                'python', 'scripts/archive_backup.py', 'verify', '--archive', '/backups/' + filename)
    finally:
        if running:
            compose('start', 'app')
            health()
    print('Sicherung geprueft: ' + str(BACKUPS / filename))
    return BACKUPS / filename


def restore(archive):
    archive = archive.resolve(strict=True)
    compose('build', 'app')
    config = json.loads(compose('config', '--format', 'json', capture=True))
    project = config['name']
    image = config['services']['app'].get('image', project + '-app')
    volume = project + '-restore-' + uuid.uuid4().hex[:12]
    # A brand new volume: never overwrite existing user data.
    run('docker', 'volume', 'create', volume)
    run('docker', 'run', '--rm', '--user', '0:0',
        '--mount', f'type=volume,source={volume},target=/restore',
        '--mount', f'type=bind,source={archive.as_posix()},target=/backup.zip,readonly',
        image, 'python', 'scripts/archive_backup.py', 'restore',
        '--archive', '/backup.zip', '--data-dir', '/restore', '--uid', '1000', '--gid', '1000')
    # Existing live state gets an additional backup before switching.
    if compose('ps', '--status', 'running', '-q', 'app', capture=True):
        backup()
    env_file = ROOT / '.env'
    previous = env_file.read_bytes() if env_file.exists() else None
    old_text = previous.decode('utf-8-sig') if previous else ''
    lines = [line for line in old_text.splitlines() if not line.strip().startswith(('ARCHIVE_VOLUME=', 'ARCHIVE_VOLUME_EXTERNAL='))]
    lines.extend(['ARCHIVE_VOLUME=' + volume, 'ARCHIVE_VOLUME_EXTERNAL=true'])
    compose('stop', 'app')
    try:
        env_file.write_text('\n'.join(lines) + '\n', encoding='utf-8')
        # Explicit environment overrides a caller's stale ARCHIVE_VOLUME.
        environment = dict(os.environ, ARCHIVE_VOLUME=volume, ARCHIVE_VOLUME_EXTERNAL='true')
        compose('up', '-d', '--force-recreate', 'app', env=environment)
        health()
    except Exception:
        if previous is None:
            env_file.unlink(missing_ok=True)
        else:
            env_file.write_bytes(previous)
        compose('up', '-d', '--force-recreate', 'app')
        raise
    print('Wiederherstellung aktiv. Neues Volume: ' + volume)
    print('Vorheriges Volume bleibt als Rueckfall erhalten.')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('action', choices=['backup', 'restore'])
    parser.add_argument('archive', type=Path, nargs='?')
    args = parser.parse_args()
    if args.action == 'backup':
        backup()
    elif args.archive:
        restore(args.archive)
    else:
        parser.error('restore benoetigt eine Sicherungsdatei')
