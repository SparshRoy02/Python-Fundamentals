## 12 : Object Oriented Programming in Python


### Introduction :

Object-Oriented Programming (OOP) is a programming paradigm that organizes code into **objects** — bundles of data (attributes) and behavior (methods).

It helps us:
- Structure programs in a modular way
- Improve reusability
- Improve maintainability
- Model real-world entities


### Classes and Objects

### Class

A **class** is a blueprint/template used to create objects. It describes what an object will look like (its attributes) and what it can do (its 
methods), but it is not the object itself. 

```python
class Car:  
brand = "Toyota"
```

### Object 

An object (or instance) is a realization of a class, it is the actual thing created based on the class blueprint.

```python
car1 = Car()  
car2 = Car()  
print(car1.brand)      # Toyota
print(car2.brand)      # Toyota  
```
We use the dot (.) operator to access attributes and methods.



### Class vs Object


| Class | Object |
|--------|---------|
| Class is a blueprint/ template. | An object is a concrete instance of a class. |
| Does not exist in memory until instantiated. | Contains actual data & occupies memory. |
| One class can create any number of objects. | Each object is independent. |


### Attributes & Methods 
Attributes are variables and Methods are functions defined inside a class.  



### Constructor in OOP

- A constructor initializes newly created objects.
- It is not responsible for creating the object, instead the constructor sets up the object with initial values. 
- In Python, constructor is defined using:   __init__(self)
- It is automatically called when an object is created.

```python
class Student:
    def __init__(self):
        print("Constructor was called")

stu1 = Student()
```


### ``self`` Keyword

``self`` is a special parameter which refers to the instance of the class that is calling the method. We don’t need to pass it explicitly. 

We can also use constructor to initialize values for objects: 

```python
class Student:
    def __init__(self, name):
        self.name = name

stu1 = Student("Rahul")
print(stu1.name)
```


### Types of Constructors
1. Default Constructors - A constructor with no parameters except ``self`` 
2. Parameterized Constructors - Takes parameters to initialize values uniquely for each object. 

```python
class Student:
    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa

s1 = Student("Rahul", 8.7)
```
- Python does NOT support constructor overloading like Java/C++.

### Attributes in OOP

Attributes are variables that belong to a class or an object. They store data/state of the object.

Types of Attributes 

1. Class Attributes 
- Belong to the **class itself**, shared by all objects. 
- Defined **outside** any method in the class. 

```python
class Student:  
   college = "ABC college"    # class attribute  
stu1 = Student ()  
print(stu1.college)  
print(Student.college)     # class attribute can also be accessed with class name
```


2. Instance Attributes 
- Belong individually to each object. 
- Defined inside the ``__init__`` method using ``self``.         . 
- Each object gets its own copy. 

```python
class Student:   
   def __init__ (self, name, gpa):      # instance attributes  
      self.name = name  
      self.gpa = gpa  
stu1 = Student("Rahul", 8.7)  
print(stu1. name, stu1.gpa) 


### NMethods in OOP

Methods are functions defined inside a class, representing the behaviour or 
actions of an object. 
 
Types of Methods:

1. Instance Methods 
- Take ``self`` as the first argument. 
- Can access both **instance attributes* and **class attributes**. 
```python
class Student:  
   def   init  (self, name, marks):  
      self.name = name  
      self. marks = marks  

   def display(self):          # Instance method  
      print(f"Name: {self.name}, Marks: {self.marks}")
```


2. Class Methods 
- Use ``@classmethod`` decorator. 
- Take ``cls`` (class) as first argument. 
- Used to work with **class-level data**. 

```python
class Student:  
   school_name = "ABC School"  

   @classmethod  
   def change_school(cls, new_name):  
       cls.school_name = new_name 
```

3. Static Methods 
• Use ``@staticmethod`` decorator. 
• Do not take ``self`` or ``cls``. 
• Behave like normal functions but belong to the class for logical grouping. 

```python
class Math:  
   @staticmethod  
   def add(a, b):  
       return a + b 
```


### The 4 Pillars of OOP


### Encapsulation 
Encapsulation is the bundling of data (variables) and methods (functions) that operate on that data into a single unit (a class).
 
To implement encapsulation, we use access modifiers. Python has 3 access levels: 
 
1. Public members 
- Accessible everywhere, written like normal variables. 

```python
class Student:  
   def __init__  (self, name):  
       self.name = name   # public variable  

s = Student("Rahul")  
print(s.name)           # Allowed 
```

2. Protected members 
- Indicated by a **single underscore _** (suggest - “Don’t access directly unless needed.”) 
- Still accessible from outside (not truly protected). 
- Intended for internal use or inheritance. 

```python
class Person:  
   def __init__ (self):  
       self._age = 20  # protected variable  

p = Person()  
print(p._age)  # Technically allowed, but not recommended 
```

 
3. Private members 
- Indicated by a **double underscore __**
- Python does name mangling: the variable name becomes ``_ClassName__variable```.                                 . 
- Cannot be accessed directly from outside. 

```python
class Bank:  
   def __init__(self, balance):  
       self.__balance = balance       # private variable  

b = Bank(5000)  
print(b.__balance)        # ERROR: attribute not accessible 
```

To access:
```python 
print(b._Bank__balance)     # Allowed (name-mangled form)
```



### Getters & Setters
 
When we make a variable private, we use methods to read it (getters) or update it 
(setters). 

```python
class Employee:  
   def __init__(self, salary):  
       self.__salary = salary          # private  

def get_salary(self):                 # getter  
    return self.__salary 
 
def set_salary(self, new_salary):     # setter  
    self.__salary = new_salary    

e = Employee(50000)  
print(e.get_salary())  
e.set_salary(60000) 
```


### Inheritance
 
- Inheritance is where one class (child) acquires the properties and behaviors (variables + methods) of another class (parent). 
- The class whose properties are inherited - Parent / Base / Superclass  
- The class that inherits - Child / Derived / Subclass 

```python
class Employee:            # parent class  
    start_time = "9AM"  
    end_time = "5PM"  

class Teacher(Employee):   # child class  
    def __init__(self, subject):  
        self.subject = subject  

t1 = Teacher("Data Science")  

print(t1.subject, t1.start_time, t1.end_time) 
```

Inheritance enables: 
- Code reuse 
- Extensibility 
- Cleaner, maintainable design 
- Polymorphism  


Types of Inheritance 

1. Single Inheritance 
A child inherits from one parent. 

```python
# Parent → Child  

class Parent:  
    def display(self):  
        print("Parent class") 
 
class Child(Parent):  
    pass 
 
c = Child()  
c.display()    # Output: Parent class
```


2. Multi-level Inheritance 
A child inherits from a parent, and another class inherits from the child.

```python 
# Grandparent(Employee) → Parent(AdminStaff) → Child(Accountant)  

class Employee:  
    start_time = "9AM"  
    end_time = "5PM" 
 
class AdminStaff(Employee):  
    def __init__(self, role):  
        self.role = role  

class Accountant(AdminStaff):  
    def __init__(self, salary, role):  
        super().__init__(role)  
        self.salary = salary 
 
acc1 = Accountant(50_000, "CA")  

print(acc1.salary, acc1.role, acc1.start_time, acc1.end_time)
```




3. Multiple Inheritance 
A child inherits from more than one parent class. 

```python
class Teacher:  
    def __init__(self, salary):  
        self.salary = salary 
 
class Student():  
    def __init__(self, gpa):  
        self.gpa = gpa 
 
class TA(Teacher, Student):  
    def __init__(self, name, salary, gpa):  
        super().  init  (salary)                # call parent constructor
        Student.  init  (self, gpa)             # call parent constructor
        self.name = name
  
ta = TA("Rahul", 50_000, 7.5)  

print(ta.name, ta.salary, ta.gpa)
```
- super() keyword - Used to call parent class’s method from child class. 





### Abstraction 
Abstraction is hiding unnecessary implementation details and showing only the 
essential features to the user.

Example - In real life when we drive a car & press the breaks, the car stops. But we don’t need to know how the hydraulic systems work. To implement same idea in 
Python, we have abstraction. 

We implement abstraction with abstract classes & abstract methods. 

#### Abstract Class 
An abstract class in Python is one which: 
- Cannot be instantiated 
- Can contain normal + abstract methods 
- Usually acts as a blueprint for child classes

```python 
from abc import ABC, abstractmethod 
 
class Animal(ABC):  
    @abstractmethod  
    def sound(self):  
        pass


### Abstract Method 
It is a method declared but not implemented (Children must override abstract methods). 

```python
@abstractmethod  
def method_name(self): 
```

- Example of Abstraction 

```python
from abc import ABC, abstractmethod  

class Animal(ABC):  
    @abstractmethod  
    def make_sound():  
        pass
  
class Lion(Animal):  
    def make_sound(self):  
        print("Roar!")

class Cow(Animal):  
    def make_sound(self):  
        print("Moo!")  

lion = Lion()  
lion.make_sound()  

cow = Cow()  
cow.make_sound()
```





