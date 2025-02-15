import os

def is_directory_exists(path):
    """
    Check if a given path exists and is a directory.
    
    Args:
        path (str): The path to check.
    
    Returns:
        bool: True if the path exists and is a directory, False otherwise.
    
    Raises:
        TypeError: If input is None
    """
    if path is None:
        raise TypeError("Path cannot be None")
    return os.path.isdir(path)