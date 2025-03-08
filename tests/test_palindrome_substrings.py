import pytest
from src.palindrome_substrings import find_shortest_palindrome_substrings

def test_basic_palindromes():
    """Test basic palindrome substring scenarios."""
    assert set(find_shortest_palindrome_substrings("abba")) == set(['a', 'b', 'bb', 'abba'])
    assert set(find_shortest_palindrome_substrings("hello")) == set(['h', 'e', 'l', 'l', 'o'])

def test_empty_string():
    """Test empty string input."""
    assert find_shortest_palindrome_substrings("") == []

def test_single_character():
    """Test input with single character."""
    assert find_shortest_palindrome_substrings("a") == ['a']

def test_no_palindromes():
    """Test string with no palindromes longer than single characters."""
    assert set(find_shortest_palindrome_substrings("abc")) == set(['a', 'b', 'c'])

def test_multiple_palindromes():
    """Test string with multiple palindromes of different lengths."""
    assert set(find_shortest_palindrome_substrings("racecar")) == set(['r', 'a', 'c', 'e', 'racecar'])

def test_overlapping_palindromes():
    """Test string with overlapping palindromes."""
    assert set(find_shortest_palindrome_substrings("aaa")) == set(['a', 'aa', 'aaa'])

def test_case_sensitivity():
    """Test that function is case-sensitive."""
    assert set(find_shortest_palindrome_substrings("Aba")) == set(['A', 'b', 'a', 'Aba'])