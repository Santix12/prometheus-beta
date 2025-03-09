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

    # Create a matrix to store substring lengths
    m, n = len(str1), len(str2)
    # Initialize the dynamic programming matrix
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Variables to track the longest substring
    max_length = 0
    end_index = 0

    # Build the dynamic programming matrix
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            # If characters match (case-sensitive) and are equal, extend the previous substring
            if str1[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
                
                # Update longest substring tracking
                if dp[i][j] > max_length:
                    max_length = dp[i][j]
                    end_index = i - 1
            else:
                dp[i][j] = 0

    # Precisely extract and return the longest common substring
    if max_length == 0:
        return ""
    
    # Ensure we return the first occurrence of the longest common substring
    result = str1[end_index - max_length + 1 : end_index + 1]
    
    # Additional check to verify the substring actually appears in both strings
    if result in str1 and result in str2:
        return result
    
    return ""