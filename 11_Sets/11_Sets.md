# 11 : Sets in Python

## Introduction to Sets

A Set is a built-in data type in Python used to store multiple items in a single variable. Sets are useful when we want only unique values.

- Sets are unordered.
- Sets are mutable.
- Sets do not allow duplicate values.
- Sets are written using curly brackets `{ }`.

Example:
```python
my_set = {1, 2, 3, 4}
print(my_set)
```
```python
info = {"Carla", 19, False, 5.9, 19}
print(info)
```

---

## Characteristics of Sets

### 1. Unordered
Unordered means that the items in a set do not have a defined order.

```python
s = {"apple", "banana", "cherry"}
print(s)
```

---

### 2. No Duplicates
Duplicate values are automatically removed.

```python
s = {1, 2, 2, 3, 4}
print(s)  # Output: {1, 2, 3, 4}
```

---

### 3. Mutable
We can add or remove elements after creation.

```python
s = {1, 2, 3}
s.add(4)
print(s)
```

---

### 4. Heterogeneous Elements
A set can contain different data types.

```python
s = {1, "hello", 3.14, True}
print(s)
```

---

## Creating a Set

### Using Curly Braces
```python
s = {10, 20, 30}
print(s)
```

### Using set() Constructor
```python
s = set([1, 2, 3])
print(s)
```

### Creating an Empty Set
```python
empty_set = set()
print(type(empty_set))
```

---

## Accessing Set Items

Sets are unordered, so we cannot access items using indexing.

We use loops instead.

```python
s = {1, 2, 3}
for item in s:
    print(item)
```

---

## Adding Items to Set

### add() Method
Adds a single element.

```python
s = {1, 2}
s.add(3)
print(s)
```

### update() Method
Adds multiple elements.

```python
s = {1, 2}
s.update([3, 4])
print(s)
```

---

## Removing Items from Set

### remove()
Removes specified item. Raises error if not present.

```python
s = {1, 2, 3}
s.remove(2)
print(s)
```

### discard()
Removes item. No error if not present.

```python
s = {1, 2, 3}
s.discard(5)
print(s)
```

### pop()
Removes random element.

```python
s = {1, 2, 3}
s.pop()
print(s)
```

### clear()
Removes all items.

```python
s = {1, 2, 3 ,4}
s.clear()
print(s)
```

---

## Deleting a Set

```python
s = {1, 2}
del s
```

---

## Set Operations

### Union
Combines elements of both sets.

```python
a = {1, 2, 3}
b = {3, 4, 5}
print(a.union(b))
```

### Intersection
Common elements.

```python
print(a.intersection(b))
```

### Difference
Elements in first set but not in second.

```python
print(a.difference(b))
```

### Symmetric Difference
Elements in either set but not both.

```python
print(a.symmetric_difference(b))
```

---

## Set Methods

### copy()
Returns shallow copy.

```python
s = {1, 2}
new_s = s.copy()
print(new_s)
```

### isdisjoint()
Returns True if no common elements.

```python
a = {1, 2}
b = {3, 4}
print(a.isdisjoint(b))
```

### issubset()
Checks if subset.

```python
a = {1, 2}
b = {1, 2, 3}
print(a.issubset(b))
```

### issuperset()
Checks if superset.

```python
print(b.issuperset(a))
```

---

## Frozen Set

A frozenset is an immutable version of a set. It contains unique, unordered, unchangeable elements. Unlike sets, elements cannot be added or removed from a frozenset.

```python
fs = frozenset([1, 2, 3])
print(fs)
```


---

# Conclusion


Sets are one of the most powerful and efficient data structures in Python when dealing with unique elements and mathematical operations.

- Sets are unordered and do not allow duplicate values.
- They are mutable, allowing elements to be added or removed.
- They are highly efficient for membership testing (`in` operator).
- They support mathematical operations like union, intersection, difference, and symmetric difference.
- They provide useful built-in methods such as `add()`, `update()`, `remove()`, `discard()`, `copy()`, `issubset()`, `issuperset()`, and more.
- `frozenset` provides an immutable version of a set.
