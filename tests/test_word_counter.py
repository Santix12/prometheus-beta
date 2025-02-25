import pytest
from src.word_counter import count_words

def test_default_separator():
    """Test counting words with default space separator."""
    assert count_words("hello world python") == 3

def test_custom_separator():
    """Test counting words with a custom separator."""
    assert count_words("apple,banana,cherry", separator=",") == 3

def test_empty_string():
    """Test counting words in an empty string."""
    assert count_words("") == 0

def test_single_word():
    """Test counting words for a single word."""
    assert count_words("hello") == 1

def test_multiple_separators():
    """Test counting words with multiple consecutive separators."""
    assert count_words("hello,,world", separator=",") == 2

def test_separator_at_ends():
    """Test counting words with separators at the beginning and end."""
    assert count_words(",hello,world,", separator=",") == 2

def test_invalid_input_type():
    """Test raising TypeError for non-string input."""
    with pytest.raises(TypeError, match="Input must be a string"):
        count_words(123)

def test_invalid_separator_type():
    """Test raising TypeError for non-string separator."""
    with pytest.raises(TypeError, match="Separator must be a string"):
        count_words("hello world", separator=123)

def test_empty_separator():
    """Test raising ValueError for empty separator."""
    with pytest.raises(ValueError, match="Separator cannot be an empty string"):
        count_words("hello world", separator="")