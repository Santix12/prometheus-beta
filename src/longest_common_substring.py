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
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Variables to track the longest substring
    max_length = 0
    end_row = 0
    end_col = 0

    # Build the dynamic programming matrix
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
                
                # Track the longest substring
                if dp[i][j] > max_length:
                    max_length = dp[i][j]
                    end_row = i
                    end_col = j
            else:
                dp[i][j] = 0

    # If no common substring found
    if max_length == 0:
        return ""

    # Extract the substring 
    start_row = end_row - max_length
    start_col = end_col - max_length
    
    # Return the substring, prioritizing the first occurrence
    result = str1[start_row:end_row]
    
    # Verify the substring exists in both strings at the correct position
    if result in str2 and str1.find(result) == start_row:
        return result
    
    return ""