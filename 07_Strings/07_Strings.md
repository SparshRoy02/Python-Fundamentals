## 07 : Strings in Python

In Python, a **string** is a **sequence of characters** written inside quotes. It can include letters, numbers, symbols, and spaces.
- Python does **not have a separate character type**.
- A single character is treated as a **string of length one**.
- Strings are commonly used for **text handling and manipulation**.

### Creating a String
Strings can be created using either **single ('...')** or **double ("...")** quotes. Both behave the same.

#### Example : 
Creating two equivalent strings one with single and other with double quotes.
```python
s1 = 'Hello'  # single quote
s2 = "Hello"  # double quote
print(s1)
print(s2)
```

#### Multi-line Strings
Use **triple quotes ('''...''' ) or ( """...""")** for strings that span multiple lines. **Newlines are preserved**.

#### Example : 
Define and print multi-line strings using both styles.
```python
s = """I am Learning
Python String """
print(s)
​
s = '''I'm a 
Student'''
print(s)
```

### Accessing characters in String
Strings are **indexed sequences**. 
- **Positive indices** start at **0** from the **left**
- **Negative indices** start at **-1** from the **right**.

#### Example 1 : 
Access specific characters through **positive indexing**.
```python
s = "SparshRoy"
print(s[0])   # first character
print(s[4])   # 5th character
```
#### Note : 
- Accessing an **index out of range** will cause an **IndexError**.
- Only **integers** are allowed as indices.
- Using a float or other types will result in a **TypeError**.

#### Example 2 : 
Read characters from the end using **negative indices**.
```python
s = "SparshRoy"
print(s[-7])   # 3rd character from start
print(s[-2])    # 2nd character from end
```

### String Slicing
Slicing is a way to extract a portion of a string by specifying the **start** and **end** indexes. The syntax for slicing is **string[start:end]**, where **start** starting index and **end** is stopping index (excluded).

#### Example :
In this example we are slicing through range and reversing a string.
```python
s = "SparshRoy"
print(s[1:4])    # characters from index 1 to 3
print(s[:3])     # from start to index 2
print(s[3:])     # from index 3 to end
print(s[::-1])   # reverse string
```

### String Iteration
Strings are **iterable** ; you can loop through characters one by one.

#### Example : 
Here, it print each character on its own line.
```python
s = "Python"
for char in s:
    print(char)
```
#### Explanation : 
- The **for loop** pulls characters in order and each iteration prints the next character.

### String Immutability
Strings are **immutable**, which means that they **cannot be changed after they are created**. If we need to manipulate strings then we can use methods like **concatenation**, **slicing** or **formatting** to create new strings based on original.

#### Example : 
In this example we are changing first character by building a new string.
```python
s = "sparshroy"
s = "S" + s[1:]   # create new string
print(s)
```

### Deleting a String
In Python, it is **not possible to delete individual characters** from a string since strings are immutable. However, we can delete an entire string variable using the **``del``** keyword.

#### Example : 
Here, we are using **del** keyword to delete a string.
```python
s = "Sparsh"
del s
```
**Note :** After deleting the string if we try to access ``s`` then it will result in a **NameError** because variable no longer exists.

### Updating a String
As strings are **immutable**, **updates** create **new strings** using slicing or methods such as ``replace()``.

#### Example : 
This code fix the first letter and replace a word.
```python
s = "hello world"
s1 = "H" + s[1:]                     # update first character
s2 = s.replace("world", "Sparsh")    # replace word
print(s1)
print(s2)
```
#### Explanation :
- **``s1``** : slice from index 1 onward and prepend ``"H"``.
- **``s2``** : ``replace("world", "Sparsh")`` returns a **new string**.


### Common String Methods
Python provides various **built-in methods** to manipulate strings. Below are some of the most useful methods:

**1. len()**
- The ``len()`` **function** returns the total number of characters in a string (including spaces and punctuation).

#### Example :
```python
s = "SparshRoy"
print(len(s))
```

**2. upper() and lower()** : 
- ``upper()`` method converts all characters to uppercase.
- ``lower()`` method converts all characters to lowercase.

#### Example :
```python
s = "Hello World"
print(s.upper())
print(s.lower())
```

**3. strip() and replace()** : 
- ``strip()`` removes leading and trailing whitespace from the string
- ``replace()`` replaces all occurrences of a specified substring with another.

#### Example :
```python
s = "   Sparsh   "
print(s.strip())    
​
s = "Python is fun"
print(s.replace("fun", "awesome"))
```


### Concatenating and Repeating Strings
We can concatenate strings using + operator and repeat them using * operator.

**1. Concatenation (``+`` operator)**
- Strings can be combined using ``+`` **operator**.
#### Example : 
Join two words with a space.
```python
s1 = "Hello"
s2 = "World"
print(s1 + " " + s2)
```

**2. Repetition (``*`` operator)**
- We can repeat a string multiple times using ``*`` **operator**.
#### Example : 
Repeat a greeting three times.
```python
s = "Hello "
print(s * 3)
```

### Formatting Strings
Python provides several ways to include variables inside strings.

#### 1. Using f-strings
- The simplest and most preferred way to format strings is by using **f-strings**.

#### Example : 
Embed variables directly using {} placeholders.
```python
name = "Sparsh"
age = 22
print(f"Name: {name}, Age: {age}")
```

#### 2. Using format()
- Another way to format strings is by using ``format()`` method.

#### Example : 
Use placeholders {} and pass values positionally.
```python
s = "My name is {} and I am {} years old.".format("Sparsh", 22)
print(s)
```

### String Membership Testing
- The ``in`` **keyword** checks if a particular substring is present in a string.

#### Example : 
Here, we are testing for the presence of substrings.
```python
s = "SparshRoy"
print("Sparsh" in s)
print("SjR" in s)
```
- Returns **True** if found
- Returns **False** if not found

### Summary
- In Python, a **string** is a sequence of characters enclosed in quotes and used for handling textual data.

- Strings support **indexing**, **slicing**, and **iteration**, allowing access and manipulation of characters. Since strings are **immutable**, any modification creates a new string rather than changing the original one.
- Python provides many **built-in methods** like `len()`, `upper()`, `lower()`, `strip()`, and `replace()` to perform common operations.
- Strings can be combined using **concatenation (`+`)**, repeated using the **`*` operator**, and formatted using **f-strings** or `format()`.
- Understanding strings is essential for text processing, user input handling, data manipulation, and real-world programming applications.
