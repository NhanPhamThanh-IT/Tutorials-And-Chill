# Python `for` Loops: A Beginner's Guide

## Introduction

In programming, we often need to repeat a block of code multiple times. A `for` loop is a fundamental control flow statement used for **iteration**. It allows you to execute a block of code repeatedly for each item in a sequence (like a list, tuple, string, or range) or any other iterable object.

## What is Iteration?

Iteration means going through items one by one. Imagine you have a list of tasks; going through each task until you've done them all is like iteration. A `for` loop helps automate this process in your code.

## Basic Syntax

The basic syntax of a `for` loop in Python is:

```python
for variable in iterable:
    # Code block to be executed for each item
    # This block is indented
    statement1
    statement2
    # ...
```

*   `for`: Keyword that starts the loop.
*   `variable`: A temporary variable that takes the value of the current item in the `iterable` during each iteration. You can name this variable almost anything you like (following Python's variable naming rules).
*   `in`: Keyword used to link the `variable` with the `iterable`.
*   `iterable`: An object that can be looped over, such as a list, tuple, string, dictionary, set, or a range object.
*   `:`: A colon that marks the end of the `for` loop statement.
*   **Indented Code Block**: The lines of code indented underneath the `for` line are the body of the loop. They will be executed once for each item in the `iterable`.

## Examples

Let's look at some common ways to use `for` loops.

### 1. Iterating Over a List

You can loop through each item in a list.

```python
fruits = ["apple", "banana", "cherry"]

print("My favorite fruits are:")
for fruit in fruits:
    print(fruit)

# Output:
# My favorite fruits are:
# apple
# banana
# cherry
```

In this example, the `fruit` variable takes the value "apple" in the first iteration, "banana" in the second, and "cherry" in the third. The `print(fruit)` statement is executed for each of these values.

### 2. Iterating Over a String

A string is a sequence of characters, so you can iterate over it.

```python
message = "Hello"

print("Characters in the message:")
for char in message:
    print(char)

# Output:
# Characters in the message:
# H
# e
# l
# l
# o
```

Each character in the string "Hello" is printed on a new line.

### 3. Using the `range()` Function

The `range()` function generates a sequence of numbers, which is often used with `for` loops to repeat an action a specific number of times.

*   `range(stop)`: Generates numbers from 0 up to (but not including) `stop`.
*   `range(start, stop)`: Generates numbers from `start` up to (but not including) `stop`.
*   `range(start, stop, step)`: Generates numbers from `start` up to (but not including) `stop`, incrementing by `step`.

```python
# Example 1: range(stop)
print("Numbers from 0 to 4:")
for i in range(5):
    print(i)
# Output: 0, 1, 2, 3, 4

# Example 2: range(start, stop)
print("\nNumbers from 2 to 5:")
for i in range(2, 6):
    print(i)
# Output: 2, 3, 4, 5

# Example 3: range(start, stop, step)
print("\nEven numbers from 0 to 8:")
for i in range(0, 10, 2):
    print(i)
# Output: 0, 2, 4, 6, 8
```

### 4. Iterating Over a Tuple

Tuples are similar to lists but are immutable (cannot be changed). You can iterate over them just like lists.

```python
colors = ("red", "green", "blue")

print("Colors in the tuple:")
for color in colors:
    print(color)

# Output:
# Colors in the tuple:
# red
# green
# blue
```

### 5. Iterating Over a Dictionary

You can iterate over the keys, values, or key-value pairs of a dictionary.

```python
student_scores = {"Alice": 85, "Bob": 92, "Charlie": 78}

# Iterating over keys (default behavior)
print("\nStudent Names (Keys):")
for name in student_scores:
    print(name)
# Output: Alice, Bob, Charlie

# Iterating over values using .values()
print("\nStudent Scores (Values):")
for score in student_scores.values():
    print(score)
# Output: 85, 92, 78

# Iterating over key-value pairs using .items()
print("\nStudent Names and Scores (Items):")
for name, score in student_scores.items():
    print(f"{name}: {score}")
# Output:
# Alice: 85
# Bob: 92
# Charlie: 78
```

## Loop Control Statements

Sometimes you need more control over how the loop executes.

### 1. `break` Statement

The `break` statement immediately exits the current loop, regardless of whether the loop has finished iterating over all items.

```python
numbers = [1, 2, 3, 4, 5, 6]

print("Searching for the number 4:")
for num in numbers:
    print(f"Checking {num}...")
    if num == 4:
        print("Found 4! Stopping the loop.")
        break # Exit the loop immediately
    print(f"{num} is not 4.")

# Output:
# Searching for the number 4:
# Checking 1...
# 1 is not 4.
# Checking 2...
# 2 is not 4.
# Checking 3...
# 3 is not 4.
# Checking 4...
# Found 4! Stopping the loop.
```

### 2. `continue` Statement

The `continue` statement skips the rest of the code inside the current iteration of the loop and proceeds to the next iteration.

```python
numbers = [1, 2, 3, 4, 5]

print("Printing only odd numbers:")
for num in numbers:
    if num % 2 == 0: # Check if the number is even
        continue     # Skip the rest of this iteration if even
    print(num)       # This line only runs for odd numbers

# Output:
# Printing only odd numbers:
# 1
# 3
# 5
```

### 3. The `else` Clause in a `for` Loop

A `for` loop can have an optional `else` block. The code in the `else` block is executed **only if** the loop completes all its iterations *without* encountering a `break` statement.

```python
my_list = [1, 3, 5]
search_for = 4

print(f"Searching for {search_for} in {my_list}")
for item in my_list:
    if item == search_for:
        print("Found it!")
        break
else:
    # This block runs only if the loop finished normally (no break)
    print(f"{search_for} not found in the list.")

# Output:
# Searching for 4 in [1, 3, 5]
# 4 not found in the list.

my_list_2 = [1, 3, 4, 5]
search_for_2 = 4

print(f"\nSearching for {search_for_2} in {my_list_2}")
for item in my_list_2:
    if item == search_for_2:
        print("Found it!")
        break
else:
    print(f"{search_for_2} not found in the list.")

# Output:
# Searching for 4 in [1, 3, 4, 5]
# Found it!
```

## Nested `for` Loops

You can put one `for` loop inside another. This is called a nested loop. The inner loop will complete all its iterations for each iteration of the outer loop.

```python
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

print("Combinations:")
for adjective in adj:      # Outer loop
    for fruit in fruits:   # Inner loop
        print(adjective, fruit)

# Output:
# Combinations:
# red apple
# red banana
# red cherry
# big apple
# big banana
# big cherry
# tasty apple
# tasty banana
# tasty cherry
```

## Summary

*   `for` loops are used to iterate over items in a sequence or iterable.
*   The basic syntax is `for variable in iterable:`.
*   You can iterate over lists, tuples, strings, dictionaries, and ranges.
*   `break` exits the loop immediately.
*   `continue` skips the current iteration and moves to the next.
*   The `else` block runs if the loop completes without a `break`.
*   Nested loops involve placing one loop inside another.

`for` loops are essential tools in Python for automating repetitive tasks and processing collections of data efficiently. Practice using them with different iterables to become comfortable with their syntax and behavior.