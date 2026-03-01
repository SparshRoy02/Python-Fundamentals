# 14 : Modules in Python

# Creating a module
# calc.py
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y


# Importing calc module
import calc
print(calc.add(10, 2))


# Import Entire Module
import math
print(math.sqrt(16))


# Import Specific Functions
from math import sqrt, factorial
print(sqrt(16))
print(factorial(6))


# Import Everything (*)
from math import *
print(sqrt(25))


# Import With Alias
import math as m
print(m.pi)


# Built-in Module Example: math module
import math
print(math.sin(0))
print(math.pi)


# Built-in Module Example: random module
import random
print(random.randint(1, 5))


# User-Defined Module Example
import module
print(module.add(6, 2))


# External (Third-Party) Module Example
import requests
r = requests.get("https://example.com")
print(r.status_code)


# Package Module Usage
from mypkg import utils
print(utils.some_func())


# Variables Inside Module
import mymodule
print(mymodule.person1["age"])


# dir() Function
import math
print(dir(math))


# Module Search Path
import sys
for path in sys.path:
    print(path)


# Naming & Renaming Modules (Alias)
import mymodule as mx
print(mx.person1["age"])
