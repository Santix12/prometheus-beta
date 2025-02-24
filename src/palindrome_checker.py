def is_palindrome(nums):
    """
    Determine if a list of integers is a palindrome.
    
    A palindrome is a sequence that reads the same backward as forward.
    
    Args:
        nums (list): A list of integers to check.
    
    Returns:
        bool: True if the list is a palindrome, False otherwise.
    
    Raises:
        TypeError: If the input is not a list.
    
    Examples:
        >>> is_palindrome([1, 2, 1])
        True
        >>> is_palindrome([1, 2, 3])
        False
        >>> is_palindrome([])
        True
    """
    # Check if input is a list
    if not isinstance(nums, list):
        raise TypeError("Input must be a list")
    
    # Empty list or list with single element is always a palindrome
    if len(nums) <= 1:
        return True
    
    # Compare elements from start and end moving inwards
    left, right = 0, len(nums) - 1
    while left < right:
        if nums[left] != nums[right]:
            return False
        left += 1
        right -= 1
    
    return True