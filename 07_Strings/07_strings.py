# 1. Creating a String

s1 = 'Hello'  # single quote
s2 = "Hello"  # double quote
print(s1)
print(s2)
print()


# 2. Multi-line Strings

s = """I am Learning
Python String """
print(s)

s = '''I'm a 
Student'''
print(s)
print()


# 3. Accessing Characters in String

# Example 1: Positive Indexing
s = "SparshRoy"
print(s[0])   # first character
print(s[4])   # 5th character

# Example 2: Negative Indexing
print(s[-7])  # 3rd character from start
print(s[-2])  # 2nd character from end
print()


# 4. String Slicing

s = "SparshRoy"
print(s[1:4])    # characters from index 1 to 3
print(s[:3])     # from start to index 2
print(s[3:])     # from index 3 to end
print(s[::-1])   # reverse string
print()


# 5. String Iteration

s = "Python"
for char in s:
    print(char)
print()


# 6. String Immutability

s = "sparshroy"
s = "S" + s[1:]        # create new string
print(s)
print()


# 7. Deleting a String

s = "Sparsh"
del s
print("String variable deleted successfully.")
print()


# 8. Updating a String

s = "hello world"
s1 = "H" + s[1:]                        # update first character
s2 = s.replace("world", "Sparsh")       # replace word

print(s1)
print(s2)
print()


# 9. Common String Methods

# len()
s = "SparshRoy"
print("Length:", len(s))

# upper() and lower()
s = "Hello World"
print(s.upper())
print(s.lower())

# strip() and replace()
s = "   Sparsh   "
print(s.strip())

s = "Python is fun"
print(s.replace("fun", "awesome"))
print()


# 10. Concatenating Strings

s1 = "Hello"
s2 = "World"
print(s1 + " " + s2)
print()


# 11. Repeating Strings

s = "Hello"
print(s * 3)
print()


# 12. Formatting Strings

# Using f-strings
name = "Sparsh"
age = 22
print(f"Name: {name}, Age: {age}")

# Using format()
s = "My name is {} and I am {} years old.".format("Sparsh", 22)
print(s)
print()


# 13. String Membership Testing

s = "SparshRoy"
print("Sparsh" in s)
print("SjR" in s)
