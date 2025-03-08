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
    
    Time Complexity: O(m + log(n)), where m is number of rows, n is number of columns
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
    
    # Use a more efficient search algorithm
    m, n = len(matrix), len(matrix[0])
    
    # Start from top-right corner
    row, col = 0, n - 1
    
    while row < m and col >= 0:
        current = matrix[row][col]
        
        if current == target:
            return True
        
        # If current is less than target, move down
        if current < target:
            row += 1
        # If current is greater than target, move left
        else:
            col -= 1
    
    return False