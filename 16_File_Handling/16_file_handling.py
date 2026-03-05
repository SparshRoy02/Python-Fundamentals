# 16 : File Handling in Python


# Opening a File
f = open("demo.txt", "r")
print(f)


# Closing a File
file = open("demo.txt", "r")
# Perform operations
file.close()


# Checking File Properties
f = open("demo.txt", "r")
print("Filename:", f.name)
print("Mode:", f.mode)
print("Is Closed?", f.closed)

f.close()

print("Is Closed?", f.closed)


# Example Modes
# "rt" → read text
# "rb" → read binary
# "wt" → write text


# Reading a File

# Reading Entire File
file = open("demo.txt", "r")
content = file.read()
print(content)
file.close()

# Reading Specific Characters
with open("demofile.txt") as f:
    print(f.read(5))


# Reading Lines from a File

# Read One Line
with open("demofile.txt") as f:
    print(f.readline())

# Read Multiple Lines
with open("demofile.txt") as f:
    print(f.readline())
    print(f.readline())

# Loop Through File
with open("demofile.txt") as f:
    for line in f:
        print(line)


# Writing to a File
with open("demo.txt", "w") as file:
    file.write("Hello, Python!\n")
    file.write("File handling is easy with Python.")


# Appending to a File
with open("demofile.txt", "a") as f:
    f.write("Now the file has more content!")


# Using the with Statement
with open("demo.txt", "r") as file:
    content = file.read()
    print(content)


# Exception Handling with Files
try:
    file = open("demo.txt", "r")
    content = file.read()
    print(content)
finally:
    file.close()


# Creating a File
file = open("Text.txt", "x")


# Deleting a File
import os

os.remove("demofile.txt")


# Checking if File Exists Before Deleting
import os

if os.path.exists("demofile.txt"):
    os.remove("demofile.txt")
else:
    print("The file does not exist")


# Deleting a Folder
import os

os.rmdir("myfolder")
