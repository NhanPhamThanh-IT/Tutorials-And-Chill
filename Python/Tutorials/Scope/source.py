# --- Python Scope Examples ---

# 1. Global Scope
# Variables defined outside of any function are in the global scope.
# They can be accessed from anywhere in the code, including inside functions.

global_var = "I am a global variable"

print(f"1. Accessing global_var from global scope: {global_var}")

def access_global():
    """This function accesses the global variable."""
    print(f"2. Accessing global_var from inside a function: {global_var}")

access_global()

# Modifying a global variable from inside a function requires the 'global' keyword.
def modify_global():
    """This function modifies the global variable."""
    global global_var  # Declare intention to modify the global variable
    global_var = "I am the MODIFIED global variable"
    print(f"3. Inside modify_global function: {global_var}")

modify_global()
print(f"4. After calling modify_global, global_var is: {global_var}")

print("-" * 20)

# 2. Local Scope
# Variables defined inside a function are in the local scope of that function.
# They only exist while the function is executing and cannot be accessed from outside.

def local_scope_example():
    """Demonstrates local scope."""
    local_var = "I am a local variable"
    print(f"5. Inside local_scope_example: {local_var}")
    # global_var can still be accessed here (read-only unless 'global' is used)
    print(f"6. Accessing global_var inside local_scope_example: {global_var}")

local_scope_example()

# Trying to access local_var outside the function will cause an error:
try:
    print(local_var)
except NameError as e:
    print(f"7. Trying to access local_var outside its function causes: {e}")

print("-" * 20)

# 3. Enclosing Function Locals (Nonlocal Scope)
# This applies when you have nested functions (a function inside another function).
# The inner function can access variables from the outer (enclosing) function's scope.

def outer_function():
    """Outer function with its own local variable."""
    outer_var = "I am in the outer function"
    print(f"8. Inside outer_function: outer_var = {outer_var}")

    def inner_function():
        """Inner function accessing outer function's variable."""
        # Inner function can READ outer_var
        print(f"9. Inside inner_function: Accessing outer_var = {outer_var}")
        # It can also access global variables
        print(f"10. Inside inner_function: Accessing global_var = {global_var}")

    inner_function() # Call the inner function

    # Trying to access inner_var here would cause an error if inner_function defined one.

outer_function()

# Modifying an enclosing function's variable requires the 'nonlocal' keyword.
def outer_function_modify():
    """Outer function demonstrating nonlocal modification."""
    outer_var_modify = "Original outer value"
    print(f"11. Inside outer_function_modify (before inner): outer_var_modify = {outer_var_modify}")

    def inner_function_modify():
        """Inner function modifying the enclosing function's variable."""
        nonlocal outer_var_modify # Declare intention to modify the enclosing scope variable
        outer_var_modify = "Modified outer value by inner function"
        print(f"12. Inside inner_function_modify: outer_var_modify = {outer_var_modify}")

    inner_function_modify()
    print(f"13. Inside outer_function_modify (after inner): outer_var_modify = {outer_var_modify}")

outer_function_modify()

print("-" * 20)

# 4. Built-in Scope
# This scope contains names that are pre-defined in Python, like functions (print, len, type)
# and exceptions (NameError, TypeError). They are always available.

print(f"14. Using built-in function 'len': Length of global_var is {len(global_var)}")
print(f"15. Using built-in function 'type': Type of global_var is {type(global_var)}")
# You can technically reassign built-in names, but it's strongly discouraged!
# Example (don't do this in real code):
# print = "Oops, I overwrote the print function!"
# print("This would now cause an error") # TypeError: 'str' object is not callable

print("-" * 20)

# --- LEGB Rule Summary ---
# When you try to access a variable, Python searches for it in the following order:
# L: Local - The current function's scope.
# E: Enclosing function locals - Scopes of any enclosing functions (from inner to outer).
# G: Global - The module's global scope.
# B: Built-in - Python's pre-defined names.
# Python uses the first variable it finds.

# --- Variable Shadowing ---
# If a variable in an inner scope has the same name as a variable in an outer scope,
# the inner variable "shadows" the outer one within its scope.

shadow_var = "I am the GLOBAL shadow_var"
print(f"16. Global scope: shadow_var = {shadow_var}")

def shadowing_example():
    """Demonstrates variable shadowing."""
    shadow_var = "I am the LOCAL shadow_var, shadowing the global one"
    print(f"17. Inside shadowing_example: shadow_var = {shadow_var}") # Prints the local one

    def inner_shadow():
        shadow_var = "I am the INNERMOST shadow_var"
        print(f"18. Inside inner_shadow: shadow_var = {shadow_var}") # Prints the innermost one

    inner_shadow()
    print(f"19. Back in shadowing_example: shadow_var = {shadow_var}") # Still the local one

shadowing_example()
print(f"20. Global scope again: shadow_var = {shadow_var}") # Prints the global one

print("-" * 20)

# --- Scope and Loops/Conditionals ---
# Loops (for, while) and conditionals (if, elif, else) do NOT create new local scopes in Python.
# Variables defined inside them belong to the scope where the loop/conditional resides.

def scope_with_loop(items):
    """Demonstrates scope within loops."""
    print(f"21. Entering scope_with_loop")
    new_var_in_loop = None # Initialize to avoid potential NameError if loop is empty
    for i in items:
        new_var_in_loop = i * 10 # This variable is local to scope_with_loop
        print(f"   Inside loop: i = {i}, new_var_in_loop = {new_var_in_loop}")

    # new_var_in_loop is accessible here because the loop doesn't create a new scope
    if new_var_in_loop is not None:
        print(f"22. After loop in scope_with_loop: new_var_in_loop = {new_var_in_loop}")
    else:
        print(f"22. After loop in scope_with_loop: Loop was empty, new_var_in_loop is None")

scope_with_loop([1, 2, 3])
scope_with_loop([])

# Trying to access new_var_in_loop outside scope_with_loop will fail:
try:
    print(new_var_in_loop)
except NameError as e:
    print(f"23. Trying to access new_var_in_loop outside its function causes: {e}")

print("-" * 20)
print("End of Scope Examples")