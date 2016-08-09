#!/usb/bin/env python3

import os
from pathlib import Path

def scan_dir_gen(dir_path):
    """Scan directory recursively and yield all files and directories.

    Args:
        dir_path: Path object to be scanned.
    """
    if dir_path is None or not isinstance(dir_path, Path):
        raise TypeError('dir_path must be a Path object')

    # The current directory.
    yield dir_path
    for path in dir_path.iterdir():
        if path.is_dir():
            # Recursively tranverse the directory.
            yield from scan_dir_gen(path)
        else:
            yield path

def dir_only_has_files_gen(dir_path):
    """Scan the directory recursively and returns directories which contain only files.

    Args:
        dir_path: Path object to be scanned.
    """
    if dir_path is None or not isinstance(dir_path, Path):
        raise TypeError('dir_path must be a Path object')

    has_dir = False
    for path in dir_path.iterdir():
        if path.is_dir():
            has_dir = True
            yield from dir_only_has_files_gen(path)
    if not has_dir:
        yield dir_path


# Run test cases with pytest.
def test_scan_dir_gen():
    dir_path = Path('.')
    for path in scan_dir_gen(dir_path):
        print(path)

def test_dir_only_has_files_gen():
    dir_path = Path('..')
    for path in dir_only_has_files_gen(dir_path):
        print(path)
