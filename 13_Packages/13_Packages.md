## 13 : Packages in Python


### Introduction

Python packages are a way to organize and structure code by grouping related modules into directories.

A package is essentially a folder that contains:
- An `__init__.py` file  
- One or more Python files (modules)

Packages allow modules to be easily shared and distributed across different applications.

---

## Key Components of a Python Package

## Module
A **module** is a single Python file containing reusable code.

Example :
```python
# math.py
def add(a, b):
    return a + b
```


## Package
A package is a directory containing:
- Multiple modules
- A special __init__.py file
The __init__.py file marks the directory as a Python package.

Example Structure:
```python
mypackage/
│
├── __init__.py
├── module1.py
├── module2.py
```


## Sub-Packages
Sub-packages are packages nested within other packages for deeper organization.

Example Structure:
```python
mypackage/
│
├── __init__.py
├── module1.py
│
└── subpackage/
    ├── __init__.py
    └── module2.py
```


### How to Create and Access Packages in Python
#### Step 1: Create a Directory
Make a directory for your package. This will serve as the root folder.

#### Step 2: Add Modules
Add Python files (modules) to the directory, each representing specific functionality.

#### Step 3: ``Include __init__.py``
Add an ``__init__.py`` file (can be empty) to mark it as a package.

#### Step 4: Add Sub-Packages (Optional)
Create subdirectories with their own __init__.py files.

#### Step 5: Import Modules
Use dot notation to import modules.

Example:
```python
from mypackage.module1 import greet
```

### Example: Math Operation Package

In this example, we are creating a Math Operation Package to organize Python code into a structured package with two sub-packages:

- ``basic`` → addition and subtraction
- ``advanced`` → multiplication and division

Each operation is implemented in separate modules, allowing for modular, reusable and maintainable code.

### Package Structure
```python
math_operations/
│
├── __init__.py
├── calculator.py
│
├── basic/
│   ├── __init__.py
│   ├── add.py
│   └── sub.py
│
└── advanced/
    ├── __init__.py
    ├── multiply.py
    └── divide.py
```

- math_operations/init.py

This __init__.py file initializes the main package by importing and exposing the calculate function and operations (add, subtract, multiply, divide) from the respective sub-packages for easier access.

```python
# Initialize the main package
from .calculator import calculate
from .basic import add, subtract
from .advanced import multiply, divide
```


- math_operations/calculator.py

This calculate file is a simple placeholder that prints "Performing calculation...", serving as a basic demonstration or utility within the package.

```python
def calculate():
    print("Performing calculation...")
```



- math_operations/basic/init.py

This __init__.py file initializes the basic sub-package by importing and exposing the add and subtract functions from their respective modules (add.py and sub.py). This makes these functions accessible when the basic sub-package is imported.

```python
# Export functions from the basic sub-package
from .add import add
from .sub import subtract
```



- math_operations/basic/add.py
```python
def add(a, b):
    return a + b
```



- math_operations/basic/sub.py
```python
def subtract(a, b):
    return a - b
```

In the same way we can create the sub package advanced with multiply and divide modules. 

- math_operations/advanced/init.py
```python
from .multiply import multiply
from .divide import divide
```



- math_operations/advanced/multiply.py
```python
def multiply(a, b):
    return a * b
```


- math_operations/advanced/divide.py
```python
def divide(a, b):
    return a / b
```



### Importing the Module and Using the Function

Now, let's take an example of importing the module into a code and using the function:

```python
from math_operations import calculate, add, subtract

# Using the placeholder calculate function
calculate()

# Perform basic operations
print("Addition:", add(5, 3))
print("Subtraction:", subtract(10, 4))
```



### Python Packages for Web Frameworks

Python provides powerful frameworks for web development:

- Flask
- Django
- FastAPI
- Pyramid
- Tornado
- Falcon
- CherryPy
- Bottle
- Web2py

These frameworks help build:

- Web applications
- REST APIs
- High-performance services


### Python Packages for AI & Machine Learning

#### Statistical Analysis
- NumPy
- Pandas
- SciPy
- XGBoost
- StatsModels
- Yellowbrick
- Arch
- Dask-ML


#### Data Visualization
- Matplotlib
- Seaborn
- Plotly
- Bokeh
- Altair
- Pygal
- Plotnine
- Dash


#### Deep Learning
- Scikit-learn
- TensorFlow
- torch
- Keras
- Keras-RL
- Lasagne
- Fastai


#### Natural Language Processing
- NLTK
- spaCy
- FastText
- Transformers
- AllenNLP
- TextBlob

#### Generative AI
- Keras
- spaCy
- GPy
- Pillow
- ImageIO
- Fastai


#### Computer Vision
- OpenCV
- TensorFlow
- torch
- scikit-image
- SimpleCV
- ImageAI
- imageio
- Dlib
- Theano
- Mahotas


#### Python Packages for GUI Applications
- Tkinter
- PyQt5
- Kivy
- PySide
- PySimpleGUI
- NiceGUI
- PyGTK


These packages help build:
- Desktop applications
- Cross-platform GUI apps
- Interactive interfaces


#### Python Packages for Web Scraping & Automation
- Requests
- BeautifulSoup
- Selenium
- MechanicalSoup
- urllib3
- Scrapy
- Requests-HTML
- lxml
- pyautogui
- schedule
- Watchdog

Used for:
- Web scraping
- Browser automation
- Task scheduling
- File monitoring


#### Python Packages for Game Development
- PyGame
- Panda3D
- Pyglet
- Arcade
- PyOpenGL
- Cocos2d

Used for:
- 2D Games
- 3D Games
- Multimedia applications


### Conclusion

Python packages play a fundamental role in building well-structured and scalable applications. They provide a systematic way to organize related modules into a hierarchical directory structure, making code easier to manage and maintain.

By using packages, developers can:

- Structure large projects into logical components  
- Promote code reusability across multiple applications  
- Improve readability and maintainability  
- Support collaborative development  
- Enable easier distribution and deployment of software  

Packages encourage modular programming, where each module focuses on a specific functionality. This approach reduces complexity, enhances debugging efficiency, and improves overall project scalability.

In real-world development — whether building web applications, machine learning systems, automation tools, or enterprise software — packages form the backbone of organized Python projects.

Understanding and implementing packages effectively is essential for writing professional, production-ready Python code.
