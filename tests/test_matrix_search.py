import pytest
from src.matrix_search import search_matrix

def test_matrix_search_basic_success():
    """Test finding an existing element in a matrix"""
    matrix = [
        [1, 3, 5, 7],
        [10, 11, 16, 20],
        [23, 30, 34, 60]
    ]
    assert search_matrix(matrix, 3) == True
    assert search_matrix(matrix, 60) == True
    assert search_matrix(matrix, 13) == False

def test_matrix_search_edge_cases():
    """Test various edge cases"""
    # Empty matrix
    assert search_matrix([], 5) == False
    
    # Matrix with empty rows
    assert search_matrix([[], []], 5) == False
    
    # Single element matrix
    assert search_matrix([[1]], 1) == True
    assert search_matrix([[1]], 2) == False

def test_matrix_search_invalid_input():
    """Test invalid input handling"""
    # Non-list input
    assert search_matrix(None, 5) == False
    
    # Matrix with non-list rows
    with pytest.raises(TypeError):
        search_matrix([1, 2, 3], 5)
    
    with pytest.raises(TypeError):
        search_matrix([[1], 2, [3]], 5)

def test_matrix_search_large_matrix():
    """Test search in a larger matrix"""
    matrix = [
        [1, 4, 7, 11, 15],
        [2, 5, 8, 12, 19],
        [3, 6, 9, 16, 22],
        [10, 13, 14, 17, 24],
        [18, 21, 23, 26, 30]
    ]
    
    # Check targets at various positions
    assert search_matrix(matrix, 5) == True
    assert search_matrix(matrix, 20) == False
    assert search_matrix(matrix, 15) == True
    assert search_matrix(matrix, 30) == True
    assert search_matrix(matrix, 0) == False

def test_matrix_search_performance():
    """Test performance with a larger matrix"""
    matrix = [[i * j for j in range(1, 101)] for i in range(1, 101)]
    
    # Verify both existing and non-existing elements
    assert search_matrix(matrix, 42 * 17) == True
    assert search_matrix(matrix, 100001) == False  # A number definitely not in the matrix