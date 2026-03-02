## 15 : Exception Handling in Python

### Introduction 
Python **Exception Handling** allows a program to **gracefully handle unexpected events** (like invalid input or missing files) without **crashing**. 

Instead of stopping execution, Python:
- **Detects errors**
- **Handles them**
- **Continues execution when possible**
It helps in building **robust, stable and production-ready applications**.

#### Basic Example : 
``Handling Simple Exception``
```python
n = 10
try:
    res = n / 0
except ZeroDivisionError:
    print("Can't be divided by zero!")
```

**Explanation :** 
Dividing a number by ``0`` raises a **ZeroDivisionError**. The **try block** contains code that may fail and **except block** catches the error, printing a safe message instead of stopping the program


### Difference Between Errors and Exceptions
### Error :
Serious problems in the program logic that cannot be handled. Examples include **syntax errors** or **memory errors**.
```python
# Syntax Error (Error)
print("Hello world" # Missing closing parenthesis
```

### Exception :
Less severe problems that occur at **runtime** and can be managed using exception handling (e.g., invalid input, missing files).
```python
n = 10
res = n / 0
```

### Exception Handling Keywords
Python provides **four main keywords** :

### 1. try Statement
The ``try`` block contains **risky code** that may cause an error.
```python
try:
    print(x)
```

### 2. except Block
Handles the error raised in ``try`` block.
```python
try:
    print(x)
except:
    print("An exception occurred")
```


### 3. else Block
Runs **only if no exception occurs** in the try block.
```python
try:
    print("Hello")
except:
    print("Error")
else:
    print("Nothing went wrong")
```


### 4. finally Block
Executes **regardless of whether an exception occurs or not**.
```python
try:
    print(x)
except:
    print("Error")
finally:
    print("Execution finished")
```


### Python Catching Exceptions

### 1. Catching Specific Exceptions
Catching specific exceptions makes code to respond to different exception types differently. It precisely makes your code **safer** and **easier** to **debug**. It avoids masking bugs by only reacting to the exact problems you expect.
```python
try:
    x = int("str")
except ValueError:
    print("Not Valid!")
```

### 2. Catching Multiple Exceptions
We can catch **multiple exceptions** in a **single block** if we need to handle them in the same way or we can **separate them** if different types of exceptions require different **handling**.
```python
try:
    total = int("10") + int("twenty")
except (ValueError, TypeError) as e:
    print("Error:", e)
```


### 3. Catch-All Exception Handlers and Their Risks
Sometimes we may use a **catch-all handler** to catch any **exception**, but it can **hide useful debugging info**.
```python
try:
    print(x)
except:
    print("Something went wrong")
```



### Complete Syntax Structure
Python provides **four main keywords** for **handling exceptions** : **try, except, else** and **finally** each plays a unique role. Let's see syntax,
```python
try:
    # risky code
except SomeException:
    # handle error
else:
    # if no error
finally:
    # always execute
```

### Raising Exceptions
We raise an exception in Python using the ``raise`` **keyword** followed by an **instance** of the **exception class** that we want to **trigger**.
```python
x = -1
if x < 0:
    raise Exception("No numbers below zero")
```


### Raising Specific Exception
Raise a **TypeError** if ``x`` is **not an integer**.
```python
x = "hello"
if not type(x) is int:
    raise TypeError("Only integers allowed")
```



### Custom Exceptions
You can also create **custom exceptions** by defining a **new class** that **inherits** from Python’s **built-in Exception class**. This is useful for application-specific errors.
```python
class AgeError(Exception):
    pass

def set_age(age):
    if age < 0:
        raise AgeError("Age cannot be negative.")
```



### Advantages of Exception Handling
- Improves **program reliability**
- **Cleaner code**
- Better **debugging** with **traceback**
- Separates **error-handling logic**



### Disadvantages of Exception Handling
- Slight **performance overhead**
- Can increase **code complexity**
- **Poor handling** may hide **bugs**
- **Security risks** if sensitive **info** exposed



### Summary

**Exception Handling** in Python is a **structured mechanism** used to manage **runtime errors** gracefully without **terminating** the program abruptly. It ensures **program stability, improves reliability,** and **enhances user experience** by handling unexpected situations such as invalid input, division by zero, missing files, or incorrect data types.

Python provides four primary keywords for exception management:
- ``try`` – Contains code that may raise an exception
- ``except`` – Handles specific or general exceptions
- ``else`` – Executes when no exception occurs
- ``finally`` – Executes regardless of whether an exception occurs

Developers can:
- Catch **specific exceptions** for precise error handling
- Handle **multiple exceptions** efficiently
- Use **catch-all handlers cautiously**
- Manually raise exceptions using the ``raise`` keyword
- Create **custom exceptions** for application-specific logic

Proper exception handling:
- Prevents program crashes
- Keeps business logic clean
- Improves debugging through meaningful error messages
- Enables resource management (e.g., file closing using finally)

