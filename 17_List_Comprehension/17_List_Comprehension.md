## 17 : List Comprehension in Python

### Introduction
**List comprehension** is a concise and powerful way to create new lists by applying an **expression** to each item in an existing **iterable** (like a **list, tuple or range**). It helps you write **clean, readable and efficient code** compared to traditional loops.

List comprehension offers a **shorter syntax** when you want to create a **new list based on the values of an existing list**.

### Why to Use List Comprehension
List comprehension is commonly used in Python because it provides several advantages.
- **Cleaner code :** Combines **looping, filtering and transformation** in one line.
- **More readable :** Avoids **verbose loops** and **temporary variables**.
- **Faster execution :** Often faster than equivalent **for-loops**.


### Syntax of List Comprehension
```python
[expression for item in iterable if condition]
```  

#### Parameters
- **expression :** Operation or value to include in the **new list**.
- **item :** Current element from the **iterable**.
- **iterable :** Sequence like a **list, tuple or range**.
- **if condition (optional) :** Filter to include only items that satisfy the condition.


### Basic Example of List Comprehension
Suppose you want to **square every number in a list**.

#### Example
```python
a = [2,3,4,5]
res = [val ** 2 for val in a]

print(res)
```

### For Loop vs List Comprehension
A **for loop** takes multiple lines to build a new list by iterating and appending each item manually.

**List comprehension** does the same in just **one line**, making code **shorter and easier to read**.

### Using For Loop
```python
a = [1, 2, 3, 4, 5]

res = []

for val in a:
    res.append(val * 2)

print(res)
```

#### Explanation
- ``res = []`` creates an **empty list** to store results.
- ``for val in a:`` loops through each number in list ``a``.
- ``res.append(val * 2)`` doubles the current number and adds it to the list.


### Using List Comprehension
```python
a = [1, 2, 3, 4, 5]

res = [val * 2 for val in a]

print(res)
```

#### Explanation
- ``res = [val * 2 for val in a]`` creates a **new list by doubling each number** in ``a``.


### Conditional Statements in List Comprehension
**List comprehensions** can use **conditions** to select or transform items based on specific rules. This allows creating **customized lists more concisely** and improves **code readability and efficiency**.

#### Example
```python
a = [1, 2, 3, 4, 5]

res = [val for val in a if val % 2 == 0]

print(res)
```


### List Comprehension Using If-Else
The **expression** can also contain conditions not as a **filter** but as a way to **manipulate the outcome**.

#### Example
```python
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x if x != "banana" else "orange" for x in fruits]

print(newlist)
```
#### Explanation
- If the fruit is **not banana** it remains **unchanged**.
- If the fruit is **banana** it is **replaced with orange**.

### Working with Iterables
The **iterable** can be **any iterable object** like a **list, tuple, set, dictionary** or **range**.

#### Example
```python
newlist = [x for x in range(10)]

print(newlist)
```


### Using Condition with Range
#### Example
```python
newlist = [x for x in range(10) if x < 5]

print(newlist)
```

### Expression Manipulation
The **expression** is the **current item in the iteration** but it is also the **outcome which you can manipulate** before it becomes a **list element**.

#### Example
```python
fruits = ["apple", "banana", "cherry"]

newlist = [x.upper() for x in fruits]

print(newlist)
```


### Setting Same Value for All Elements
The **expression** can return a **constant value**.

#### Example
```python
fruits = ["apple","banana","cherry"]

newlist = ["hello" for x in fruits]

print(newlist)
```

### Examples of List Comprehension
### 1. Creating a List from a Range
**List comprehension** can quickly generate numbers within a **specific range**.
```python
a = [i for i in range(10)]

print(a)
```

### 2. Using Nested Loops
**Multiple loops** can be used inside **list comprehension**.
```python
c = [(x, y) for x in range(3) for y in range(3)]

print(c)
```

### 3. Flattening a List of Lists
A **nested list** can be converted into a **single list**.
```python
mat = [[1,2,3],[4,5,6],[7,8,9]]

res = [val for row in mat for val in row]

print(res)
```

#### Explanation
- ``mat`` is a list of lists.
- The comprehension first iterates through **each row** and then through **each value inside the row** to create a **single flattened list**.


### Real Example with Strings

#### Example
```python
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]

print(newlist)
```

#### Explanation
The condition checks whether the **letter** ``a`` **is present** in each **fruit name**.

### Conclusion
**List comprehension** is a powerful feature in Python that allows creating **new lists using a concise syntax**. It combines **looping, filtering and transformation** in a single line, making code **shorter, cleaner and more readable**. 

It can also handle **conditions, nested loops and transformations** efficiently, making it one of the **most commonly used Python features**.
