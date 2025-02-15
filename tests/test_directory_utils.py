import os
import pytest
import tempfile

from src.directory_utils import is_directory_exists

def test_is_directory_exists_valid_directory():
    """Test that existing directory returns True."""
    with tempfile.TemporaryDirectory() as temp_dir:
        assert is_directory_exists(temp_dir) is True

def test_is_directory_exists_nonexistent_directory():
    """Test that nonexistent directory returns False."""
    assert is_directory_exists('/path/to/nonexistent/directory') is False

def test_is_directory_exists_file_instead_of_directory():
    """Test that a file path returns False."""
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        try:
            assert is_directory_exists(temp_file.name) is False
        finally:
            os.unlink(temp_file.name)

def test_is_directory_exists_empty_string():
    """Test empty string path."""
    assert is_directory_exists('') is False

def test_is_directory_exists_none_input():
    """Test None input."""
    with pytest.raises(TypeError):
        is_directory_exists(None)