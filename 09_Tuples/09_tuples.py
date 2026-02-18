# 09 : Tuples in Python

# Creating a Tuple
tuple1 = (1, 2, 2, 3, 5, 4, 6)
tuple2 = ("Red", "Green", "Blue")
print(tuple1)
print(tuple2)
print()


# Tuple Length
thistuple = ("apple", "banana", "cherry")
print(len(thistuple))
print()


# Tuple Items - Data Types

# String, int and boolean data types
tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)
print(tuple1)
print(tuple2)
print(tuple3)

# Tuple with strings, integers and boolean values
tuple1 = ("abc", 34, True, 40, "male")
print(tuple1)
print()


# Accessing Tuple Items - Positive Indexing
country = ("Spain", "Italy", "India", "England", "Germany")
print(country[1])
print(country[3])
print(country[0])
print()

# Accessing Tuple Items - Negative Indexing
country = ("Spain", "Italy", "India", "England", "Germany")
print(country[-1])
print(country[-3])
print(country[-4])
print()

# Check for Item
country = ("Spain", "Italy", "India", "England", "Germany")
if "Germany" in country:
    print("Germany is present.")
else:
    print("Germany is absent.")
print()


# Range of Index

# Printing elements within a particular rang
animals = ("cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow")
print(animals[3:7])
print(animals[-7:-2])
print()

# Printing all elements from a given index till the end
print(animals[4:])
print(animals[-4:])
print()

# Printing all elements from start to a given index
print(animals[:6])
print(animals[:-3])
print()

# Print alternate values
print(animals[::2])
print(animals[-8:-1:2])
print()

# Printing every 3rd consecutive within given range
print(animals[1:8:3])
print()


# Concatenation of Tuples
tup1 = (0, 1, 2, 3)
tup2 = ('Sparsh', 'J', 'Roy')
tup3 = tup1 + tup2
print(tup3)
print()


# Slicing of Tuple
tup = tuple('SPARSHJROY')
print(tup[1:])              # Removing First element
print(tup[::-1])            # Reversing the Tuple
print(tup[4:8])             # Printing elements of a Range
print()


# Deleting a Tuple
tup = (0, 1, 2, 3, 4)
del tup
# Uncommenting below line will raise an error
# print(tup)


# Change Tuple Values

# Convert the tuple into a list 
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print(x)
print()


# Packing a Tuple
fruits = ("apple", "banana", "cherry")
print(fruits)
print()

# Unpacking a Tuple
fruits = ("apple", "banana", "cherry")
(green, yellow, red) = fruits
print(green)
print(yellow)
print(red)
print()

# Using Asterisk *
tup = (1, 2, 3, 4, 5)
a, *b, c = tup
print(a)
print(b)
print(c)
print()


# Loop Through a Tuple (for loop)
thistuple = ("apple", "banana", "cherry")
for x in thistuple:
    print(x)
print()

# Loop Through Index Numbers
thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)):
    print(thistuple[i])
print()

# Using a While Loop
thistuple = ("apple", "banana", "cherry")
i = 0
while i < len(thistuple):
    print(thistuple[i])
    i = i + 1
print()


# Join Two Tuples
tuple1 = ("a", "b", "c")
tuple2 = (1, 2, 3)
tuple3 = tuple1 + tuple2
print(tuple3)
print()

# Multiply Tuples
fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2
print(mytuple)
print()


# Tuple Methods
t = (1, 2, 2, 3, 5)
print(t.index(2))       # index() method
print(t.count(2))       # count() method
