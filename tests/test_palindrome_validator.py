import pytest
from src.palindrome_validator import is_valid_palindrome

def test_valid_palindromes():
    """Test various valid palindromes with different formatting."""
    assert is_valid_palindrome("A man, a plan, a canal: Panama") == True
    assert is_valid_palindrome("race a car") == False
    assert is_valid_palindrome("") == True
    assert is_valid_palindrome("a") == True

def test_case_insensitive():
    """Test that the function is case-insensitive."""
    assert is_valid_palindrome("Able was I ere I saw Elba") == True
    assert is_valid_palindrome("RaCeCaR") == True

def test_punctuation_and_spaces():
    """Test handling of punctuation and spaces."""
    assert is_valid_palindrome("Was it a car or a cat I saw?") == True
    assert is_valid_palindrome("No 'x' in Nixon") == True

def test_non_alphanumeric():
    """Test strings with various non-alphanumeric characters."""
    assert is_valid_palindrome("Hello, World!") == False
    assert is_valid_palindrome("12321") == True
    assert is_valid_palindrome("A1b22b1a") == True

def test_edge_cases():
    """Test edge cases and boundary conditions."""
    assert is_valid_palindrome(" ") == True
    assert is_valid_palindrome("!!") == True
    assert is_valid_palindrome("a.") == True