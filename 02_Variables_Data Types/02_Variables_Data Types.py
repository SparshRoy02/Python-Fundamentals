# VARIABLES 

name = "Python"
age = 22
price = 199.99
print("Name:", name)
print("Age:", age)
print("Price:", price)

# Multiple Variable Assignment
a, b, c = 10, 20, 30
print("\nMultiple Assignment:", a, b, c)

# Same Value to Multiple Variables
x = y = z = 100
print("\nSame Value Assignment:", x, y, z)

# Variable Reassignment
count = 5
print("\nBefore Reassignment:", count)
count = 15
print("After Reassignment:", count)

# Dynamic Typing
value = 10
print("\nValue:", value, "| Type:", type(value))
value = "Python Programming"
print("Value:", value, "| Type:", type(value))

# Object Identity (Memory Location)
a = 10
b = 10
print("\nObject Identity:")
print("id(a):", id(a))
print("id(b):", id(b))

# Variable Deletion
temp = 50
print("\nBefore deletion:", temp)
del temp
# print(temp)  # Uncommenting this line will raise NameError



# DATA TYPES

integer_num = 10
float_num = 3.14
complex_num = 2 + 3j
print("Integer:", integer_num, "|", type(integer_num))
print("Float:", float_num, "|", type(float_num))
print("Complex:", complex_num, "|", type(complex_num))

# String Data Type
text = "Hello Python"
print("\nString:", text, "|", type(text))

# Sequence Data Types

# List 
numbers_list = [1, 2, 3]
numbers_list.append(4)
print("\nList:", numbers_list, "|", type(numbers_list))

# Tuple 
numbers_tuple = (10, 20, 30)
print("Tuple:", numbers_tuple, "|", type(numbers_tuple))

# Range
number_range = range(1, 5)
print("Range:", list(number_range), "|", type(number_range))

# Set Data Type
unique_values = {1, 2, 3, 3, 4}
print("\nSet:", unique_values, "|", type(unique_values))

# Dictionary Data Type
student = {
    "name": "Sparsh",
    "age": 23,
    "course": "Python"
}
student["age"] = 23
print("\nDictionary:", student, "|", type(student))

# Boolean Data Type
is_python_easy = True
print("\nBoolean:", is_python_easy, "|", type(is_python_easy))

# None Data Type
result = None
print("\nNone:", result, "|", type(result))

# Type Casting (Conversion)
x = "100"
y = int(x)
z = float(y)
print("\nType Casting:")
print(y, type(y))
print(z, type(z))

# Mutable vs Immutable
print("\nMutable vs Immutable:")

# Immutable example
a = 10
print("Before:", a, "| id:", id(a))
a = 20
print("After:", a, "| id:", id(a))

# Mutable example
lst = [1, 2]
print("Before:", lst, "| id:", id(lst))
lst.append(3)
print("After:", lst, "| id:", id(lst))
