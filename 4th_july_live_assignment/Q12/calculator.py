## 12. Write a Python module named calculator.py containing functions for addition, subtraction, 
## multiplication, and division

# calculator.py

def add(a, b):
    """Returns the sum of a and b."""
    return a + b

def subtract(a, b):
    """Returns the difference between a and b."""
    return a - b

def multiply(a, b):
    """Returns the product of a and b."""
    return a * b

def divide(a, b):
    """Returns the quotient of a divided by b.
    
    Raises:
        ValueError: If b is zero, since division by zero is not allowed.
    """
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b
