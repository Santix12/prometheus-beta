import os
from typing import Union, Optional

def find_largest_file(directory: str) -> Optional[str]:
    """
    Find the largest file in a given directory.

    Args:
        directory (str): Path to the directory to search.

    Returns:
        Optional[str]: Path to the largest file, or None if no files exist or directory is invalid.

    Raises:
        ValueError: If the provided path is not a directory.
    """
    # Validate input
    if not os.path.exists(directory):
        return None
    
    if not os.path.isdir(directory):
        raise ValueError(f"Provided path '{directory}' is not a directory")
    
    # Initialize variables
    largest_file = None
    max_size = 0
    
    # Iterate through all files in the directory
    try:
        for filename in os.listdir(directory):
            filepath = os.path.join(directory, filename)
            
            # Skip directories
            if os.path.isfile(filepath):
                try:
                    file_size = os.path.getsize(filepath)
                    if file_size > max_size:
                        max_size = file_size
                        largest_file = filepath
                except (OSError, PermissionError):
                    # Skip files that can't be accessed
                    continue
    except (PermissionError, OSError):
        # Handle cases where directory can't be read
        return None
    
    return largest_file