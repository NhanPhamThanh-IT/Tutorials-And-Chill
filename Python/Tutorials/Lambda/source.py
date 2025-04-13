# -*- coding: utf-8 -*-
"""
Topic: Python Lambda Functions (Anonymous Functions)

Lambda functions are small, anonymous functions defined using the `lambda` keyword.
They can take any number of arguments but can only have one expression.
The expression is evaluated and returned when the function is called.

Syntax:
lambda arguments: expression
"""

# 1. Basic Syntax and Simple Examples
# -----------------------------------

# A lambda function that adds 10 to the input argument 'x'
add_ten = lambda x: x + 10
print(f"Using add_ten lambda: 5 + 10 = {add_ten(5)}") # Output: 15

# A lambda function that multiplies two arguments 'a' and 'b'
multiply = lambda a, b: a * b
print(f"Using multiply lambda: 5 * 6 = {multiply(5, 6)}") # Output: 30

# A lambda function that adds three arguments 'x', 'y', and 'z'
add_three = lambda x, y, z: x + y + z
print(f"Using add_three lambda: 5 + 6 + 7 = {add_three(5, 6, 7)}") # Output: 18

# Lambda functions don't need a name (they are anonymous)
# You can call them immediately after definition (though less common)
result = (lambda x: x * 2)(10) # Define and call immediately
print(f"Immediately invoked lambda: 10 * 2 = {result}") # Output: 20

# 2. Why Use Lambda Functions?
# ----------------------------
# The primary use case for lambda functions is when you need a simple,
# short-lived function for a short period, often as an argument to
# higher-order functions (functions that take other functions as arguments).

# 3. Use with Higher-Order Functions
# ----------------------------------

# a) `map()` function: Applies a function to all items in an iterable (like a list).
#    Syntax: map(function, iterable)

numbers = [1, 2, 3, 4, 5]

# Using map with a regular function
def square(n):
    return n * n
squared_numbers_def = list(map(square, numbers))
print(f"Squared numbers (using def): {squared_numbers_def}") # Output: [1, 4, 9, 16, 25]

# Using map with a lambda function (more concise)
squared_numbers_lambda = list(map(lambda x: x * x, numbers))
print(f"Squared numbers (using lambda): {squared_numbers_lambda}") # Output: [1, 4, 9, 16, 25]

# Example: Convert list of strings to uppercase
words = ["hello", "world", "lambda"]
upper_words = list(map(lambda s: s.upper(), words))
print(f"Uppercase words: {upper_words}") # Output: ['HELLO', 'WORLD', 'LAMBDA']


# b) `filter()` function: Creates an iterator from elements of an iterable
#    for which a function returns true.
#    Syntax: filter(function, iterable)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Using filter with a regular function
def is_even(n):
    return n % 2 == 0
even_numbers_def = list(filter(is_even, numbers))
print(f"Even numbers (using def): {even_numbers_def}") # Output: [2, 4, 6, 8, 10]

# Using filter with a lambda function (more concise)
even_numbers_lambda = list(filter(lambda x: x % 2 == 0, numbers))
print(f"Even numbers (using lambda): {even_numbers_lambda}") # Output: [2, 4, 6, 8, 10]

# Example: Filter out short words
words = ["apple", "banana", "kiwi", "grape", "fig"]
long_words = list(filter(lambda w: len(w) > 4, words))
print(f"Long words (length > 4): {long_words}") # Output: ['apple', 'banana', 'grape']


# c) `sorted()` function: Returns a new sorted list from the items in an iterable.
#    It has an optional `key` argument to specify a function to be called on each
#    list element prior to making comparisons.
#    Syntax: sorted(iterable, key=function, reverse=False)

points = [(1, 5), (3, 2), (8, 1), (4, 9)]

# Sort points based on the first element (x-coordinate) - default behavior
sorted_by_x = sorted(points)
print(f"Points sorted by x-coordinate (default): {sorted_by_x}")
# Output: [(1, 5), (3, 2), (4, 9), (8, 1)]

# Sort points based on the second element (y-coordinate) using lambda
sorted_by_y = sorted(points, key=lambda p: p[1])
print(f"Points sorted by y-coordinate (using lambda): {sorted_by_y}")
# Output: [(8, 1), (3, 2), (1, 5), (4, 9)]

# Sort points based on the sum of coordinates using lambda
sorted_by_sum = sorted(points, key=lambda p: p[0] + p[1])
print(f"Points sorted by sum of coordinates (using lambda): {sorted_by_sum}")
# Output: [(3, 2), (1, 5), (8, 1), (4, 9)] # 5, 6, 9, 13

# Sort list of dictionaries by age
people = [
        {'name': 'Alice', 'age': 30},
        {'name': 'Bob', 'age': 25},
        {'name': 'Charlie', 'age': 35}
]
sorted_people = sorted(people, key=lambda person: person['age'])
print(f"People sorted by age: {sorted_people}")
# Output: [{'name': 'Bob', 'age': 25}, {'name': 'Alice', 'age': 30}, {'name': 'Charlie', 'age': 35}]


# 4. Lambda Functions with Conditional Logic
# ------------------------------------------
# Lambda functions can use conditional expressions (ternary operator).
# Syntax: value_if_true if condition else value_if_false

# Example: Return 'even' or 'odd' based on input number
check_even_odd = lambda x: "even" if x % 2 == 0 else "odd"
print(f"Check 4: {check_even_odd(4)}")   # Output: even
print(f"Check 7: {check_even_odd(7)}")   # Output: odd

# Example: Find the maximum of two numbers
find_max = lambda a, b: a if a > b else b
print(f"Max of 10, 20: {find_max(10, 20)}") # Output: 20


# 5. Lambda in Data Structures
# ----------------------------
# You can store lambda functions in data structures like lists or dictionaries.

# List of operations
operations = [
        lambda x: x + 1, # Increment
        lambda x: x * 2, # Double
        lambda x: x ** 2 # Square
]

number = 5
results = [op(number) for op in operations]
print(f"Applying operations [inc, double, square] to {number}: {results}")
# Output: [6, 10, 25]

# Dictionary mapping operation names to lambda functions
math_ops = {
        'add': lambda x, y: x + y,
        'subtract': lambda x, y: x - y,
        'multiply': lambda x, y: x * y
}

a, b = 10, 7
print(f"Using math_ops dictionary:")
print(f"  Add: {math_ops['add'](a, b)}")       # Output: 17
print(f"  Subtract: {math_ops['subtract'](a, b)}") # Output: 3
print(f"  Multiply: {math_ops['multiply'](a, b)}") # Output: 70


# 6. Comparison with `def` Functions
# ----------------------------------

# `def` function:
# - Can have multiple expressions/statements.
# - Has a name (unless nested inside another function).
# - Can have docstrings.
# - More suitable for complex logic.

def add_def(x, y):
    """This function adds two numbers."""
    result = x + y
    # You could add more complex logic here
    print(f"Adding {x} and {y} using def")
    return result

# `lambda` function:
# - Restricted to a single expression.
# - Is anonymous (though often assigned to a variable).
# - Cannot have docstrings in the same way.
# - Best for simple, inline functions.

add_lambda = lambda x, y: x + y # No easy way to add docstring or multiple steps

print(f"Result from add_def: {add_def(3, 4)}")
print(f"Result from add_lambda: {add_lambda(3, 4)}")


# 7. Limitations of Lambda Functions
# ----------------------------------
# - Can only contain a single expression, not statements (like `if`/`else` blocks,
#   `for`/`while` loops, `print` statements directly inside, `return` statement).
#   The expression's result is implicitly returned.
# - Cannot have type annotations directly within the lambda definition in the
#   same way as `def` (though the variable it's assigned to can be annotated).
# - Can sometimes make code harder to read if the expression becomes too complex.
#   In such cases, a regular `def` function is preferred for clarity.

# Example of what you CANNOT do directly in a lambda:
# my_lambda = lambda x:
#     if x > 10:  # SyntaxError: invalid syntax
#         return "Big"
#     else:
#         return "Small"

# my_lambda = lambda x: print(x) # This works, but the lambda returns None,
                                                                # as print() returns None. Usually not the intent.

# Summary:
# Lambda functions provide a concise way to create small, anonymous functions.
# They are particularly useful with higher-order functions like map(), filter(),
# and sorted(), where you need a simple function for a specific, localized task.
# For more complex logic or when readability is paramount, standard `def`
# functions are generally the better choice.