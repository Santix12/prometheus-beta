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
    
    # Compute expected result using the actual multiplication logic
    result = sparse_matrix_multiply(matrix_a, matrix_b)
    
    # Check the structure of the expected result
    assert 0 in result
    assert 50 in result
    assert 100 in result
    
    # Verify non-zero entries
    assert result[0][0] == 27
    assert result[0][50] == 48
    
    assert result[50][0] == 3
    assert result[50][100] == 18
    
    assert result[100][0] == 4
    assert result[100][25] == 16
    assert result[100][50] == 6
    assert result[100][75] == 32