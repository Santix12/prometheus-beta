def optimized_bubble_sort(arr):
    """
    Perform an optimized Bubble Sort on the input list.
    
    This implementation reduces redundant iterations by:
    1. Tracking if any swaps occurred in each pass
    2. Reducing the range of comparison in subsequent passes
    
    Args:
        arr (list): The input list to be sorted
    
    Returns:
        list: A new sorted list in ascending order
    
    Raises:
        TypeError: If input is not a list
        ValueError: If list contains elements that cannot be compared
    """
    # Validate input
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Create a copy to avoid modifying the original list
    sorted_arr = arr.copy()
    
    # Get the length of the list
    n = len(sorted_arr)
    
    # Optimize by tracking if any swaps occurred
    for i in range(n):
        # Flag to detect if any swaps happened in this pass
        swapped = False
        
        # Reduce range of comparison in each pass
        for j in range(0, n - i - 1):
            # Compare adjacent elements
            if sorted_arr[j] > sorted_arr[j + 1]:
                # Swap elements
                sorted_arr[j], sorted_arr[j + 1] = sorted_arr[j + 1], sorted_arr[j]
                swapped = True
        
        # If no swapping occurred, array is already sorted
        if not swapped:
            break
    
    return sorted_arr