# 12 : Object Oriented Programming in Python


# Classes and Objects

# ===============================
# Classes 
# ===============================

class Car:
    brand = "Toyota"

# ===============================
# Objects
# ===============================

car1 = Car()
car2 = Car()

print(car1.brand)     # Toyota
print(car2.brand)     # Toyota


# ===============================
# Constructor in OOP
# ===============================

class Student:
    def __init__(self):
        print("Constructor was called")


stu1 = Student()


# ===============================
# self Keyword
# ===============================

class Student:
    def __init__(self, name):
        self.name = name


stu1 = Student("Rahul")
print(stu1.name)


# ===============================
# Parameterized Constructor
# ===============================

class Student:
    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa


s1 = Student("Rahul", 8.7)


# Types of Attributes 

# ===============================
# 1. Class Attribute
# ===============================

class Student:
    college = "ABC college"        # class attribute


stu1 = Student()
print(stu1.college)
print(Student.college)     # class attribute can also be accessed with class name



# ===============================
# 2. Instance Attributes
# ===============================

class Student:
    def __init__(self, name, gpa):       # instance attributes
        self.name = name
        self.gpa = gpa


stu1 = Student("Rahul", 8.7)
print(stu1.name, stu1.gpa)



# Types of Methods

# ===============================
# 1. Instance Method
# ===============================

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):            # Instance method
        print(f"Name: {self.name}, Marks: {self.marks}")


# ===============================
# 2. Class Method
# ===============================

class Student:
    school_name = "ABC School"

    @classmethod
    def change_school(cls, new_name):
        cls.school_name = new_name


# ===============================
# 3. Static Method
# ===============================

class Math:
    @staticmethod
    def add(a, b):
        return a + b


# The 4 Pillars of OOP
# ===============================
# Encapsulation
# ===============================

# 1. Public Members
class Student:
    def __init__(self, name):
        self.name = name        # public variable 


s = Student("Rahul")
print(s.name)               # Allowed 


# 2. Protected Members
class Person:
    def __init__(self):
        self._age = 20     # protected variable


p = Person()
print(p._age)        # Technically allowed, but not recommended


# 3. Private Members
class Bank:
    def __init__(self, balance):
        self.__balance = balance     # private variable


b = Bank(5000)
# print(b.__balance)      # ERROR : attribute not accessible

print(b._Bank__balance)       # Allowed (name-mangled form)


# ===============================
# Getters & Setters
# ===============================

class Employee:
    def __init__(self, salary):
        self.__salary = salary            # private

    def get_salary(self):                 # getter
        return self.__salary

    def set_salary(self, new_salary):     # setter 
        self.__salary = new_salary


e = Employee(50000)
print(e.get_salary())
e.set_salary(60000)


# ===============================
# Inheritance
# ===============================

class Employee:                  # parent class        
    start_time = "9AM"
    end_time = "5PM"


class Teacher(Employee):         # child class
    def __init__(self, subject):
        self.subject = subject


t1 = Teacher("Data Science")
print(t1.subject, t1.start_time, t1.end_time)



# Types of Inheritance 		
					
# ===============================
# 1. Single Inheritance
# ===============================

class Parent:
    def display(self):
        print("Parent class")


class Child(Parent):
    pass


c = Child()
c.display()         # Output: Parent class


# ===============================
# 2. Multi-level Inheritance
# ===============================

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


# ===============================
# 3. Multiple Inheritance
# ===============================

class Teacher:
    def __init__(self, salary):
        self.salary = salary


class Student:
    def __init__(self, gpa):
        self.gpa = gpa


class TA(Teacher, Student):
    def __init__(self, name, salary, gpa):
        Teacher.__init__(self, salary)         # call parent constructor
        Student.__init__(self, gpa)            # call parent constructor
        self.name = name


ta = TA("Rahul", 50_000, 7.5)
print(ta.name, ta.salary, ta.gpa)


# ===============================
# Abstraction
# ===============================

from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass


class Lion(Animal):
    def sound(self):
        print("Roar!")


class Cow(Animal):
    def sound(self):
        print("Moo!")


lion = Lion()
lion.sound()

cow = Cow()
cow.sound()


# ===============================
# Polymorphism
# ===============================

# Operator Overloading
print(1 + 2)
print("1" + "2")


# Method Overriding
class Animal:
    def sound(self):
        print("Some generic sound")


class Dog(Animal):
    def sound(self):
        print("Bark")


a = Animal() 
dog = Dog()

a.sound()         # Some generic sound 
dog.sound()       # Bark


# Duck Typing

class Dog:
    def speak(self):
        print("Bark")


class Cat:
    def speak(self):
        print("Meow")


class Robot:
    def speak(self):
        print("Beep Boop")


def make_it_speak(entity):
    entity.speak()               # doesn’t care about type


d = Dog()
c = Cat()
r = Robot()

for e in [d, c, r]:
    make_it_speak(e)

