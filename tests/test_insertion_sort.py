import pytest
from src.insertion_sort import insertion_sort

def test_empty_list():
    """Test sorting an empty list."""
    assert insertion_sort([]) == []

def test_single_element_list():
    """Test sorting a list with a single element."""
    assert insertion_sort([42]) == [42]

def test_already_sorted_list():
    """Test sorting a list that is already sorted."""
    input_list = [1, 2, 3, 4, 5]
    assert insertion_sort(input_list) == [1, 2, 3, 4, 5]

def test_reverse_sorted_list():
    """Test sorting a list in reverse order."""
    input_list = [5, 4, 3, 2, 1]
    assert insertion_sort(input_list) == [1, 2, 3, 4, 5]

def test_list_with_duplicates():
    """Test sorting a list with duplicate elements."""
    input_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
    assert insertion_sort(input_list) == [1, 1, 2, 3, 3, 4, 5, 5, 6, 9]

def test_list_with_negative_numbers():
    """Test sorting a list with negative numbers."""
    input_list = [-3, 4, -1, 7, -5, 2]
    assert insertion_sort(input_list) == [-5, -3, -1, 2, 4, 7]

def test_list_with_floating_point_numbers():
    """Test sorting a list with floating-point numbers."""
    input_list = [3.14, 2.71, 1.41, 0.58]
    assert insertion_sort(input_list) == [0.58, 1.41, 2.71, 3.14]

def test_invalid_input_type():
    """Test that a TypeError is raised for non-list input."""
    with pytest.raises(TypeError, match="Input must be a list"):
        insertion_sort("not a list")

def test_list_with_uncomparable_types():
    """Test that a TypeError is raised for list with uncomparable types."""
    with pytest.raises(TypeError):
        insertion_sort([1, 'a', None])