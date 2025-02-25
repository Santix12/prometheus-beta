import pytest
from src.max_subarray import find_max_subarray

def test_positive_numbers():
    """Test with an array of positive numbers"""
    assert find_max_subarray([1, 2, 3, 4]) == 10

def test_mixed_numbers():
    """Test with mixed positive and negative numbers"""
    assert find_max_subarray([1, -2, 3, 4, -1, 5]) == 11

def test_all_negative_numbers():
    """Test with an array of all negative numbers"""
    assert find_max_subarray([-1, -2, -3, -4]) == -1

def test_single_element():
    """Test with a single element array"""
    assert find_max_subarray([42]) == 42

def test_zero_sum():
    """Test with an array that sums to zero"""
    assert find_max_subarray([1, -1, 2, -2]) == 2

def test_invalid_input_empty_list():
    """Test that empty list raises ValueError"""
    with pytest.raises(ValueError, match="Input list cannot be empty"):
        find_max_subarray([])

def test_invalid_input_not_a_list():
    """Test that non-list input raises TypeError"""
    with pytest.raises(TypeError, match="Input must be a list"):
        find_max_subarray("not a list")

def test_invalid_input_non_numeric():
    """Test that list with non-numeric elements raises TypeError"""
    with pytest.raises(TypeError, match="All elements must be numeric"):
        find_max_subarray([1, 2, "three", 4])

def test_floating_point_numbers():
    """Test that the function works with floating point numbers"""
    result = find_max_subarray([1.5, -2.5, 3.5, 4.5])
    assert abs(result - 8.0) < 1e-10  # Use approximate comparison for floating point