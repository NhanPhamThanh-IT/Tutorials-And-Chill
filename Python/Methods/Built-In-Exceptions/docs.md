# Built-in Exceptions in Python

## Introduction to Exceptions

In Python, an **exception** is an error that occurs during the execution of a program. When an error happens, Python generates an exception object. If this exception object is not handled, the program stops executing and prints a traceback message, indicating where the error occurred and what type of error it was.

Handling exceptions allows your program to manage errors gracefully, perhaps by logging the error, prompting the user for different input, or trying an alternative approach, instead of just crashing.

## What are Built-in Exceptions?

Python comes with a number of **built-in exceptions**. These are predefined error types that Python raises automatically when specific error conditions are met during runtime. You don't need to define them yourself; they are part of the Python language standard library.

All built-in, non-system-exiting exceptions are derived from the `Exception` class. All exceptions are derived from the `BaseException` class. Understanding these common exceptions helps you anticipate potential errors in your code and write more robust programs.

## Common Built-in Exceptions

Here's a list of some of the most common built-in exceptions in Python, along with explanations and simple examples:

---

### `Exception`

*   **Description**: The base class for almost all built-in, non-system-exiting exceptions. It's rarely raised directly but often used in `except` clauses to catch nearly any error.
*   **Example**: While not raised directly often, you can catch it:
    ```python
    try:
        # Code that might raise various errors
        result = 10 / 0 # Raises ZeroDivisionError
    except Exception as e:
        print(f"Caught a general exception: {e}")
        print(f"Type of exception: {type(e)}")
    ```

---

### `ArithmeticError`

*   **Description**: Base class for built-in exceptions raised for various arithmetic errors.
*   **Subclasses**: `OverflowError`, `ZeroDivisionError`, `FloatingPointError`.

    *   **`ZeroDivisionError`**: Raised when the second argument of a division or modulo operation is zero.
        ```python
        try:
            result = 10 / 0
        except ZeroDivisionError:
            print("Error: Cannot divide by zero!")
        # Output: Error: Cannot divide by zero!
        ```
    *   **`OverflowError`**: Raised when the result of an arithmetic operation is too large to be represented (less common in standard Python integers due to arbitrary precision, but can occur with floats or specific libraries).
        ```python
        import math
        try:
            # This might raise OverflowError for very large numbers with floats
            large_number = 1e308 # A large float
            result = math.exp(large_number * 2) # Exponentiation can grow very fast
        except OverflowError:
            print("Error: Calculation resulted in overflow!")
        # Note: Exact behavior might vary.
        ```

---

### `AssertionError`

*   **Description**: Raised when an `assert` statement fails. Assertions are used as internal self-checks within the code.
*   **Example**:
    ```python
    x = 10
    y = 5
    try:
        assert x < y, "x should be less than y, but it's not!"
    except AssertionError as e:
        print(f"Assertion failed: {e}")
    # Output: Assertion failed: x should be less than y, but it's not!
    ```

---

### `AttributeError`

*   **Description**: Raised when an attribute reference or assignment fails. This usually means you're trying to access a method or property that doesn't exist for an object.
*   **Example**:
    ```python
    my_list = [1, 2, 3]
    try:
        # Lists don't have a 'push' method (it's 'append')
        my_list.push(4)
    except AttributeError:
        print("Error: The object does not have that attribute/method.")
    # Output: Error: The object does not have that attribute/method.
    ```

---

### `EOFError` (End-of-File Error)

*   **Description**: Raised when the `input()` function hits an end-of-file condition (EOF) without reading any data. This typically happens when reading from a file that ends unexpectedly or when input is redirected and finishes.
*   **Example**: (Harder to demonstrate directly without file I/O or specific terminal interaction)
    ```python
    # Conceptual example - running this might require specific input redirection
    try:
        # If input stream ends immediately (e.g., ctrl+d in Unix, ctrl+z then Enter in Windows)
        data = input("Enter something: ")
    except EOFError:
        print("EOFError: Reached end of input unexpectedly.")
    ```

---

### `ImportError`

*   **Description**: Raised when the `import` statement has trouble trying to load a module.
*   **Subclass**: `ModuleNotFoundError` (Python 3.6+)

    *   **`ModuleNotFoundError`**: A subclass of `ImportError`, specifically raised when a module could not be found.
        ```python
        try:
            import non_existent_module
        except ModuleNotFoundError:
            print("Error: The specified module could not be found.")
        # Output: Error: The specified module could not be found.
        ```
    *   **General `ImportError`**: Can also be raised if a name within a module cannot be found during a `from ... import ...` statement.
        ```python
        try:
            # Assuming 'math' module exists, but 'non_existent_function' does not
            from math import non_existent_function
        except ImportError as e:
            print(f"ImportError: {e}")
        # Output: ImportError: cannot import name 'non_existent_function' from 'math' (...)
        ```

---

### `LookupError`

*   **Description**: Base class for exceptions raised when a key or index used on a mapping or sequence is invalid.
*   **Subclasses**: `IndexError`, `KeyError`.

    *   **`IndexError`**: Raised when a sequence subscript (index) is out of range.
        ```python
        my_list = [10, 20, 30]
        try:
            print(my_list[5]) # Index 5 is out of bounds
        except IndexError:
            print("Error: Index out of range.")
        # Output: Error: Index out of range.
        ```
    *   **`KeyError`**: Raised when a mapping (dictionary) key is not found in the set of existing keys.
        ```python
        my_dict = {'a': 1, 'b': 2}
        try:
            print(my_dict['c']) # Key 'c' does not exist
        except KeyError:
            print("Error: Key not found in dictionary.")
        # Output: Error: Key not found in dictionary.
        ```

---

### `KeyboardInterrupt`

*   **Description**: Raised when the user hits the interrupt key (normally `Ctrl+C` or `Delete`). This exception inherits directly from `BaseException` so it's not caught by `except Exception`.
*   **Example**: (Run this in a terminal and press `Ctrl+C`)
    ```python
    try:
        print("Program running... Press Ctrl+C to interrupt.")
        while True:
            pass # Keep running indefinitely
    except KeyboardInterrupt:
        print("\nProgram interrupted by user.")
    # Output (after pressing Ctrl+C):
    # Program running... Press Ctrl+C to interrupt.
    # ^C
    # Program interrupted by user.
    ```

---

### `MemoryError`

*   **Description**: Raised when an operation runs out of memory. This is usually due to trying to create a very large data structure.
*   **Example**: (This might make your system slow or unresponsive - use caution)
    ```python
    try:
        # Attempt to create a huge list (might consume too much RAM)
        very_large_list = [0] * (10**12)
    except MemoryError:
        print("MemoryError: Not enough memory to complete the operation.")
    # Note: The actual limit depends on your system's available memory.
    ```

---

### `NameError`

*   **Description**: Raised when a local or global name (variable, function, class) is not found.
*   **Example**:
    ```python
    try:
        print(undefined_variable)
    except NameError:
        print("Error: The name 'undefined_variable' is not defined.")
    # Output: Error: The name 'undefined_variable' is not defined.
    ```

---

### `OSError`

*   **Description**: Base class for exceptions related to operating system errors, like file not found, permission errors, etc. It can be raised for various I/O failures.
*   **Subclasses**: `FileNotFoundError`, `PermissionError`, `ConnectionError`, etc.

    *   **`FileNotFoundError`**: Raised when trying to open or operate on a file that does not exist.
        ```python
        try:
            with open("non_existent_file.txt", "r") as f:
                content = f.read()
        except FileNotFoundError:
            print("Error: The file was not found.")
        # Output: Error: The file was not found.
        ```

---

### `RuntimeError`

*   **Description**: Raised when an error is detected that doesn't fall in any of the other categories. It indicates something went wrong during runtime that wasn't expected or specific enough for another exception type.
*   **Example**: (Less common to encounter directly unless explicitly raised or from certain complex operations)
    ```python
    # Example: Raising it explicitly
    try:
        raise RuntimeError("Something unexpected happened during runtime.")
    except RuntimeError as e:
        print(f"Caught RuntimeError: {e}")
    # Output: Caught RuntimeError: Something unexpected happened during runtime.
    ```

---

### `SyntaxError`

*   **Description**: Raised by the parser when a syntax error is encountered. This means the code is not valid Python code. This usually happens *before* execution starts.
*   **Example**: (This code won't run if typed directly into a file, as the error prevents execution)
    ```python
    # Invalid syntax: missing colon
    # try:
    #     if True
    #         print("Hello")
    # except SyntaxError: # You usually can't catch SyntaxError this way
    #     print("Syntax error detected")
    # Instead, Python will fail to parse the file:
    # File "<stdin>", line 1
    #   if True
    #          ^
    # SyntaxError: expected ':'
    ```

    *   **`IndentationError`**: A subclass of `SyntaxError`. Raised when there is incorrect indentation.
        ```python
        # Invalid indentation
        # try:
        # def my_function():
        # print("Inside function") # Incorrect indentation
        # except IndentationError:
        #     print("Indentation error")
        # Python will raise IndentationError during parsing:
        # File "<stdin>", line 2
        #   print("Inside function")
        #   ^
        # IndentationError: expected an indented block
        ```
    *   **`TabError`**: A subclass of `IndentationError`. Raised when indentation contains inconsistent use of tabs and spaces.

---

### `SystemError`

*   **Description**: Raised when the interpreter finds an internal error, but the situation doesn't look serious enough to cause it to abort entirely. This usually indicates a bug in the Python interpreter itself or in a C extension module. You typically shouldn't encounter this in normal Python code.

---

### `TypeError`

*   **Description**: Raised when an operation or function is applied to an object of an inappropriate type.
*   **Example**:
    ```python
    try:
        result = "hello" + 5 # Cannot concatenate string and integer
    except TypeError:
        print("TypeError: Unsupported operand types for +.")
    # Output: TypeError: Unsupported operand types for +.

    try:
        len(123) # len() requires a sequence (string, list, tuple, etc.), not an integer
    except TypeError:
        print("TypeError: Object does not have length.")
    # Output: TypeError: Object does not have length.
    ```

---

### `ValueError`

*   **Description**: Raised when an operation or function receives an argument that has the right type but an inappropriate value. Also raised when an index is not an integer, but the situation cannot be described more precisely by `IndexError`.
*   **Example**:
    ```python
    try:
        # int() can convert strings, but only if they represent a valid integer
        number = int("abc")
    except ValueError:
        print("ValueError: Could not convert string to integer.")
    # Output: ValueError: Could not convert string to integer.

    import math
    try:
        # math.sqrt requires a non-negative number
        result = math.sqrt(-10)
    except ValueError:
        print("ValueError: math domain error (e.g., sqrt of negative number).")
    # Output: ValueError: math domain error (e.g., sqrt of negative number).
    ```

---

### `StopIteration`

*   **Description**: Raised by the built-in function `next()` and an iterator's `__next__()` method to signal that there are no further items produced by the iterator. This is used internally by `for` loops to know when to stop.
*   **Example**:
    ```python
    my_list = [1, 2]
    my_iterator = iter(my_list)

    try:
        print(next(my_iterator)) # Output: 1
        print(next(my_iterator)) # Output: 2
        print(next(my_iterator)) # Raises StopIteration here
    except StopIteration:
        print("StopIteration: Reached the end of the iterator.")
    # Output:
    # 1
    # 2
    # StopIteration: Reached the end of the iterator.
    ```

---

## Handling Exceptions (`try...except`)

The primary way to handle exceptions in Python is using the `try...except` block:

```python
try:
    # Code that might raise an exception
    x = int(input("Enter a number: "))
    result = 100 / x
    print(f"Result is: {result}")

except ValueError:
    # Handle the case where input is not a valid number
    print("Invalid input. Please enter a number.")

except ZeroDivisionError:
    # Handle the case where the user enters 0
    print("You cannot divide by zero.")

except Exception as e:
    # Catch any other exceptions that might occur
    print(f"An unexpected error occurred: {e}")

finally:
    # Optional: Code that always runs, whether an exception occurred or not
    print("Execution finished or handled.")
```

By understanding these built-in exceptions, you can write `except` blocks to catch specific errors and make your Python programs more reliable and user-friendly.
```