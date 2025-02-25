def find_max_subarray(arr):
    """
    Find the maximum sum of a contiguous subarray within a one-dimensional array of integers.
    
    This function uses Kadane's algorithm to efficiently find the subarray with the largest sum.
    Works with arrays containing positive and negative integers.
    
    Args:
        arr (list): A list of integers
    
    Returns:
        int: The maximum sum of any contiguous subarray
    
    Raises:
        TypeError: If input is not a list or contains non-numeric elements
        ValueError: If the input list is empty
    
    Time Complexity: O(n)
    Space Complexity: O(1)
    
    Examples:
        >>> find_max_subarray([1, -2, 3, 4, -1, 5])
        11
        >>> find_max_subarray([-1, -2, -3, -4])
        -1
    """
    # Input validation
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    if not arr:
        raise ValueError("Input list cannot be empty")
    
    # Check for non-numeric elements
    if not all(isinstance(x, (int, float)) for x in arr):
        raise TypeError("All elements must be numeric")
    
    # Kadane's algorithm
    max_so_far = float('-inf')
    max_ending_here = 0
    
    for num in arr:
        max_ending_here = max(num, max_ending_here + num)
        max_so_far = max(max_so_far, max_ending_here)
    
    return max_so_far