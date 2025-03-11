"""
Test suite for write_string_to_file function.

This module contains comprehensive tests to verify the functionality 
of the write_string_to_file function under various scenarios.
"""

import os
import pytest
from src.file_writer import write_string_to_file

def test_write_string_to_file_default_mode(tmp_path):
    """Test writing a string to a file using default write mode."""
    file_path = str(tmp_path / "test_file.txt")
    test_content = "Hello, World!"
    
    write_string_to_file(file_path, test_content)
    
    with open(file_path, 'r', encoding='utf-8') as file:
        assert file.read() == test_content

def test_write_string_to_file_append_mode(tmp_path):
    """Test appending a string to an existing file."""
    file_path = str(tmp_path / "append_file.txt")
    
    # First write
    write_string_to_file(file_path, "First line\n")
    
    # Append
    write_string_to_file(file_path, "Second line\n", mode='a')
    
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
        assert content == "First line\nSecond line\n"

def test_write_string_to_file_exclusive_mode(tmp_path):
    """Test creating a new file in exclusive mode."""
    file_path = str(tmp_path / "exclusive_file.txt")
    
    write_string_to_file(file_path, "Exclusive content", mode='x')
    
    with open(file_path, 'r', encoding='utf-8') as file:
        assert file.read() == "Exclusive content"

def test_write_string_to_file_invalid_type_filepath():
    """Test that TypeError is raised for non-string filepath."""
    with pytest.raises(TypeError, match="file_path must be a string"):
        write_string_to_file(123, "test content")

def test_write_string_to_file_invalid_type_content():
    """Test that TypeError is raised for non-string content."""
    with pytest.raises(TypeError, match="content must be a string"):
        write_string_to_file("test.txt", 123)

def test_write_string_to_file_invalid_mode(tmp_path):
    """Test that ValueError is raised for invalid mode."""
    file_path = str(tmp_path / "invalid_mode_file.txt")
    
    with pytest.raises(ValueError, match="mode must be one of 'w', 'a', or 'x'"):
        write_string_to_file(file_path, "test", mode='invalid')

def test_write_string_to_file_existing_file_exclusive_mode(tmp_path):
    """Test that exclusive mode fails if file already exists."""
    file_path = str(tmp_path / "exclusive_existing.txt")
    
    # First creation
    write_string_to_file(file_path, "First content", mode='x')
    
    # Attempt to create again should raise FileExistsError
    with pytest.raises(FileExistsError):
        write_string_to_file(file_path, "Second content", mode='x')

def test_write_string_to_file_empty_string(tmp_path):
    """Test writing an empty string to a file."""
    file_path = str(tmp_path / "empty_file.txt")
    
    write_string_to_file(file_path, "")
    
    with open(file_path, 'r', encoding='utf-8') as file:
        assert file.read() == ""