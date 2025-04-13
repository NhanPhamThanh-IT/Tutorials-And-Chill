# Booleans in Python

# 1. What are Booleans?
# Booleans represent one of two values: True or False.
# They are fundamental in programming for logic and decision making.
# Note: True and False are keywords and must be capitalized.

print("--- 1. Boolean Values ---")
print(True)
print(False)
# print(true) # This would cause an error because 'true' is not defined
# print(false) # This would cause an error because 'false' is not defined

# 2. Boolean Variables
# You can assign True or False to variables.
print("\n--- 2. Boolean Variables ---")
is_learning = True
is_difficult = False

print("Am I learning Python?", is_learning)
print("Is Python difficult?", is_difficult)
print("Type of is_learning:", type(is_learning)) # Output: <class 'bool'>

# 3. Comparison Operators
# These operators compare two values and return a boolean result.
print("\n--- 3. Comparison Operators ---")
x = 10
y = 5

# Equal to (==)
print(f"{x} == {y}:", x == y)  # False
print(f"5 == 5:", 5 == 5)      # True

# Not equal to (!=)
print(f"{x} != {y}:", x != y)  # True
print(f"5 != 5:", 5 != 5)      # False

# Greater than (>)
print(f"{x} > {y}:", x > y)    # True
print(f"{y} > {x}:", y > x)    # False

# Less than (<)
print(f"{x} < {y}:", x < y)    # False
print(f"{y} < {x}:", y < x)    # True

# Greater than or equal to (>=)
print(f"{x} >= {y}:", x >= y)  # True
print(f"{x} >= 10:", x >= 10) # True

# Less than or equal to (<=)
print(f"{y} <= {x}:", y <= x)  # True
print(f"{y} <= 5:", y <= 5)   # True

# Comparing strings
print("'hello' == 'hello':", 'hello' == 'hello') # True
print("'hello' == 'world':", 'hello' == 'world') # False
print("'apple' < 'banana':", 'apple' < 'banana') # True (lexicographical comparison)

# 4. Logical Operators
# These operators combine boolean values.
print("\n--- 4. Logical Operators ---")
has_coffee = True
is_tired = False

# and: Returns True only if BOTH operands are True
print(f"has_coffee and is_tired:", has_coffee and is_tired) # False
print(f"True and True:", True and True)                     # True
print(f"True and False:", True and False)                   # False
print(f"False and False:", False and False)                 # False

# or: Returns True if AT LEAST ONE operand is True
print(f"has_coffee or is_tired:", has_coffee or is_tired)   # True
print(f"True or True:", True or True)                       # True
print(f"True or False:", True or False)                     # True
print(f"False or False:", False or False)                   # False

# not: Reverses the boolean value (negation)
print(f"not is_tired:", not is_tired)                       # True
print(f"not has_coffee:", not has_coffee)                   # False
print(f"not True:", not True)                               # False
print(f"not False:", not False)                             # True

# Combining logical operators (use parentheses for clarity)
can_code = has_coffee and (not is_tired)
print(f"Can I code? (has_coffee and not is_tired):", can_code) # True

# 5. Truthiness (Boolean Context)
# In Python, many values other than True and False have a boolean meaning
# when used in conditions (like if statements).

print("\n--- 5. Truthiness ---")

# Values considered False (Falsy):
# - The boolean value False itself
# - None (represents the absence of a value)
# - Zero of any numeric type (0, 0.0, 0j)
# - Empty sequences ( '', [], (), {} )
# - Empty mappings ( {} )
# - Objects from user-defined classes that have a __bool__ or __len__ method
#   that returns False or 0.

print("Boolean value of False:", bool(False))     # False
print("Boolean value of None:", bool(None))       # False
print("Boolean value of 0:", bool(0))           # False
print("Boolean value of 0.0:", bool(0.0))         # False
print("Boolean value of empty string '':", bool('')) # False
print("Boolean value of empty list []:", bool([]))   # False
print("Boolean value of empty tuple ():", bool(()))   # False
print("Boolean value of empty dictionary {}:", bool({})) # False

# Values considered True (Truthy):
# - The boolean value True itself
# - Most non-zero numbers (e.g., 1, -1, 0.5)
# - Non-empty sequences (e.g., 'hello', [1, 2], (3,))
# - Non-empty mappings (e.g., {'a': 1})
# - Most objects

print("Boolean value of True:", bool(True))       # True
print("Boolean value of 1:", bool(1))           # True
print("Boolean value of -10:", bool(-10))         # True
print("Boolean value of 'hello':", bool('hello')) # True
print("Boolean value of [1, 2]:", bool([1, 2]))   # True
print("Boolean value of {'key': 'value'}:", bool({'key': 'value'})) # True

# Example using truthiness in an if statement:
my_list = []
if my_list: # This checks if my_list is truthy (it's not, because it's empty)
    print("My list is not empty.")
else:
    print("My list is empty.")

my_name = "Alice"
if my_name: # This checks if my_name is truthy (it is, because it's a non-empty string)
    print(f"Hello, {my_name}!")
else:
    print("Name is not provided.")


# 6. Booleans in Control Flow
print("\n--- 6. Booleans in Control Flow ---")

# if/elif/else statements rely heavily on boolean conditions
age = 25
has_ticket = True

if age >= 18 and has_ticket:
    print("Access granted to the event.")
elif age < 18:
    print("Access denied: Too young.")
else: # This covers the case where age >= 18 but has_ticket is False
    print("Access denied: No ticket.")

# while loops continue as long as a condition is True
count = 0
keep_counting = True
while keep_counting:
    print(f"Count is: {count}")
    count += 1
    if count >= 3:
        keep_counting = False # Change the boolean to stop the loop

print("Loop finished.")

# A more direct way to use booleans in while loops:
count = 0
while count < 3: # The loop continues as long as count < 3 is True
    print(f"Direct count: {count}")
    count += 1
print("Direct loop finished.")


# 7. The bool() Function
# You can explicitly convert other types to booleans using bool().
# This is useful for understanding truthiness or when a function requires
# a strict boolean type.
print("\n--- 7. The bool() Function ---")

value1 = 100
value2 = 0
value3 = "Python"
value4 = ""
value5 = None
value6 = [1, 2]
value7 = []

print(f"bool({value1}) =", bool(value1)) # True
print(f"bool({value2}) =", bool(value2)) # False
print(f"bool('{value3}') =", bool(value3)) # True
print(f"bool('{value4}') =", bool(value4)) # False
print(f"bool({value5}) =", bool(value5)) # False
print(f"bool({value6}) =", bool(value6)) # True
print(f"bool({value7}) =", bool(value7)) # False

# Summary:
# Booleans (True/False) are essential for:
# - Representing logical states.
# - Making decisions using comparison and logical operators.
# - Controlling the flow of execution in if statements and loops.
# - Understanding the "truthiness" of different data types in Python.