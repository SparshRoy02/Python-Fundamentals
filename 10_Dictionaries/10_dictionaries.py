# 10 : Dictionaries in Python

# Example
student = {
    "name": "Rahul",
    "age": 21,
    "course": "B.Tech"
}
print(student)


# Creating a Dictionary

# Using Curly Braces {}
person = {"name": "Aman", "city": "Delhi"}
print(person)

# Using dict() Constructor
person = dict(name="Aman", city="Delhi")
print(person)


# Accessing Dictionary Items

# Accessing Single Values (get() method) 
info = {'name':'Karan', 'age':19, 'eligible':True}
print(info['name'])
print(info.get('eligible'))

# Accessing Multiple Values
info = {'name':'Karan', 'age':19, 'eligible':True}
print(info.values())

# Accessing Keys
info = {'name':'Karan', 'age':19, 'eligible':True}
print(info.keys())

# Accessing Key-Value Pairs
info = {'name':'Karan', 'age':19, 'eligible':True}
print(info.items())


# Add and Remove Items

# Adding items to a dictionary
info = {'name': 'Karan', 'age': 19, 'eligible': True}
print(info)
info['DOB'] = 2001
print(info)

# Using update() method
info = {'name': 'Karan', 'age': 19, 'eligible': True}
print(info)
info.update({'age': 20})
info.update({'DOB': 2001})
print(info)


# Removing items from dictionary:

# clear()
info = {'name': 'Karan', 'age': 19, 'eligible': True}
info.clear()
print(info)

# pop()
info = {'name': 'Karan', 'age': 19, 'eligible': True}
info.pop('eligible')
print(info)

# popitem()
info = {'name': 'Karan', 'age': 19, 'eligible': True, 'DOB': 2003}
info.popitem()
print(info)

# del keyword (removing key)
info = {'name': 'Karan', 'age': 19, 'eligible': True, 'DOB': 2003}
del info['age']
print(info)

# del keyword (deleting entire dictionary)
info = {'name': 'Karan', 'age': 19, 'eligible': True, 'DOB': 2003}
del info
print(info)  
# NameError : name 'info' is not defined


# Dictionary Length
print(len(person))


# Looping Through Dictionary

# Loop Through Keys
d = {1: 'Sparsh', 2: 'Roy', 'age':23}
for key in d:
    print(key)

# Loop Through Values
d = {1: 'Sparsh', 2: 'Roy', 'age':23}
for value in d.values():
    print(value)

# Loop Through Key-Value Pairs
d = {1: 'Sparsh', 2: 'Roy', 'age':23}
for key, value in d.items():
    print(f"{key}: {value}")


# Dictionary Methods Example

d = {
     "name": "Sparsh",
     "subjects": ["math", "science", "physics"],
     "cgpa": 9.5
}
print(d.keys())                  # dict_keys
print(d.values())                # dict_values
print(d.items())                 # dict_items

info = {'name':'Karan', 'age':19, 'eligible':True, 'DOB':2003}
newDictionary = info.copy()      # dict_copy
print(newDictionary)

new_item = {"city": "Delhi"}     # dict_update
d.update(new_item)
print(d)


# Nested Dictionary

students = {
    "student1": {"name": "Rahul", "age": 21},
    "student2": {"name": "Aman", "age": 22}
}
print(students["student1"]["name"])
