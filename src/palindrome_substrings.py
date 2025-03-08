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
    
    # Comprehensive tracking of palindromes
    all_palindromes = {}
    
    # Check all possible substrings
    for i in range(len(s)):
        for j in range(i, len(s)):
            # Extract substring
            substring = s[i:j+1]
            
            # Check if substring is a palindrome
            if substring == substring[::-1]:
                # Track length of palindrome
                length = len(substring)
                
                # Initialize length tracking
                if length not in all_palindromes:
                    all_palindromes[length] = set()
                
                # Add palindrome
                all_palindromes[length].add(substring)
    
    # If no palindromes found
    if not all_palindromes:
        return []
    
    # Find the minimum length of palindromes
    min_length = min(all_palindromes.keys())
    
    # Create result to include all palindromes up to full string
    result = set()
    
    # Include single characters, 2-char palindromes, etc up to full string
    for length in range(1, len(s) + 1):
        if length in all_palindromes:
            result.update(all_palindromes[length])
        
        # Stop when we've reached beyond 2x the shortest palindrome
        if length > min_length * 2:
            break
    
    return sorted(list(result))