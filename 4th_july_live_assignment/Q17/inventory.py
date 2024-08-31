'''
17. Develop a Python script that opens an existing text file named "inventory.txt" in read mode and displays 
the contents of the file line by line.
'''

def read_and_display_file(file_path: str) -> None:
    """
    Reads the contents of a file and displays them line by line.

    Args:
        file_path (str): The path of the file to read.
    """
    try:
        with open(file_path, 'r') as file:
            # Read and display each line
            for line in file:
                print(line.strip())
    except FileNotFoundError:
        print(f"The file {file_path} does not exist.")
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")

# File path
file_path = "inventory.txt"

# Read and display the file contents
read_and_display_file(file_path)
