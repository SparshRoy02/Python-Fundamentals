## 02 : Variables and Data Types 

### Variables

- Variables are containers that store information that can be manipulated and referenced later by the programmer within the code.
- In Python, the programmer does not need to declare the variable type explicitly; we just need to assign the value to the variable.


Example:
```shell
name = "Sparsh"       # type str
age = 23              # type int
passed = True         # type bool
```

It is always advisable to keep variable names descriptive and to follow a set of conventions while creating variables:

- Variable names can only contain alphanumeric characters and underscores (A-Z, 0-9, and _).
- Variable names must start with a letter or the underscore character.
- Variables are case sensitive.
- Variable names cannot start with a number.

Example:

```shell
Color = "yellow"    # valid variable name
cOlor = "red"       # valid variable name
_color = "blue"     # valid variable name
 
5color = "green"    # invalid variable name
$color = "orange"   # invalid variable name


2name = "Bob"       # invalid variable names as it starts with a number  
class = 10          # invalid variable names as 'class' is a keyword 
```
### Data Types

Data type specifies the type of value a variable requires to do various operations without causing an error. By default, Python provides the following built-in data types:

- **Numeric Data :** Int, Float, Complex
  - **Int** : 3, -8, 0
  - **Float** : 7.349, -9.0, 0.0000001
  - **Complex** : 6 + 2j

- **Text data :** Str
   - **Str** : "Hello World!!!", "Python Programming"

- **Boolean data :**
   - Boolean data consists of values **True** or **False**.

- **Sequenced data :** List, Tuple, Range
   - **List** : A list is an ordered collection of data with elements separated by a comma and enclosed within square brackets. Lists are mutable and can be modified after creation..
   - **Tuple** : A tuple is an ordered collection of data with elements separated by a comma and enclosed within parentheses.
   - **Range** : Returns a sequence of numbers as specified by the user. If not specified by the user, it starts from 0 by default and increments by 1.

- **Mapped data :** Dict
   - **Dict** : A dictionary is an unordered collection of data containing a key:value pair. The key-value pairs are enclosed within curly brackets.

- **Binary data :** bytes, bytearray, memoryview
   - **bytes** : It is used to convert objects into byte objects
   - **bytearray** : It is used to convert objects into bytearray objects
   - **memoryview** : It returns a memory view object from a specified object

- **Set data :** Set is an unordered collection of elements in which no element is repeated.

- **None :** None is used to define a null value

```shell
x = 10  
print(type(x))          # <class 'int'>  
 
PI = 3.14  
print(type(PI))         # <class 'float'>  

name = "Sparsh"  
print(type(name))       # <class 'str'>  

isStudent = True  
print(type(isAdult))    # <class 'bool'>  

empty_var = None  
print(type(empty_var))  # <class 'NoneType'> 
```

### Type Conversion & Type Casting 

Type conversion is when we convert(cast) variables from one type to another. It can 
happen in 2 ways: 

- **Type conversion :** Implicit, done automatically by Python 
```shell
a = 5  
b = 3.0  
print(a + b)      # Python converts ans in float by default
```

- **Type Casting :** Explicitly, done by the programmer 
```shell
x = 10           # int
y = float(x)     # convert to float  
z = str(x)       # convert to string 
```
