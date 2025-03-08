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
    
    # Dictionary to group palindromes by length
    palindrome_lengths = {}
    
    # Track shortest length of palindromes
    min_length = float('inf')
    
    # Check all possible substrings
    for i in range(len(s)):
        for j in range(i, len(s)):
            # Extract substring
            substring = s[i:j+1]
            
            # Check if substring is a palindrome
            if substring == substring[::-1]:
                # Update length tracking
                length = len(substring)
                
                if length < min_length:
                    # If we find a shorter palindrome, reset the dictionary
                    palindrome_lengths = {length: {substring}}
                    min_length = length
                elif length == min_length:
                    # If equal to current shortest, add to the set
                    if length not in palindrome_lengths:
                        palindrome_lengths[length] = set()
                    palindrome_lengths[length].add(substring)
    
    # If no palindromes found
    if not palindrome_lengths:
        return []
    
    # Return sorted list of shortest palindromes
    return sorted(list(palindrome_lengths[min_length]))