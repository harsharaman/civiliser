def remove_escape_characters(text):
    """
    Remove escape characters from a string.

    This function replaces newline characters ('\n') with spaces and removes Unicode bullet points ('\xc2\xb7') from the input string.

    Args:
        text (str): The input string to process.

    Returns:
        str: The input string with escape characters removed.
    """
    return text.replace('\n','').replace('\xc2\xb7', '')