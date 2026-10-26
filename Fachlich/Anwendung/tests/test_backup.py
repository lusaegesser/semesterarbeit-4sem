import json
import sqlite3
import zipfile
from pathlib import Path
import pytest
from scripts.archive_backup import create, restore, verify


def source(tmp_path):
    directory = tmp_path / 'source'
    (directory / 'uploads').mkdir(parents=True)
    with sqlite3.connect(directory / 'archive.db') as db:
        db.execute('CREATE TABLE tracks(id INTEGER PRIMARY KEY, audio_file TEXT)')
        db.execute("INSERT INTO tracks VALUES(1, 'uploads/example.wav')")
        db.execute('CREATE TABLE comments(id INTEGER PRIMARY KEY, body TEXT)')
        db.execute("INSERT INTO comments VALUES(1, 'Test feedback')")
    (directory / 'uploads/example.wav').write_bytes(b'RIFF-test-audio')
    (directory / 'admin-password.hash').write_text('test-password-hash')
    return directory


def test_backup_roundtrip_and_existing_destination(tmp_path):
    original = source(tmp_path)
    backup = tmp_path / 'backup.zip'
    manifest = create(original, backup)
    assert manifest == verify(backup)
    restored = tmp_path / 'restored'
    assert restore(backup, restored) == manifest
    assert (restored / 'uploads/example.wav').read_bytes() == b'RIFF-test-audio'
    assert (restored / 'admin-password.hash').read_text() == 'test-password-hash'
    with pytest.raises(ValueError, match='leeres'):
        restore(backup, original)
    with pytest.raises(ValueError, match='existiert'):
        create(original, backup)


def test_missing_audio_prevents_backup(tmp_path):
    original = source(tmp_path)
    (original / 'uploads/example.wav').unlink()
    with pytest.raises(ValueError, match='Audiodatei'):
        create(original, tmp_path / 'missing.zip')


def test_corrupt_content_not_restored(tmp_path):
    original = source(tmp_path)
    archive = tmp_path / 'good.zip'
    create(original, archive)
    corrupted = tmp_path / 'corrupted.zip'
    with zipfile.ZipFile(archive) as src, zipfile.ZipFile(corrupted, 'w') as dst:
        for name in src.namelist():
            data = src.read(name)
            if name == 'uploads/example.wav':
                data = b'X' * len(data)
            dst.writestr(name, data)
    destination = tmp_path / 'target'
    with pytest.raises(ValueError, match='Pruefsumme'):
        restore(corrupted, destination)
    assert not destination.exists()


def test_unsafe_paths_rejected(tmp_path):
    original = source(tmp_path)
    archive = tmp_path / 'good.zip'
    create(original, archive)
    bad = tmp_path / 'bad.zip'
    with zipfile.ZipFile(archive) as src, zipfile.ZipFile(bad, 'w') as dst:
        manifest = json.loads(src.read('manifest.json'))
        manifest['files']['../escape'] = manifest['files'].pop('uploads/example.wav')
        for name in src.namelist():
            if name == 'manifest.json':
                dst.writestr(name, json.dumps(manifest))
            else:
                dst.writestr('../escape' if name == 'uploads/example.wav' else name, src.read(name))
    with pytest.raises(ValueError, match='Archivpfad'):
        verify(bad)
    assert not (tmp_path / 'escape').exists()


def test_existing_partial_not_deleted(tmp_path):
    original = source(tmp_path)
    archive = tmp_path / 'backup.zip'
    partial = tmp_path / 'backup.zip.partial'
    partial.write_bytes(b'keep this earlier partial backup')
    with pytest.raises(ValueError, match='Unvollstaendige'):
        create(original, archive)
    assert partial.read_bytes() == b'keep this earlier partial backup'
