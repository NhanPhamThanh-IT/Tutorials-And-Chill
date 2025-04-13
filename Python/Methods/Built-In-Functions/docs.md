# Python Built-in Functions

Python comes with a set of functions that are always available for you to use without needing to import any module. These are known as built-in functions. They perform common tasks and are essential tools for any Python programmer.

Here's a look at some of the most commonly used built-in functions:

## `print()`

Prints the specified message to the screen or other standard output device.

**Syntax:** `print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)`

**Example:**

```python
print("Hello, World!")
# Output: Hello, World!

name = "Alice"
age = 30
print("Name:", name, "Age:", age)
# Output: Name: Alice Age: 30
```

## `input()`

Allows user input. It reads a line from the input (usually the user), converts it into a string, and returns it.

**Syntax:** `input(prompt)`

**Example:**

```python
name = input("Enter your name: ")
print("Hello,", name)

# Example run:
# Enter your name: Bob
# Hello, Bob
```

## `len()`

Returns the number of items (length) in an object. The object can be a sequence (like a string, list, tuple) or a collection (like a dictionary or set).

**Syntax:** `len(s)`

**Example:**

```python
my_list = [1, 2, 3, 4]
print(len(my_list))
# Output: 4

my_string = "Python"
print(len(my_string))
# Output: 6
```

## `type()`

Returns the type of an object.

**Syntax:** `type(object)`

**Example:**

```python
x = 5
print(type(x))
# Output: <class 'int'>

y = "Hello"
print(type(y))
# Output: <class 'str'>

z = [1, 2, 3]
print(type(z))
# Output: <class 'list'>
```

## `int()`, `float()`, `str()`

These functions convert values from one type to another.
*   `int()`: Converts a value to an integer.
*   `float()`: Converts a value to a floating-point number.
*   `str()`: Converts a value to a string.

**Syntax:**
`int(x, base=10)`
`float(x)`
`str(object)`

**Example:**

```python
num_str = "10"
num_int = int(num_str)
print(num_int, type(num_int))
# Output: 10 <class 'int'>

num_int = 5
num_float = float(num_int)
print(num_float, type(num_float))
# Output: 5.0 <class 'float'>

num_float = 9.99
num_str = str(num_float)
print(num_str, type(num_str))
# Output: 9.99 <class 'str'>

# int() can also handle different bases
binary_str = "101"
decimal_val = int(binary_str, 2) # Convert binary string to integer
print(decimal_val)
# Output: 5
```

## `list()`, `tuple()`, `set()`, `dict()`

These functions create lists, tuples, sets, and dictionaries, respectively, often from iterables.

**Syntax:**
`list(iterable)`
`tuple(iterable)`
`set(iterable)`
`dict(**kwarg)` or `dict(mapping, **kwarg)` or `dict(iterable, **kwarg)`

**Example:**

```python
my_tuple = (1, 2, 3)
my_list = list(my_tuple)
print(my_list, type(my_list))
# Output: [1, 2, 3] <class 'list'>

my_list = [1, 2, 2, 3]
my_set = set(my_list) # Sets only store unique elements
print(my_set, type(my_set))
# Output: {1, 2, 3} <class 'set'>

my_set = {1, 2, 3}
my_tuple_from_set = tuple(my_set)
print(my_tuple_from_set, type(my_tuple_from_set))
# Output: (1, 2, 3) <class 'tuple'> (Note: set order is not guaranteed)

# Creating a dictionary
my_dict = dict(name="Bob", age=25)
print(my_dict, type(my_dict))
# Output: {'name': 'Bob', 'age': 25} <class 'dict'>
```

## `range()`

Returns a sequence of numbers, starting from 0 by default, increments by 1 by default, and stops before a specified number.

**Syntax:** `range(stop)` or `range(start, stop, step)`

**Example:**

```python
# Sequence from 0 up to (but not including) 5
for i in range(5):
    print(i, end=" ")
# Output: 0 1 2 3 4

print() # New line

# Sequence from 2 up to (but not including) 6
for i in range(2, 6):
    print(i, end=" ")
# Output: 2 3 4 5

print() # New line

# Sequence from 1 up to (but not including) 10, with a step of 2
for i in range(1, 10, 2):
    print(i, end=" ")
# Output: 1 3 5 7 9
```
*Note: `range()` creates a range object, which is efficient for loops. To see the numbers as a list, you can use `list(range(5))`.*

## `sum()`

Sums the items of an iterable (like a list or tuple) from left to right and returns the total.

**Syntax:** `sum(iterable, start=0)`

**Example:**

```python
numbers = [1, 2, 3, 4, 5]
total = sum(numbers)
print(total)
# Output: 15

# You can provide an optional start value
total_with_start = sum(numbers, 10) # 10 + 1 + 2 + 3 + 4 + 5
print(total_with_start)
# Output: 25
```

## `min()`, `max()`

*   `min()`: Returns the smallest item in an iterable or the smallest of two or more arguments.
*   `max()`: Returns the largest item in an iterable or the largest of two or more arguments.

**Syntax:**
`min(iterable, *[, key, default])` or `min(arg1, arg2, *args[, key])`
`max(iterable, *[, key, default])` or `max(arg1, arg2, *args[, key])`

**Example:**

```python
numbers = [3, 1, 4, 1, 5, 9]
print(min(numbers))
# Output: 1

print(max(numbers))
# Output: 9

# Can also compare arguments directly
print(min(10, 5, 20))
# Output: 5

print(max(10, 5, 20))
# Output: 20
```

## `abs()`

Returns the absolute value of a number (the value without regard to its sign).

**Syntax:** `abs(x)`

**Example:**

```python
print(abs(-5))
# Output: 5

print(abs(5))
# Output: 5

print(abs(-3.14))
# Output: 3.14
```

## `pow()`

Returns the value of x to the power of y (x^y). Can also compute (x^y) % z.

**Syntax:** `pow(base, exp, mod=None)`

**Example:**

```python
# 2 to the power of 3
print(pow(2, 3))
# Output: 8

# (2 to the power of 3) modulo 5 (8 % 5)
print(pow(2, 3, 5))
# Output: 3
```

## `round()`

Rounds a number to a specified number of decimal places. If the number of decimals is not specified, it rounds to the nearest integer.

**Syntax:** `round(number, ndigits=None)`

**Example:**

```python
print(round(3.14159))
# Output: 3

print(round(3.7))
# Output: 4

print(round(3.14159, 2)) # Round to 2 decimal places
# Output: 3.14

print(round(3.146, 2))
# Output: 3.15
```
*Note: `round()` behavior for numbers exactly halfway between two options (like 2.5) can sometimes be surprising due to rounding towards the nearest even number in some Python versions/floating-point representations.*

## `sorted()`

Returns a new sorted list from the items in an iterable.

**Syntax:** `sorted(iterable, *, key=None, reverse=False)`

**Example:**

```python
numbers = [3, 1, 4, 1, 5, 9]
sorted_numbers = sorted(numbers)
print(sorted_numbers)
# Output: [1, 1, 3, 4, 5, 9]

# Original list is unchanged
print(numbers)
# Output: [3, 1, 4, 1, 5, 9]

# Sort in descending order
desc_sorted_numbers = sorted(numbers, reverse=True)
print(desc_sorted_numbers)
# Output: [9, 5, 4, 3, 1, 1]

# Sort strings
names = ["Charlie", "Alice", "Bob"]
sorted_names = sorted(names)
print(sorted_names)
# Output: ['Alice', 'Bob', 'Charlie']
```

## `any()`

Returns `True` if at least one item in an iterable is true. If the iterable is empty, returns `False`.

**Syntax:** `any(iterable)`

**Example:**

```python
list1 = [False, False, True]
print(any(list1))
# Output: True

list2 = [0, 0, 0] # 0 is considered False
print(any(list2))
# Output: False

list3 = [0, 1, 0] # 1 is considered True
print(any(list3))
# Output: True

list4 = [] # Empty iterable
print(any(list4))
# Output: False
```

## `all()`

Returns `True` if all items in an iterable are true. If the iterable is empty, returns `True`.

**Syntax:** `all(iterable)`

**Example:**

```python
list1 = [True, True, True]
print(all(list1))
# Output: True

list2 = [True, False, True]
print(all(list2))
# Output: False

list3 = [1, 1, 1] # Non-zero numbers are True
print(all(list3))
# Output: True

list4 = [1, 0, 1] # 0 is False
print(all(list4))
# Output: False

list5 = [] # Empty iterable
print(all(list5))
# Output: True
```

## `help()`

Invokes the built-in help system. If no argument is given, the interactive help system starts. If an argument is given, it prints help information about that object.

**Syntax:** `help(object)`

**Example:**

```python
# Get help on the list type
# help(list)

# Get help on the print function
# help(print)

# Start interactive help (in a Python console)
# help()
```
*(Running `help()` directly in some environments might behave differently than in a standard Python interpreter)*

---

This list covers many of the most common built-in functions. There are more available, and you can find the full list in the official Python documentation. Understanding and using these functions effectively is a key part of writing concise and efficient Python code.