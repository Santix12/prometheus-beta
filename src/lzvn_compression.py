"""
LZVN (Lempel-Ziv Variable-Length Encoding) Compression Algorithm Implementation.

This module provides a basic implementation of the LZVN compression algorithm.
LZVN is a variant of LZ compression with variable-length encoding.
"""

def compress_lzvn(data):
    """
    Compress input data using the LZVN compression algorithm.
    
    Args:
        data (bytes or bytearray): Input data to be compressed
    
    Returns:
        bytearray: Compressed data
    
    Raises:
        TypeError: If input is not bytes or bytearray
        ValueError: If input is empty
    """
    # Input validation
    if not isinstance(data, (bytes, bytearray)):
        raise TypeError("Input must be bytes or bytearray")
    
    if not data:
        raise ValueError("Input data cannot be empty")
    
    # Compression output 
    compressed = bytearray()
    
    # Sliding window settings
    window_size = 4096
    current_pos = 0
    
    while current_pos < len(data):
        # Find longest match in sliding window
        best_length = 0
        best_offset = 0
        
        # Search backwards in the window
        search_start = max(0, current_pos - window_size)
        for offset in range(1, current_pos - search_start + 1):
            match_length = 0
            
            # Check match length
            while (current_pos + match_length < len(data) and 
                   match_length < 255 and 
                   data[current_pos - offset + match_length] == data[current_pos + match_length]):
                match_length += 1
            
            # Update best match if found
            if match_length > best_length:
                best_length = match_length
                best_offset = offset
        
        # Encode match or literal
        if best_length > 2:
            # Encode match
            compressed.append(best_length)
            compressed.extend(best_offset.to_bytes(2, byteorder='little'))
            current_pos += best_length
        else:
            # Encode literal byte
            compressed.append(data[current_pos])
            current_pos += 1
    
    return compressed

def decompress_lzvn(compressed_data):
    """
    Decompress data previously compressed with LZVN algorithm.
    
    Args:
        compressed_data (bytes or bytearray): Compressed input data
    
    Returns:
        bytearray: Decompressed data
    
    Raises:
        TypeError: If input is not bytes or bytearray
        ValueError: If input is empty or invalid
    """
    # Input validation
    if not isinstance(compressed_data, (bytes, bytearray)):
        raise TypeError("Input must be bytes or bytearray")
    
    if not compressed_data:
        raise ValueError("Input data cannot be empty")
    
    # Decompression output
    decompressed = bytearray()
    current_pos = 0
    
    while current_pos < len(compressed_data):
        # Check for end of stream
        if current_pos >= len(compressed_data):
            break
        
        # Read next token
        token = compressed_data[current_pos]
        current_pos += 1
        
        if token < 255:  # Match token
            # Ensure sufficient bytes for offset
            if current_pos + 1 >= len(compressed_data):
                break
            
            # Read match length and offset
            match_length = token
            match_offset = int.from_bytes(compressed_data[current_pos:current_pos+2], byteorder='little')
            current_pos += 2
            
            # Basic match validation
            if match_offset == 0:
                decompressed.append(token)
                continue
            
            # Perform match reconstruction
            start_pos = max(0, len(decompressed) - match_offset)
            
            # Replicate bytes from previous stream
            for _ in range(match_length):
                if start_pos < len(decompressed):
                    decompressed.append(decompressed[start_pos])
                    start_pos += 1
                else:
                    break
        else:
            # Literal byte
            decompressed.append(token)
    
    return decompressed