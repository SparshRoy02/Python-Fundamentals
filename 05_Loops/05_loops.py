"""
05 : Loops in Python
This file contains runnable examples for all loop concepts covered in loops.md
"""

print("===== FOR LOOP =====")

# Example: Iterating over a list
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)

print("\n===== LOOPING THROUGH A STRING =====")

# Example: Iterating over a string
for x in "banana":
    print(x)

print("\n===== BREAK STATEMENT (for loop) =====")

# Example: break when item is 'banana'
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)
    if x == "banana":
        break

print("\n===== CONTINUE STATEMENT (for loop) =====")

# Example: skip 'banana'
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        continue
    print(x)

print("\n===== range() FUNCTION =====")

# Example: range with single argument
for x in range(6):
    print(x)

print("\n===== range() WITH START VALUE =====")

# Example: range with start and stop
for x in range(2, 6):
    print(x)

print("\n===== range() WITH STEP VALUE =====")

# Example: range with step
for x in range(2, 30, 3):
    print(x)

print("\n===== ELSE IN FOR LOOP =====")

# Example: else block in for loop
for x in range(6):
    print(x)
else:
    print("Finally finished!")

print("\n===== NESTED LOOPS =====")

# Example: nested loops
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
    for y in fruits:
        print(x, y)

print("\n===== PASS STATEMENT =====")

# Example: pass statement
for x in [0, 1, 2]:
    pass

print("Pass statement executed successfully")

print("\n===== WHILE LOOP =====")

# Example: basic while loop
i = 1
while i < 6:
    print(i)
    i += 1

print("\n===== BREAK STATEMENT (while loop) =====")

# Example: break in while loop
i = 1
while i < 6:
    print(i)
    if i == 3:
        break
    i += 1

print("\n===== CONTINUE STATEMENT (while loop) =====")

# Example: continue in while loop
i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)

print("\n===== ELSE IN WHILE LOOP =====")

# Example: else in while loop
i = 1
while i < 6:
    print(i)
    i += 1
else:
    print("i is no longer less than 6")

print("\n===== END OF LOOPS.py =====")
