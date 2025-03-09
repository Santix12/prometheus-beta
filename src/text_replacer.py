def replace_words(text: str, replacements: dict) -> str:
    """
    Perform in-place word replacements in a given text using a dictionary of replacements.

    Args:
        text (str): The input text to perform replacements on.
        replacements (dict): A dictionary where keys are words to be replaced 
                             and values are their replacements.

    Returns:
        str: The text with all specified replacements made.

    Notes:
        - Replacements are case-sensitive by default.
        - If a replacement key is not found in the text, no changes are made.
        - Whole word replacements only (prevents partial word replacements).
    """
    # Validate inputs
    if not isinstance(text, str):
        raise TypeError("Input text must be a string")
    if not isinstance(replacements, dict):
        raise TypeError("Replacements must be a dictionary")

    # Split the text into words
    words = text.split()

    # Perform replacements
    replaced_words = [
        replacements.get(word, word) for word in words
    ]

    # Reconstruct the text
    return ' '.join(replaced_words)