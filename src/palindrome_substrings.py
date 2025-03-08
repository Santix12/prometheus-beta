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
    
    # List to store palindromes
    palindromes = []
    
    # Minimum length to track
    min_length = float('inf')
    
    # Check all possible substrings
    for i in range(len(s)):
        for j in range(i, len(s)):
            # Extract substring
            substring = s[i:j+1]
            
            # Check if substring is a palindrome
            if substring == substring[::-1]:
                # If this is a shorter palindrome, reset the list
                if len(substring) < min_length:
                    palindromes = [substring]
                    min_length = len(substring)
                # If this is equal to the current shortest, add to the list
                elif len(substring) == min_length:
                    palindromes.append(substring)
    
    return sorted(list(set(palindromes)))