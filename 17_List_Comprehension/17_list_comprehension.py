# 17 : List Comprehension in Python

# Basic Example of List Comprehension
a = [2,3,4,5]
res = [val ** 2 for val in a]
print(res)


# Using For Loop
a = [1, 2, 3, 4, 5]
res = []
for val in a:
    res.append(val * 2)
print(res)

# Using List Comprehension
a = [1, 2, 3, 4, 5]
res = [val * 2 for val in a]
print(res)


# Conditional Statements in List Comprehension
a = [1, 2, 3, 4, 5]
res = [val for val in a if val % 2 == 0]
print(res)


# List Comprehension Using If-Else
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x if x != "banana" else "orange" for x in fruits]
print(newlist)


# Working with Iterables
newlist = [x for x in range(10)]
print(newlist)


# Using Condition with Range
newlist = [x for x in range(10) if x < 5]
print(newlist)


# Expression Manipulation
fruits = ["apple", "banana", "cherry"]
newlist = [x.upper() for x in fruits]
print(newlist)


# Setting Same Value for All Elements
fruits = ["apple","banana","cherry"]
newlist = ["hello" for x in fruits]
print(newlist)


# Examples of List Comprehension

# 1. Creating a List from a Range
a = [i for i in range(10)]
print(a)

# 2. Using Nested Loops
c = [(x, y) for x in range(3) for y in range(3)]
print(c)

# 3. Flattening a List of Lists
mat = [[1,2,3],[4,5,6],[7,8,9]]
res = [val for row in mat for val in row]
print(res)


# Real Example with Strings
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
print(newlist)
