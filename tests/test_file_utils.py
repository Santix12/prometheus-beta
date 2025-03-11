import os
import pytest
import tempfile
import shutil

from src.file_utils import find_largest_file

def test_find_largest_file_basic():
    """Test finding the largest file in a directory."""
    with tempfile.TemporaryDirectory() as tmpdir:
        # Create files with different sizes
        with open(os.path.join(tmpdir, 'small.txt'), 'w') as f:
            f.write('small')
        
        with open(os.path.join(tmpdir, 'large.txt'), 'w') as f:
            f.write('large' * 100)
        
        result = find_largest_file(tmpdir)
        assert result is not None
        assert os.path.basename(result) == 'large.txt'

def test_find_largest_file_empty_directory():
    """Test behavior with an empty directory."""
    with tempfile.TemporaryDirectory() as tmpdir:
        result = find_largest_file(tmpdir)
        assert result is None

def test_find_largest_file_nonexistent_directory():
    """Test behavior with a nonexistent directory."""
    result = find_largest_file('/path/that/does/not/exist')
    assert result is None

def test_find_largest_file_file_instead_of_directory():
    """Test behavior when a file is passed instead of a directory."""
    with tempfile.NamedTemporaryFile() as tmpfile:
        with pytest.raises(ValueError):
            find_largest_file(tmpfile.name)

def test_find_largest_file_multiple_files():
    """Test finding the largest file when multiple files exist."""
    with tempfile.TemporaryDirectory() as tmpdir:
        # Create multiple files of varying sizes
        files = [
            ('small1.txt', 'small'),
            ('medium.txt', 'medium' * 50),
            ('large.txt', 'large' * 100),
            ('small2.txt', 'tiny')
        ]
        
        for filename, content in files:
            with open(os.path.join(tmpdir, filename), 'w') as f:
                f.write(content)
        
        result = find_largest_file(tmpdir)
        assert result is not None
        assert os.path.basename(result) == 'large.txt'

def test_find_largest_file_handles_subdirectories():
    """Test that subdirectories are not considered."""
    with tempfile.TemporaryDirectory() as tmpdir:
        # Create a file and a subdirectory
        with open(os.path.join(tmpdir, 'file.txt'), 'w') as f:
            f.write('content')
        
        os.mkdir(os.path.join(tmpdir, 'subdir'))
        with open(os.path.join(tmpdir, 'subdir', 'bigfile.txt'), 'w') as f:
            f.write('big' * 1000)
        
        result = find_largest_file(tmpdir)
        assert result is not None
        assert os.path.basename(result) == 'file.txt'