import pytest
from src.text_replacer import replace_words

def test_basic_replacement():
    """Test basic word replacement."""
    text = "hello world"
    replacements = {"hello": "hi"}
    assert replace_words(text, replacements) == "hi world"

def test_multiple_replacements():
    """Test multiple word replacements."""
    text = "the quick brown fox jumps over the lazy dog"
    replacements = {
        "quick": "slow", 
        "brown": "white", 
        "lazy": "energetic"
    }
    assert replace_words(text, replacements) == "the slow white fox jumps over the energetic dog"

def test_no_replacements():
    """Test when no replacements match."""
    text = "hello world"
    replacements = {"test": "replacement"}
    assert replace_words(text, replacements) == "hello world"

def test_empty_input():
    """Test with empty string."""
    text = ""
    replacements = {"test": "replacement"}
    assert replace_words(text, replacements) == ""

def test_invalid_text_type():
    """Test with invalid text type."""
    with pytest.raises(TypeError, match="Input text must be a string"):
        replace_words(123, {"test": "replacement"})

def test_invalid_replacements_type():
    """Test with invalid replacements type."""
    with pytest.raises(TypeError, match="Replacements must be a dictionary"):
        replace_words("hello world", "not a dict")

def test_case_sensitivity():
    """Test case sensitivity of replacements."""
    text = "Hello hello HELLO"
    replacements = {"hello": "hi"}
    assert replace_words(text, replacements) == "Hello hi HELLO"