from pathlib import Path
import sys

# Ensure the package root is on the import path
sys.path.append(str(Path(__file__).resolve().parents[1]))

import organiser

def test_organise_directory(tmp_path):
    # create files with different extensions
    files = {
        'image.jpg': 'images',
        'doc.pdf': 'documents',
        'song.mp3': 'audio',
        'video.mp4': 'video',
        'archive.zip': 'archives',
        'script.py': 'code',
        'note.xyz': 'other',
    }
    for name in files:
        (tmp_path / name).write_text('data')

    organiser.organise_directory(tmp_path)

    for name, folder in files.items():
        expected = tmp_path / folder / name
        assert expected.exists(), f"{name} should be in {folder}"
