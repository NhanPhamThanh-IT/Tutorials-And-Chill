# Python Keywords

Keywords in Python are reserved words that have special meanings and purposes. You cannot use them as variable names, function names, or any other identifiers. They are part of the fundamental syntax of the language.

Here is a list of Python keywords along with explanations and examples for beginners:

---

### `False`

*   **Purpose:** Represents the boolean value 'false'. It's often used in conditional statements.
*   **Example:**
    ```python
    is_active = False
    if not is_active:
        print("User is not active.")
    ```
*   **Explanation:** `False` is assigned to `is_active`. The `if` statement checks if `is_active` is not true (which it is, because it's `False`), and then prints the message.

---

### `None`

*   **Purpose:** Represents the absence of a value or a null value. It's often used to indicate that a variable doesn't have a value assigned yet.
*   **Example:**
    ```python
    user_input = None
    if user_input is None:
        print("No input received yet.")
    ```
*   **Explanation:** `user_input` is initialized to `None`. The `if` statement checks if `user_input` is still `None`.

---

### `True`

*   **Purpose:** Represents the boolean value 'true'. Used in conditional logic.
*   **Example:**
    ```python
    is_logged_in = True
    if is_logged_in:
        print("Welcome back!")
    ```
*   **Explanation:** `is_logged_in` is set to `True`. The `if` statement executes its block because the condition is `True`.

---

### `and`

*   **Purpose:** A logical operator. Returns `True` if both the statements on its left and right are true.
*   **Example:**
    ```python
    age = 25
    has_license = True
    if age > 18 and has_license:
        print("Allowed to drive.")
    ```
*   **Explanation:** The message is printed only if `age` is greater than 18 *and* `has_license` is `True`.

---

### `as`

*   **Purpose:** Used to create an alias when importing modules or in `with` statements.
*   **Example (Import):**
    ```python
    import math as m
    print(m.sqrt(16)) # Output: 4.0
    ```
*   **Example (With):**
    ```python
    with open("myfile.txt", "w") as f:
        f.write("Hello, file!")
    ```
*   **Explanation:** In the first example, `math` module is imported with the shorter name `m`. In the second, the opened file object is referred to as `f` within the `with` block.

---

### `assert`

*   **Purpose:** Used for debugging. It tests a condition; if the condition is `False`, it raises an `AssertionError`.
*   **Example:**
    ```python
    x = 5
    assert x > 0, "x must be positive"
    print("x is positive.")
    ```
*   **Explanation:** The code checks if `x` is greater than 0. Since it is, the program continues. If `x` were 0 or negative, an `AssertionError` with the message "x must be positive" would be raised.

---

### `async`

*   **Purpose:** Used to declare an asynchronous function (a coroutine). Requires `await`. Used in asynchronous programming.
*   **Example:**
    ```python
    import asyncio

    async def main():
        print('Hello')
        await asyncio.sleep(1) # Pause execution for 1 second
        print('World')

    # To run it (in a context that supports async):
    # asyncio.run(main())
    ```
*   **Explanation:** `async def` defines `main` as a coroutine. `await` pauses `main` while `asyncio.sleep(1)` runs. (Requires Python 3.5+)

---

### `await`

*   **Purpose:** Used inside `async` functions to wait for an awaitable object (like a coroutine) to complete.
*   **Example:** See the `async` example above.
*   **Explanation:** `await` pauses the execution of the current coroutine (`main`) until the awaited task (`asyncio.sleep(1)`) is finished.

---

### `break`

*   **Purpose:** Exits the current loop (`for` or `while`) prematurely.
*   **Example:**
    ```python
    for i in range(10):
        if i == 5:
            break # Exit the loop when i is 5
        print(i)
    # Output: 0 1 2 3 4
    ```
*   **Explanation:** The loop iterates from 0. When `i` becomes 5, the `if` condition is true, and `break` is executed, terminating the loop immediately.

---

### `class`

*   **Purpose:** Used to define a new user-defined class. Classes are blueprints for creating objects.
*   **Example:**
    ```python
    class Dog:
        def __init__(self, name): # Constructor
            self.name = name

        def bark(self):
            print(f"{self.name} says Woof!")

    my_dog = Dog("Buddy") # Create an object (instance) of the Dog class
    my_dog.bark() # Output: Buddy says Woof!
    ```
*   **Explanation:** `class Dog:` starts the definition of a class named `Dog`. `__init__` is a special method (constructor) called when an object is created. `bark` is another method. `my_dog` is an instance of the `Dog` class.

---

### `continue`

*   **Purpose:** Skips the rest of the current iteration of a loop (`for` or `while`) and proceeds to the next iteration.
*   **Example:**
    ```python
    for i in range(5):
        if i == 2:
            continue # Skip printing when i is 2
        print(i)
    # Output: 0 1 3 4
    ```
*   **Explanation:** When `i` is 2, `continue` is executed. The `print(i)` statement for that iteration is skipped, and the loop moves to the next iteration (`i = 3`).

---

### `def`

*   **Purpose:** Used to define a function.
*   **Example:**
    ```python
    def greet(name):
        print(f"Hello, {name}!")

    greet("Alice") # Call the function
    # Output: Hello, Alice!
    ```
*   **Explanation:** `def greet(name):` defines a function named `greet` that takes one argument (`name`). The indented code block is the function's body.

---

### `del`

*   **Purpose:** Used to delete objects. This can be variables, items from a list, keys from a dictionary, etc.
*   **Example (Variable):**
    ```python
    x = 10
    print(x) # Output: 10
    del x
    # print(x) # This would cause a NameError because x is deleted
    ```
*   **Example (List Item):**
    ```python
    my_list = [1, 2, 3, 4]
    del my_list[1] # Delete item at index 1
    print(my_list) # Output: [1, 3, 4]
    ```
*   **Explanation:** `del` removes the reference to the object. If no other references exist, the object may be garbage collected.

---

### `elif`

*   **Purpose:** Short for "else if". Used in `if` statements to check multiple conditions sequentially.
*   **Example:**
    ```python
    score = 75
    if score >= 90:
        print("Grade: A")
    elif score >= 80:
        print("Grade: B")
    elif score >= 70:
        print("Grade: C") # This condition is met
    else:
        print("Grade: D")
    # Output: Grade: C
    ```
*   **Explanation:** If the `if` condition is false, the `elif` condition is checked. If it's true, its block executes, and the rest of the `elif`/`else` chain is skipped.

---

### `else`

*   **Purpose:** Used in `if` statements and loops.
    *   In `if`: Executes a block of code if the preceding `if` and `elif` conditions are all false.
    *   In loops (`for`, `while`): Executes a block of code only if the loop completed normally (i.e., was not terminated by `break`).
*   **Example (If):** See the `elif` example above.
*   **Example (Loop):**
    ```python
    for i in range(3):
        print(i)
    else:
        print("Loop finished normally.")
    # Output:
    # 0
    # 1
    # 2
    # Loop finished normally.

    for i in range(3):
        if i == 1:
            break
        print(i)
    else:
        print("Loop finished normally.") # This else block does NOT execute
    # Output:
    # 0
    ```
*   **Explanation:** The `else` block provides an alternative path when conditions aren't met or indicates normal loop completion.

---

### `except`

*   **Purpose:** Used with `try` to catch and handle exceptions (errors) that occur in the `try` block.
*   **Example:**
    ```python
    try:
        result = 10 / 0
    except ZeroDivisionError:
        print("Error: Cannot divide by zero!")
    # Output: Error: Cannot divide by zero!
    ```
*   **Explanation:** The code inside `try` is executed. If a `ZeroDivisionError` occurs, the code inside the `except ZeroDivisionError:` block is executed.

---

### `finally`

*   **Purpose:** Used with `try...except`. The `finally` block always executes, regardless of whether an exception occurred or not. Often used for cleanup actions (like closing files).
*   **Example:**
    ```python
    try:
        f = open("temp.txt", "w")
        f.write("test")
        # result = 10 / 0 # Uncomment to see finally still run
    except ZeroDivisionError:
        print("Cannot divide by zero")
    finally:
        print("Closing the file.")
        f.close() # Ensure file is closed
    ```
*   **Explanation:** The `finally` block runs after the `try` (and potentially `except`) block finishes, ensuring cleanup code like `f.close()` is always executed.

---

### `for`

*   **Purpose:** Used to iterate over a sequence (like a list, tuple, dictionary, set, or string) or other iterable object.
*   **Example:**
    ```python
    fruits = ["apple", "banana", "cherry"]
    for fruit in fruits:
        print(fruit)
    # Output:
    # apple
    # banana
    # cherry
    ```
*   **Explanation:** The loop assigns each item from the `fruits` list to the `fruit` variable one by one and executes the indented block for each item.

---

### `from`

*   **Purpose:** Used with `import` to import specific parts (functions, classes, variables) from a module.
*   **Example:**
    ```python
    from math import sqrt # Import only the sqrt function from math module

    print(sqrt(25)) # Output: 5.0
    # print(math.pi) # This would cause a NameError because only sqrt was imported
    ```
*   **Explanation:** Instead of importing the whole `math` module, only the `sqrt` function is imported directly into the current namespace.

---

### `global`

*   **Purpose:** Declares that a variable inside a function is global (i.e., it belongs to the global scope outside the function).
*   **Example:**
    ```python
    count = 0 # Global variable

    def increment():
        global count # Declare intent to modify the global variable
        count += 1

    increment()
    print(count) # Output: 1
    ```
*   **Explanation:** Without `global count`, the line `count += 1` inside `increment` would try to create a *new* local variable `count`, leading to an error because it's used before assignment. `global` tells Python to use the existing global `count`.

---

### `if`

*   **Purpose:** Used for conditional execution. Executes a block of code only if a specified condition is true.
*   **Example:**
    ```python
    temperature = 30
    if temperature > 25:
        print("It's a warm day!")
    # Output: It's a warm day!
    ```
*   **Explanation:** The code inside the `if` block is executed because the condition `temperature > 25` is true.

---

### `import`

*   **Purpose:** Used to import modules (files containing Python code) into the current script.
*   **Example:**
    ```python
    import math

    print(math.pi) # Access pi constant from the math module
    print(math.sqrt(16)) # Use sqrt function from the math module
    # Output:
    # 3.141592653589793
    # 4.0
    ```
*   **Explanation:** `import math` makes all the functions and variables defined in the `math` module available, accessed using `math.`.

---

### `in`

*   **Purpose:**
    *   Checks if a value is present in a sequence (list, tuple, string, etc.).
    *   Used in `for` loops to iterate over a sequence.
*   **Example (Membership Test):**
    ```python
    my_list = [1, 2, 3]
    print(2 in my_list) # Output: True
    print(5 in my_list) # Output: False
    ```
*   **Example (For Loop):** See the `for` keyword example.
*   **Explanation:** `in` returns `True` or `False` for membership tests. In `for` loops, it facilitates iteration.

---

### `is`

*   **Purpose:** Tests if two variables refer to the exact same object in memory (not just if they have the same value).
*   **Example:**
    ```python
    a = [1, 2, 3]
    b = a       # b refers to the same list object as a
    c = [1, 2, 3] # c refers to a new list object with the same content

    print(a is b) # Output: True (same object)
    print(a is c) # Output: False (different objects, even if content is same)
    print(a == c) # Output: True (content is the same)
    ```
*   **Explanation:** `is` checks for object identity, while `==` checks for value equality. Use `is` often when checking against `None`.

---

### `lambda`

*   **Purpose:** Used to create small, anonymous functions (functions without a name).
*   **Example:**
    ```python
    # A lambda function that adds 10 to its input
    add_ten = lambda x: x + 10

    print(add_ten(5)) # Output: 15
    ```
*   **Explanation:** `lambda x: x + 10` defines a function that takes one argument `x` and returns `x + 10`. It's assigned to the variable `add_ten`. Lambdas are often used where a simple function is needed for a short period (e.g., as an argument to `map` or `filter`).

---

### `nonlocal`

*   **Purpose:** Used inside nested functions. Declares that a variable refers to a variable in the nearest enclosing scope (that isn't global).
*   **Example:**
    ```python
    def outer():
        count = 0
        def inner():
            nonlocal count # Refer to count in outer function's scope
            count += 1
            print(count)
        inner()
        inner()

    outer()
    # Output:
    # 1
    # 2
    ```
*   **Explanation:** Without `nonlocal count`, `inner` would try to create its own local `count`. `nonlocal` allows `inner` to modify the `count` variable belonging to `outer`.

---

### `not`

*   **Purpose:** A logical operator. Reverses the boolean value of its operand. `not True` is `False`, `not False` is `True`.
*   **Example:**
    ```python
    is_raining = False
    if not is_raining:
        print("No need for an umbrella.")
    # Output: No need for an umbrella.
    ```
*   **Explanation:** `not is_raining` evaluates to `not False`, which is `True`. So, the `if` block executes.

---

### `or`

*   **Purpose:** A logical operator. Returns `True` if at least one of the statements on its left or right is true.
*   **Example:**
    ```python
    day = "Sunday"
    if day == "Saturday" or day == "Sunday":
        print("It's the weekend!")
    # Output: It's the weekend!
    ```
*   **Explanation:** Since `day == "Sunday"` is true, the entire `or` condition is true, and the message is printed.

---

### `pass`

*   **Purpose:** Acts as a placeholder. When the Python interpreter encounters `pass`, it does nothing. It's used where syntax requires a statement, but you don't want any code to execute (e.g., in empty function or class definitions).
*   **Example:**
    ```python
    def my_empty_function():
        pass # Avoids an IndentationError

    class MyEmptyClass:
        pass # Avoids an error

    my_empty_function() # Does nothing
    obj = MyEmptyClass() # Creates an object
    ```
*   **Explanation:** `pass` allows you to define structures without implementing them yet.

---

### `raise`

*   **Purpose:** Used to explicitly raise an exception (error).
*   **Example:**
    ```python
    def check_age(age):
        if age < 0:
            raise ValueError("Age cannot be negative.")
        print("Age is valid.")

    try:
        check_age(-5)
    except ValueError as e:
        print(e) # Output: Age cannot be negative.
    ```
*   **Explanation:** If `check_age` is called with a negative number, it raises a `ValueError` with a specific message. This error can then be caught using a `try...except` block.

---

### `return`

*   **Purpose:** Used inside a function to exit the function and optionally send a value back to the caller.
*   **Example:**
    ```python
    def add(a, b):
        result = a + b
        return result # Send the value of result back

    sum_value = add(5, 3)
    print(sum_value) # Output: 8
    ```
*   **Explanation:** The `add` function calculates the sum and `return result` sends that value back. The returned value is then assigned to `sum_value`. A function without an explicit `return` statement implicitly returns `None`.

---

### `try`

*   **Purpose:** Starts a block of code where exceptions might occur. Used with `except` and optionally `finally` and `else`.
*   **Example:** See `except` and `finally` examples.
*   **Explanation:** The code within the `try` block is monitored for errors.

---

### `while`

*   **Purpose:** Creates a loop that executes as long as a specified condition is true.
*   **Example:**
    ```python
    count = 0
    while count < 3:
        print(f"Count is {count}")
        count += 1 # Increment count, otherwise it's an infinite loop!
    # Output:
    # Count is 0
    # Count is 1
    # Count is 2
    ```
*   **Explanation:** The loop continues as long as `count < 3`. Inside the loop, `count` is printed and incremented. When `count` becomes 3, the condition `count < 3` becomes false, and the loop terminates.

---

### `with`

*   **Purpose:** Used to wrap the execution of a block of code with methods defined by a context manager. Often used for resource management (like files or network connections) to ensure resources are set up and torn down properly.
*   **Example:**
    ```python
    # Ensures the file is automatically closed even if errors occur
    with open("example.txt", "w") as file:
        file.write("Hello with 'with'!")

    # The file is guaranteed to be closed here
    ```
*   **Explanation:** The `with` statement gets a context manager from `open()`. It calls special methods (`__enter__` and `__exit__`) on the context manager. The `__exit__` method (which closes the file) is automatically called when the block is exited, even if errors happened inside. This is safer than manually calling `file.close()`.

---

### `yield`

*   **Purpose:** Used in functions like `return`, but `yield` turns the function into a generator. Generators produce a sequence of values over time, pausing execution between each value.
*   **Example:**
    ```python
    def count_up_to(n):
        i = 1
        while i <= n:
            yield i # Produce the value i and pause
            i += 1

    # Iterate through the generator
    for number in count_up_to(3):
        print(number)
    # Output:
    # 1
    # 2
    # 3
    ```
*   **Explanation:** When `count_up_to(3)` is called, it doesn't run immediately but returns a generator object. The `for` loop requests values from the generator. Each time `yield i` is hit, the value `i` is sent to the loop, and the function's state is saved. When the loop asks for the next value, the function resumes from where it left off. This is memory-efficient for large sequences.

---