## 09 : Tuples in Python

- Python provides another way to store multiple items: tuples. Tuples look similar to lists, but have one important difference: they cannot be changed after creation.

- Tuples are ordered collections of data items. They store multiple items in a single variable. Tuple items are separated by commas and enclosed within round brackets (). Tuples are unchangeable, meaning we cannot alter them after creation.



### Creating a Tuple
A tuple is created by placing all the items inside parentheses (), separated by commas. A tuple can have any number of items and they can be of different data types.

**Note** : 
- It is the comma that creates a tuple, not the parentheses.
- a = (5) is not a tuple. It is just the number 5. To create a tuple with one item, you must add a comma. a = (5,)

#### Example 1:
```python
tuple1 = (1, 2, 2, 3, 5, 4, 6)
tuple2 = ("Red", "Green", "Blue")
print(tuple1)
print(tuple2)
```


### Tuples Characteristics

1. Ordered 
2. Immutable – Items cannot be changed after the tuple is created.
3. Allows duplicates 
4. Heterogeneous 

Tuples are very similar to lists. Some of the differences are that tuples are 
immutable & because of this immutability they are also faster. 



### Tuple Length
To determine how many items a tuple has, use the len() function:

#### Example
Print the number of items in the tuple:
```python
thistuple = ("apple", "banana", "cherry")
print(len(thistuple))
```


### Tuple Items - Data Types
Tuple items can be of any data type:

#### Example
String, int and boolean data types:
```python
tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)
```

A tuple can contain different data types:

#### Example
A tuple with strings, integers and boolean values:
```python
tuple1 = ("abc", 34, True, 40, "male")
```



### Python Tuple Basic Operations
Below are the Python tuple operations.

- Accessing of Python Tuples
- Concatenation of Tuples
- Slicing of Tuple
- Deleting a Tuple


### Accessing tuple items:

1. Positive Indexing:
As we have seen that tuple items have an index, we can access items using these indexes.

#### Example:
```python
country = ("Spain", "Italy", "India", "England", "Germany")
#            [0]      [1]      [2]       [3]        [4]
print(country[1])
print(country[3])
print(country[0])
```

2. Negative Indexing:
Similar to positive indexing, negative indexing is also used to access items, but from the end of the tuple. The last item has index [-1], the second last item has index [-2], the third last item has index [-3], and so on.

#### Example:
```python
country = ("Spain", "Italy", "India", "England", "Germany")
#            [0]      [1]      [2]       [3]        [4]
print(country[-1])
print(country[-3])
print(country[-4])
```

3. Check for item:
We can check if a given item is present in the tuple. This is done using the in keyword.

#### Example 1:
```python
country = ("Spain", "Italy", "India", "England", "Germany")
if "Germany" in country:
    print("Germany is present.")
else:
    print("Germany is absent.")
```


4. Range of Index:
You can print a range of tuple items by specifying where you want to start, where you want to end, and if you want to skip elements in between the range.

#### Syntax:
```python
Tuple[start : end : jumpIndex]
```

#### Example: 
Printing elements within a particular range:
```python
animals = ("cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow")
print(animals[3:7])     # using positive indexes
print(animals[-7:-2])   # using negative indexes
```
**Note** : The element of the end index provided will not be included.

#### Example: 
Printing all elements from a given index till the end
```python
animals = ("cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow")
print(animals[4:])      # using positive indexes
print(animals[-4:])     # using negative indexes
```

#### Example: 
Printing all elements from start to a given index
```python
animals = ("cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow")
print(animals[:6])      # using positive indexes
print(animals[:-3])     # using negative indexes
```


#### Example: 
Print alternate values
```python
animals = ("cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow")
print(animals[::2])     # using positive indexes
print(animals[-8:-1:2]) # using negative indexes
```

#### Example: 
Printing every 3rd consecutive within given range
```python
animals = ("cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow")
print(animals[1:8:3])
```




### Concatenation of Tuples

Tuples can be concatenated using the + operator. This operation combines two or more tuples to create a new tuple.

Note: Only the same datatypes can be combined with concatenation, an error arises if a list and a tuple are combined. 

```python
tup1 = (0, 1, 2, 3)
tup2 = ('Sparsh', 'J', 'Roy')
​
tup3 = tup1 + tup2
print(tup3)
```


### Slicing of Tuple

Slicing a tuple means creating a new tuple from a subset of elements of the original tuple. The slicing syntax is tuple[start:stop:step].

**Note** - Negative Increment values can also be used to reverse the sequence of Tuples. 

```python
tup = tuple('SPARSHJROY')
​
# Removing First element
print(tup[1:])
​
# Reversing the Tuple
print(tup[::-1])
​
# Printing elements of a Range
print(tup[4:8])
```


### Deleting a Tuple
Since tuples are immutable, we cannot delete individual elements of a tuple. However, we can delete an entire tuple using del statement.

**Note** : Printing of Tuple after deletion results in an Error. 

```python
tup = (0, 1, 2, 3, 4)
del tup
​
print(tup)
```


### Change Tuple Values
Once a tuple is created, you cannot change its values. Tuples are unchangeable, or immutable as it also is called.

But there is a workaround. You can convert the tuple into a list, change the list, and convert the list back into a tuple.

#### Example
Convert the tuple into a list to be able to change it:
```python
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)
```



### Unpacking a Tuple
When we create a tuple, we normally assign values to it. This is called "packing" a tuple:

#### Example
Packing a tuple:
```python
fruits = ("apple", "banana", "cherry")
```

But, in Python, we are also allowed to extract the values back into variables. This is called "unpacking":

#### Example
Unpacking a tuple:
```python
fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)
```



### Using Asterisk*
If the number of variables is less than the number of values, you can add an * to the variable name and the values will be assigned to the variable as a list:

Example
```python
tup = (1, 2, 3, 4, 5)

a, *b, c = tup

print(a) 
print(b) 
print(c)
```

#### Explanation :
- ``a`` gets the first item.
- ``c`` gets the last item.
- ``*b`` collects everything in between into a list.




### Loop Through a Tuple
You can loop through the tuple items by using a ``for`` loop.

#### Example
Iterate through the items and print the values:
```python
thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x)
```

### Loop Through the Index Numbers
- You can also loop through the tuple items by referring to their index number.

- Use the ``range()`` and ``len()`` functions to create a suitable iterable.

#### Example
Print all items by referring to their index number:
```python
thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)):
  print(thistuple[i])
```

### Using a While Loop
- You can loop through the tuple items by using a ``while`` loop.
- Use the ``len()`` function to determine the length of the tuple, then start at 0 and loop your way through the tuple items by referring to their indexes.
- Remember to increase the index by 1 after each iteration.

#### Example
Print all items, using a ``while`` loop to go through all the index numbers:
```python
thistuple = ("apple", "banana", "cherry")
i = 0
while i < len(thistuple):
  print(thistuple[i])
  i = i + 1
```


### Join Two Tuples
To join two or more tuples you can use the + operator:

#### Example
Join two tuples:
```python
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)
```

### Multiply Tuples
If you want to multiply the content of a tuple a given number of times, you can use the * operator:

#### Example
Multiply the fruits tuple by 2:
```python
fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2

print(mytuple)
```


### Tuple Methods 
Python has two built-in methods that you can use on tuples.

| Method  | Description |
|----------|-------------|
| count() | Returns the number of times a specified value occurs in a tuple |
| index() | Searches the tuple for a specified value and returns the position where it was found |


```python
t = (1, 2, 2, 3, 5)  
print(t.index(2)) # 1  
print(t.count(2)) # 3 
```


## Conclusion

Tuples in Python are ordered and immutable collections used to store fixed data securely.  
They are memory-efficient, faster than lists, and ideal when data should not be modified after creation.

Key Takeaways:
- Tuples are immutable.
- They allow duplicate and heterogeneous values.
- They support indexing, slicing, and built-in functions.
- Only two built-in methods are available: `count()` and `index()`.
- Useful for dictionary keys and returning multiple values from functions.

Tuples are best used when data integrity and performance are important.
