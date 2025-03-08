import pytest
from src.unique_sum import sum_unique_elements

def test_basic_unique_sum():
    """Test basic functionality with unique and duplicate elements"""
    assert sum_unique_elements([1, 2, 3, 2]) == 6
    assert sum_unique_elements([1, 1, 1, 1]) == 1
    assert sum_unique_elements([]) == 0

def test_different_sequences():
    """Test various input sequences"""
    assert sum_unique_elements([5, 5, 5, 5, 5]) == 5
    assert sum_unique_elements([1, 2, 3, 4, 5]) == 15
    assert sum_unique_elements([-1, -1, 2, 3, 4, 5]) == 13

def test_error_handling():
    """Test error handling for invalid inputs"""
    # Non-list input
    with pytest.raises(TypeError, match="Input must be a list"):
        sum_unique_elements("not a list")
    
    # Non-integer elements
    with pytest.raises(TypeError, match="All elements must be integers"):
        sum_unique_elements([1, 2, "3", 4])
    
    # Mixed type list
    with pytest.raises(TypeError, match="All elements must be integers"):
        sum_unique_elements([1, 2, 3.5, 4])

def test_edge_cases():
    """Test edge cases"""
    # Single element
    assert sum_unique_elements([42]) == 42
    
    # Negative numbers
    assert sum_unique_elements([-1, -1, -2, -2]) == -3
    
    # Zero handling
    assert sum_unique_elements([0, 0, 0]) == 0