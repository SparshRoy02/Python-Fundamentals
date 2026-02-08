# 1. If Statement

age = 20
if age >= 18:
    print("Eligible to vote")
print("-" * 40)


# 2. If–Else Statement

number = 5
if number % 2 == 0:
    print("Even")
else:
    print("Odd")
print("-" * 40)


# 3. Elif Statement

age = 25
if age <= 12:
    print("Child")
elif age <= 19:
    print("Teenager")
elif age <= 35:
    print("Young Adult")
else:
    print("Adult")
print("-" * 40)


# 4. If–Elif–Else Ladder

marks = 78
if marks >= 90:
    grade = "A+"
elif marks >= 75:
    grade = "A"
elif marks >= 60:
    grade = "B"
else:
    grade = "C"
print("Grade:", grade)
print("-" * 40)


# 5. Nested Conditionals

username = "admin"
password = "1234"
if username == "admin":
    if password == "1234":
        print("Login successful")
    else:
        print("Wrong password")
else:
    print("Invalid username")
print("-" * 40)


# 6. Ternary Conditional Statement

age = 20
status = "Adult" if age >= 18 else "Minor"
print("Status:", status)
print("-" * 40)


# 7. Input-Based Conditionals

age = int(input("Enter your age: "))
if age >= 60:
    print("Senior Citizen")
elif age >= 18:
    print("Adult")
else:
    print("Minor")
print("-" * 40)


# 8. Match-Case Statement (Python 3.10+)

number = 2
match number:
    case 1:
        print("One")
    case 2 | 3:
        print("Two or Three")
    case _:
        print("Other number")
print("-" * 40)
