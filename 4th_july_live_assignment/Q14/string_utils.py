# string_utils.py
'''
14. Implement a Python module named string_utils.py containing functions for string manipulation, such as 
reversing and capitalizing strings.
'''
def reverse_string(s: str) -> str:
    """
    Reverses the given string.

    Args:
        s (str): The string to reverse.

    Returns:
        str: The reversed string.
    """
    return s[::-1]

def capitalize_string(s: str) -> str:
    """
    Capitalizes the first letter of each word in the given string.

    Args:
        s (str): The string to capitalize.

    Returns:
        str: The capitalized string.
    """
    return s.title()

def to_uppercase(s: str) -> str:
    """
    Converts the entire string to uppercase.

    Args:
        s (str): The string to convert.

    Returns:
        str: The uppercase string.
    """
    return s.upper()

def to_lowercase(s: str) -> str:
    """
    Converts the entire string to lowercase.

    Args:
        s (str): The string to convert.

    Returns:
        str: The lowercase string.
    """
    return s.lower()

def is_palindrome(s: str) -> bool:
    """
    Checks if the given string is a palindrome.

    Args:
        s (str): The string to check.

    Returns:
        bool: True if the string is a palindrome, False otherwise.
    """
    return s == s[::-1]
