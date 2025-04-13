import math
from random import randint, choice
import asyncio

# Python Keywords Explained with Examples

# This file demonstrates the usage of various Python keywords.
# Keywords are reserved words in Python that have special meanings and purposes.
# You cannot use keywords as variable names, function names, or any other identifiers.

# --------------------
# Boolean Values: True, False
# --------------------
# Represent boolean truth values.
print("--- True and False ---")
is_active = True
is_greater = False
print(f"is_active is: {is_active}")
print(f"is_greater is: {is_greater}")
print(f"Type of True: {type(True)}")

# --------------------
# Null Value: None
# --------------------
# Represents the absence of a value or a null value.
print("\n--- None ---")
no_value = None
print(f"no_value is: {no_value}")
print(f"Type of None: {type(None)}")
if no_value is None:
    print("no_value holds None")

# --------------------
# Logical Operators: and, or, not
# --------------------
# Used to combine conditional statements.
print("\n--- and, or, not ---")
a = True
b = False

# and: Returns True if both statements are true
print(f"a and b: {a and b}")  # False
print(f"a and True: {a and True}") # True

# or: Returns True if one of the statements is true
print(f"a or b: {a or b}")    # True
print(f"b or False: {b or False}") # False

# not: Reverses the result, returns False if the result is true, and vice versa
print(f"not a: {not a}")      # False
print(f"not b: {not b}")      # True

# --------------------
# Conditional Statements: if, elif, else
# --------------------
# Used for decision making.
print("\n--- if, elif, else ---")
x = 10
y = 20

if x > y:
    print("x is greater than y")
elif x < y: # 'elif' is short for 'else if'
    print("x is less than y")
else:
    print("x is equal to y")

# --------------------
# Loops: for, while
# --------------------
# Used for iterating over a sequence or executing a block as long as a condition is true.

# for: Iterates over a sequence (like list, tuple, dictionary, set, or string).
print("\n--- for ---")
fruits = ["apple", "banana", "cherry"]
print("Fruits:")
for fruit in fruits:
    print(f"- {fruit}")

# while: Executes a set of statements as long as a condition is true.
print("\n--- while ---")
count = 0
print("Counting up to 3:")
while count < 3:
    print(f"Count is: {count}")
    count += 1 # Increment count

# --------------------
# Loop Control: break, continue
# --------------------
# Used to alter the flow of a loop.

# break: Stops the loop even if the while condition is true or the for loop has items left.
print("\n--- break ---")
print("Finding 'banana' and breaking:")
for fruit in fruits:
    print(f"Checking {fruit}")
    if fruit == "banana":
        print("Found banana, stopping loop.")
        break # Exit the loop immediately

# continue: Skips the current iteration and moves to the next one.
print("\n--- continue ---")
print("Skipping 'banana':")
for fruit in fruits:
    if fruit == "banana":
        print("Skipping banana.")
        continue # Skip the rest of the code in this iteration
    print(f"Processing {fruit}")

# --------------------
# Function Definition: def, return
# --------------------
# def: Used to define a function.
# return: Used to exit a function and optionally pass back a value.
print("\n--- def, return ---")

def greet(name):
    """This function greets the person passed in as a parameter."""
    message = f"Hello, {name}!"
    return message # Return the greeting message

greeting = greet("Alice")
print(greeting)

def add_numbers(num1, num2):
    """This function returns the sum of two numbers."""
    return num1 + num2

sum_result = add_numbers(5, 3)
print(f"Sum of 5 and 3 is: {sum_result}")

def print_greeting(name):
    """This function prints a greeting but doesn't return a value explicitly."""
    print(f"Hi there, {name}!")
    # If no return statement is used, the function implicitly returns None

result_from_print = print_greeting("Bob")
print(f"Result from print_greeting: {result_from_print}") # Will print None

# --------------------
# Class Definition: class
# --------------------
# Used to define a class (blueprint for creating objects).
print("\n--- class ---")

class Dog:
    """A simple class representing a dog."""
    def __init__(self, name, breed): # Constructor method
        self.name = name
        self.breed = breed

    def bark(self):
        return f"{self.name} says Woof!"

# Create an object (instance) of the Dog class
my_dog = Dog("Buddy", "Golden Retriever")
print(f"My dog's name is {my_dog.name}")
print(f"My dog's breed is {my_dog.breed}")
print(my_dog.bark())

# --------------------
# Exception Handling: try, except, finally, raise
# --------------------
# Used to handle errors gracefully.
print("\n--- try, except, finally, raise ---")

# try: Lets you test a block of code for errors.
# except: Lets you handle the error.
# finally: Lets you execute code, regardless of the result of the try- and except blocks.
# raise: Allows you to force a specified exception to occur.

def divide(x, y):
    try:
        if y == 0:
            # raise: Manually trigger an exception
            raise ZeroDivisionError("Cannot divide by zero!")
        result = x / y
        print(f"{x} / {y} = {result}")
    except ZeroDivisionError as e: # Catch specific error
        print(f"Error caught: {e}")
    except TypeError as e: # Catch another type of error
        print(f"Type error caught: {e}")
    except Exception as e: # Catch any other exceptions (use sparingly)
        print(f"An unexpected error occurred: {e}")
    else:
        # Optional 'else' block: Executes if no exceptions were raised in the 'try' block
        print("Division successful (within else block).")
    finally:
        # finally: Always executes, whether an exception occurred or not.
        # Useful for cleanup actions (e.g., closing files).
        print("Executing finally block.")

divide(10, 2)
print("-" * 10)
divide(10, 0)
print("-" * 10)
divide(10, "a") # This will cause a TypeError
print("-" * 10)
divide(5, 1) # This will execute the 'else' block

# --------------------
# Context Management: with, as
# --------------------
# with: Used to wrap the execution of a block with methods defined by a context manager.
#       Often used for resource management (like files), ensuring resources are set up and torn down properly.
# as: Used to assign the object created by the context manager to a variable.
print("\n--- with, as ---")

try:
    # Open a file for writing using 'with'. The file is automatically closed afterwards.
    with open("example.txt", "w") as file: # 'as file' assigns the file object to the variable 'file'
        file.write("This is written using the 'with' statement.\n")
        file.write("It ensures the file is closed automatically.")
    print("File 'example.txt' written successfully and closed.")

    # Open the file for reading
    with open("example.txt", "r") as file:
        content = file.read()
        print("\nContent of 'example.txt':")
        print(content)
except IOError as e:
    print(f"An error occurred with file operation: {e}")

# --------------------
# Modules: import, from, as
# --------------------
# Used to bring code from other modules into your current script.

# import: Imports an entire module.
print("\n--- import ---")
print(f"Value of pi using 'math' module: {math.pi}")
print(f"Square root of 16: {math.sqrt(16)}")

# from: Imports specific parts (functions, classes, variables) from a module.
print("\n--- from ---")
random_number = randint(1, 10) # Use randint directly
random_choice = choice(["apple", "banana", "cherry"])
print(f"Random integer between 1 and 10: {random_number}")
print(f"Random choice from list: {random_choice}")

# as: Used to give an alias (alternative name) to an imported module or part of a module.
print("\n--- as ---")
import numpy as np # Common alias for the numpy library
array_example = np.array([1, 2, 3])
print(f"Numpy array created using alias 'np': {array_example}")

from math import factorial as fact # Give an alias to a specific function
print(f"Factorial of 5 (using alias 'fact'): {fact(5)}")

# --------------------
# Membership Testing: in
# --------------------
# Checks if a value exists within a sequence (list, tuple, string, set, dictionary keys).
print("\n--- in ---")
my_list = [1, 2, 3, 4, 5]
my_string = "hello world"
my_dict = {"a": 1, "b": 2}

print(f"Is 3 in my_list? {3 in my_list}")       # True
print(f"Is 6 in my_list? {6 in my_list}")       # False
print(f"Is 'hello' in my_string? {'hello' in my_string}") # True
print(f"Is 'z' in my_string? {'z' in my_string}")     # False
print(f"Is 'a' in my_dict (checks keys)? {'a' in my_dict}") # True
print(f"Is 1 in my_dict (checks keys)? {1 in my_dict}")   # False (checks keys by default)
print(f"Is 1 in my_dict.values()? {1 in my_dict.values()}") # True (checking values explicitly)

# Can also be used with 'not'
print(f"Is 6 not in my_list? {6 not in my_list}") # True

# --------------------
# Identity Testing: is
# --------------------
# Checks if two variables refer to the exact same object in memory (not just if they have the same value).
print("\n--- is ---")
list1 = [1, 2, 3]
list2 = [1, 2, 3]
list3 = list1 # list3 now refers to the same object as list1

print(f"list1 == list2: {list1 == list2}") # True (values are the same)
print(f"list1 is list2: {list1 is list2}") # False (they are different objects in memory)

print(f"list1 == list3: {list1 == list3}") # True (values are the same)
print(f"list1 is list3: {list1 is list3}") # True (they refer to the same object)

# Often used to check against None
x = None
print(f"x is None: {x is None}") # True (preferred way to check for None)
print(f"x is not None: {x is not None}") # False

# Small integers and strings might be cached by Python, leading to 'is' returning True
a = 5
b = 5
print(f"a is b (for small integers): {a is b}") # Often True due to caching

s1 = "hello"
s2 = "hello"
print(f"s1 is s2 (for identical strings): {s1 is s2}") # Often True due to interning

# --------------------
# Deleting Variables/Objects: del
# --------------------
# Used to delete objects, variables, or items from lists, dictionaries, etc.
print("\n--- del ---")
my_var = 100
print(f"my_var before del: {my_var}")
del my_var
# print(my_var) # This would now cause a NameError because my_var is deleted

my_list_to_del = [10, 20, 30, 40]
print(f"my_list_to_del before del: {my_list_to_del}")
del my_list_to_del[1] # Delete the item at index 1 (value 20)
print(f"my_list_to_del after deleting index 1: {my_list_to_del}")

my_dict_to_del = {"a": 1, "b": 2, "c": 3}
print(f"my_dict_to_del before del: {my_dict_to_del}")
del my_dict_to_del["b"] # Delete the key 'b' and its value
print(f"my_dict_to_del after deleting key 'b': {my_dict_to_del}")

# --------------------
# Placeholder: pass
# --------------------
# Is a null operation; nothing happens when it executes.
# Used as a placeholder where syntax requires a statement, but no code needs to be executed.
print("\n--- pass ---")

def my_empty_function():
    pass # Avoids an error for an empty function body

class MyEmptyClass:
    pass # Avoids an error for an empty class body

if x > 0: # Assuming x was defined earlier
    pass # Placeholder if no action is needed yet
else:
    print("x is not positive")

my_empty_function() # Calling the function does nothing
my_obj = MyEmptyClass() # Creating an instance works fine
print("Used 'pass' in function and class definitions.")

# --------------------
# Assertions: assert
# --------------------
# Used for debugging. Checks if a condition is true. If not, it raises an AssertionError.
# Assertions can be disabled globally in the Python interpreter.
print("\n--- assert ---")

def calculate_discount(price, discount_percent):
    assert 0 <= discount_percent <= 100, "Discount percentage must be between 0 and 100"
    assert price >= 0, "Price cannot be negative"
    discount_amount = price * (discount_percent / 100)
    return price - discount_amount

final_price = calculate_discount(100, 10) # Should work
print(f"Final price (10% off 100): {final_price}")

try:
    # This will raise an AssertionError because the discount is invalid
    calculate_discount(50, 150)
except AssertionError as e:
    print(f"AssertionError caught: {e}")

try:
    # This will raise an AssertionError because the price is invalid
    calculate_discount(-20, 10)
except AssertionError as e:
    print(f"AssertionError caught: {e}")

# --------------------
# Anonymous Functions: lambda
# --------------------
# Used to create small, anonymous functions (functions without a name).
# Syntax: lambda arguments: expression
print("\n--- lambda ---")

# A regular function
def multiply(x, y):
    return x * y

# Equivalent lambda function
multiply_lambda = lambda x, y: x * y

print(f"Using regular function: multiply(5, 4) = {multiply(5, 4)}")
print(f"Using lambda function: multiply_lambda(5, 4) = {multiply_lambda(5, 4)}")

# Lambdas are often used with functions like map(), filter(), sorted()
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x * x, numbers))
print(f"Squared numbers using lambda and map: {squared_numbers}")

even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(f"Even numbers using lambda and filter: {even_numbers}")

points = [(1, 5), (3, 2), (8, 9), (4, 1)]
# Sort points based on the second element (y-coordinate) using lambda
points_sorted_by_y = sorted(points, key=lambda point: point[1])
print(f"Points sorted by y-coordinate using lambda: {points_sorted_by_y}")

# --------------------
# Generators: yield
# --------------------
# Used in functions like 'return', but the function returns a generator object.
# Generators produce a sequence of values over time, saving memory for large sequences.
# Each time 'yield' is encountered, the function's state is saved, and the value is returned.
# Execution resumes from the same point the next time the generator's next() method is called.
print("\n--- yield ---")

def count_up_to(n):
    """A generator function that yields numbers from 1 up to n."""
    i = 1
    while i <= n:
        yield i # Yield the current value of i
        i += 1  # Increment i for the next iteration

# Create a generator object
counter_gen = count_up_to(5)

print(f"Type of counter_gen: {type(counter_gen)}")

# Iterate through the generator to get the yielded values
print("Values yielded by count_up_to(5):")
for number in counter_gen:
    print(number)

# Another example: Infinite sequence generator (use carefully!)
def infinite_sequence():
    num = 0
    while True:
        yield num
        num += 1

# gen_inf = infinite_sequence()
# print(next(gen_inf)) # 0
# print(next(gen_inf)) # 1
# ... this would go on forever if iterated without a break condition

# --------------------
# Scope Modifiers: global, nonlocal
# --------------------
# Used to modify the scope of variables.

# global: Declares that a variable inside a function is global (belongs to the global scope).
print("\n--- global ---")
global_var = "I am global"

def modify_global():
    # Without 'global' keyword, this would create a new local variable
    global global_var
    global_var = "Modified global variable"
    print(f"Inside function: {global_var}")

print(f"Before function call: {global_var}")
modify_global()
print(f"After function call: {global_var}")

# nonlocal: Declares that a variable inside a nested function refers to a variable
#           in the nearest enclosing scope (that is not global).
print("\n--- nonlocal ---")

def outer_function():
    outer_var = "I am outer"

    def inner_function():
        # Without 'nonlocal', this would create a new local variable 'outer_var'
        nonlocal outer_var
        outer_var = "Modified outer variable by inner function"
        print(f"Inside inner_function: {outer_var}")

    print(f"Before inner_function call: {outer_var}")
    inner_function()
    print(f"After inner_function call: {outer_var}")

outer_function()
# print(outer_var) # This would cause a NameError, outer_var is not global

# --------------------
# Asynchronous Programming: async, await
# --------------------
# Used for writing asynchronous code (coroutines), allowing programs to perform
# other tasks while waiting for operations like I/O to complete.
# Requires the 'asyncio' library or similar frameworks.

# async def: Defines an asynchronous function (coroutine).
# await: Pauses the execution of the current coroutine, waiting for an awaitable
#        object (like another coroutine or a Future) to complete.

# Note: Running async code typically requires an event loop (e.g., asyncio.run()).
# These examples illustrate the syntax but won't run independently without an event loop setup.

print("\n--- async, await (Conceptual Example) ---")

async def fetch_data(url):
    """Simulates fetching data asynchronously."""
    print(f"Starting to fetch data from {url}...")
    # In a real scenario, this would be an actual network request
    await asyncio.sleep(1) # Simulate I/O delay
    print(f"Finished fetching data from {url}.")
    return {"data": f"Some data from {url}"}

async def main_async_task():
    """Main coroutine to run other async tasks."""
    print("Starting main async task.")
    task1 = asyncio.create_task(fetch_data("http://example.com"))
    task2 = asyncio.create_task(fetch_data("http://anotherexample.org"))

    # await: Wait for the tasks to complete
    result1 = await task1
    result2 = await task2

    print(f"Result 1: {result1}")
    print(f"Result 2: {result2}")
    print("Finished main async task.")

# To run this async code:
# asyncio.run(main_async_task())
# We'll just print a message here as running requires top-level setup.
print("Defined async functions. Use asyncio.run() to execute them.")

print("\n--- All Python Keywords Demonstrated ---")