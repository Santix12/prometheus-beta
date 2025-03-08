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
    palindrome_by_length = {}
    
    # Check all possible substrings
    for i in range(len(s)):
        for j in range(i, len(s)):
            # Extract substring
            substring = s[i:j+1]
            
            # Check if substring is a palindrome
            if substring == substring[::-1]:
                # Store palindromes by their length
                if len(substring) not in palindrome_by_length:
                    palindrome_by_length[len(substring)] = set()
                palindrome_by_length[len(substring)].add(substring)
    
    # If no palindromes found
    if not palindrome_by_length:
        return []
    
    # Find the minimum length of palindromes
    min_length = min(palindrome_by_length.keys())
    
    # Return all palindromes with the minimum length
    return sorted(list(palindrome_by_length[min_length]))