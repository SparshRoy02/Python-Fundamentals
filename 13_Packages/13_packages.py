# 13 : Packages in Python

# Module Example

# math.py
def add(a, b):
    return a + b

# Example usage of module function
print("Module Example - Addition:", add(2, 3))


# Math Operation Package Example

# math_operations/calculator.py
def calculate():
    print("Performing calculation...")

# math_operations/basic/add.py
def add_basic(a, b):
    return a + b

# math_operations/basic/sub.py
def subtract(a, b):
    return a - b

# math_operations/advanced/multiply.py
def multiply(a, b):
    return a * b

# math_operations/advanced/divide.py
def divide(a, b):
    return a / b


# Using the Functions 

# Using the placeholder calculate function
calculate()

# Perform basic operations
print("Addition:", add_basic(5, 3))
print("Subtraction:", subtract(10, 4))

# Perform advanced operations
print("Multiplication:", multiply(6, 2))
print("Division:", divide(8, 2))
