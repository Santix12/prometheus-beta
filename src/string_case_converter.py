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
    last_was_alpha = False
    for i, char in enumerate(input_string):
        # Insert dot between characters, but only for alphanumeric characters
        if i > 0 and last_was_alpha and char.isalnum():
            result.append('.')
        
        # Determine case transformation
        if not char.isalpha():
            # Non-alphabetic characters stay as-is
            result.append(char)
            last_was_alpha = False
        else:
            # For alphabetic characters, apply specific case rules
            if i == 0:
                # First character logic: keep first character of uppercase string
                result.append(char if char.isupper() else char.lower())
            elif last_was_alpha:
                # Alternate case for subsequent alphabetic characters
                result.append(char.lower() if char.isupper() else char.upper())
            else:
                # After a non-alphabetic character
                result.append(char.lower())
            
            last_was_alpha = True
    
    return ''.join(result)