# Basic Example – Handling Simple Exception
n = 10
try:
    res = n / 0
except ZeroDivisionError:
    print("Can't be divided by zero!")


# Error Example (Syntax Error – commented to avoid crash)

# print("Hello world"  # Missing closing parenthesis


# Exception Example
n = 10
res = n / 0


# try Statement Example
try:
    print(x)


# except Block Example
try:
    print(x)
except:
    print("An exception occurred")


# else Block Example
try:
    print("Hello")
except:
    print("Error")
else:
    print("Nothing went wrong")


# finally Block Example
try:
    print(x)
except:
    print("Error")
finally:
    print("Execution finished")


# Catching Specific Exceptions
try:
    x = int("str")
except ValueError:
    print("Not Valid!")


# Catching Multiple Exceptions
try:
    total = int("10") + int("twenty")
except (ValueError, TypeError) as e:
    print("Error:", e)


# Catch-All Exception
try:
    print(x)
except:
    print("Something went wrong")


# Complete Syntax Structure 
try:
    pass            # risky code
except Exception:
    pass            # handle error
else:
    pass            # if no error
finally:
    pass            # always execute


# Raising Exception
x = -1
if x < 0:
    raise Exception("No numbers below zero")


# Raising Specific Exception
x = "hello"
if not type(x) is int:
    raise TypeError("Only integers allowed")


# Custom Exception
class AgeError(Exception):
    pass

def set_age(age):
    if age < 0:
        raise AgeError("Age cannot be negative.")
