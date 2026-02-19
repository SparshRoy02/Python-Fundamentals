## 10 : Dictionaries in Python

A dictionary in Python is a built-in data type used to store data in **key-value pairs** that are separated by commas and enclosed within curly brackets {}. Dictionary items are stored as key-value pairs, separated by commas and enclosed within curly brackets {}.


### Explanation :
- Each key has a corresponding value.
- Keys must be unique.
- Dictionaries are mutable (changeable).
- Written inside curly braces {}.
- **Syntax** : {key: value}

#### Example :
```python
student = {
    "name": "Rahul",
    "age": 21,
    "course": "B.Tech"
}
print(student)
```



### Creating a Dictionary

#### Using Curly Braces {}
A dictionary is created by writing key-value pairs inside { }, where each key is connected to a value using colon (:). 
```python
person = {"name": "Aman", "city": "Delhi"}
```

#### Using dict() Constructor
A dictionary can also be created using the dict() function.
```python
person = dict(name="Aman", city="Delhi")
```



### Accessing Dictionary Items:
1. Accessing Single Values:
Values in a dictionary can be accessed using keys. We can access dictionary values by mentioning keys either in square brackets or by using the ``get`` method.

#### Example :
```python
info = {'name':'Karan', 'age':19, 'eligible':True}
print(info['name'])
print(info.get('eligible'))
```

2. Accessing Multiple Values:
We can print all the values in the dictionary using the values() method.

#### Example :
```python
info = {'name':'Karan', 'age':19, 'eligible':True}
print(info.values())
```

3. Accessing Keys:
We can print all the keys in the dictionary using the keys() method.

#### Example :
```python
info = {'name':'Karan', 'age':19, 'eligible':True}
print(info.keys())
```

4. Accessing Key-Value Pairs:
We can print all the key-value pairs in the dictionary using the items() method.

#### Example :
```python
info = {'name':'Karan', 'age':19, 'eligible':True}
print(info.items())
```



### Add and Remove Items

### Adding items to a dictionary:
There are two common ways to add items to a dictionary.

1. Create a new key and assign a value to it:
#### Example :
```python
info = {'name': 'Karan', 'age': 19, 'eligible': True}
print(info)
info['DOB'] = 2001
print(info)
```

2. Use the update() method:
The update() method updates the value of an existing key, and if the key does not exist, it creates a new key-value pair.

#### Example :
```python
info = {'name': 'Karan', 'age': 19, 'eligible': True}
print(info)
info.update({'age': 20})
info.update({'DOB': 2001})
print(info)
```


### Removing items from dictionary:
There are several methods available to remove items from a dictionary.

### clear()
The clear() method removes all the items from the dictionary.

#### Example :
```python
info = {'name': 'Karan', 'age': 19, 'eligible': True}
info.clear()
print(info)
```

### pop() 
The pop() method removes the key-value pair whose key matches the parameter passed.

#### Example :
```python
info = {'name': 'Karan', 'age': 19, 'eligible': True}
info.pop('eligible')
print(info)
```

### popitem()
The ``popitem()`` method removes the last inserted key-value pair from the dictionary.

#### Example :
```python
info = {'name': 'Karan', 'age': 19, 'eligible': True, 'DOB': 2003}
info.popitem()
print(info)
```

### del
Apart from these three methods, we can also use the del keyword to remove a dictionary item.

#### Example :
```python
info = {'name': 'Karan', 'age': 19, 'eligible': True, 'DOB': 2003}
del info['age']
print(info)
```


If a key is not provided, the del keyword will delete the entire dictionary.

#### Example :
```python
info = {'name': 'Karan', 'age': 19, 'eligible': True, 'DOB': 2003}
del info
print(info)

#NameError: name 'info' is not defined

```


### Dictionary Length

Use ``len()`` to count number of key-value pairs.
```python
print(len(person))
```



### Looping Through Dictionary

#### Loop Through Keys
```python
d = {1: 'Sparsh', 2: 'Roy', 'age':23}
for key in d:
    print(key)
```

#### Loop Through Values
```python
d = {1: 'Sparsh', 2: 'Roy', 'age':23}
for value in d.values():
    print(value)
```

#### Loop Through Key-Value Pairs
```python
d = {1: 'Sparsh', 2: 'Roy', 'age':23}
for key, value in d.items():
    print(f"{key}: {value}")
```


### Dictionary Methods
Python has a set of built-in methods that you can use on dictionaries.


| Method    | Description |
|-----------|-------------|
| `keys()`  | Returns a list containing the dictionary's keys |
| `values()`| Returns a list of all the values in the dictionary |
| `items()` | Returns a list containing a tuple for each key-value pair |
| `update()`| Updates the dictionary with the specified key-value pairs |
| `copy()`  | Returns a copy of the dictionary |


```python
d = {  
     "name": "Sparsh,  
     "subjects": ["math", "science", "physics"],  
     "cgpa": 9.5  
}  
print(d.keys())           # dict_keys  
print(d.values())         # dict_values  
print(d.items())          # dict_items 

info = {'name':'Karan', 'age':19, 'eligible':True, 'DOB':2003}
newDictionary = info.copy()    # dict_copy
print(newDictionary)

new_item = {"city": "Delhi"}   # dict_update
print(d.update(new_item))  
print(d) 
```


### Nested Dictionary 

A nested dictionary is a dictionary that contains another dictionary as one of its values. 
```python
students = {
    "student1": {"name": "Rahul", "age": 21},
    "student2": {"name": "Aman", "age": 22}
}

print(students["student1"]["name"])
```




## Conclusion

Dictionaries are one of the most powerful and commonly used data structures in Python.  
They allow us to store data in a **key-value pair format**, making data retrieval fast, organized, and efficient.


Dictionaries are widely used in:
- Storing user data
- Configuration settings
- JSON data handling
- Counting frequencies
- Database-like record structures

Understanding dictionaries is essential because they are heavily used in real-world applications, data analysis, backend development, and competitive programming.





