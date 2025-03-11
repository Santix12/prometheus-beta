import pytest
from src.array_rotation import rotate_array_left

def test_basic_rotation():
    """Test basic left rotation of an array"""
    arr = [1, 2, 3, 4, 5]
    assert rotate_array_left(arr, 2) == [3, 4, 5, 1, 2]

def test_rotation_full_array():
    """Test rotation equal to array length"""
    arr = [1, 2, 3, 4, 5]
    assert rotate_array_left(arr, 5) == [1, 2, 3, 4, 5]

def test_rotation_more_than_length():
    """Test rotation more than array length"""
    arr = [1, 2, 3, 4, 5]
    assert rotate_array_left(arr, 7) == [3, 4, 5, 1, 2]

def test_empty_array():
    """Test rotation of an empty array"""
    assert rotate_array_left([], 3) == []

def test_single_element_array():
    """Test rotation of a single-element array"""
    arr = [42]
    assert rotate_array_left(arr, 1) == [42]

def test_invalid_input_type():
    """Test handling of non-list input"""
    with pytest.raises(TypeError, match="Input must be a list"):
        rotate_array_left("not a list", 2)

def test_invalid_rotation_type():
    """Test handling of non-integer rotation amount"""
    with pytest.raises(TypeError, match="Rotation amount must be an integer"):
        rotate_array_left([1, 2, 3], "2")

def test_negative_rotation():
    """Test handling of negative rotation amount"""
    with pytest.raises(ValueError, match="Rotation amount cannot be negative"):
        rotate_array_left([1, 2, 3], -1)

def test_zero_rotation():
    """Test rotation by zero positions"""
    arr = [1, 2, 3, 4, 5]
    assert rotate_array_left(arr, 0) == [1, 2, 3, 4, 5]