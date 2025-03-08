import pytest
from src.bubble_sort import optimized_bubble_sort

def test_normal_list():
    """Test sorting a normal list of integers"""
    input_list = [64, 34, 25, 12, 22, 11, 90]
    expected = sorted(input_list)
    assert optimized_bubble_sort(input_list) == expected

def test_already_sorted_list():
    """Test a list that is already sorted"""
    input_list = [1, 2, 3, 4, 5]
    assert optimized_bubble_sort(input_list) == input_list

def test_reverse_sorted_list():
    """Test a list sorted in descending order"""
    input_list = [5, 4, 3, 2, 1]
    expected = sorted(input_list)
    assert optimized_bubble_sort(input_list) == expected

def test_list_with_duplicates():
    """Test a list with duplicate elements"""
    input_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    expected = sorted(input_list)
    assert optimized_bubble_sort(input_list) == expected

def test_empty_list():
    """Test an empty list"""
    input_list = []
    assert optimized_bubble_sort(input_list) == []

def test_single_element_list():
    """Test a list with a single element"""
    input_list = [42]
    assert optimized_bubble_sort(input_list) == [42]

def test_input_type_error():
    """Test that a TypeError is raised for non-list inputs"""
    with pytest.raises(TypeError, match="Input must be a list"):
        optimized_bubble_sort("not a list")
        optimized_bubble_sort(123)
        optimized_bubble_sort(None)

def test_original_list_unchanged():
    """Verify that the original list remains unchanged"""
    input_list = [5, 2, 9, 1, 7]
    original_copy = input_list.copy()
    _ = optimized_bubble_sort(input_list)
    assert input_list == original_copy

def test_mixed_type_comparable_list():
    """Test a list with comparable mixed types"""
    input_list = [3, 1.5, 2, 4.2, 0]
    expected = sorted(input_list)
    assert optimized_bubble_sort(input_list) == expected