## 14 : Modules in Python

### What is a Module?
A **module** in Python is a ``.py`` **file** that contains **functions, classes, variables, or runnable code** which can be reused in other Python programs.

Think of a module as a **code library**.

### Why Modules?
- **Improve code reusability**
- **Organize code logically**
- **Reduce redundancy**
- **Improve maintainability**

### Creating a Module
A **module is created** by writing **Python code** in a file and saving it with a ``.py`` **extension**.

#### Example : 

Creating ``calc.py``
```python
# calc.py
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y
```

### Importing a Module
The ``import`` **keyword** is used to load a module into another Python file.

#### Example :
```python
import calc

print(calc.add(10, 2))
```

#### Explanation
- ``import calc`` loads the module.
- ``calc.add()`` accesses function using **dot notation**.

### Types of Import Statements
### 1. Import Entire Module
Imports **complete module**.

```python
import math
print(math.sqrt(16))
```

### 2. Import Specific Functions
Imports only **selected functions** from a module.

```python
from math import sqrt, factorial

print(sqrt(16))
print(factorial(6))
```

### 3. Import Everything (*)
Imports **all public names** from a module.

```python
from math import *

print(sqrt(25))
```

**NOTE :** **Not recommended in large projects** due to **namespace conflicts**.

### 4. Import With Alias
Use ``as`` **keyword** to give module a **shorter name**.

```python
import math as m

print(m.pi)
```

### Built-in Modules
Modules that come **pre-installed with Python**.

#### Examples :
- ``math``
- ``random``
- ``datetime``
- ``json``
- ``os``
- ``sqlite3``
- ``statistics``
- ``tkinter``
- ``turtle``

#### Example : math module

```python
import math

print(math.sin(0))
print(math.pi)
```

#### Example : random module

```python
import random

print(random.randint(1, 5))
```

### User-Defined Modules
Modules **created by the programmer** or user.

#### Example

``module.py``
```python
def add(a, b):
    return a + b

def sub(a, b):
    return a - b
```


 ``main.py``
```python
import module

print(module.add(6, 2))
```


### External (Third-Party) Modules
Modules **installed using** ``pip``.

#### Examples :
- ``requests``
- ``numpy``
- ``pandas``


#### Example

```python
import requests

r = requests.get("https://example.com")
print(r.status_code)
```


### Package Modules
A **package** is a **folder** containing multiple modules (usually with ``__init__.py``).

#### Structure :

```python
mypkg/
    __init__.py
    calc.py
    utils.py
```

#### Usage :

```python
from mypkg import utils
print(utils.some_func())
```

### Variables Inside Module
Modules can store **variables**, **lists**, **dictionaries** and **objects** along with functions.

``mymodule.py``
```python
person1 = {
    "name": "John",
    "age": 36
}
```

#### Usage :

```python
import mymodule
print(mymodule.person1["age"])
```

### dir() Function  
``dir()`` lists all **attributes**, **functions**, and **variables** of a module.

```python
import math

print(dir(math))
```


### Module Search Path
Python searches modules from **predefined directories** stored in ``sys.path``.

```python
import sys

for path in sys.path:
    print(path)
```

### Naming & Renaming Modules
- Module file **must end with** ``.py``.
- Use ``as`` **keyword** to rename.

#### Using Alias :

```python
import mymodule as mx
print(mx.person1["age"])
```
### Summary 

| **Topic** | **Definition** |
|-----------|---------------|
| **Module** | A `.py` file containing reusable Python code |
| **Import** | Loads a module into another file |
| **Built-in Module** | Comes pre-installed with Python |
| **User-defined Module** | Created by the programmer |
| **Third-party Module** | Installed using `pip` |
| **Package** | Folder containing multiple modules |
| **Alias** | Short name given using `as` |
| **dir()** | Lists module attributes |
| **sys.path** | Shows module search path |
	    

###  Conclusion

Modules are a **fundamental building block of Python programming** that promote **code reusability, modularity, and maintainability**. Instead of writing all logic in a single file, Python allows developers to divide programs into smaller, manageable components called **modules**.

Understanding modules is essential because :
- They make applications **scalable** 
- They improve **readability**
- They reduce **code duplication**
- They help in building **large professional projects**
- They prepare you for **real-world software development**
