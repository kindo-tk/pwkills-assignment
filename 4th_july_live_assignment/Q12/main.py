# main.py

import calculator

# Get user input for the two numbers
a = float(input("Enter the first number:"))
b = float(input("Enter the second number:"))

# Perform arithmetic operations and display the results
print(f"Sum: {a} + {b} = {calculator.add(a, b)}")
print(f"Difference: {a} - {b} = {calculator.subtract(a, b)}")
print(f"Product: {a} * {b} =  {calculator.multiply(a, b)}")
print(f"Quotient : {a} / {b} =  {calculator.divide(a, b)}")