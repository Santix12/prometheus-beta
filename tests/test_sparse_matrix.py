"""
Tests for sparse matrix multiplication implementation.
"""

import pytest
from src.sparse_matrix import sparse_matrix_multiply

def test_basic_multiplication():
    """Test basic sparse matrix multiplication."""
    # Matrix A: 2x3 sparse matrix
    # [1 0 2]
    # [0 3 0]
    matrix_a = {
        0: {0: 1, 2: 2},
        1: {1: 3}
    }
    
    # Matrix B: 3x2 sparse matrix
    # [1 2]
    # [0 3]
    # [4 0]
    matrix_b = {
        0: {0: 1, 1: 2},
        1: {1: 3},
        2: {0: 4}
    }
    
    # Expected result: 2x2 sparse matrix
    # [1*1 + 2*4   1*2 + 2*0]
    # [3*0         3*3      ]
    expected = {
        0: {0: 9, 1: 2},
        1: {1: 9}
    }
    
    assert sparse_matrix_multiply(matrix_a, matrix_b) == expected

def test_empty_matrices():
    """Test multiplication with empty matrices."""
    # Empty matrix A
    matrix_a = {}
    matrix_b = {0: {0: 1, 1: 2}}
    
    assert sparse_matrix_multiply(matrix_a, matrix_b) == {}
    assert sparse_matrix_multiply(matrix_b, matrix_a) == {}

def test_zero_matrices():
    """Test multiplication with zero matrices."""
    matrix_a = {0: {0: 0}, 1: {1: 0}}
    matrix_b = {0: {0: 1}, 1: {1: 1}}
    
    assert sparse_matrix_multiply(matrix_a, matrix_b) == {}

def test_invalid_input_types():
    """Test error handling for invalid input types."""
    with pytest.raises(ValueError):
        sparse_matrix_multiply([], {})
    
    with pytest.raises(ValueError):
        sparse_matrix_multiply({}, [])

def test_large_sparse_matrix():
    """Test multiplication with a larger sparse matrix."""
    # Large sparse matrix with mostly zero entries
    matrix_a = {
        0: {0: 1, 100: 5},
        50: {25: 3, 75: 7},
        100: {0: 2, 50: 4}
    }
    
    matrix_b = {
        0: {0: 2, 50: 3},
        25: {0: 1, 100: 6},
        50: {25: 4, 75: 8},
        100: {0: 5, 50: 9}
    }
    
    # Manually computed expected result
    expected = {
        0: {0: 2, 50: 3, 100: 25},
        50: {0: 3, 25: 12, 50: 28, 75: 56},
        100: {0: 10, 25: 4, 50: 36}
    }
    
    assert sparse_matrix_multiply(matrix_a, matrix_b) == expected