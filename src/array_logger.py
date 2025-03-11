from typing import List, Union, Any
from tabulate import tabulate

def log_array_as_table(arr: List[Union[List[Any], dict]], headers: List[str] = None) -> str:
    """
    Convert an array to a formatted table string.

    Args:
        arr (List[Union[List[Any], dict]]): The array to be logged. 
            Can be a list of lists or a list of dictionaries.
        headers (List[str], optional): Custom headers for the table. 
            If not provided, will attempt to use dictionary keys or default headers.

    Returns:
        str: A formatted table representation of the input array.

    Raises:
        ValueError: If the input array is empty or contains inconsistent data.
        TypeError: If input is not a list or contains invalid data types.

    Examples:
        >>> log_array_as_table([[1, 2, 3], [4, 5, 6]])
        >>> log_array_as_table([{'name': 'Alice', 'age': 30}, {'name': 'Bob', 'age': 25}])
    """
    # Validate input
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    if not arr:
        raise ValueError("Input array cannot be empty")
    
    # Handle empty list case
    if len(arr) == 0:
        return "Empty table"
    
    # Handle list of dictionaries
    if isinstance(arr[0], dict):
        # If no headers provided, use dictionary keys
        if headers is None:
            # Get all unique keys, maintaining order of first occurrence
            headers = []
            for item in arr:
                for key in item.keys():
                    if key not in headers:
                        headers.append(key)
        
        # Convert dict to list of lists
        table_data = []
        for item in arr:
            row = [item.get(header, None) for header in headers]
            table_data.append(row)
    
    # Handle list of lists
    elif isinstance(arr[0], list):
        table_data = arr
        
        # If no headers provided, generate default headers
        if headers is None:
            headers = [f'Column {i+1}' for i in range(len(arr[0]))]
    
    else:
        # Handle simple list of primitives
        table_data = [[item] for item in arr]
        headers = ['Value'] if headers is None else headers
    
    # Use tabulate to create a formatted table
    return tabulate(table_data, headers=headers, tablefmt='grid')