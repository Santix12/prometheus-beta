"""
Test suite for LZJH compression algorithm implementation.
"""

import pytest
import random
import string
from src.lzjh_compression import lzjh_compress, lzjh_decompress

def generate_random_data(length):
    """Generate random bytes for testing."""
    return bytes(random.randint(0, 255) for _ in range(length))

def test_basic_compression_decompression():
    """Test basic compression and decompression."""
    original_data = b"HELLO WORLD"
    compressed = lzjh_compress(original_data)
    decompressed = lzjh_decompress(compressed)
    assert decompressed == original_data

def test_random_data_compression():
    """Test compression and decompression with random data."""
    for length in [10, 100, 1000]:
        original_data = generate_random_data(length)
        compressed = lzjh_compress(original_data)
        decompressed = lzjh_decompress(compressed)
        assert decompressed == original_data

def test_repeated_pattern_compression():
    """Test compression of repeated patterns."""
    repeated_data = b"ABCABCABCABC" * 10
    compressed = lzjh_compress(repeated_data)
    decompressed = lzjh_decompress(compressed)
    assert decompressed == repeated_data

def test_empty_input_error():
    """Test error handling for empty input."""
    with pytest.raises(ValueError, match="Input data cannot be empty"):
        lzjh_compress(b"")
    with pytest.raises(ValueError, match="Input data cannot be empty"):
        lzjh_decompress(b"")

def test_invalid_input_type():
    """Test error handling for invalid input types."""
    with pytest.raises(TypeError, match="Input must be bytes or bytearray"):
        lzjh_compress("not bytes")
    with pytest.raises(TypeError, match="Input must be bytes or bytearray"):
        lzjh_decompress("not bytes")

def test_invalid_compressed_data():
    """Test error handling for invalid compressed data."""
    with pytest.raises(ValueError, match="Compressed data length must be even"):
        lzjh_decompress(b"\x01")  # Odd-length input

def test_edge_cases():
    """Test edge cases and boundary conditions."""
    # Single byte
    single_byte = b"\xFF"
    compressed = lzjh_compress(single_byte)
    decompressed = lzjh_decompress(compressed)
    assert decompressed == single_byte

    # Large repeated sequence
    large_repeated = b"\xAA" * 1000
    compressed = lzjh_compress(large_repeated)
    decompressed = lzjh_decompress(compressed)
    assert decompressed == large_repeated

def test_compression_ratio():
    """Verify basic compression behavior."""
    # Highly compressible data
    compressible_data = b"ABCDEFG" * 100
    compressed = lzjh_compress(compressible_data)
    assert len(compressed) < len(compressible_data)

    # Decompression should recover original data
    decompressed = lzjh_decompress(compressed)
    assert decompressed == compressible_data