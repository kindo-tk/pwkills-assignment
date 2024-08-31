'''
18. Create a Python script that reads a text file named "expenses.txt" and calculates the total amount spent 
on various expenses listed in the file.
'''

def calculate_total_expenses(file_path: str) -> float:
    """
    Reads the expenses from a file and calculates the total amount spent.

    Args:
        file_path (str): The path of the file containing expenses.

    Returns:
        float: The total amount spent.
    """
    total_expense = 0.0
    
    try:
        with open(file_path, 'r') as file:
            for line in file:
                # Split the line by comma and strip any leading/trailing whitespace
                parts = line.strip().split(',')
                
                # Assuming the amount is the second element, convert to float and add to total
                if len(parts) >= 2:
                    try:
                        amount = float(parts[1])
                        total_expense += amount
                    except ValueError:
                        print(f"Invalid amount found: {parts[1]} - skipping this entry.")
    except FileNotFoundError:
        print(f"The file {file_path} does not exist.")
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")

    return total_expense

# File path
file_path = "expenses.txt"

# Calculate and print the total expenses
total = calculate_total_expenses(file_path)
print(f"Total amount spent: {total}")
