def is_valid_palindrome(s: str) -> bool:
    """
    Check if a given string is a valid palindrome, ignoring spaces, 
    punctuation, and case.

    A palindrome reads the same backward as forward when considering 
    only alphanumeric characters.

    Args:
        s (str): The input string to check for palindrome validity.

    Returns:
        bool: True if the string is a valid palindrome, False otherwise.

    Examples:
        >>> is_valid_palindrome("A man, a plan, a canal: Panama")
        True
        >>> is_valid_palindrome("race a car")
        False
        >>> is_valid_palindrome("")
        True
    """
    # Convert to lowercase and keep only alphanumeric characters
    cleaned_str = ''.join(char.lower() for char in s if char.isalnum())
    
    # Compare the cleaned string with its reverse
    return cleaned_str == cleaned_str[::-1]