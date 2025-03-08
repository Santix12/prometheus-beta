import pytest
from src.multi_array_manipulator import multiArrayManipulator

def test_multiply_scalar():
    arr = [[1, 2], [3, 4]]
    result = multiArrayManipulator(arr, {'multiply': 2})
    assert result == [[2, 4], [6, 8]]

def test_multiply_matrix():
    arr = [[1, 2], [3, 4]]
    mult_matrix = [[2, 0], [0, 2]]
    result = multiArrayManipulator(arr, {'multiply': mult_matrix})
    assert result == [[2, 4], [6, 8]]

def test_add_scalar():
    arr = [[1, 2], [3, 4]]
    result = multiArrayManipulator(arr, {'add': 2})
    assert result == [[3, 4], [5, 6]]

def test_add_matrix():
    arr = [[1, 2], [3, 4]]
    add_matrix = [[2, 2], [2, 2]]
    result = multiArrayManipulator(arr, {'add': add_matrix})
    assert result == [[3, 4], [5, 6]]

def test_transpose():
    arr = [[1, 2], [3, 4]]
    result = multiArrayManipulator(arr, {'transpose': True})
    assert result == [[1, 3], [2, 4]]

def test_multiple_operations():
    arr = [[1, 2], [3, 4]]
    result = multiArrayManipulator(arr, {
        'multiply': 2,
        'add': 1,
        'transpose': True
    })
    assert result == [[3, 7], [5, 9]]

def test_no_manipulations():
    arr = [[1, 2], [3, 4]]
    result = multiArrayManipulator(arr, {})
    assert result == [[1, 2], [3, 4]]

def test_matrix_multiply_incompatible_dimensions():
    arr = [[1, 2], [3, 4]]
    with pytest.raises(ValueError, match="Matrix dimensions incompatible for multiplication"):
        multiArrayManipulator(arr, {'multiply': [[1], [2], [3]]})

def test_matrix_add_incompatible_dimensions():
    arr = [[1, 2], [3, 4]]
    with pytest.raises(ValueError, match="Matrix dimensions must match for addition"):
        multiArrayManipulator(arr, {'add': [[1], [2]]})