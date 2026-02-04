# VARIABLES 

name = "Python"
age = 22
price = 199.99

print("Name:", name)
print("Age:", age)
print("Price:", price)


# Multiple Variable Assignment

a, b, c = 10, 20, 30
print("\nMultiple Assignment:", a, b, c)



# Same Value to Multiple Variables

x = y = z = 100
print("\nSame Value Assignment:", x, y, z)



# Variable Reassignment

count = 5
print("\nBefore Reassignment:", count)

count = 15
print("After Reassignment:", count)



# Dynamic Typing

value = 10
print("\nValue:", value, "| Type:", type(value))

value = "Python Programming"
print("Value:", value, "| Type:", type(value))



# Object Identity (Memory Location)

a = 10
b = 10
print("\nObject Identity:")
print("id(a):", id(a))
print("id(b):", id(b))



# Variable Deletion

temp = 50
print("\nBefore deletion:", temp)

del temp
# print(temp)  # Uncommenting this line will raise NameError



# Variable Scope (Intro)

global_var = "I am global"

def demo_scope():
    local_var = "I am local"
    print("\nInside function:", global_var)
    print("Inside function:", local_var)

demo_scope()
# print(local_var)  # NameError (local scope)
