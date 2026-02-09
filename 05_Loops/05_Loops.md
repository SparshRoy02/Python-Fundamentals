## 05 : Loops in Python

### Introduction to Loops
Loops allow a program to execute a block of code repeatedly based on a **condition** or **sequence**. They help reduce **redundancy** and improve **efficiency**.

**Loops are mainly used for** :
- Repetition
- Iteration over collections
- Automation of tasks
- Data processing

**Python provides** :
- for loop
- while loop

---

### for Loop
- A **for loop** is used for iterating over a sequence such as **a list, a tuple, a dictionary, a set, or a string**.
- This is less like the for keyword in other programming languages, and works more like an **iterator method** as found in other object-orientated programming languages.
- With the for loop we can execute a set of statements, **once for each item** in a list, tuple, set etc.
- The for loop does **not require an indexing variable** to be set beforehand.

#### Example :
Print each fruit in a fruit list.  
```python
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
```
- **NOTE** : The for loop does not require an indexing variable to set beforehand.

### Looping Through a String
Even strings are iterable objects, they contain a sequence of characters.

#### Example :
Loop through the letters in the word **"banana"**.
```python
for x in "banana":
  print(x)
```

### The break Statement
With the **break statement** we can stop the loop before it has **looped through all the items**.

#### Example :
Exit the loop when x is **"banana"**.
```python
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break
```

### The continue Statement
With the **continue statement** we can stop the **current iteration** of the loop, and continue with the **next iteration**.

#### Example :
Do not print banana.
```python
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)
```

### The range() Function
- To loop through a set of code a **specified number of times**, we can use the **``range()``** function.
- The range() function returns a **sequence of numbers**, starting from ``0`` by default, and increments by ``1`` (by default), and ends at a specified number.

#### Example :
Using the range() function:
```python
for x in range(6):
  print(x)
```
- **Note** : That ``range(6)`` is not the values of 0 to 6, but the **values 0 to 5**.

### Using the Start Parameter
- The starting value can be specified using **range(start, stop)**.
- The stop value is **not included**.
- The range() function defaults to 0 as a starting value, however it is possible to specify the starting value by adding a parameter: range(2, 6), which means values from 2 to 6 (but not including 6).

#### Example :
Using the start parameter.
```python
for x in range(2, 6):
  print(x)
```

### Using the Step Parameter
- The increment value can be specified using **range(start, stop, step)**.
- The range() function defaults to increment the sequence by 1, however it is possible to specify the increment value by adding a third parameter: range(2, 30, 3).

#### Example :
Increment the sequence with ``3`` (default is 1).
```python
for x in range(2, 30, 3):
  print(x)
```

### Else in For Loop
The **else** keyword in a for loop specifies a block of code to be executed when the **loop is finished**.

#### Example :
Print all numbers from 0 to 5, and print a message when the loop has ended.
```python
for x in range(6):
  print(x)
else:
  print("Finally finished!")
```
- **Note** : The else block will **NOT** be executed if the loop is stopped by a ``break`` statement.

### Nested Loops
A **nested loop** is a loop inside a loop. The **inner loop** will be executed one time for each iteration of the **outer loop**.

#### Example :
Print each adjective for every fruit.
```python
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)
```

### The pass Statement
for loops cannot be empty, but if you for some reason have a for loop with no content, put in the pass statement to avoid getting an error.

#### Example :
```python
for x in [0, 1, 2]:
  pass
```


### while Loop
With the **while loop** we can execute a set of statements **as long as a condition is True**.

#### Example :
Print ``i`` as long as ``i`` is less than 6.
```python
i = 1
while i < 6:
  print(i)
  i += 1
```
- **Note** : Remember to **increment i**, or else the loop will **continue forever**.
- The while loop requires relevant variables to be ready, in this example we need to define an **indexing variable**, i, which we set to 1.

### The break Statement
With the **break statement** we can stop the loop even if the **while condition is true**.

#### Example :
Exit the loop when i is 3.
```python
i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1
```

### The continue Statement
With the **continue statement** we can stop the current iteration, and continue with the next.

#### Example :
Continue to the next iteration if ``i`` is 3 :
```python
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)
```

### The else Statement
With the **else statement** we can run a block of code once when the condition no longer is true.

#### Example :
Print a message once the condition is false.
```python
i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")
```
- **Note** : The else block will **NOT** be executed if the loop is stopped by a **`break`** statement.

### Summary
- **Loops** are used to repeat a **block of code** efficiently.
- Python provides **``for``** **loop** and **``while``** **loop**.
- **``for``** **loops** iterate over sequences, whereas **``while``** **loops** run based on conditions.
- **``break``**, **``continue``**, and **``pass``** control loop execution.
- **Nested loops** handle multi-level iterations.
- The **``else``** **block** runs when a loop completes without ``break``.
