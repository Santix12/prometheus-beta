"""
Module for calculating the variance of a list of numbers.

This module provides a function to compute the variance of a numeric list,
handling various input scenarios and edge cases.
"""

from typing import List, Union
import math


def calculate_variance(numbers: List[Union[int, float]]) -> float:
    """
    Calculate the variance of a list of numbers.

    Variance is a measure of variability that represents the average squared 
    deviation from the mean. This function calculates the population variance.

    Args:
        numbers (List[Union[int, float]]): A list of numeric values.

    Returns:
        float: The variance of the input list.

    Raises:
        TypeError: If the input is not a list or contains non-numeric values.
        ValueError: If the input list is empty.
    """
    # Validate input
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list of numbers")
    
    # Check if list is empty
    if len(numbers) == 0:
        raise ValueError("Cannot calculate variance of an empty list")
    
    # Validate all elements are numeric
    if not all(isinstance(x, (int, float)) for x in numbers):
        raise TypeError("All elements must be numeric (int or float)")
    
    # Calculate mean
    mean = sum(numbers) / len(numbers)
    
    # Calculate variance (population variance)
    variance = sum((x - mean) ** 2 for x in numbers) / len(numbers)
    
    return variance