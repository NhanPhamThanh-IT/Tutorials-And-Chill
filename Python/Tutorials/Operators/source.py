# Python Operators Tutorial for Beginners

# --- 1. Arithmetic Operators ---
# Used to perform mathematical operations like addition, subtraction, multiplication, etc.

print("--- Arithmetic Operators ---")
a = 10
b = 3

# Addition (+)
sum_result = a + b
print(f"{a} + {b} = {sum_result}")  # Output: 10 + 3 = 13

# Subtraction (-)
diff_result = a - b
print(f"{a} - {b} = {diff_result}")  # Output: 10 - 3 = 7

# Multiplication (*)
prod_result = a * b
print(f"{a} * {b} = {prod_result}")  # Output: 10 * 3 = 30

# Division (/) - always returns a float
div_result = a / b
print(f"{a} / {b} = {div_result}")  # Output: 10 / 3 = 3.333...

# Modulus (%) - returns the remainder of the division
mod_result = a % b
print(f"{a} % {b} = {mod_result}")  # Output: 10 % 3 = 1

# Exponentiation (**) - raises the first operand to the power of the second
exp_result = a ** b
print(f"{a} ** {b} = {exp_result}") # Output: 10 ** 3 = 1000

# Floor Division (//) - divides and rounds down to the nearest whole number (integer)
floor_div_result = a // b
print(f"{a} // {b} = {floor_div_result}") # Output: 10 // 3 = 3
print("-" * 20)


# --- 2. Comparison (Relational) Operators ---
# Used to compare two values. They return either True or False.

print("--- Comparison Operators ---")
x = 5
y = 8

# Equal to (==)
print(f"{x} == {y} is {x == y}")  # Output: 5 == 8 is False

# Not equal to (!=)
print(f"{x} != {y} is {x != y}")  # Output: 5 != 8 is True

# Greater than (>)
print(f"{x} > {y} is {x > y}")   # Output: 5 > 8 is False

# Less than (<)
print(f"{x} < {y} is {x < y}")   # Output: 5 < 8 is True

# Greater than or equal to (>=)
print(f"{x} >= {y} is {x >= y}") # Output: 5 >= 8 is False
print(f"5 >= 5 is {5 >= 5}")   # Output: 5 >= 5 is True

# Less than or equal to (<=)
print(f"{x} <= {y} is {x <= y}") # Output: 5 <= 8 is True
print(f"8 <= 5 is {8 <= 5}")   # Output: 8 <= 5 is False
print("-" * 20)


# --- 3. Assignment Operators ---
# Used to assign values to variables.

print("--- Assignment Operators ---")
num = 10
print(f"Initial num: {num}") # Output: Initial num: 10

# Add and assign (+=)
num += 5  # Equivalent to: num = num + 5
print(f"After += 5: {num}") # Output: After += 5: 15

# Subtract and assign (-=)
num -= 3  # Equivalent to: num = num - 3
print(f"After -= 3: {num}") # Output: After -= 3: 12

# Multiply and assign (*=)
num *= 2  # Equivalent to: num = num * 2
print(f"After *= 2: {num}") # Output: After *= 2: 24

# Divide and assign (/=)
num /= 4  # Equivalent to: num = num / 4
print(f"After /= 4: {num}") # Output: After /= 4: 6.0 (Note: division results in float)

# Modulus and assign (%=)
num = 10 # Reset num
num %= 3  # Equivalent to: num = num % 3
print(f"After %= 3 (starting from 10): {num}") # Output: After %= 3 (starting from 10): 1

# Exponentiate and assign (**=)
num = 2
num **= 3 # Equivalent to: num = num ** 3
print(f"After **= 3 (starting from 2): {num}") # Output: After **= 3 (starting from 2): 8

# Floor divide and assign (//=)
num = 17
num //= 5 # Equivalent to: num = num // 5
print(f"After //= 5 (starting from 17): {num}") # Output: After //= 5 (starting from 17): 3
print("-" * 20)


# --- 4. Logical Operators ---
# Used to combine conditional statements. Return True or False.

print("--- Logical Operators ---")
p = True
q = False

# Logical AND (and) - True only if both operands are True
print(f"{p} and {q} is {p and q}")   # Output: True and False is False
print(f"{p} and {True} is {p and True}") # Output: True and True is True

# Logical OR (or) - True if at least one operand is True
print(f"{p} or {q} is {p or q}")     # Output: True or False is True
print(f"{q} or {False} is {q or False}") # Output: False or False is False

# Logical NOT (not) - Reverses the logical state
print(f"not {p} is {not p}")         # Output: not True is False
print(f"not {q} is {not q}")         # Output: not False is True

# Example combining comparison and logical operators
age = 25
has_ticket = True
print(f"Can enter (age > 18 and has_ticket)? {(age > 18) and has_ticket}") # Output: Can enter (age > 18 and has_ticket)? True
print("-" * 20)


# --- 5. Bitwise Operators ---
# Used to perform operations on binary representations of integers.
# (Often less common for absolute beginners, but good to know they exist)

print("--- Bitwise Operators ---")
val1 = 6  # Binary: 0110
val2 = 2  # Binary: 0010

# Bitwise AND (&) - Sets each bit to 1 if both bits are 1
print(f"{val1} & {val2} = {val1 & val2}") # 0110 & 0010 = 0010 (Decimal 2)

# Bitwise OR (|) - Sets each bit to 1 if one of the two bits is 1
print(f"{val1} | {val2} = {val1 | val2}") # 0110 | 0010 = 0110 (Decimal 6)

# Bitwise XOR (^) - Sets each bit to 1 if only one of the two bits is 1
print(f"{val1} ^ {val2} = {val1 ^ val2}") # 0110 ^ 0010 = 0100 (Decimal 4)

# Bitwise NOT (~) - Inverts all the bits (tricky due to two's complement representation)
print(f"~{val1} = {~val1}") # -(val1 + 1) = -(6 + 1) = -7

# Left Shift (<<) - Shifts bits left, filling with zeros (equivalent to multiplying by 2^n)
print(f"{val1} << 1 = {val1 << 1}") # 0110 << 1 = 1100 (Decimal 12)

# Right Shift (>>) - Shifts bits right, discarding bits (equivalent to floor dividing by 2^n)
print(f"{val1} >> 1 = {val1 >> 1}") # 0110 >> 1 = 0011 (Decimal 3)
print("-" * 20)


# --- 6. Membership Operators ---
# Used to test if a sequence (like list, tuple, string, set, dictionary) contains a value.

print("--- Membership Operators ---")
my_list = [1, 2, 3, "apple", "banana"]
my_string = "hello world"

# in - Returns True if the value is found in the sequence
print(f"3 in my_list? {3 in my_list}")             # Output: 3 in my_list? True
print(f"'orange' in my_list? {'orange' in my_list}") # Output: 'orange' in my_list? False
print(f"'world' in my_string? {'world' in my_string}") # Output: 'world' in my_string? True

# not in - Returns True if the value is NOT found in the sequence
print(f"4 not in my_list? {4 not in my_list}")         # Output: 4 not in my_list? True
print(f"'apple' not in my_list? {'apple' not in my_list}") # Output: 'apple' not in my_list? False
print("-" * 20)


# --- 7. Identity Operators ---
# Used to compare the memory locations of two objects.

print("--- Identity Operators ---")
list1 = [1, 2, 3]
list2 = [1, 2, 3]
list3 = list1 # list3 now refers to the *same* object as list1

# is - Returns True if both variables point to the same object in memory
print(f"list1 is list2? {list1 is list2}") # Output: list1 is list2? False (different objects, even if content is same)
print(f"list1 is list3? {list1 is list3}") # Output: list1 is list3? True (same object)

# is not - Returns True if both variables point to different objects in memory
print(f"list1 is not list2? {list1 is not list2}") # Output: list1 is not list2? True
print(f"list1 is not list3? {list1 is not list3}") # Output: list1 is not list3? False

# Note: For immutable types like integers, strings (sometimes), Python might reuse objects
a = 5
b = 5
print(f"a=5, b=5. a is b? {a is b}") # Output: a=5, b=5. a is b? True (Python often reuses small integers)

c = "hello"
d = "hello"
print(f"c='hello', d='hello'. c is d? {c is d}") # Output: c='hello', d='hello'. c is d? True (String interning)
print("-" * 20)

print("End of Operator Examples")