def sum_unique_elements(arr):
    """
    Calculate the sum of unique elements in the given array.
    
    Args:
        arr (list): A list of integers
    
    Returns:
        int: Sum of unique elements in the array
    
    Time Complexity: O(n)
    Space Complexity: O(n)
    
    Raises:
        TypeError: If input is not a list
        TypeError: If list contains non-integer elements
    """
    # Check if input is a list
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Check if all elements are integers
    if not all(isinstance(x, int) for x in arr):
        raise TypeError("All elements must be integers")
    
    # Use a set to track unique elements efficiently
    unique_elements = set()
    unique_sum = 0
    
    # Single pass through the array
    for num in arr:
        # If this is the first time seeing the number, add to sum
        # and mark as seen in the set
        if num not in unique_elements:
            unique_sum += num
            unique_elements.add(num)
    
    return unique_sum