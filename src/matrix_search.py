def search_matrix(matrix: list[list[int]], target: int) -> bool:
    """
    Search for a target integer in an M x N matrix.
    
    The matrix is assumed to be sorted in ascending order from left to right 
    and top to bottom for an efficient search.
    
    Args:
        matrix (list[list[int]]): A 2D matrix of integers
        target (int): The integer to search for in the matrix
    
    Returns:
        bool: True if the target exists in the matrix, False otherwise
    
    Raises:
        TypeError: If matrix is not a list or contains non-list elements
        ValueError: If the matrix is empty or contains empty rows
    
    Time Complexity: O(m * log(n)), where m is number of rows, n is number of columns
    Space Complexity: O(1)
    """
    # Check for invalid input
    if not matrix or not isinstance(matrix, list):
        return False
    
    # Check if all rows are valid lists
    if not all(isinstance(row, list) for row in matrix):
        raise TypeError("Matrix must be a list of lists")
    
    # Check for empty matrix or rows
    if len(matrix) == 0 or len(matrix[0]) == 0:
        return False
    
    # Perform binary search on each row
    for row in matrix:
        # Validate row
        if not isinstance(row, list):
            raise TypeError("Each row must be a list")
        
        # Binary search within the row
        left, right = 0, len(row) - 1
        while left <= right:
            mid = (left + right) // 2
            mid_value = row[mid]
            
            if mid_value == target:
                return True
            elif mid_value < target:
                left = mid + 1
            else:
                right = mid - 1
    
    return False