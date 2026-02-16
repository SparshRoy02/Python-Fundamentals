# 08 : Lists in Python

# Introduction
lst1 = [1, 2, 2, 3, 5, 4, 6]
lst2 = ["Red", "Green", "Blue"]
print(lst1)
print(lst2)


# List Indexes
colors = ["Red", "Green", "Blue", "Yellow", "Green"]
#          [0]      [1]     [2]      [3]      [4]


# Accessing list items:

# Positive Indexing
colors = ["Red", "Green", "Blue", "Yellow", "Green"]
print(colors[2])
print(colors[4])
print(colors[0])


# Negative Indexing
colors = ["Red", "Green", "Blue", "Yellow", "Green"]
#          [-5]    [-4]    [-3]     [-2]      [-1]
print(colors[-1])
print(colors[-3])
print(colors[-5])


# Check for item
colors = ["Red", "Green", "Blue", "Yellow", "Green"]
if "Yellow" in colors:
    print("Yellow is present.")
else:
    print("Yellow is absent.")


# Range of Index

# Print Particular Range
animals = ["cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow"]
print(animals[3:7])            # using positive indexes
print(animals[-7:-2])          # using negative indexes


# Print alternate values
animals = ["cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow"]
print(animals[::2])               # using positive indexes
print(animals[-8:-1:2])           # using negative indexes


# Add List Items

# append()
colors = ["violet", "indigo", "blue"]
colors.append("green")
print(colors)


# insert()
colors = ["violet", "indigo", "blue"]
colors.insert(1, "green")          # insert item at index 1
# updated list : colors = ["violet", "green", "indigo", "blue"]
print(colors)


# extend()
colors = ["violet", "indigo", "blue"]
rainbow = ["green", "yellow", "orange", "red"]
colors.extend(rainbow)
print(colors)


# Concatenate two lists
colors = ["violet", "indigo", "blue", "green"]
colors2 = ["yellow", "orange", "red"]
print(colors + colors2)


# Remove List Items

# pop()
colors = ["Red", "Green", "Blue", "Yellow", "Green"]
colors.pop()          # removes last item of the list
print(colors)

colors = ["Red", "Green", "Blue", "Yellow", "Green"]
colors.pop(1)         # removes item at index 1
print(colors)


# remove()
colors = ["violet", "indigo", "blue", "green", "yellow"]
colors.remove("blue")
print(colors)


# del
colors = ["violet", "indigo", "blue", "green", "yellow"]
del colors[3]
print(colors)


# clear()
colors = ["violet", "indigo", "blue", "green", "yellow"]
colors.clear()
print(colors)


# Change List Items

# Change Single Name
names = ["Harry", "Sarah", "Nadia", "Oleg", "Steve"]
names[2] = "Millie"
print(names)

# Change Multiple Name
names = ["Harry", "Sarah", "Nadia", "Oleg", "Steve"]
names[2:4] = ["juan", "Anastasia"]
print(names)

# Replace with Fewer Items
names = ["Harry", "Sarah", "Nadia", "Oleg", "Steve"]
names[1:4] = ["juan", "Anastasia"]
print(names)

# Replace with More Items
names = ["Harry", "Sarah", "Nadia", "Oleg", "Steve"]
names[2:3] = ["juan", "Anastasia", "Bruno", "Olga", "Rosa"]
print(names)


# List Comprehension

# accepts items with the small letter “o” in the new list
names = ["Milo", "Sarah", "Bruno", "Anastasia", "Rosa"]
namesWith_O = [item for item in names if "o" in item]
print(namesWith_O)

# accepts items which have more than 4 letters
names = ["Milo", "Sarah", "Bruno", "Anastasia", "Rosa"]
namesLong = [item for item in names if len(item) > 4]
print(namesLong)


# List Methods

# sort()
colors = ["violet", "indigo", "blue", "green"]
colors.sort()
print(colors)
 
num = [4,2,5,3,6,1,2,1,2,8,9,7]
num.sort()
print(num)


# sort descending
colors = ["violet", "indigo", "blue", "green"]
colors.sort(reverse=True)
print(colors)
 
num = [4,2,5,3,6,1,2,1,2,8,9,7]
num.sort(reverse=True)
print(num)


# reverse()
colors = ["violet", "indigo", "blue", "green"]
colors.reverse()
print(colors)
 
num = [4,2,5,3,6,1,2,1,2,8,9,7]
num.reverse()
print(num)


# index()
colors = ["violet", "green", "indigo", "blue", "green"]
print(colors.index("green"))
 
num = [4,2,5,3,6,1,2,1,3,2,8,9,7]
print(num.index(3))


# count()
colors = ["violet", "green", "indigo", "blue", "green"]
print(colors.count("green"))
 
num = [4,2,5,3,6,1,2,1,3,2,8,9,7]
print(num.count(2))


# copy()
colors = ["violet", "green", "indigo", "blue"]
newlist = colors.copy()
print(colors)
print(newlist)


# Nested Lists
students = [
    ["Harry", 20],
    ["Sarah", 22],
    ["Bruno", 21]
]
print(students)


# Accessing Nested Lists
students = [
    ["Harry", 20],
    ["Sarah", 22],
    ["Bruno", 21]
]
 
print(students[0][0])          # First student's name
print(students[1][1])          # Second student's age


# Modifying Nested Lists
students = [
    ["Harry", 20],
    ["Sarah", 22],
    ["Bruno", 21]
]
 
students[0][1] = 25          # Updating Harry's age
print(students)


# Iterating Through Nested Lists

# Looping through nested lists
students = [
    ["Harry", 20],
    ["Sarah", 22],
    ["Bruno", 21]
]
 
for student in students:
    print(student)


# Looping through values inside nested lists
students = [
    ["Harry", 20],
    ["Sarah", 22],
    ["Bruno", 21]
]
 
for student in students:
    for value in student:
        print(value)


# Nested Lists as Matrices (2D Lists)

# Matrix representation using nested lists
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
 
print(matrix[1][2])            # Row 1, Column 2
