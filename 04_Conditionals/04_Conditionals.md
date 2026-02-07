## 04 : Conditionals in Python

### Introduction to Conditionals
- Conditional statements allow a Python program to make decisions and execute different blocks of code based on whether a condition evaluates to `True` or `False`.
- Conditional statements allow you to execute code based on certain conditions.
- Python uses if, elif, and else for decision-making.

They are essential for: 
- Decision-making
- Input validation
- Flow control
- Real-world logic such as authentication, grading, and payments

### If Statement
The if statement executes a block of code only when the condition is true.

Syntax
```python
if condition:
    statement
```

Example
```python
age = 20

if age >= 18:
    print("Eligible to vote")
```


### If–Else Statement
The else block executes when the if condition is false.

```python
number = 5

if number % 2 == 0:
    print("Even")
else:
    print("Odd")
```


### Elif Statement

The Elif statement in Python stands for "else if." It allows us to check multiple conditions, providing a way to execute different blocks of code based on which condition is true. 

```python
age = 25

if age <= 12:
    print("Child.")
elif age <= 19:
    print("Teenager.")
elif age <= 35:
    print("Young adult.")
else:
    print("Adult.")
```


### If–elif–else Ladder

Used to evaluate multiple conditions sequentially.

```python
marks = 78

if marks >= 90:
    grade = "A+"
elif marks >= 75:
    grade = "A"
elif marks >= 60:
    grade = "B"
else:
    grade = "C"
```

Only the first true condition is executed.


### Nested Conditionals

A conditional inside another conditional.

```python
username = "admin"
password = "1234"

if username == "admin":
    if password == "1234":
        print("Login successful")
    else:
        print("Wrong password")
else:
    print("Invalid username")
```
Nested conditionals are useful for multi-level validation.


### Ternary Conditional Statement
A ternary conditional statement is a compact way to write an if-else condition in a single line. It’s sometimes called a "conditional expression."

```python
# Assign a value based on a condition
age = 20
s = "Adult" if age >= 18 else "Minor"
print(s)
```
#### Here:
- If age >= 18 is True, status is assigned "Adult".
- Otherwise, status is assigned "Minor".


### Input-Based Conditionals

Conditionals that depend on runtime user input.

```python
age = int(input("Enter age: "))

if age >= 60:
    print("Senior Citizen")
elif age >= 18:
    print("Adult")
else:
    print("Minor")
```


### Match-Case Statement
Match-case statement is Python's version of a switch-case found in other languages. It allows us to match a variable's value against a set of patterns.


```python
number = 2
​
match number:
    case 1:
        print("One")
    case 2 | 3:
        print("Two or Three")
    case _:
        print("Other number")
```

### Summary
- Conditionals control the flow of a Python program
- They are based on Boolean logic
- Python relies on indentation instead of braces
- Conditionals are essential for real-world applications
