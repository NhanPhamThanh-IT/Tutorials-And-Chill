# Python Operators

Operators are special symbols in Python that carry out arithmetic or logical computation. The value that the operator operates on is called the operand.

For example:
```python
>>> 2 + 3
5
```
Here, `+` is the operator that performs addition. `2` and `3` are the operands.

Python includes the following types of operators:

1.  **Arithmetic Operators**
2.  **Comparison (Relational) Operators**
3.  **Assignment Operators**
4.  **Logical Operators**
5.  **Bitwise Operators**
6.  **Membership Operators**
7.  **Identity Operators**

Let's look at them in detail.

## 1. Arithmetic Operators

Arithmetic operators are used to perform mathematical operations like addition, subtraction, multiplication, etc.

| Operator | Name                 | Description                                           | Example (a=10, b=3) |
| :------- | :------------------- | :---------------------------------------------------- | :------------------ |
| `+`      | Addition             | Adds values on either side of the operator            | `a + b` = 13        |
| `-`      | Subtraction          | Subtracts right hand operand from left hand operand   | `a - b` = 7         |
| `*`      | Multiplication       | Multiplies values on either side of the operator      | `a * b` = 30        |
| `/`      | Division             | Divides left hand operand by right hand operand       | `a / b` = 3.333...  |
| `%`      | Modulus              | Divides left hand operand by right hand operand and returns remainder | `a % b` = 1         |
| `**`     | Exponent (Power)     | Performs exponential (power) calculation on operators | `a ** b` = 1000     |
| `//`     | Floor Division       | Division of operands where the result is the quotient in which the digits after the decimal point are removed. | `a // b` = 3        |

**Examples:**

```python
a = 10
b = 3

print('a + b =', a + b)      # Output: a + b = 13
print('a - b =', a - b)      # Output: a - b = 7
print('a * b =', a * b)      # Output: a * b = 30
print('a / b =', a / b)      # Output: a / b = 3.3333333333333335
print('a % b =', a % b)      # Output: a % b = 1
print('a ** b =', a ** b)    # Output: a ** b = 1000
print('a // b =', a // b)    # Output: a // b = 3

# Example with floating point numbers
x = 10.5
y = 2.0
print('x / y =', x / y)      # Output: x / y = 5.25
print('x // y =', x // y)    # Output: x // y = 5.0
```

## 2. Comparison (Relational) Operators

Comparison operators are used to compare values. They return either `True` or `False` according to the condition.

| Operator | Name                     | Description                                                                               | Example (a=10, b=20) |
| :------- | :----------------------- | :---------------------------------------------------------------------------------------- | :------------------- |
| `==`     | Equal                    | If the values of two operands are equal, then the condition becomes true.                 | `(a == b)` is False. |
| `!=`     | Not equal                | If values of two operands are not equal, then condition becomes true.                     | `(a != b)` is True.  |
| `>`      | Greater than             | If the value of left operand is greater than the value of right operand, then condition becomes true. | `(a > b)` is False.  |
| `<`      | Less than                | If the value of left operand is less than the value of right operand, then condition becomes true. | `(a < b)` is True.   |
| `>=`     | Greater than or equal to | If the value of left operand is greater than or equal to the value of right operand, then condition becomes true. | `(a >= b)` is False. |
| `<=`     | Less than or equal to    | If the value of left operand is less than or equal to the value of right operand, then condition becomes true. | `(a <= b)` is True.  |

**Examples:**

```python
a = 10
b = 20

print('a == b:', a == b)  # Output: a == b: False
print('a != b:', a != b)  # Output: a != b: True
print('a > b:', a > b)    # Output: a > b: False
print('a < b:', a < b)    # Output: a < b: True
print('a >= b:', a >= b)  # Output: a >= b: False
print('a <= b:', a <= b)  # Output: a <= b: True
```

## 3. Assignment Operators

Assignment operators are used in Python to assign values to variables. `a = 5` is a simple assignment operator that assigns the value 5 on the right to the variable `a` on the left.

There are various compound operators in Python like `a += 5` that adds to the variable and later assigns the same. It is equivalent to `a = a + 5`.

| Operator | Example   | Equivalent to |
| :------- | :-------- | :------------ |
| `=`      | `x = 5`   | `x = 5`       |
| `+=`     | `x += 5`  | `x = x + 5`   |
| `-=`     | `x -= 5`  | `x = x - 5`   |
| `*=`     | `x *= 5`  | `x = x * 5`   |
| `/=`     | `x /= 5`  | `x = x / 5`   |
| `%=`     | `x %= 5`  | `x = x % 5`   |
| `//=`    | `x //= 5` | `x = x // 5`  |
| `**=`    | `x **= 5` | `x = x ** 5`  |
| `&=`     | `x &= 5`  | `x = x & 5`   |
| `|=`     | `x |= 5`  | `x = x | 5`   |
| `^=`     | `x ^= 5`  | `x = x ^ 5`   |
| `>>=`    | `x >>= 5` | `x = x >> 5`  |
| `<<=`    | `x <<= 5` | `x = x << 5`  |

**Examples:**

```python
a = 10

# Assign value
b = a
print('b =', b) # Output: b = 10

# Add and assign
b += a  # equivalent to b = b + a
print('b += a -> b =', b) # Output: b += a -> b = 20

# Subtract and assign
b -= a  # equivalent to b = b - a
print('b -= a -> b =', b) # Output: b -= a -> b = 10

# Multiply and assign
b *= a  # equivalent to b = b * a
print('b *= a -> b =', b) # Output: b *= a -> b = 100

# Divide and assign
b /= a  # equivalent to b = b / a
print('b /= a -> b =', b) # Output: b /= a -> b = 10.0

# Modulus and assign
c = 15
c %= a # equivalent to c = c % a
print('c %= a -> c =', c) # Output: c %= a -> c = 5

# Floor Division and assign
d = 27
d //= a # equivalent to d = d // a
print('d //= a -> d =', d) # Output: d //= a -> d = 2

# Exponent and assign
e = 2
e **= a # equivalent to e = e ** a
print('e **= a -> e =', e) # Output: e **= a -> e = 1024
```

## 4. Logical Operators

Logical operators are used to combine conditional statements.

| Operator | Description                                                | Example (x=True, y=False) |
| :------- | :--------------------------------------------------------- | :------------------------ |
| `and`    | Returns `True` if both statements are true                 | `x and y` is False        |
| `or`     | Returns `True` if one of the statements is true            | `x or y` is True          |
| `not`    | Reverse the result, returns `False` if the result is true | `not x` is False          |

**Examples:**

```python
x = True
y = False

# and operator
print('x and y is', x and y) # Output: x and y is False
print('x and x is', x and x) # Output: x and x is True

# or operator
print('x or y is', x or y)   # Output: x or y is True
print('y or y is', y or y)   # Output: y or y is False

# not operator
print('not x is', not x)     # Output: not x is False
print('not y is', not y)     # Output: not y is True

# Combining with comparison operators
a = 5
b = 10
c = 5

print((a < b) and (a == c)) # Output: True (True and True)
print((a > b) or (a != c))  # Output: False (False or False)
print(not (a == c))         # Output: False (not True)
```

## 5. Bitwise Operators

Bitwise operators act on operands as if they were strings of binary digits. They operate bit by bit, hence the name.

*(Note: These are often used in more advanced scenarios and might be less common for absolute beginners, but are included for completeness.)*

| Operator | Name                 | Description                                                                 |
| :------- | :------------------- | :-------------------------------------------------------------------------- |
| `&`      | Bitwise AND          | Sets each bit to 1 if both bits are 1                                       |
| `|`      | Bitwise OR           | Sets each bit to 1 if one of two bits is 1                                  |
| `^`      | Bitwise XOR          | Sets each bit to 1 if only one of two bits is 1                             |
| `~`      | Bitwise NOT          | Inverts all the bits                                                        |
| `<<`     | Bitwise left shift   | Shift left by pushing zeros in from the right and let the leftmost bits fall off |
| `>>`     | Bitwise right shift  | Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off |

**Examples:**

```python
a = 10  # Binary: 1010
b = 4   # Binary: 0100

# Bitwise AND
print('a & b =', a & b)    # Output: a & b = 0 (Binary: 0000)

# Bitwise OR
print('a | b =', a | b)    # Output: a | b = 14 (Binary: 1110)

# Bitwise XOR
print('a ^ b =', a ^ b)    # Output: a ^ b = 14 (Binary: 1110)

# Bitwise NOT
# Note: The result of ~a is -(a+1) due to two's complement representation
print('~a =', ~a)          # Output: ~a = -11

# Bitwise left shift
print('a << 2 =', a << 2)  # Output: a << 2 = 40 (Binary: 101000)

# Bitwise right shift
print('a >> 2 =', a >> 2)  # Output: a >> 2 = 2 (Binary: 10)
```

## 6. Membership Operators

Membership operators are used to test if a sequence is presented in an object, such as strings, lists, tuples, sets, or dictionaries.

| Operator | Description                                                                    | Example                               |
| :------- | :----------------------------------------------------------------------------- | :------------------------------------ |
| `in`     | Returns `True` if a sequence with the specified value is present in the object | `x in y`                              |
| `not in` | Returns `True` if a sequence with the specified value is not present in the object | `x not in y`                          |

**Examples:**

```python
my_list = [1, 2, 3, 4, 5]
my_string = "Hello World"

# in operator
print(3 in my_list)         # Output: True
print(6 in my_list)         # Output: False
print('H' in my_string)     # Output: True
print('hello' in my_string) # Output: False (case-sensitive)

# not in operator
print(6 not in my_list)     # Output: True
print(3 not in my_list)     # Output: False
print('World' not in my_string) # Output: False
print('Bye' not in my_string)   # Output: True

# Example with dictionary (checks keys by default)
my_dict = {'a': 1, 'b': 2}
print('a' in my_dict)       # Output: True
print(1 in my_dict)       # Output: False (checks keys, not values)
print('c' not in my_dict)   # Output: True
```

## 7. Identity Operators

Identity operators compare the memory locations of two objects.

| Operator | Description                                                            | Example      |
| :------- | :--------------------------------------------------------------------- | :----------- |
| `is`     | Returns `True` if both variables are the same object (point to the same memory location) | `x is y`     |
| `is not` | Returns `True` if both variables are not the same object               | `x is not y` |

**Important Note:** `is` is different from `==`. The `==` operator compares the *values* of two objects, while the `is` operator checks if two variables refer to the *exact same object* in memory.

**Examples:**

```python
x1 = 5
y1 = 5
x2 = 'Hello'
y2 = 'Hello'
x3 = [1, 2, 3]
y3 = [1, 2, 3]
z3 = x3 # z3 now refers to the same list object as x3

# Comparing immutable types like integers and strings
# Python often reuses objects for small integers and strings for efficiency
print('x1 is y1:', x1 is y1)     # Output: x1 is y1: True (Often True for small integers)
print('x1 == y1:', x1 == y1)     # Output: x1 == y1: True
print('x2 is y2:', x2 is y2)     # Output: x2 is y2: True (Often True for identical string literals)
print('x2 == y2:', x2 == y2)     # Output: x2 == y2: True

# Comparing mutable types like lists
print('x3 is y3:', x3 is y3)     # Output: x3 is y3: False (x3 and y3 are different list objects in memory)
print('x3 == y3:', x3 == y3)     # Output: x3 == y3: True (The contents/values are the same)

# Comparing when one variable is assigned to another
print('x3 is z3:', x3 is z3)     # Output: x3 is z3: True (Both refer to the same list object)
print('x3 == z3:', x3 == z3)     # Output: x3 == z3: True

# Using 'is not'
print('x1 is not y1:', x1 is not y1) # Output: x1 is not y1: False
print('x3 is not y3:', x3 is not y3) # Output: x3 is not y3: True
print('x3 is not z3:', x3 is not z3) # Output: x3 is not z3: False
```

Understanding these operators is fundamental to writing Python code for performing calculations, making decisions, and manipulating data.