"""Offline SQLite/media backups. Stop the application before creating a backup."""
import argparse
import hashlib
import json
import os
import shutil
import sqlite3
import tempfile
import zipfile
from contextlib import closing
from datetime import datetime, timezone
from pathlib import Path, PurePosixPath


def digest(path):
    with path.open('rb') as stream:
        return hashlib.file_digest(stream, 'sha256').hexdigest()


def safe_name(name):
    parts = PurePosixPath(name).parts
    return (name in {'archive.db', 'admin-password.hash'} or
            (len(parts) == 2 and parts[0] == 'uploads' and parts[1] not in {'.', '..'})) and '\\' not in name and ':' not in name


def inspect_data(directory):
    database = directory / 'archive.db'
    if not database.is_file():
        raise ValueError('archive.db fehlt')
    with closing(sqlite3.connect(database.resolve().as_uri() + '?mode=ro', uri=True)) as db:
        if db.execute('PRAGMA integrity_check').fetchone()[0] != 'ok':
            raise ValueError('SQLite-Integritaetspruefung fehlgeschlagen')
        counts = {}
        for table in ('tracks', 'comments', 'shares', 'admin_sessions'):
            exists = db.execute("SELECT 1 FROM sqlite_master WHERE type='table' AND name=?", (table,)).fetchone()
            counts[table] = db.execute(f'SELECT COUNT(*) FROM {table}').fetchone()[0] if exists else 0
        if db.execute("SELECT 1 FROM sqlite_master WHERE type='table' AND name='tracks'").fetchone():
            for (name,) in db.execute('SELECT audio_file FROM tracks WHERE audio_file IS NOT NULL'):
                if not safe_name(name) or not name.startswith('uploads/') or not (directory / name).is_file():
                    raise ValueError('Eine in der Datenbank referenzierte Audiodatei fehlt oder ist ungueltig')
    return counts


def create(data_dir, archive):
    if archive.exists():
        raise ValueError('Zieldatei existiert bereits')
    counts = inspect_data(data_dir)
    files = [data_dir / 'archive.db']
    if (data_dir / 'admin-password.hash').exists():
        files.append(data_dir / 'admin-password.hash')
    files += sorted((data_dir / 'uploads').glob('*'))
    if any(path.is_symlink() or not path.is_file() for path in files):
        raise ValueError('Nur regulaere Dateien werden gesichert')
    archive.parent.mkdir(parents=True, exist_ok=True)
    # Snapshot SQLite via its backup API, even though writes are stopped.
    with tempfile.TemporaryDirectory(prefix='archive-snapshot-') as temporary:
        snapshot = Path(temporary) / 'archive.db'
        with closing(sqlite3.connect((data_dir / 'archive.db').resolve().as_uri() + '?mode=ro', uri=True)) as source:
            with closing(sqlite3.connect(snapshot)) as target:
                source.backup(target)
        manifest = {'version': 1, 'created_at': datetime.now(timezone.utc).isoformat(), 'counts': counts, 'files': {}}
        partial = archive.with_name(archive.name + '.partial')
        if partial.exists():
            raise ValueError('Unvollstaendige Sicherung existiert bereits; nicht ueberschreiben')
        try:
            with zipfile.ZipFile(partial, 'x', compression=zipfile.ZIP_STORED) as bundle:
                for path in files:
                    name = path.relative_to(data_dir).as_posix()
                    if not safe_name(name):
                        raise ValueError('Nicht unterstuetzter Dateiname')
                    source = snapshot if name == 'archive.db' else path
                    manifest['files'][name] = {'sha256': digest(source), 'size': source.stat().st_size}
                    bundle.write(source, name)
                bundle.writestr('manifest.json', json.dumps(manifest, indent=2))
            partial.rename(archive)
        except Exception:
            # Only remove our newly-created incomplete archive.
            if partial.exists():
                partial.unlink()
            raise
    return manifest


def unpack_verified(archive, destination):
    with zipfile.ZipFile(archive) as bundle:
        names = bundle.namelist()
        if len(names) != len(set(names)) or 'manifest.json' not in names:
            raise ValueError('Ungueltige oder doppelte Archiveintraege')
        if bundle.getinfo('manifest.json').file_size > 4 * 1024 * 1024:
            raise ValueError('Manifest zu gross')
        manifest = json.loads(bundle.read('manifest.json'))
        if manifest.get('version') != 1 or 'archive.db' not in manifest.get('files', {}):
            raise ValueError('Unbekanntes Sicherungsformat')
        if set(names) != set(manifest['files']) | {'manifest.json'}:
            raise ValueError('Archiv und Manifest stimmen nicht ueberein')
        for name, expected in manifest['files'].items():
            if not safe_name(name):
                raise ValueError('Unsicherer Archivpfad')
            info = bundle.getinfo(name)
            if info.file_size != expected['size'] or (info.external_attr >> 16) & 0o170000 == 0o120000:
                raise ValueError('Ungueltige Dateigroesse oder symbolischer Link')
            target = destination / name
            target.parent.mkdir(parents=True, exist_ok=True)
            with bundle.open(name) as source, target.open('xb') as output:
                shutil.copyfileobj(source, output, length=1024 * 1024)
            if digest(target) != expected['sha256']:
                raise ValueError('Pruefsumme stimmt nicht ueberein')
    if inspect_data(destination) != manifest['counts']:
        raise ValueError('Datensatzanzahlen stimmen nicht ueberein')
    return manifest


def verify(archive):
    with tempfile.TemporaryDirectory(prefix='archive-verify-') as temporary:
        return unpack_verified(archive, Path(temporary))


def restore(archive, target, uid=None, gid=None):
    if target.is_symlink() or (target.exists() and any(target.iterdir())):
        raise ValueError('Wiederherstellung nur in ein leeres neues Verzeichnis')
    with tempfile.TemporaryDirectory(prefix='archive-restore-') as temporary:
        staging = Path(temporary)
        manifest = unpack_verified(archive, staging)
        target.mkdir(parents=True, exist_ok=True)
        shutil.copytree(staging, target, dirs_exist_ok=True)
        (target / 'uploads').mkdir(exist_ok=True)
        if uid is not None and gid is not None:
            for path in [target, *target.rglob('*')]:
                os.chown(path, uid, gid)
        return manifest


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('action', choices=['create', 'verify', 'restore'])
    parser.add_argument('--archive', type=Path, required=True)
    parser.add_argument('--data-dir', type=Path, default=Path('/app/data'))
    parser.add_argument('--uid', type=int)
    parser.add_argument('--gid', type=int)
    args = parser.parse_args()
    if args.action == 'create':
        result = create(args.data_dir, args.archive)
    elif args.action == 'verify':
        result = verify(args.archive)
    else:
        result = restore(args.archive, args.data_dir, args.uid, args.gid)
    print(json.dumps({'action': args.action, 'files': len(result['files']), 'counts': result['counts']}))


if __name__ == '__main__':
    main()
