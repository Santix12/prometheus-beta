"""
Test suite for the file_size utility function.
"""

import os
import pytest
import tempfile

from src.file_size import get_file_size


def test_get_file_size_normal_file():
    """Test getting size of a normal file."""
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        temp_file.write(b'Hello, World!')
        temp_file.close()
        
        try:
            file_size = get_file_size(temp_file.name)
            assert file_size == 13  # Length of 'Hello, World!'
        finally:
            os.unlink(temp_file.name)


def test_get_file_size_empty_file():
    """Test getting size of an empty file."""
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        temp_file.close()
        
        try:
            file_size = get_file_size(temp_file.name)
            assert file_size == 0
        finally:
            os.unlink(temp_file.name)


def test_get_file_size_non_existent_file():
    """Test that FileNotFoundError is raised for non-existent file."""
    with pytest.raises(FileNotFoundError):
        get_file_size('/path/to/non/existent/file.txt')


def test_get_file_size_directory():
    """Test that IsADirectoryError is raised when path is a directory."""
    with pytest.raises(IsADirectoryError):
        get_file_size(os.path.dirname(os.path.abspath(__file__)))


def test_get_file_size_relative_path():
    """Test getting file size using a relative path."""
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        temp_file.write(b'Relative Path Test')
        temp_file.close()
        
        try:
            # Create a relative path
            relative_path = os.path.relpath(temp_file.name)
            file_size = get_file_size(relative_path)
            assert file_size == 18  # Length of 'Relative Path Test'
        finally:
            os.unlink(temp_file.name)