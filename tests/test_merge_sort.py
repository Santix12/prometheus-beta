import pytest
from src.merge_sort import merge_sort

def test_merge_sort_empty_list():
    """Test sorting an empty list."""
    assert merge_sort([]) == []

def test_merge_sort_single_element():
    """Test sorting a list with a single element."""
    assert merge_sort([5]) == [5]

def test_merge_sort_sorted_list():
    """Test sorting an already sorted list."""
    input_list = [1, 2, 3, 4, 5]
    assert merge_sort(input_list) == input_list

def test_merge_sort_reverse_sorted_list():
    """Test sorting a reverse-sorted list."""
    input_list = [5, 4, 3, 2, 1]
    assert merge_sort(input_list) == [1, 2, 3, 4, 5]

def test_merge_sort_unsorted_list():
    """Test sorting a random unsorted list."""
    input_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    assert merge_sort(input_list) == [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]

def test_merge_sort_with_duplicates():
    """Test sorting a list with duplicate values."""
    input_list = [3, 3, 3, 1, 1, 4, 4, 2, 2]
    assert merge_sort(input_list) == [1, 1, 2, 2, 3, 3, 3, 4, 4]

def test_merge_sort_with_negative_numbers():
    """Test sorting a list with negative numbers."""
    input_list = [-3, 0, -1, 5, -2, 4]
    assert merge_sort(input_list) == [-3, -2, -1, 0, 4, 5]

def test_merge_sort_with_floats():
    """Test sorting a list with floating-point numbers."""
    input_list = [3.14, 2.71, 1.41, 0.58]
    assert merge_sort(input_list) == [0.58, 1.41, 2.71, 3.14]

def test_merge_sort_non_list_input():
    """Test that a TypeError is raised for non-list input."""
    with pytest.raises(TypeError, match="Input must be a list"):
        merge_sort("not a list")
        merge_sort(123)
        merge_sort(None)

def test_merge_sort_original_list_unchanged():
    """Test that the original list remains unchanged."""
    input_list = [3, 1, 4, 1, 5, 9, 2, 6]
    original_copy = input_list.copy()
    merge_sort(input_list)
    assert input_list == original_copy