import pytest
from src.longest_common_substring import longest_common_substring

def test_basic_common_substring():
    """Test finding a basic common substring"""
    assert longest_common_substring("abcdxyz", "xyzabcd") == "abcd"
    assert longest_common_substring("zxabcdezy", "yzabcdezx") == "abcdez"

def test_no_common_substring():
    """Test when no common substring exists"""
    assert longest_common_substring("hello", "world") == ""

def test_empty_strings():
    """Test with empty input strings"""
    assert longest_common_substring("", "") == ""
    assert longest_common_substring("abc", "") == ""
    assert longest_common_substring("", "xyz") == ""

def test_identical_strings():
    """Test when strings are identical"""
    assert longest_common_substring("python", "python") == "python"

def test_partial_overlapping_substrings():
    """Test strings with partially overlapping substrings"""
    assert longest_common_substring("ABABC", "BABCA") == "BABC"

def test_case_sensitivity():
    """Test case sensitivity of substring matching"""
    assert longest_common_substring("Hello", "hello") == ""

def test_single_character_common_substring():
    """Test when only a single character is common"""
    assert longest_common_substring("abc", "cde") == "c"

def test_repeated_characters():
    """Test with repeated characters"""
    assert longest_common_substring("aaaaaa", "aaabbb") == "aaaa"

def test_long_strings():
    """Test with longer input strings"""
    str1 = "abcdefghijklmnopqrstuvwxyz"
    str2 = "mnopqrstuvwxyzabcdefghijkl"
    assert longest_common_substring(str1, str2) == "abcdefghijkl"