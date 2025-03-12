"""
Test suite for LZW Compression module
"""

import pytest
from src.lzw_compression import lzw_compress, lzw_decompress

def test_basic_compression_decompression():
    """Test basic string compression and decompression"""
    original = "TOBEORNOTTOBEORTOBEORNOT"
    compressed = lzw_compress(original)
    decompressed = lzw_decompress(compressed)
    assert decompressed == original

def test_single_character_string():
    """Test compression and decompression of a single character string"""
    original = "A"
    compressed = lzw_compress(original)
    decompressed = lzw_decompress(compressed)
    assert decompressed == original

def test_repeated_string():
    """Test compression and decompression of a repeated string"""
    original = "AAAAAAAAAA"
    compressed = lzw_compress(original)
    decompressed = lzw_decompress(compressed)
    assert decompressed == original

def test_mixed_characters():
    """Test compression and decompression of mixed character string"""
    original = "Hello, World!"
    compressed = lzw_compress(original)
    decompressed = lzw_decompress(compressed)
    assert decompressed == original

def test_empty_string_raises_error():
    """Test that empty string raises ValueError"""
    with pytest.raises(ValueError):
        lzw_compress("")

def test_invalid_input_type_raises_error():
    """Test that non-string input raises TypeError"""
    with pytest.raises(TypeError):
        lzw_compress(123)
    with pytest.raises(TypeError):
        lzw_decompress("not a list")

def test_invalid_compressed_data():
    """Test handling of invalid compressed data"""
    with pytest.raises(ValueError):
        lzw_decompress([])
    
    # Test with an invalid code that doesn't exist in dictionary
    with pytest.raises(ValueError):
        lzw_decompress([256, 257, 1000])

def test_reversibility():
    """Ensure compression and decompression are perfectly reversible"""
    test_strings = [
        "TOBEORNOTTOBEORTOBEORNOT",
        "Hello, World!",
        "AaBbCcDdEeFfGg",
        "12345678901234567890"
    ]
    
    for original in test_strings:
        compressed = lzw_compress(original)
        decompressed = lzw_decompress(compressed)
        assert decompressed == original, f"Failed for input: {original}"