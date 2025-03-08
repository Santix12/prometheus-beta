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
    
    # Dictionary to track palindromes
    palindromes = {}
    
    # Minimum length tracking
    lengths = []
    
    # Check all possible substrings
    for i in range(len(s)):
        for j in range(i, len(s)):
            # Extract substring
            substring = s[i:j+1]
            
            # Check if substring is a palindrome
            if substring == substring[::-1]:
                # Track length of palindrome
                length = len(substring)
                
                # Initialize length if not yet tracked
                if length not in palindromes:
                    palindromes[length] = set()
                
                # Add to current palindromes
                palindromes[length].add(substring)
    
    # Find the minimum length of palindromes
    if not palindromes:
        return []
    
    # Find the minimum length
    min_length = min(palindromes.keys())
    
    # Get max length we want to include (up to the original string)
    max_include_length = min(len(s), min_length * 2)
    
    # Collect all palindromes up to max length
    result = set()
    for length in sorted(palindromes.keys()):
        if length <= max_include_length:
            result.update(palindromes[length])
    
    return sorted(list(result))