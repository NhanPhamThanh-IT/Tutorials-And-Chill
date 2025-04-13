import non_existent_module
import time

# Python Built-in Exceptions Examples

# Exceptions are errors detected during execution.
# When an error occurs, Python raises an exception.
# If not handled, the program terminates.
# We use try...except blocks to handle exceptions gracefully.

print("--- Demonstrating Built-in Exceptions ---")

# 1. SyntaxError
# This error occurs when the Python parser encounters incorrect syntax.
# It cannot be caught by a standard try...except block because it happens
# before the code starts running.
# Example (commented out because it would stop the script):
# print "Hello, World!"  # Missing parentheses in Python 3

print("\n1. SyntaxError: Cannot be caught easily in script.")
print("   Example: Missing parentheses -> print 'hello'")
print("   Another Example: IndentationError (subclass of SyntaxError)")
# def my_func():
# print("Indented incorrectly") # IndentationError

# 2. NameError
# Raised when a variable or function name is not found in the current scope.
print("\n2. NameError Example:")
try:
    print(undefined_variable)
except NameError as e:
    print(f"   Caught NameError: {e}")
    print("   Reason: Tried to use a variable that hasn't been assigned a value.")

# 3. TypeError
# Raised when an operation or function is applied to an object of an inappropriate type.
print("\n3. TypeError Example:")
try:
    result = "hello" + 5
except TypeError as e:
    print(f"   Caught TypeError: {e}")
    print("   Reason: Tried to concatenate a string and an integer.")

# 4. ValueError
# Raised when a function receives an argument of the correct type but an inappropriate value.
print("\n4. ValueError Example:")
try:
    number = int("not_a_number")
except ValueError as e:
    print(f"   Caught ValueError: {e}")
    print("   Reason: Tried to convert a string that doesn't represent an integer.")

# 5. IndexError
# Raised when trying to access an index that is outside the bounds of a sequence (list, tuple, etc.).
print("\n5. IndexError Example:")
my_list = [1, 2, 3]
try:
    print(my_list[5])
except IndexError as e:
    print(f"   Caught IndexError: {e}")
    print(f"   Reason: Tried to access index 5 in a list of size {len(my_list)}.")

# 6. KeyError
# Raised when trying to access a key that doesn't exist in a dictionary.
print("\n6. KeyError Example:")
my_dict = {"a": 1, "b": 2}
try:
    print(my_dict["c"])
except KeyError as e:
    print(f"   Caught KeyError: {e}")
    print(f"   Reason: Tried to access the key 'c' which is not in the dictionary {my_dict.keys()}.")

# 7. ZeroDivisionError
# Raised when the second operand of a division or modulo operation is zero.
# It's a subclass of ArithmeticError.
print("\n7. ZeroDivisionError Example:")
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print(f"   Caught ZeroDivisionError: {e}")
    print("   Reason: Tried to divide a number by zero.")

# 8. FileNotFoundError
# Raised when trying to open a file that does not exist.
# It's a subclass of OSError.
print("\n8. FileNotFoundError Example:")
try:
    with open("non_existent_file.txt", "r") as f:
        content = f.read()
except FileNotFoundError as e:
    print(f"   Caught FileNotFoundError: {e}")
    print("   Reason: Tried to open a file that does not exist in the specified path.")

# 9. AttributeError
# Raised when an attribute reference or assignment fails.
print("\n9. AttributeError Example:")
my_string = "hello"
try:
    my_string.append(" world") # Strings don't have an 'append' method (lists do)
except AttributeError as e:
    print(f"   Caught AttributeError: {e}")
    print("   Reason: Tried to call the 'append' method on a string object, which doesn't have it.")

# 10. ImportError / ModuleNotFoundError
# Raised when the import statement fails to find the module definition.
# ModuleNotFoundError is a subclass of ImportError (introduced in Python 3.6).
print("\n10. ImportError / ModuleNotFoundError Example:")
try:
except ModuleNotFoundError as e: # More specific than ImportError
    print(f"   Caught ModuleNotFoundError: {e}")
    print("   Reason: Tried to import a module that Python cannot find.")
except ImportError as e: # Catches older ImportErrors too
    print(f"   Caught ImportError: {e}")
    print("   Reason: Tried to import a module that Python cannot find.")


# 11. AssertionError
# Raised when an assert statement fails.
print("\n11. AssertionError Example:")
x = 5
y = 10
try:
    assert x > y, "x should be greater than y, but it's not."
except AssertionError as e:
    print(f"   Caught AssertionError: {e}")
    print("   Reason: The condition in the assert statement evaluated to False.")

# 12. RecursionError
# Raised when the interpreter detects that the maximum recursion depth is exceeded.
# This usually happens with functions that call themselves indefinitely.
print("\n12. RecursionError Example:")
def recursive_function(count=0):
    # To prevent actual infinite recursion, we add a base case for the demo
    if count > 10: # Set a low limit for demonstration
        print("   Reached demo limit, stopping recursion.")
        return
    # print(f"   Recursive call {count}") # Uncomment to see calls
    try:
        # This inner try/except is just to catch the error for the demo
        # In real code, you'd fix the recursion logic
        if count > 995: # Python's default limit is often around 1000
             # Simulate reaching the limit slightly early for safety
             raise RecursionError("maximum recursion depth exceeded (simulated for demo)")
        recursive_function(count + 1)
    except RecursionError as e:
        print(f"   Caught RecursionError: {e}")
        print("   Reason: The function called itself too many times, exceeding the recursion depth limit.")

# Call the function carefully
try:
    recursive_function()
except RecursionError as e:
     # This outer catch might be needed if the inner one fails or limit is hit differently
    print(f"   Caught RecursionError (outer): {e}")


# 13. KeyboardInterrupt
# Raised when the user hits the interrupt key (normally Control-C or Delete).
print("\n13. KeyboardInterrupt Example:")
print("   Try pressing Ctrl+C while the script is waiting...")
try:
    # Simulate a long-running process
    time.sleep(5) # Wait for 5 seconds
    print("   Wait finished without interruption.")
except KeyboardInterrupt:
    print("\n   Caught KeyboardInterrupt!")
    print("   Reason: User pressed Ctrl+C to interrupt the program.")

# 14. StopIteration
# Raised by built-in function next() and an iterator's __next__() method
# to signal that there are no further items produced by the iterator.
print("\n14. StopIteration Example:")
my_iter = iter([1, 2])
try:
    print(f"   Next item: {next(my_iter)}")
    print(f"   Next item: {next(my_iter)}")
    print(f"   Next item: {next(my_iter)}") # This will raise StopIteration
except StopIteration:
    print(f"   Caught StopIteration")
    print("   Reason: Called next() on an iterator that has no more items.")

# 15. UnboundLocalError
# Raised when a local variable is referenced before it has been assigned a value.
# It's a subclass of NameError.
print("\n15. UnboundLocalError Example:")
def unbound_error_func():
    try:
        # print(local_var) # This would be NameError if local_var wasn't assigned later
        if False: # This condition ensures the assignment is skipped
            local_var = 1
        print(local_var) # Referenced before potential assignment if condition is False
    except UnboundLocalError as e:
        print(f"   Caught UnboundLocalError: {e}")
        print("   Reason: A local variable was used before it was assigned a value within the function's scope.")

unbound_error_func()


# General Exception Handling
# You can catch multiple exceptions or use a base class like Exception.
print("\n--- General Exception Handling ---")
try:
    # Choose one line to test different errors:
    # result = 10 / 0             # ZeroDivisionError
    # my_list = []
    # print(my_list[0])           # IndexError
    number = int("abc")         # ValueError
except (ZeroDivisionError, IndexError) as e:
    print(f"   Caught specific error (ZeroDivision or Index): {type(e).__name__} - {e}")
except ValueError as e:
     print(f"   Caught ValueError: {e}")
except Exception as e: # Catch any other exception that inherits from Exception
    print(f"   Caught a general exception: {type(e).__name__} - {e}")
finally:
    # The finally block always executes, whether an exception occurred or not.
    # Useful for cleanup actions (e.g., closing files).
    print("   This 'finally' block always runs.")


print("\n--- End of Demonstrations ---")