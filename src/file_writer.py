"""
Module for writing strings to text files.

This module provides a utility function to write a string to a text file 
with error handling and optional mode selection.
"""

def write_string_to_file(file_path: str, content: str, mode: str = 'w') -> None:
    """
    Write a string to a text file.

    Args:
        file_path (str): The path to the file where the string will be written.
        content (str): The string content to write to the file.
        mode (str, optional): File open mode. Defaults to 'w' (write).
            'w' - write (overwrite existing content)
            'a' - append to existing content
            'x' - create a new file (fail if file exists)

    Raises:
        TypeError: If file_path or content is not a string.
        ValueError: If mode is not one of 'w', 'a', or 'x'.
        PermissionError: If the file cannot be written due to permissions.
        IOError: For other file-related errors.
    """
    # Validate input types
    if not isinstance(file_path, str):
        raise TypeError("file_path must be a string")
    if not isinstance(content, str):
        raise TypeError("content must be a string")
    
    # Validate mode
    if mode not in ['w', 'a', 'x']:
        raise ValueError("mode must be one of 'w', 'a', or 'x'")
    
    # Write to file
    try:
        with open(file_path, mode, encoding='utf-8') as file:
            file.write(content)
    except PermissionError:
        raise PermissionError(f"Permission denied when trying to write to {file_path}")
    except IOError as e:
        raise IOError(f"Error writing to file {file_path}: {str(e)}")