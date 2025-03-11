"""
Test suite for the variance calculation function.

This module contains unit tests to verify the functionality of the 
calculate_variance function under various scenarios.
"""

import pytest
import math
from src.variance_calculator import calculate_variance


def test_basic_variance():
    """Test variance calculation for a simple list of numbers."""
    numbers = [1, 2, 3, 4, 5]
    expected_variance = 2.0  # (1-3)^2 + (2-3)^2 + (3-3)^2 + (4-3)^2 + (5-3)^2 / 5
    assert math.isclose(calculate_variance(numbers), expected_variance, rel_tol=1e-10)


def test_variance_with_floats():
    """Test variance calculation with floating-point numbers."""
    numbers = [1.5, 2.5, 3.5, 4.5, 5.5]
    expected_variance = 2.0
    assert math.isclose(calculate_variance(numbers), expected_variance, rel_tol=1e-10)


def test_single_number_variance():
    """Test variance calculation with a single number."""
    numbers = [42]
    assert calculate_variance(numbers) == 0.0


def test_zero_variance():
    """Test variance calculation for a list with identical numbers."""
    numbers = [7, 7, 7, 7, 7]
    assert calculate_variance(numbers) == 0.0


def test_empty_list_raises_value_error():
    """Verify that an empty list raises a ValueError."""
    with pytest.raises(ValueError, match="Cannot calculate variance of an empty list"):
        calculate_variance([])


def test_non_list_input_raises_type_error():
    """Verify that non-list inputs raise a TypeError."""
    with pytest.raises(TypeError, match="Input must be a list of numbers"):
        calculate_variance("not a list")
    with pytest.raises(TypeError, match="Input must be a list of numbers"):
        calculate_variance(123)


def test_non_numeric_list_raises_type_error():
    """Verify that lists with non-numeric elements raise a TypeError."""
    with pytest.raises(TypeError, match="All elements must be numeric"):
        calculate_variance([1, 2, "three", 4, 5])
    with pytest.raises(TypeError, match="All elements must be numeric"):
        calculate_variance([1, 2, None, 4, 5])