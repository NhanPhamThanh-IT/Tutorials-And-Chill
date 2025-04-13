```markdown
# Understanding Scope in Python

## What is Scope?

In programming, **scope** refers to the region or context where a particular variable, function, or object is accessible or visible. When you define a variable, it doesn't exist everywhere in your program. Its scope determines where you can use it.

Think of it like rooms in a house:
*   A variable defined inside a specific room (function) might only be usable within that room (local scope).
*   A variable defined in the main hallway (module level) might be accessible from many rooms (global scope).

Understanding scope is crucial for writing correct, organized, and maintainable Python code. It helps prevent naming conflicts and makes it clear where data is coming from.

## The LEGB Rule: How Python Finds Names

Python has a specific order it follows when looking for a variable (or any name):

1.  **L**ocal: Inside the current function.
2.  **E**nclosing function locals: In the local scopes of any enclosing functions (if the current function is nested inside another function).
3.  **G**lobal: At the top level of the module (the file you are running).
4.  **B**uilt-in: Pre-defined names in Python itself (like `print`, `len`, `str`, `list`, etc.).

Python checks these scopes in order (L -> E -> G -> B). The first place it finds the name is the one it uses. If it can't find the name in any of these scopes, it raises a `NameError`.

Let's explore each scope in detail.

---

## 1. Local Scope (L)

*   **Definition:** Variables defined *inside* a function belong to that function's local scope.
*   **Accessibility:** These variables can only be accessed from within that specific function.
*   **Lifetime:** They are created when the function is called and destroyed when the function finishes executing.

**Example:**

```python
def my_function():
    # message is defined inside the function - it's local
    message = "Hello from inside the function!"
    print(message)
    # We can access 'message' here because we are inside its scope.

# Call the function
my_function()

# Try to access 'message' outside the function
# This will cause a NameError because 'message' only exists inside my_function
# print(message)
# NameError: name 'message' is not defined
```

In this example, `message` is local to `my_function`. Trying to print `message` outside the function results in an error because it's out of scope.

---

## 2. Enclosing Function Locals Scope (E)

*   **Definition:** This scope exists only for *nested functions* (functions defined inside other functions). It refers to the local scope of the outer (enclosing) function.
*   **Accessibility:** The inner function can *access* (read) variables from the outer function's scope.
*   **Closures:** This concept is closely related to closures, where an inner function "remembers" the environment (including variables) of its enclosing function, even after the outer function has finished executing.

**Example:**

```python
def outer_function():
    outer_var = "I am from the outer function."

    def inner_function():
        # inner_function can ACCESS outer_var from the enclosing scope
        print(f"Inside inner_function: {outer_var}")
        inner_var = "I am from the inner function." # Local to inner_function
        print(inner_var)

    # Call the inner function from within the outer function
    inner_function()

    # Trying to access inner_var here would cause a NameError
    # print(inner_var) # NameError

# Call the outer function, which in turn calls the inner function
outer_function()

# Trying to access outer_var or inner_var here would cause NameErrors
# print(outer_var) # NameError
# print(inner_var) # NameError
```

Here, `inner_function` can read `outer_var` because it's in the enclosing scope (E). `inner_var` is local (L) to `inner_function`.

*(Note: To *modify* a variable in the enclosing scope from the inner function, you need the `nonlocal` keyword, discussed later.)*

---

## 3. Global Scope (G)

*   **Definition:** Variables defined at the top level of a Python script or module (outside of any function).
*   **Accessibility:** Global variables can be *accessed* (read) from anywhere in the module, including inside functions.
*   **Lifetime:** They are created when the module is loaded and usually last until the program terminates.

**Example:**

```python
# global_var is defined at the top level - it's global
global_var = "I am a global variable."

def print_global():
    # We can ACCESS global_var from inside the function
    print(f"Inside print_global: {global_var}")

def try_modify_global_incorrectly():
    # If you assign to a variable inside a function, Python assumes
    # it's a NEW LOCAL variable unless you explicitly say otherwise.
    # This creates a NEW local variable named 'global_var', shadowing the global one.
    global_var = "I am trying to change the global, but creating a local instead."
    print(f"Inside try_modify_global_incorrectly: {global_var}") # Prints the local one

# Call the functions
print_global()
try_modify_global_incorrectly()

# The original global variable remains unchanged
print(f"Outside functions, global_var is still: {global_var}")
```

Notice that `try_modify_global_incorrectly` didn't actually change the *global* `global_var`. It created a *new local* variable with the same name. To modify a global variable from within a function, you need the `global` keyword.

---

## 4. Built-in Scope (B)

*   **Definition:** This scope contains all the names that are built into Python itself.
*   **Examples:** `print()`, `len()`, `str()`, `int()`, `list`, `dict`, `True`, `False`, `None`, exceptions like `ValueError`, `TypeError`, etc.
*   **Accessibility:** These names are always available anywhere in your code without needing to import anything.
*   **Caution:** While possible, you should avoid creating variables with the same names as built-in functions or types, as it can lead to confusion and errors (this is called shadowing).

**Example:**

```python
# Using built-in functions
my_list = [1, 2, 3]
length = len(my_list) # 'len' is found in the built-in scope
print(length)         # 'print' is found in the built-in scope

# Avoid doing this (shadowing a built-in):
# list = [10, 20] # Now 'list' refers to your variable, not the type
# print(list)     # Prints [10, 20]
# my_new_list = list((1, 2, 3)) # TypeError: 'list' object is not callable
```

---

## Modifying Variables in Outer Scopes

By default, assigning a value to a variable name inside a function creates a *local* variable within that function. If you need to modify a variable that exists in a wider scope (Global or Enclosing), you must explicitly tell Python using keywords.

### The `global` Keyword

Use the `global` keyword inside a function to indicate that an assignment should modify a variable in the *global* scope, rather than creating a new local variable.

**Example:**

```python
count = 0 # Global variable

def increment_global_counter():
    # Tell Python we want to work with the 'count' from the GLOBAL scope
    global count
    count = count + 1 # Modify the global variable
    print(f"Inside function, global count is now: {count}")

print(f"Before calling function, global count is: {count}")
increment_global_counter()
increment_global_counter()
print(f"After calling function, global count is: {count}")
```

Without `global count`, assigning to `count` inside the function would create a local `count` and raise an `UnboundLocalError` because you'd be trying to read the local `count` (in `count + 1`) before it was assigned a value within the function's scope.

**When to use `global`:** Use it sparingly. Over-reliance on global variables can make code harder to understand and debug, as changes in one function can unexpectedly affect other parts of the program. It's often better to pass values into functions as arguments and return results.

### The `nonlocal` Keyword

Use the `nonlocal` keyword inside a *nested* function to indicate that an assignment should modify a variable in the nearest *enclosing* function's scope (the 'E' in LEGB). It does *not* apply to the global scope.

**Example:**

```python
def outer():
    outer_count = 0 # Variable in the enclosing scope

    def inner():
        # Tell Python we want to modify 'outer_count' from the ENCLOSING scope
        nonlocal outer_count
        outer_count += 1 # Modify the enclosing scope variable
        print(f"Inside inner, outer_count is: {outer_count}")

    print(f"Before calling inner, outer_count is: {outer_count}")
    inner()
    inner()
    print(f"After calling inner, outer_count is: {outer_count}")

outer()
# print(outer_count) # NameError: outer_count is not defined globally
```

Without `nonlocal outer_count`, assigning to `outer_count` inside `inner` would create a new local variable within `inner`, leaving the `outer_count` in the `outer` function unchanged.

**`nonlocal` vs `global`:**
*   `global`: Modifies a variable in the module's top-level (global) scope.
*   `nonlocal`: Modifies a variable in the nearest enclosing function's scope (but not global).

---

## Summary of Scope Rules (LEGB)

When you use a variable name `x`:
1.  Python looks for `x` defined locally within the current function.
2.  If not found, it looks for `x` in the local scopes of any enclosing functions, from the innermost to the outermost.
3.  If still not found, it looks for `x` defined at the global (module) level.
4.  If still not found, it looks for `x` in the Python built-in names.
5.  If not found anywhere, Python raises a `NameError`.

Assignment (`=`) inside a function creates a local variable by default, unless the `global` or `nonlocal` keyword is used for that variable name within the function.

Understanding scope helps you organize your code, prevent bugs related to variable names, and manage the lifetime and accessibility of your data effectively.
```