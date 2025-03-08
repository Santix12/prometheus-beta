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
    
    # Dictionary to store palindromes by length
    palindrome_lengths = {}
    
    # Track the lengths of palindromes
    for length_type in ['min', 'current', 'max']:
        palindrome_lengths[length_type] = set()
    
    # Check all possible substrings
    for i in range(len(s)):
        for j in range(i, len(s)):
            # Extract substring
            substring = s[i:j+1]
            
            # Check if substring is a palindrome
            if substring == substring[::-1]:
                # Track palindrome length
                length = len(substring)
                palindrome_lengths['current'].add(substring)
                
                # Update min/max as we go
                if not palindrome_lengths['min'] or length < len(list(palindrome_lengths['min'])[0]):
                    palindrome_lengths['min'] = {substring}
                elif length == len(list(palindrome_lengths['min'])[0]):
                    palindrome_lengths['min'].add(substring)
                
                # Track max length if needed for future use
                if not palindrome_lengths['max'] or length > len(list(palindrome_lengths['max'])[0]):
                    palindrome_lengths['max'] = {substring}
                elif length == len(list(palindrome_lengths['max'])[0]):
                    palindrome_lengths['max'].add(substring)
    
    # Return sorted list of minimum length palindromes
    return sorted(list(palindrome_lengths['min']))