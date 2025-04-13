# Python Functions

## What is a Function?

In programming, a function is a named block of reusable code that performs a specific task. Think of it like a mini-program within your main program. You define it once and can then call (or execute) it whenever you need to perform that task.

## Why Use Functions?

Functions are fundamental building blocks in Python and offer several advantages:

1.  **Reusability:** Write the code once and use it multiple times in different parts of your program or even in other programs. This saves time and effort.
2.  **Modularity:** Break down complex problems into smaller, manageable, and logical chunks. Each function handles a specific part of the overall task.
3.  **Organization:** Make your code easier to read, understand, and maintain by giving descriptive names to blocks of code.
4.  **Abstraction:** Hide the complex implementation details of a task behind a simple function call. You only need to know *what* the function does, not necessarily *how* it does it.

## Defining a Function

You define a function using the `def` keyword, followed by the function name, parentheses `()`, and a colon `:`. The code block that belongs to the function is indented.

```python
def function_name(parameters):
    """Optional docstring explaining what the function does."""
    # Code block (indented)
    # Perform actions
    # Maybe return a value
    pass # 'pass' is a placeholder, replace it with actual code
```

*   **`def`**: Keyword to start the function definition.
*   **`function_name`**: A descriptive name for the function (follows standard Python naming conventions - usually lowercase with underscores).
*   **`parameters`**: (Optional) Variables listed inside the parentheses. They act as placeholders for values that will be passed into the function when it's called.
*   **`:`**: Colon marks the end of the function header.
*   **`"""Docstring"""`**: (Optional but highly recommended) A string literal used to document the function's purpose, parameters, and what it returns.
*   **Indented Code Block**: The actual instructions the function will execute.
*   **`return`**: (Optional) Keyword to send a value back from the function to the place where it was called. If omitted, the function implicitly returns `None`.

**Example:**

```python
def greet():
    """This function prints a simple greeting."""
    print("Hello, World!")

def add_two_numbers(num1, num2):
    """This function takes two numbers and returns their sum."""
    sum_result = num1 + num2
    return sum_result
```

## Calling a Function

To execute the code inside a function, you "call" it by using its name followed by parentheses `()`. If the function expects parameters, you provide values (called arguments) inside the parentheses.

```python
# Calling the greet function
greet()

# Calling the add_two_numbers function with arguments
result = add_two_numbers(5, 3)
print(result)
```

**Output:**

```
Hello, World!
8
```

## Parameters vs. Arguments

*   **Parameters:** Variables listed inside the parentheses in the function *definition*. They are placeholders. (e.g., `num1`, `num2` in `def add_two_numbers(num1, num2):`)
*   **Arguments:** Actual values passed into the function when it is *called*. (e.g., `5`, `3` in `add_two_numbers(5, 3)`)

## The `return` Statement

The `return` statement is used to exit a function and optionally send a value back to the caller.

*   A function can return any type of data (numbers, strings, lists, dictionaries, even other functions!).
*   If a function reaches the end without a `return` statement, it automatically returns `None`.
*   Once a `return` statement is executed, the function terminates immediately.

```python
def get_greeting(name):
    """Returns a personalized greeting string."""
    if not name:
        return None # Return None if no name is provided
    return f"Hello, {name}!" # Return the greeting string

message1 = get_greeting("Alice")
message2 = get_greeting("")

print(message1)
print(message2)
```

**Output:**

```
Hello, Alice!
None
```

## Types of Arguments

### 1. Positional Arguments

These are the most common type. Arguments are passed to the function in the order the parameters are defined.

```python
def describe_pet(animal_type, pet_name):
    """Displays information about a pet."""
    print(f"I have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet('hamster', 'harry') # 'hamster' maps to animal_type, 'harry' to pet_name
```

### 2. Keyword Arguments

You can explicitly specify which parameter an argument corresponds to by using the parameter name followed by an equals sign `=`. The order doesn't matter when using keyword arguments.

```python
describe_pet(pet_name='willie', animal_type='dog') # Order changed, but mapping is clear
```

### 3. Default Argument Values

You can provide default values for parameters in the function definition. If an argument for that parameter is not provided during the function call, the default value is used. Parameters with default values must come *after* parameters without default values.

```python
def describe_pet_default(pet_name, animal_type='dog'): # 'dog' is the default
    """Displays information about a pet, defaulting to dog."""
    print(f"I have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet_default(pet_name='charlie') # Uses default animal_type 'dog'
describe_pet_default(pet_name='goldie', animal_type='fish') # Overrides default
```

### 4. Variable-Length Arguments (`*args` and `**kwargs`)

Sometimes, you don't know in advance how many arguments a function will receive.

*   **`*args` (Non-Keyword Arguments):** Collects extra positional arguments into a *tuple*. The name `args` is conventional, but any name preceded by `*` will work.

        ```python
        def make_pizza(size, *toppings):
            """Summarize the pizza we are about to make."""
            print(f"\nMaking a {size}-inch pizza with the following toppings:")
            for topping in toppings:
                print(f"- {topping}")

        make_pizza(12, 'pepperoni')
        make_pizza(16, 'mushrooms', 'green peppers', 'extra cheese')
        ```

*   **`**kwargs` (Keyword Arguments):** Collects extra keyword arguments into a *dictionary*. The name `kwargs` is conventional, but any name preceded by `**` will work.

        ```python
        def build_profile(first, last, **user_info):
            """Build a dictionary containing everything we know about a user."""
            user_info['first_name'] = first
            user_info['last_name'] = last
            return user_info

        user_profile = build_profile('albert', 'einstein',
                                                                 location='princeton',
                                                                 field='physics')
        print(user_profile)
        ```

        **Output:**
        ```
        {'location': 'princeton', 'field': 'physics', 'first_name': 'albert', 'last_name': 'einstein'}
        ```

You can use `*args` and `**kwargs` together in a function definition (in that order, after regular and default parameters).

## Variable Scope

Scope refers to the region of your program where a variable can be accessed.

*   **Local Scope:** Variables defined *inside* a function are local to that function. They can only be accessed from within that function. They are created when the function is called and destroyed when the function returns.
*   **Global Scope:** Variables defined *outside* of any function have global scope. They can be accessed from anywhere in your code, including inside functions (though modifying them from inside requires the `global` keyword, which should generally be used sparingly).

```python
global_var = "I am global"

def my_function():
    local_var = "I am local"
    print(local_var)    # Accessing local variable (OK)
    print(global_var) # Accessing global variable (OK)

my_function()
print(global_var)     # Accessing global variable (OK)
# print(local_var)    # This would cause an error (NameError)
```

## Docstrings

As mentioned earlier, docstrings (documentation strings) are string literals enclosed in triple quotes (`"""Docstring goes here"""`) placed immediately after the function definition. They are used to explain what the function does. Good docstrings are crucial for writing understandable and maintainable code.

```python
def calculate_area(length, width):
    """
    Calculates the area of a rectangle.

    Args:
            length (float or int): The length of the rectangle.
            width (float or int): The width of the rectangle.

    Returns:
            float or int: The calculated area of the rectangle.
    """
    if length < 0 or width < 0:
            raise ValueError("Length and width cannot be negative.")
    return length * width
```

Tools and IDEs often use docstrings to provide help and context about functions. You can also access a function's docstring using the `help()` function or the `__doc__` attribute:

```python
help(calculate_area)
print(calculate_area.__doc__)
```

Functions are a powerful tool in Python. Mastering them is essential for writing efficient, readable, and reusable code.