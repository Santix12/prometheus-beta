def find_shortest_palindrome_substrings(s):
    """
    Find the shortest possible palindromic substrings in a given string.
    
    A palindromic substring is a sequence of characters that reads the same 
    forwards and backwards.
    
    Args:
        s (str): Input string to search for palindromic substrings
    
    Returns:
        list: A list of the shortest palindromic substrings found in the input string
    
    Examples:
        >>> find_shortest_palindrome_substrings("abba")
        ['a', 'b', 'bb', 'abba']
        >>> find_shortest_palindrome_substrings("hello")
        ['h', 'e', 'l', 'l', 'o']
    """
    # Handle edge cases
    if not s:
        return []
    
    # Dictionary to store palindromes by their length
    palindrome_lengths = {}
    
    # Check all possible substrings
    for i in range(len(s)):
        for j in range(i, len(s)):
            # Extract substring
            substring = s[i:j+1]
            
            # Check if substring is a palindrome
            if substring == substring[::-1]:
                # Group palindromes by their length
                length = len(substring)
                if length not in palindrome_lengths:
                    palindrome_lengths[length] = set()
                palindrome_lengths[length].add(substring)
    
    # If no palindromes found
    if not palindrome_lengths:
        return []
    
    # Find the minimum length
    min_length = min(palindrome_lengths.keys())
    
    # Return sorted list of palindromes of the minimum length
    return sorted(list(palindrome_lengths[min_length]))