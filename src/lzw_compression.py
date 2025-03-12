"""
Lempel-Ziv-Welch (LZW) Compression Implementation

This module provides functions for LZW compression and decompression.
LZW is a universal lossless data compression algorithm that builds a 
dynamic dictionary of data sequences encountered in the input.
"""

def lzw_compress(input_string):
    """
    Compress a string using the Lempel-Ziv-Welch (LZW) algorithm.
    
    Args:
        input_string (str): The string to be compressed.
    
    Returns:
        list: A list of integer codes representing the compressed data.
    
    Raises:
        TypeError: If input is not a string.
        ValueError: If input is an empty string.
    """
    # Validate input
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    if not input_string:
        raise ValueError("Input string cannot be empty")
    
    # Initialize dictionary with single-character strings
    dictionary = {chr(i): i for i in range(256)}
    next_code = 256
    
    # Compression process
    result = []
    current_sequence = input_string[0]
    
    for char in input_string[1:]:
        # Construct potential sequence
        potential_sequence = current_sequence + char
        
        # If sequence is in dictionary, extend current sequence
        if potential_sequence in dictionary:
            current_sequence = potential_sequence
        else:
            # Output code for current sequence
            result.append(dictionary[current_sequence])
            
            # Add new sequence to dictionary
            dictionary[potential_sequence] = next_code
            next_code += 1
            
            # Reset current sequence
            current_sequence = char
    
    # Output last sequence
    if current_sequence:
        result.append(dictionary[current_sequence])
    
    return result

def lzw_decompress(compressed_data):
    """
    Decompress data previously compressed using LZW algorithm.
    
    Args:
        compressed_data (list): List of integer codes to decompress.
    
    Returns:
        str: The decompressed original string.
    
    Raises:
        TypeError: If input is not a list.
        ValueError: If input list is empty or contains invalid codes.
    """
    # Validate input
    if not isinstance(compressed_data, list):
        raise TypeError("Input must be a list of integer codes")
    
    if not compressed_data:
        raise ValueError("Compressed data cannot be empty")
    
    # Initialize dictionary with single-character strings
    dictionary = {i: chr(i) for i in range(256)}
    next_code = 256
    
    # Ensure first code is valid
    first_code = compressed_data[0]
    if first_code not in dictionary:
        raise ValueError(f"Invalid first compression code: {first_code}")
    
    # Decompression process
    result = []
    current_code = first_code
    current_string = dictionary[current_code]
    result.append(current_string)
    
    for code in compressed_data[1:]:
        # Validate each code
        if code < 0:
            raise ValueError(f"Invalid negative code: {code}")
        
        # Determine the string for the current code
        try:
            if code in dictionary:
                new_string = dictionary[code]
            else:
                # Special case: new sequence not yet in dictionary
                # This can only happen when code == next_code
                if code != next_code:
                    raise ValueError(f"Invalid compression code: {code}")
                new_string = current_string + current_string[0]
            
            # Add new string to result
            result.append(new_string)
            
            # Add new sequence to dictionary
            dictionary[next_code] = current_string + new_string[0]
            next_code += 1
            
            # Update current string
            current_string = new_string
        
        except KeyError:
            raise ValueError(f"Code {code} not found in dictionary")
    
    return ''.join(result)