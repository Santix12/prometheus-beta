"""
Utility function to get the size of a given file.

This module provides a function to retrieve the size of a file in bytes,
with error handling for common file-related issues.
"""

import os


def get_file_size(file_path):
    """
    Get the size of a file in bytes.

    Args:
        file_path (str): Path to the file whose size is to be determined.

    Returns:
        int: Size of the file in bytes.

    Raises:
        FileNotFoundError: If the specified file does not exist.
        PermissionError: If there are insufficient permissions to access the file.
        IsADirectoryError: If the path points to a directory instead of a file.
    """
    # Normalize the path to handle potential relative paths
    normalized_path = os.path.normpath(file_path)

    # Check if the path exists
    if not os.path.exists(normalized_path):
        raise FileNotFoundError(f"The file {file_path} does not exist.")

    # Check if it's a file (not a directory)
    if not os.path.isfile(normalized_path):
        raise IsADirectoryError(f"The path {file_path} is not a file.")

    # Get and return the file size
    return os.path.getsize(normalized_path)