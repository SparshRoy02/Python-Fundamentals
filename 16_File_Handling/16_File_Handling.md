## 16 : File Handling in Python

### Introduction
**File handling** refers to the process of performing operations on a file such as **creating, opening, reading, writing, appending** and **deleting** it through a programming interface. It manages the **data flow between a Python program and the file system** on the storage device, ensuring that data is handled **safely and efficiently**.


### Why Do We Need File Handling
**File handling** is used to **store and manage data in external files** so that information remains available even after the program finishes execution.

### Reasons for Using File Handling
- To **store data permanently** even after the program ends
- To **access external files** like `.txt`, `.csv`, `.json`
- To **process large files efficiently**
- To **automate tasks** like reading configuration files or saving program outputs


### Opening a File
Opening a file means **establishing a connection between the Python program and the file** so that operations like **reading or writing** can be performed.

#### Syntax
```python
file = open("filename.txt", "mode")
```

#### Parameters
- **filename.txt →** name or path of the file
- **mode →** specifies how the file should be opened
If **mode is not specified**, Python uses **read** ``(r)`` **mode by default**.

#### Example
```python
f = open("demo.txt", "r")
print(f)`
```

#### Explanation
- The file ``demo.txt`` is opened in **read mode**.
- If the file exists, Python returns a **file object**.
- If the file does not exist, Python raises ``FileNotFoundError``.


### Closing a File
Closing a file **releases system resources** and ensures that any changes made to the file are **saved properly**.

#### Syntax
```python
file.close()
```

#### Example
```python
file = open("demo.txt", "r")
# Perform operations
file.close()
```

### Checking File Properties
Python allows checking certain **properties of a file object** such as its **name, mode, and status**.

#### Example
```python
f = open("demo.txt", "r")
print("Filename:", f.name)
print("Mode:", f.mode)
print("Is Closed?", f.closed)

f.close()

print("Is Closed?", f.closed)
```

#### Explanation
- ``f.name`` → returns the **name of the file**
- ``f.mode`` → shows the **mode in which file is opened**
- ``f.closed`` → returns **True if file is closed** otherwise **False**


### File Opening Modes
**Modes determine how a file will be accessed** (reading, writing, appending, etc).

#### Modes

| Mode | Description |
|------|-------------|
| ``r`` | **Read mode** (default). Error if file does not exist |
| ``w`` | **Write mode**. Creates new file or overwrites existing file |
| ``a`` | **Append mode**. Adds data at the end of file |
| ``x`` | **Create mode**. Creates new file, error if file exists |

#### Text and Binary Modes

| Mode | Description |
|------|-------------|
| ``t`` | **Text mode** (default) |
| ``b`` | **Binary mode** (used for images, videos, etc) |

**Example Modes :**
```python
"rt" → read text  
"rb" → read binary  
"wt" → write text  
```

### Reading a File
Reading a file means **retrieving data stored in the file**.

#### Read Entire File
```python
file = open("demo.txt", "r")
content = file.read()
print(content)
file.close()
```

### Reading Specific Characters
The ``read(n)`` method allows reading only a **specific number of characters**.

#### Example
```python
with open("demofile.txt") as f:
    print(f.read(5))
```

### Reading Lines from a File
Python provides methods to **read a file line by line**.

#### Read One Line
```python
with open("demofile.txt") as f:
    print(f.readline())
```

#### Read Multiple Lines
```python
with open("demofile.txt") as f:
    print(f.readline())
    print(f.readline())
```

#### Loop Through File
```python
with open("demofile.txt") as f:
    for line in f:
        print(line)
```


### Writing to a File
Writing to a file means **storing data inside the file**.

#### Write Mode (``w``)
Creates a **new file** or **overwrites an existing file**.

#### Example
```python
with open("demo.txt", "w") as file:
    file.write("Hello, Python!\n")
    file.write("File handling is easy with Python.")
```

### Appending to a File
Appending adds **new data to the end of an existing file** without deleting previous content.

#### Example
```python
with open("demofile.txt", "a") as f:
    f.write("Now the file has more content!")
```


### Using the ``with`` Statement
The ``with`` **statement** automatically **closes the file after operations are completed**, making the code **safer** and **cleaner**.

#### Example
```python
with open("demo.txt", "r") as file:
    content = file.read()
    print(content)
```


### Exception Handling with Files
**Exception handling** ensures that files are **properly closed even if an error occurs** during file operations.

#### Example
```python
try:
    file = open("demo.txt", "r")
    content = file.read()
    print(content)
finally:
    file.close()
```


### Creating a File
A new file can be created using mode ``x``, ``w``, or ``a``.

#### Example
```python
file = open("Text.txt", "x")
```


### Deleting a File
Files can be deleted using the ``os.remove()`` function.

#### Example
```python
import os

os.remove("demofile.txt")
```


### Checking if File Exists Before Deleting
#### Example
```python
import os

if os.path.exists("demofile.txt"):
    os.remove("demofile.txt")
else:
    print("The file does not exist")
```


### Deleting a Folder
Python allows removing **empty folders** using ``os.rmdir()``.

#### Example
```python
import os

os.rmdir("myfolder")
```
**Note :** Only **empty folders** can be removed.

### Conclusion
**File handling** in Python allows programs to interact with **external files** for **storing, reading, updating**, and **deleting** data. Using proper **file modes, exception handling**, and the ``with`` **statement** ensures **safe** and **efficient** file operations.


### Summary

File handling in Python allows programs to interact with external files stored on a computer. It enables operations such as **creating, opening, reading, writing, appending, and deleting files**, allowing data to be stored permanently and accessed whenever required. Python uses the **`open()`** function to work with files in different modes like **read (`r`)**, **write (`w`)**, **append (`a`)**, and **create (`x`)**. Methods such as **`read()`**, **`readline()`**, and **`write()`** help retrieve and store data efficiently, while the **`with` statement** ensures files are automatically closed after use, improving code safety and resource management.

- File handling enables **permanent data storage** beyond program execution.
- The **`open()`** function is used to open files in different modes.
- Common modes include **`r` (read), `w` (write), `a` (append), and `x` (create)**.
- Methods like **`read()` and `readline()`** are used to read file content.
- **`write()`** allows storing or updating data inside a file.
- The **`with` statement** automatically closes files after operations.
- The **`os` module** can be used to **delete files and directories**.
- File handling is essential for **data storage, automation, and real-world applications**.
