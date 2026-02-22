# 11 : Sets in Python

# Introduction to Sets Examples
my_set = {1, 2, 3, 4}
print(my_set)

info = {"Carla", 19, False, 5.9, 19}
print(info)

# Characteristics of Sets
# 1. Unordered Example
s = {"apple", "banana", "cherry"}
print(s)

# 2. No Duplicates Example
s = {1, 2, 2, 3, 4}
print(s)

# 3. Mutable Example
s = {1, 2, 3}
s.add(4)
print(s)

# 4. Heterogeneous Elements Example
s = {1, "hello", 3.14, True}
print(s)

# Creating a Set
# Using Curly Braces
s = {10, 20, 30}
print(s)

# Using set() Constructor
s = set([1, 2, 3])
print(s)

# Creating an Empty Set
empty_set = set()
print(type(empty_set))

# Accessing Set Items using Loop
s = {1, 2, 3}
for item in s:
    print(item)

# Adding Items to Set
# add() Method
s = {1, 2}
s.add(3)
print(s)

# update() Method
s = {1, 2}
s.update([3, 4])
print(s)

# Removing Items from Set
# remove() Method
s = {1, 2, 3}
s.remove(2)
print(s)

# discard() Method
s = {1, 2, 3}
s.discard(5)
print(s)

# pop() Method
s = {1, 2, 3}
s.pop()
print(s)

# clear() Method
s = {1, 2, 3, 4}
s.clear()
print(s)

# Deleting a Set
s = {1, 2}
del s

# Set Operations
a = {1, 2, 3}
b = {3, 4, 5}
print(a.union(b))                    # Union

print(a.intersection(b))             # Intersection

print(a.difference(b))               # Difference

print(a.symmetric_difference(b))     # Symmetric Difference

# Set Methods
# copy() Method
s = {1, 2}
new_s = s.copy()
print(new_s)

# isdisjoint() Method
a = {1, 2}
b = {3, 4}
print(a.isdisjoint(b))

# issubset() Method
a = {1, 2}
b = {1, 2, 3}
print(a.issubset(b))

# issuperset() Method
print(b.issuperset(a))

# Frozen Set
fs = frozenset([1, 2, 3])
print(fs)
