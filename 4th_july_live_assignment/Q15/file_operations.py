# file_operations.py
'''
15. Write a Python module named file_operations.py with functions for reading, writing, and appending 
data to a file.
'''

def write_to_file(file_path: str, data: str) -> None:
    """
    Writes data to a file. If the file exists, it overwrites the existing content.

    Args:
        file_path (str): The path of the file to write to.
        data (str): The data to write to the file.
    """
    with open(file_path, 'w') as file:
        file.write(data)


def read_from_file(file_path: str) -> str:
    """
    Reads the content of a file.

    Args:
        file_path (str): The path of the file to read from.

    Returns:
        str: The content of the file.
    """
    with open(file_path, 'r') as file:
        return file.read()


def append_to_file(file_path: str, data: str) -> None:
    """
    Appends data to a file. If the file does not exist, it creates a new file.

    Args:
        file_path (str): The path of the file to append to.
        data (str): The data to append to the file.
    """
    with open(file_path, 'a') as file:
        file.write(data)
