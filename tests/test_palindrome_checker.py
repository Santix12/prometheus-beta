import pytest
from src.palindrome_checker import is_palindrome

def test_palindrome_positive_cases():
    """Test various positive palindrome scenarios."""
    assert is_palindrome([]) == True
    assert is_palindrome([1]) == True
    assert is_palindrome([1, 2, 1]) == True
    assert is_palindrome([1, 2, 2, 1]) == True
    assert is_palindrome([5, 7, 7, 5]) == True

def test_palindrome_negative_cases():
    """Test various non-palindrome scenarios."""
    assert is_palindrome([1, 2, 3]) == False
    assert is_palindrome([1, 2, 3, 4]) == False
    assert is_palindrome([1, 2, 3, 2]) == False

def test_palindrome_error_cases():
    """Test error handling."""
    with pytest.raises(TypeError):
        is_palindrome("not a list")
    
    with pytest.raises(TypeError):
        is_palindrome(123)
    
    with pytest.raises(TypeError):
        is_palindrome(None)

def test_palindrome_complex_cases():
    """Test more complex palindrome scenarios."""
    assert is_palindrome([1, 1, 1, 1]) == True
    assert is_palindrome([0, 0, 0]) == True
    assert is_palindrome([-1, 0, -1]) == True
    assert is_palindrome([1, -1, 1]) == True