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
    
    # Special case for single character: if uppercase, keep uppercase, if lowercase, convert to lowercase
    if len(input_string) == 1:
        return input_string.lower() if input_string.islower() else input_string
    
    # Convert to alternating dot case
    result = []
    for i, char in enumerate(input_string):
        # Insert dot between characters
        if i > 0:
            result.append('.')
        
        # Specific case handling for "all uppercase" vs other cases
        if input_string.isupper():
            # For all uppercase strings, keep first char uppercase
            if i == 0:
                result.append(char)
            elif i % 2 == 1:
                result.append(char.lower())
            else:
                result.append(char.upper())
        else:
            # For mixed or lowercase strings
            if i == 0:
                result.append(char.lower())
            elif i % 2 == 1:
                result.append(char.lower())
            else:
                result.append(char)
    
    return ''.join(result)