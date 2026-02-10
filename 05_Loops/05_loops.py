print("=== 1. FOR LOOP ===")
# Example: Iterating over a list
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)

print("\n=== 2. LOOPING THROUGH A STRING ===")
# Example: Iterating over a string
for x in "banana":
    print(x)

print("\n=== 3. BREAK STATEMENT (for loop) ===")
# Example: break when item is 'banana'
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)
    if x == "banana":
        break

print("\n=== 4. CONTINUE STATEMENT (for loop) ===")
# Example: skip 'banana'
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        continue
    print(x)

print("\n=== 5. range() FUNCTION ===")
# Example: range with single argument
for x in range(6):
    print(x)

print("\n=== 6. range() WITH START VALUE ===")
# Example: range with start and stop
for x in range(2, 6):
    print(x)

print("\n=== 7. range() WITH STEP VALUE ===")
# Example: range with step
for x in range(2, 30, 3):
    print(x)

print("\n=== 8. ELSE IN FOR LOOP ===")
# Example: else block in for loop
for x in range(6):
    print(x)
else:
    print("Finally finished!")

print("\n=== 9. NESTED LOOPS ===")
# Example: nested loops
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]
for x in adj:
    for y in fruits:
        print(x, y)

print("\n=== 10. PASS STATEMENT ===")
# Example: pass statement
for x in [0, 1, 2]:
    pass
print("Pass statement executed successfully")

print("\n=== 11. WHILE LOOP ===")
# Example: basic while loop
i = 1
while i < 6:
    print(i)
    i += 1

print("\n=== 12. BREAK STATEMENT (while loop) ===")
# Example: break in while loop
i = 1
while i < 6:
    print(i)
    if i == 3:
        break
    i += 1

print("\n=== 13. CONTINUE STATEMENT (while loop) ===")
# Example: continue in while loop
i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)

print("\n=== 14. ELSE IN WHILE LOOP ===")
# Example: else in while loop
i = 1
while i < 6:
    print(i)
    i += 1
else:
    print("i is no longer less than 6")
