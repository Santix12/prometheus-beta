"""
LZJH (Lempel-Ziv-Johnson-Hoan) Compression Algorithm Implementation

This module provides a compression function for the LZJH compression algorithm.
"""

def lzjh_compress(data):
    """
    Compress input data using the LZJH compression algorithm.
    
    Args:
        data (bytes or bytearray): The input data to be compressed.
    
    Returns:
        bytearray: Compressed data.
    
    Raises:
        TypeError: If input is not bytes or bytearray.
        ValueError: If input is empty.
    """
    # Input validation
    if not isinstance(data, (bytes, bytearray)):
        raise TypeError("Input must be bytes or bytearray")
    
    if not data:
        raise ValueError("Input data cannot be empty")
    
    # Initialize compression dictionary and output
    dictionary = {bytes([i]): i for i in range(256)}
    next_code = 256
    result = bytearray()
    current_sequence = bytearray()
    
    # Compression algorithm implementation
    for byte in data:
        # Extend current sequence
        test_sequence = current_sequence + bytes([byte])
        
        # If sequence exists in dictionary, continue
        if bytes(test_sequence) in dictionary:
            current_sequence = test_sequence
        else:
            # Output the code for current sequence
            result.extend(dictionary[bytes(current_sequence)].to_bytes(2, 'big'))
            
            # Add new sequence to dictionary if not at max
            if next_code < 65536:  # 16-bit codes
                dictionary[bytes(test_sequence)] = next_code
                next_code += 1
            
            # Reset current sequence
            current_sequence = bytes([byte])
    
    # Output final sequence
    if current_sequence:
        result.extend(dictionary[bytes(current_sequence)].to_bytes(2, 'big'))
    
    return result

def lzjh_decompress(compressed_data):
    """
    Decompress data compressed with the LZJH algorithm.
    
    Args:
        compressed_data (bytes or bytearray): The compressed input data.
    
    Returns:
        bytearray: Decompressed data.
    
    Raises:
        TypeError: If input is not bytes or bytearray.
        ValueError: If input is empty or has invalid length.
    """
    # Input validation
    if not isinstance(compressed_data, (bytes, bytearray)):
        raise TypeError("Input must be bytes or bytearray")
    
    if not compressed_data:
        raise ValueError("Input data cannot be empty")
    
    if len(compressed_data) % 2 != 0:
        raise ValueError("Compressed data length must be even")
    
    # Initialize decompression dictionary
    dictionary = {i: bytes([i]) for i in range(256)}
    next_code = 256
    result = bytearray()
    
    # Read first two bytes as initial code
    current_code = int.from_bytes(compressed_data[:2], 'big')
    result.extend(dictionary[current_code])
    previous_sequence = dictionary[current_code]
    
    # Process remaining compressed data
    for i in range(2, len(compressed_data), 2):
        # Read next code
        code = int.from_bytes(compressed_data[i:i+2], 'big')
        
        # Retrieve sequence for current code
        if code in dictionary:
            current_sequence = dictionary[code]
        elif code == next_code:
            current_sequence = previous_sequence + previous_sequence[:1]
        else:
            raise ValueError(f"Invalid compression code: {code}")
        
        # Output current sequence
        result.extend(current_sequence)
        
        # Add new dictionary entry
        if next_code < 65536:  # 16-bit codes
            dictionary[next_code] = previous_sequence + current_sequence[:1]
            next_code += 1
        
        # Update previous sequence
        previous_sequence = current_sequence
    
    return result