## 08 : Lists in Python

### Introduction
- **Lists** are **ordered collections** of data items.
- They store **multiple items in a single variable**.
- List items are separated by **commas and enclosed within square brackets []**.
- Lists are **changeable**, meaning we can alter them after creation.

#### Example 1:
```python
lst1 = [1, 2, 2, 3, 5, 4, 6]
lst2 = ["Red", "Green", "Blue"]
print(lst1)
print(lst2)
```



### List Indexes
Each item/element in a list has its own **unique index**. This index can be used to access any particular item from the list. The first item has index [0], the second item has index [1], the third item has index [2], and so on.

#### Example:
```python
colors = ["Red", "Green", "Blue", "Yellow", "Green"]
#          [0]      [1]     [2]      [3]      [4]
```

### Accessing list items:
- **Positive Indexing**
As we have seen that list items have an index, we can access items using these indexes.

#### Example:
```python
colors = ["Red", "Green", "Blue", "Yellow", "Green"]
#          [0]      [1]     [2]      [3]      [4]
print(colors[2])
print(colors[4])
print(colors[0])
```

- **Negative Indexing**
Similar to positive indexing, negative indexing is also used to access items, but from the end of the list. The last item has index [-1], the second last item has index [-2], the third last item has index [-3], and so on.

#### Example:
```python
colors = ["Red", "Green", "Blue", "Yellow", "Green"]
#          [-5]    [-4]    [-3]     [-2]      [-1]
print(colors[-1])
print(colors[-3])
print(colors[-5])
```


### Check for item:
We can check if a given item is present in the list. This is done using the ``in`` **keyword**.
```python
colors = ["Red", "Green", "Blue", "Yellow", "Green"]
if "Yellow" in colors:
    print("Yellow is present.")
else:
    print("Yellow is absent.")
```


### Range of Index:
You can print a range of list items by specifying where you want to start, where you want to end, and if you want to skip elements in between the range.

#### Syntax:
```python
List[start : end : jumpIndex]
```

**Note** : jumpIndex is optional. We will see this in given examples.

- **Example : printing elements within a particular range**
```python
animals = ["cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow"]
print(animals[3:7])  # using positive indexes
print(animals[-7:-2])  # using negative indexes
```

Here, we provide the index of the element from where we want to start and the index of the element till which we want to print the values.

**Note** : The element of the end index provided will not be included.



- **Example: print alternate values**
```python
animals = ["cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow"]
print(animals[::2])  # using positive indexes
print(animals[-8:-1:2])  # using negative indexes
```

Here, we have not provided start and end indexes, which means all the values will be considered. But as we have provided a jump index of 2, only alternate values will be printed.



### Add List Items
There are **three methods** to add items to a list: **append()**, **insert()**, and **extend()**.

### append():
This method appends items to the **end** of the existing list.

#### Example:
```python
colors = ["violet", "indigo", "blue"]
colors.append("green")
print(colors)
```

### insert():
This method inserts an item at the given index. The user has to **specify the index** and the item to be **inserted within the ``insert()`` method**.

#### Example:
```python
colors = ["violet", "indigo", "blue"]
#           [0]        [1]      [2]
 
colors.insert(1, "green")   # inserts item at index 1
# updated list: colors = ["violet", "green", "indigo", "blue"]
#       indexes              [0]       [1]       [2]      [3]
 
print(colors)
```

### extend():
This method adds an entire list or any **other collection datatype** to the existing list.

#### Example 1:
```python
# add a list to a list
colors = ["violet", "indigo", "blue"]
rainbow = ["green", "yellow", "orange", "red"]
colors.extend(rainbow)
print(colors)
```

### Concatenate two lists:
You can simply concatenate two lists to join them.

#### Example:
```python
colors = ["violet", "indigo", "blue", "green"]
colors2 = ["yellow", "orange", "red"]
print(colors + colors2)
```


### Remove List Items
There are various methods to remove items from the list: pop(), remove(), del, clear()

### pop():
This method removes the **last item** of the list if no index is provided. If an index is provided, then it removes the item at that specified index.

#### Example 1:
```python
colors = ["Red", "Green", "Blue", "Yellow", "Green"]
colors.pop()        # removes the last item of the list
print(colors)
```

#### Example 2:
```python
colors = ["Red", "Green", "Blue", "Yellow", "Green"]
colors.pop(1)       # removes item at index 1
print(colors)
```

### remove():
This method removes a **specific item** from the list.

#### Example:
```python
colors = ["violet", "indigo", "blue", "green", "yellow"]
colors.remove("blue")
print(colors)
```


#### del:
del is not a method; rather, it is a keyword which deletes an item at a specific index from the list, or deletes the list entirely.

##### Example 1:
```python
colors = ["violet", "indigo", "blue", "green", "yellow"]
del colors[3]
print(colors)
```


#### clear():
This method clears all items in the list and prints an empty list.

##### Example:
```python
colors = ["violet", "indigo", "blue", "green", "yellow"]
colors.clear()
print(colors)
```



### Change List Items
Lists are mutable, which means we can change their items after creating them. Here’s how to update items using indexes and index ranges. Changing items from a list is easier; you just have to specify the index where you want to replace the item with a new value.

##### Example:
```python
names = ["Harry", "Sarah", "Nadia", "Oleg", "Steve"]
names[2] = "Millie"
print(names)
```

#### change more than a single item at once. 
To do this, just specify the index range over which you want to change the items.

##### Example:
```python
names = ["Harry", "Sarah", "Nadia", "Oleg", "Steve"]
names[2:4] = ["juan", "Anastasia"]
print(names)
```


#### What if the range of the index is more than the list of items provided?

In this case, all the items within the index range of the original list are replaced by the items that are provided.

##### Example:
```python
names = ["Harry", "Sarah", "Nadia", "Oleg", "Steve"]
names[1:4] = ["juan", "Anastasia"]
print(names)
```


#### What if we have more items to be replaced than the index range provided?

In this case, the original items within the range are replaced by the new items, and Python inserts all the new items and shifts the remaining elements to the right.

##### Example:
```python
names = ["Harry", "Sarah", "Nadia", "Oleg", "Steve"]
names[2:3] = ["juan", "Anastasia", "Bruno", "Olga", "Rosa"]
print(names)
```



### List Comprehension
List comprehensions are used to create new lists from existing iterables such as lists, tuples, dictionaries, sets, arrays, or even strings.

#### Syntax:
```python
example_list = [expression(item) for item in iterable if condition]
```

- expression: the value to put into the new list.
- iterable: a sequence or collection you can loop over (lists, tuples, dictionaries, sets, strings, etc.)
- condition: condition checks if the item should be added to the new list or not.

#### Example 1: accepts items with the small letter “o” in the new list
```python
names = ["Milo", "Sarah", "Bruno", "Anastasia", "Rosa"]
namesWith_O = [item for item in names if "o" in item]
print(namesWith_O)
```
This comprehension checks each name and includes it only if it contains the letter "o".


#### Example 2: accepts items which have more than 4 letters
```python
names = ["Milo", "Sarah", "Bruno", "Anastasia", "Rosa"]
namesLong = [item for item in names if len(item) > 4]
print(namesLong)
```




### List Methods
Now let’s look at some additional list methods that help us sort, reverse, count, and copy list items. We have discussed methods like append(), clear(), extend(), insert(), pop(), remove() before. Now we will learn about some more list methods:

#### sort():
This method sorts the list in ascending order.

##### Example 1:
```python
colors = ["violet", "indigo", "blue", "green"]
colors.sort()
print(colors)
 
num = [4,2,5,3,6,1,2,1,2,8,9,7]
num.sort()
print(num)
```


#### What if you want to print the list in descending order?
We must give ``reverse=True`` as a parameter in the sort method.

##### Example:
```python
colors = ["violet", "indigo", "blue", "green"]
colors.sort(reverse=True)
print(colors)
 
num = [4,2,5,3,6,1,2,1,2,8,9,7]
num.sort(reverse=True)
print(num)
```
The reverse parameter is set to False by default.

**Note** : Do not confuse the reverse parameter with the reverse() method. The reverse=True option works only inside the sort() method and sorts the list in descending order, while the reverse() method simply reverses the current order of the list and does not perform any sorting.



#### reverse():
This method reverses the order of the list.

##### Example:
```python
colors = ["violet", "indigo", "blue", "green"]
colors.reverse()
print(colors)
 
num = [4,2,5,3,6,1,2,1,2,8,9,7]
num.reverse()
print(num)
```


#### index():
This method returns the index of the first occurrence of the list item.

##### Example:
```python
colors = ["violet", "green", "indigo", "blue", "green"]
print(colors.index("green"))
 
num = [4,2,5,3,6,1,2,1,3,2,8,9,7]
print(num.index(3))
```
**Note** : If the item is not present in the list, ``index()`` will raise a ValueError.

#### count():
Returns the count of the number of items with the given value.

##### Example:
```python
colors = ["violet", "green", "indigo", "blue", "green"]
print(colors.count("green"))
 
num = [4,2,5,3,6,1,2,1,3,2,8,9,7]
print(num.count(2))
```


#### copy():
Returns a copy of the list. This can be done to perform operations on the list without modifying the original list.

##### Example:
```python
colors = ["violet", "green", "indigo", "blue"]
newlist = colors.copy()
print(colors)
print(newlist)
```




### Nested Lists
Nested Lists allow us to store lists inside another list. These are useful when we want to store structured or table-like data.

#### What are Nested Lists?
A nested list simply means a list that contains other lists as items.
```python
# Nested List Example
students = [
    ["Harry", 20],
    ["Sarah", 22],
    ["Bruno", 21]
]
 
print(students)
```


#### Accessing Items in Nested Lists
To access elements inside nested lists, we use multiple indexes:

- First index → selects the inner list
- Second index → selects the item inside that inner list
```python
# Accessing elements inside nested lists
students = [
    ["Harry", 20],
    ["Sarah", 22],
    ["Bruno", 21]
]
 
print(students[0][0])     # First student's name
print(students[1][1])     # Second student's age
```


#### Modifying Items in Nested Lists
We can change values inside nested lists using indexing.
```python
# Modifying nested list items
students = [
    ["Harry", 20],
    ["Sarah", 22],
    ["Bruno", 21]
]
 
students[0][1] = 25       # Updating Harry's age
 
print(students)
```


### Iterating Through Nested Lists
#### 1. Looping through each inner list
```python
# Looping through nested lists
students = [
    ["Harry", 20],
    ["Sarah", 22],
    ["Bruno", 21]
]
 
for student in students:
    print(student)
```


#### 2. Looping through each value inside inner lists
```python
# Looping through values inside nested lists
students = [
    ["Harry", 20],
    ["Sarah", 22],
    ["Bruno", 21]
]
 
for student in students:
    for value in student:
        print(value)
```


#### Nested Lists as Matrices (2D Lists)
Nested lists are useful when representing 2D data such as matrices.
```python
# Matrix representation using nested lists
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
 
print(matrix[1][2])       # Row 1, Column 2
```


### Real-World Use Cases
- Storing student marks
- Managing inventory
- Data processing
- Queue implementation
- Stack implementation



### Conclusion
- Lists are one of the most powerful and flexible data structures in Python.
- They support dynamic sizing, multiple data types, and numerous built-in methods, making them essential for programming and data manipulation.




