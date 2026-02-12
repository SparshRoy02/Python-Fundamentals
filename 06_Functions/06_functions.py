"""
================================================
06 : Functions in Python
=================================================
"""

# Defining a Function

def fun():
    print("Welcome")


# Calling a Function (Driver Code Example)

def fun():
    print("Welcome")
fun()  # Driver code to call a function


# Function Arguments
# Example: Even or Odd

def evenOdd(x):
    if (x % 2 == 0):
        return "Even"
    else:
        return "Odd"
print(evenOdd(16))
print(evenOdd(7))


# Types of Function Arguments
# 1. Default Arguments

def myFun(x, y=50):
    print("x: ", x)
    print("y: ", y)
myFun(10)

# 2. Keyword Arguments

def student(fname, lname):
    print(fname, lname)
student(fname='Now', lname='Practice')
student(lname='Practice', fname='Now')

# 3. Positional Arguments

def nameAge(name, age):
    print("Hi, I am", name)
    print("My age is ", age)

print("Case-1:")
nameAge("Suraj", 27)

print("\nCase-2:")
nameAge(27, "Suraj")

# 4. Arbitrary Arguments (*args and **kwargs)

def myFun(*args, **kwargs):
    print("Non-Keyword Arguments (*args):")
    for arg in args:
        print(arg)

    print("\nKeyword Arguments (**kwargs):")
    for key, value in kwargs.items():
        print(f"{key} == {value}")

myFun('Hey', 'Welcome', first='Sparsh', mid='J.', last='Roy')


# Function within Functions (Nested Functions)

def f1():
    s = 'I love Python'
    def f2():
        print(s)        
    f2()
f1()


# Anonymous Functions (Lambda Functions)

def cube(x):
    return x*x*x           # without lambda
cube_l = lambda x: x*x*x   # with lambda
print(cube(7))
print(cube_l(7))


# Return Statement in Function

def square_value(num):
    """This function returns the square value of the entered number"""
    return num**2
print(square_value(2))
print(square_value(-4))


# Pass by Reference and Pass by Value

# Mutable object example
def myFun(x):
    x[0] = 20
lst = [10, 11, 12, 13]
myFun(lst)
print(lst)   # list is modified

# Immutable object example
def myFun2(x):
    x = 20
a = 10
myFun2(a)
print(a)     # integer is not modified


# Recursive Functions

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
print(factorial(4))


# Structure of Recursive Function (Template Example)

def recursive_function(n):
    if n <= 0:  # Base case
        return "Base Case Reached"
    else:
        return recursive_function(n - 1)
print(recursive_function(3))

# Example 1: Factorial Calculation

def factorial(n):
    if n == 0:  # Base case
        return 1
    else:       # Recursive case
        return n * factorial(n - 1)
print(factorial(5))

# Example 2: Fibonacci Sequence

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
print(fibonacci(10))


# Python Lambda Functions (Uppercase Example)

a = 'Hello'
upper = lambda x: x.upper()
print(upper(a))

# Lambda Syntax Example

square = lambda x: x**2
print(square(5))
