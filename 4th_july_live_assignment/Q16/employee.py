''' 16. Write a Python program to create a text file named "employees.txt" and write the details of employees, 
including their name, age, and salary, into the file.
'''


def write_employee_details(file_path: str, employees: list) -> None:
    """
    Writes the details of employees to a file.

    Args:
        file_path (str): The path of the file to write to.
        employees (list): A list of tuples, each containing employee name, age, and salary.
    """
    with open(file_path, 'w') as file:
        file.write("Name, \tAge, \tSalary\n")
        for name, age, salary in employees:
            file.write(f"{name}, \t{age}, \t{salary}\n")

# List of employees (name, age, salary)
employees = [
    ("Salman Khan", 60, 50000),
    ("Sachin Tendulkar", 45, 60000),
    ("Rajat", 22, 45000),
    ("Reena", 30, 52000),
    ("Raj Patel", 26, 48000)
]

# File path
file_path = "employees.txt"

# Write employee details to the file
write_employee_details(file_path, employees)

print(f"Employee details written to {file_path}")
