# Topic: Try Except in Python - Detailed Examples for Beginners

# --- 1. Basic Try-Except Block ---
# The `try` block lets you test a block of code for errors.
# The `except` block lets you handle the error if one occurs.

print("--- 1. Basic Try-Except ---")
try:
    # This code might cause an error (division by zero)
    numerator = 10
    denominator = 0
    result = numerator / denominator
    print(f"The result is: {result}") # This line won't be reached if an error occurs
except ZeroDivisionError:
    # This block executes ONLY if a ZeroDivisionError occurs in the try block
    print("Error: Cannot divide by zero!")
print("Execution continues after the first try-except block.\n")

# --- 2. Handling Specific Exceptions ---
# It's good practice to catch specific exceptions you anticipate.
# This prevents catching unexpected errors unintentionally.

print("--- 2. Handling Specific Exceptions ---")
try:
    # Let's try accessing a list element that doesn't exist
    my_list = [1, 2, 3]
    print(my_list[5]) # This will raise an IndexError
except IndexError:
    # This block handles only IndexError
    print("Error: Index out of bounds!")
except ZeroDivisionError:
    # This block handles only ZeroDivisionError (won't be triggered here)
    print("Error: Cannot divide by zero!")
print("Execution continues...\n")

# --- 3. Handling Multiple Exceptions in One Block ---
# You can handle multiple specific exceptions with a single `except` block
# by putting them in a tuple.

print("--- 3. Handling Multiple Exceptions ---")
try:
    value = int("abc") # This will raise a ValueError
    # result = 10 / 0   # Uncomment this to test ZeroDivisionError
except (ValueError, TypeError, ZeroDivisionError):
    # This block handles ValueError OR TypeError OR ZeroDivisionError
    print("Error: A ValueError, TypeError, or ZeroDivisionError occurred!")
print("Execution continues...\n")

# --- 4. Catching Any Exception (Generic Exception) ---
# You can catch *any* exception using `except Exception`.
# Use this sparingly, as it can hide bugs. It's usually better
# to catch specific exceptions you expect.

print("--- 4. Catching Any Exception ---")
try:
    # Let's cause a TypeError
    result = "hello" + 5
except Exception as e: # 'e' is a variable holding the exception object
    # This catches *any* exception that inherits from the base Exception class
    print(f"An unexpected error occurred: {e}")
    print(f"Type of error: {type(e)}")
print("Execution continues...\n")

# --- 5. The `else` Block ---
# The `else` block executes only if the `try` block completes
# successfully *without* raising any exceptions.

print("--- 5. The `else` Block ---")
try:
    numerator = 10
    denominator = 2 # No error here
    result = numerator / denominator
except ZeroDivisionError:
    print("Error: Cannot divide by zero!")
else:
    # This code runs ONLY if the try block had NO exceptions
    print(f"Division successful! Result: {result}")
print("Execution continues...\n")

# --- 6. The `finally` Block ---
# The `finally` block *always* executes, regardless of whether an
# exception occurred in the `try` block or not. It's often used for
# cleanup actions (like closing files or network connections).

print("--- 6. The `finally` Block ---")
try:
    print("Trying to open a file (simulation)...")
    # file = open("non_existent_file.txt", "r") # This would cause FileNotFoundError
    # result = 10 / 0 # This would cause ZeroDivisionError
    result = 10 / 2 # This works
    print("Operation inside try block successful.")
except FileNotFoundError:
    print("Error: File not found!")
except ZeroDivisionError:
    print("Error: Cannot divide by zero!")
else:
    print("Else block: No exceptions occurred in the try block.")
finally:
    # This code ALWAYS runs
    print("Finally block: This always executes, used for cleanup.")
print("Execution continues after the finally example.\n")

# --- 7. Accessing the Exception Object ---
# You can get information about the exception using `as variable_name`.

print("--- 7. Accessing the Exception Object ---")
try:
    x = int("not_a_number")
except ValueError as ve: # 've' now holds the ValueError object
    print(f"Caught a ValueError!")
    print(f"  Error details: {ve}")
    print(f"  Error type: {type(ve)}")
    print(f"  Error arguments: {ve.args}")
print("Execution continues...\n")

# --- 8. Raising Exceptions ---
# You can intentionally raise an exception using the `raise` keyword.
# This is useful when a certain condition is met that makes further
# execution impossible or incorrect.

print("--- 8. Raising Exceptions ---")
def check_age(age):
    if age < 0:
        # Raise a ValueError with a custom message
        raise ValueError("Age cannot be negative.")
    elif age < 18:
        print("User is a minor.")
    else:
        print("User is an adult.")

try:
    check_age(25)
    check_age(-5) # This will trigger the raise statement
    check_age(10) # This line won't be reached
except ValueError as e:
    print(f"Error checking age: {e}")
print("Execution continues...\n")

# --- 9. Custom Exceptions ---
# You can define your own exception types by creating a new class
# that inherits from the base `Exception` class (or a more specific one).

print("--- 9. Custom Exceptions ---")

# Define a custom exception class
class MyCustomError(Exception):
    """A custom exception for a specific scenario."""
    def __init__(self, message="A custom error occurred"):
        self.message = message
        super().__init__(self.message)

def process_data(data):
    if data is None:
        raise MyCustomError("Input data cannot be None.")
    elif not isinstance(data, str):
        raise TypeError("Input data must be a string.")
    else:
        print(f"Processing data: {data}")

try:
    process_data("Sample Data")
    # process_data(123) # Uncomment to test TypeError
    process_data(None) # This will raise MyCustomError
except MyCustomError as mce:
    print(f"Caught custom error: {mce}")
except TypeError as te:
    print(f"Caught type error: {te}")
except Exception as e:
    print(f"Caught some other error: {e}")
finally:
    print("Data processing attempt finished.")

print("\nEnd of Try-Except examples.")