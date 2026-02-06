# 1. ARITHMETIC OPERATORS

a = 10
b = 3

print("Arithmetic Operators")
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)        # Always returns float
print("Floor Division:", a // b)
print("Modulus:", a % b)
print("Exponentiation:", a ** b)

print("-" * 40)



# 2. ASSIGNMENT OPERATORS

x = 5
print("Initial x:", x)

x += 2
print("x += 2:", x)

x -= 1
print("x -= 1:", x)

x *= 3
print("x *= 3:", x)

x /= 2
print("x /= 2:", x)

x //= 2
print("x //= 2:", x)

x %= 3
print("x %= 3:", x)

x **= 2
print("x **= 2:", x)

print("-" * 40)



# 3. COMPARISON (RELATIONAL) OPERATORS

p = 10
q = 20

print("Comparison Operators")
print("p == q:", p == q)
print("p != q:", p != q)
print("p > q:", p > q)
print("p < q:", p < q)
print("p >= q:", p >= q)
print("p <= q:", p <= q)

print("-" * 40)



# 4. LOGICAL OPERATORS

age = 25

print("Logical Operators")
print("AND:", age > 18 and age < 60)
print("OR:", age > 60 or age < 18)
print("NOT:", not(age < 18))

print("-" * 40)



# 5. BITWISE OPERATORS

m = 5   # 0101
n = 3   # 0011

print("Bitwise Operators")
print("AND (&):", m & n)
print("OR (|):", m | n)
print("XOR (^):", m ^ n)
print("NOT (~):", ~m)
print("Left Shift (<<):", m << 1)
print("Right Shift (>>):", m >> 1)

print("-" * 40)



# 6. MEMBERSHIP OPERATORS

languages = ["Python", "Java", "C++"]

print("Membership Operators")
print("'Python' in languages:", "Python" in languages)
print("'Go' not in languages:", "Go" not in languages)

print("-" * 40)



# 7. IDENTITY OPERATORS

a = [1, 2, 3]
b = a
c = [1, 2, 3]

print("Identity Operators")
print("a is b:", a is b)        # Same memory
print("a is c:", a is c)        # Different memory
print("a == c:", a == c)        # Same values

print("-" * 40)



# 8. OPERATOR PRECEDENCE

result1 = 10 + 3 * 2
result2 = (10 + 3) * 2

print("Operator Precedence")
print("10 + 3 * 2 =", result1)
print("(10 + 3) * 2 =", result2)

print("-" * 40)
