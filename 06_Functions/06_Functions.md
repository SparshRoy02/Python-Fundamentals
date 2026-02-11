## 06 : Functions in Python

### Defining a Function

We can define a function in Python using the `def` keyword.  
A function might take input in the form of parameters.

#### Syntax of Python Function Declaration :

```python
def function_name(parameters):
    # body of function
    return expression
```

#### Example :
Here, we define a function using def that prints a welcome message when called.
```python
def fun():
    print("Welcome")
```
### Calling a Function
After creating a function in Python, we can call it by using the name of the function followed by parentheses containing parameters of that particular function.
```python
def fun():
    print("Welcome to GFG")
    
fun()  # Driver code to call a function
```

### Function Arguments
Arguments are the values passed inside the parentheses of the function.
A function can have any number of arguments separated by a comma.

#### Syntax :
```python
def function_name(parameters):
    """Docstring"""
    # body of the function
    return expression
```
#### Example: Even or Odd
```python
def evenOdd(x):
    if (x % 2 == 0):
        return "Even"
    else:
        return "Odd"

print(evenOdd(16))
print(evenOdd(7))
```

### Types of Function Arguments
Python supports various types of arguments that can be passed at the time of the function call.

1. Default Arguments
A default argument is a parameter that assumes a default value if a value is not provided in the function call for that argument.
```python
def myFun(x, y=50):
    print("x: ", x)
    print("y: ", y)

myFun(10)
```

2. Keyword Arguments
In keyword arguments, values are passed by explicitly specifying the parameter names, so the order doesn’t matter.
```python
def student(fname, lname):
    print(fname, lname)

student(fname='Now', lname='Practice')
student(lname='Practice', fname='Now')
```

3. Positional Arguments
In positional arguments, values are assigned to parameters based on their order in the function call.
```python
def nameAge(name, age):
    print("Hi, I am", name)
    print("My age is ", age)

print("Case-1:")
nameAge("Suraj", 27)

print("\nCase-2:")
nameAge(27, "Suraj")
```

4. Arbitrary Arguments
In Python, arbitrary arguments allow passing a variable number of arguments using special symbols:

- *args → Non-keyword arguments

- **kwargs → Keyword arguments
```python
def myFun(*args, **kwargs):
    print("Non-Keyword Arguments (*args):")
    for arg in args:
        print(arg)

    print("\nKeyword Arguments (**kwargs):")
    for key, value in kwargs.items():
        print(f"{key} == {value}")

# Function call with both types of arguments
myFun('Hey', 'Welcome', first='Geeks', mid='for', last='Geeks')
```

### Function within Functions (Nested Functions)
A function defined inside another function is called an inner function (or nested function).
It can access variables from the enclosing function’s scope.
```python
def f1():
    s = 'I love GeeksforGeeks'
    def f2():
        print(s)
        
    f2()

f1()
```

### Anonymous Functions (Lambda Functions)
An anonymous function is a function without a name.
The lambda keyword is used to create anonymous functions.
```python
def cube(x): 
    return x*x*x   # without lambda

cube_l = lambda x: x*x*x  # with lambda

print(cube(7))
print(cube_l(7))
```

### Return Statement in Function
The return statement ends a function and sends a value back to the caller.

It can return any data type, multiple values (as a tuple or none if no value is given.

#### Syntax :
```python
return [expression]
```

#### Example :
```python
def square_value(num):
    """This function returns the square value of the entered number"""
    return num**2

print(square_value(2))
print(square_value(-4))
```

### Pass by Reference and Pass by Value
In Python, variables are references to objects.
Python uses pass-by-object-reference.

- **Mutable objects** → Changes affect original object

- **Immutable objects** → Original value remains unchanged
```python
# Function modifies the first element of list
def myFun(x):
    x[0] = 20

lst = [10, 11, 12, 13]
myFun(lst)
print(lst)   # list is modified

# Function tries to modify an integer
def myFun2(x):
    x = 20

a = 10
myFun2(a)
print(a)     # integer is not modified
```
