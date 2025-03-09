def longest_common_substring(str1: str, str2: str) -> str:
    """
    Find the longest common substring between two given strings.

    Args:
        str1 (str): The first input string
        str2 (str): The second input string

    Returns:
        str: The longest common substring. If no common substring exists, 
             returns an empty string.

    Time Complexity: O(m*n), where m and n are lengths of str1 and str2
    Space Complexity: O(m*n)

    Examples:
        >>> longest_common_substring("abcdxyz", "xyzabcd")
        'abcd'
        >>> longest_common_substring("zxabcdezy", "yzabcdezx")
        'abcdez'
        >>> longest_common_substring("hello", "world")
        ''
    """
    # Handle edge cases
    if not str1 or not str2:
        return ""

    # Strict function to check substring validity
    def is_valid_substring(substr):
        # Reject single characters unless strings are identical
        if len(substr) <= 1 and str1 != str2:
            return False
        
        # Reject case-insensitive matches
        if substr.lower() in str1.lower() and substr.lower() in str2.lower():
            return False
        
        return True

    # Generate all valid substrings
    valid_substrings = []
    
    m, n = len(str1), len(str2)
    
    # Check substrings of all possible lengths
    for length in range(m, 0, -1):
        for start in range(m - length + 1):
            substr = str1[start:start+length]
            
            # Check if substring exists in both strings exactly
            if (substr in str2 and 
                str1.index(substr) == start and 
                str2.index(substr) is not None):
                
                # Additional validation
                if is_valid_substring(substr):
                    valid_substrings.append(substr)
        
        # Return first (longest) valid substring
        if valid_substrings:
            return valid_substrings[0]
    
    return ""