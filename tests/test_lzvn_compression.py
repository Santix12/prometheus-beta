"""
Test suite for LZVN compression and decompression functions.
"""

import pytest
import sys
import os

# Add the src directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from lzvn_compression import compress_lzvn, decompress_lzvn

def test_compress_decompress_basic():
    """Test basic compression and decompression of simple data."""
    original_data = b"Hello, world! This is a test of LZVN compression."
    compressed = compress_lzvn(original_data)
    decompressed = decompress_lzvn(compressed)
    
    assert decompressed == original_data, "Decompressed data does not match original"
    assert len(compressed) < len(original_data), "Compression did not reduce data size"

def test_compress_decompress_repeated_data():
    """Test compression of data with repeated patterns."""
    original_data = b"ABCABCABCABCABCABCABC" * 10
    compressed = compress_lzvn(original_data)
    decompressed = decompress_lzvn(compressed)
    
    assert decompressed == original_data, "Decompressed data does not match original"
    assert len(compressed) < len(original_data), "Compression did not reduce data size"

def test_empty_input_error():
    """Test error handling for empty input."""
    with pytest.raises(ValueError, match="Input data cannot be empty"):
        compress_lzvn(b"")
    
    with pytest.raises(ValueError, match="Input data cannot be empty"):
        decompress_lzvn(b"")

def test_invalid_input_type():
    """Test error handling for invalid input types."""
    with pytest.raises(TypeError, match="Input must be bytes or bytearray"):
        compress_lzvn("Not bytes")
    
    with pytest.raises(TypeError, match="Input must be bytes or bytearray"):
        decompress_lzvn("Not bytes")

def test_large_data():
    """Test compression and decompression of larger data."""
    original_data = b"This is a larger test data with some repeated content " * 1000
    compressed = compress_lzvn(original_data)
    decompressed = decompress_lzvn(compressed)
    
    assert decompressed == original_data, "Decompressed data does not match original"
    assert len(compressed) < len(original_data), "Compression did not reduce data size"

def test_binary_data():
    """Test compression of binary data."""
    original_data = bytes([i % 256 for i in range(1000)])
    compressed = compress_lzvn(original_data)
    decompressed = decompress_lzvn(compressed)
    
    assert decompressed == original_data, "Decompressed data does not match original"