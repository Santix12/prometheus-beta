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
    
    # Sliding window and lookahead buffer
    window_size = 4096  # Typical window size for LZ variants
    current_pos = 0
    
    while current_pos < len(data):
        # Find longest match in the sliding window
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
        
        # Encode the match or literal
        if best_length > 2:
            # Encode match (length, offset)
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
        # Check if we can read next token
        if current_pos >= len(compressed_data):
            break
        
        try:
            token = compressed_data[current_pos]
            current_pos += 1
            
            if token < 255:  # Match token
                # Ensure we have enough bytes for match
                match_length = token
                match_offset = int.from_bytes(compressed_data[current_pos:current_pos+2], byteorder='little')
                current_pos += 2
                
                # Reconstruct match
                if match_offset == 0:
                    raise ValueError("Invalid match offset")
                
                # Start with the initial reference point
                start_index = max(0, len(decompressed) - match_offset)
                
                # Extended match computation
                match_remaining = match_length
                ref_pos = start_index
                while match_remaining > 0:
                    # If reference point is beyond current stream, 
                    # use the last known byte repeatedly
                    if ref_pos >= len(decompressed):
                        if decompressed:
                            last_byte = decompressed[-1]
                        else:
                            last_byte = 0  # Default value if empty
                        decompressed.append(last_byte)
                    else:
                        decompressed.append(decompressed[ref_pos])
                        ref_pos += 1
                    
                    match_remaining -= 1
            else:
                # Literal byte
                decompressed.append(token)
        except IndexError:
            # Incomplete compressed data
            break
    
    return decompressed