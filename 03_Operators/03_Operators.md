## Operators in Python

Python provides different types of operators to perform various operations.  
These operators are categorized based on the type of operation they perform.

---

## 1. Arithmetic Operators

Arithmetic operators are used to perform mathematical calculations.

| Name            | Operator | Example |
|-----------------|----------|---------|
| Addition        | `+`      | `a + b` |
| Subtraction     | `-`      | `a - b` |
| Multiplication  | `*`      | `a * b` |
| Division        | `/`      | `a / b` |
| Exponential     | `**`     | `a ** b` |
| Modulus         | `%`      | `a % b` |
| Floor Division  | `//`     | `a // b` |

---

## 2. Assignment Operators

Assignment operators are used to assign values to variables.

| Name                    | Evaluated As |
|-------------------------|--------------|
| Assignment              | `a = b` |
| Add and Assign          | `a += b` → `a = a + b` |
| Subtract and Assign     | `a -= b` → `a = a - b` |
| Multiply and Assign     | `a *= b` → `a = a * b` |
| Divide and Assign       | `a /= b` → `a = a / b` |
| Floor Divide and Assign | `a //= b` → `a = a // b` |
| Modulus and Assign      | `a %= b` → `a = a % b` |
| Exponential and Assign  | `a **= b` → `a = a ** b` |
| Bitwise AND Assign      | `a &= b` → `a = a & b` |
| Bitwise XOR Assign      | `a ^= b` → `a = a ^ b` |
| Right Shift Assign      | `a >>= b` → `a = a >> b` |
| Left Shift Assign       | `a <<= b` → `a = a << b` |

---

## 3. Bitwise Operators

Bitwise operators are used to perform operations on binary numbers.

| Name                   | Operator | Example |
|------------------------|----------|---------|
| Bitwise AND            | `&`      | `a & b` |
| Bitwise OR             | `|`      | `a | b` |
| Bitwise NOT            | `~`      | `~a` |
| Bitwise XOR            | `^`      | `a ^ b` |
| Bitwise Right Shift    | `>>`     | `a >> b` |
| Bitwise Left Shift     | `<<`     | `a << b` |

---

## 4. Comparison Operators

Comparison operators are used to compare two values and return a boolean result.

| Name                     | Operator | Example |
|--------------------------|----------|---------|
| Equal                    | `==`     | `a == b` |
| Not Equal                | `!=`     | `a != b` |
| Less Than                | `<`      | `a < b` |
| Greater Than             | `>`      | `a > b` |
| Less Than or Equal To    | `<=`     | `a <= b` |
| Greater Than or Equal To | `>=`     | `a >= b` |

---

## 5. Identity Operators

Identity operators are used to compare the memory locations of two objects.

| Name      | Example      | Evaluated As |
|-----------|--------------|--------------|
| is        | `a is b`     | Returns `True` if both refer to the same object |
| is not    | `a is not b` | Returns `True` if both refer to different objects |

---

## 6. Logical Operators

Logical operators are used to combine conditional statements.

| Name | Operator | Example |
|-----|----------|---------|
| AND | `and` | `a == 2 and b == 3` |
| OR  | `or`  | `a == 2 or b == 3` |
| NOT | `not` | `not (a == 2 or b == 3)` |

---

## 7. Membership Operators

Membership operators are used to test whether a value exists in a sequence or collection.

| Name     | Example     | Evaluated As |
|----------|-------------|--------------|
| in       | `a in b`    | Returns `True` if `a` is present in `b` |
| not in   | `a not in b`| Returns `True` if `a` is not present in `b` |

---

## 8. Operator Precedence in Python

Operator precedence determines the order in which operations are evaluated.

| Precedence Level | Operator |
|------------------|----------|
| Highest          | `()` |
|                  | `**` |
|                  | `~`, `+`, `-` (Unary) |
|                  | `*`, `/`, `%`, `//` |
|                  | `+`, `-` |
|                  | `<<`, `>>` |
|                  | `&` |
|                  | `^`, `|` |
|                  | `<`, `>`, `<=`, `>=` |
|                  | `==`, `!=` |
|                  | `=`, `+=`, `-=`, `*=`, `/=`, `//=`, `%=` , `**=` |
|                  | `is`, `is not` |
| Lowest           | `in`, `not in`, `and`, `or`, `not` |

---
