def convert_to_alternating_dot_case(input_string):
    """
    Convert a string to alternating dot case.
    
    Args:
        input_string (str): The input string to convert.
    
    Returns:
        str: The string converted to alternating dot case.
    
    Raises:
        TypeError: If the input is not a string.
    
    Examples:
        >>> convert_to_alternating_dot_case("hello world")
        'h.e.l.l.o. .w.o.r.l.d'
        >>> convert_to_alternating_dot_case("PYTHON")
        'P.y.T.h.O.n'
        >>> convert_to_alternating_dot_case("")
        ''
    """
    # Check if input is a string
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    # Handle empty string case
    if not input_string:
        return ""
    
    # Convert to alternating dot case
    result = []
    for i, char in enumerate(input_string):
        # If even index (0, 2, 4, etc.), insert dot before character
        if i > 0:
            result.append('.')
        
        # If character is uppercase, convert to lowercase. If lowercase, convert to uppercase
        if char.isupper():
            result.append(char.lower())
        elif char.islower():
            result.append(char.upper())
        else:
            # For non-alphabetic characters, keep as-is
            result.append(char)
    
    return ''.join(result)