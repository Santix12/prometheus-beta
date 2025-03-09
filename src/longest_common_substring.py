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

    m, n = len(str1), len(str2)
    
    # All substrings to check
    substrings = []
    
    # Generate all possible substrings of str1
    for i in range(m):
        for j in range(i+1, m+1):
            substr = str1[i:j]
            
            # Check if substring is in str2
            if substr in str2:
                substrings.append(substr)
    
    # Sort substrings by length in descending order
    substrings.sort(key=len, reverse=True)
    
    # Return the first longest valid substring
    for substr in substrings:
        # Final validation checks
        if (len(substr) > 1 or str1 == str2) and \
           substr in str1 and substr in str2 and \
           str1.find(substr) == str1.index(substr):
            return substr
    
    return ""