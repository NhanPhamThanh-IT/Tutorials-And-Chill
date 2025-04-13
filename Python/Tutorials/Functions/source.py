# Functions in Python
# A function is a block of organized, reusable code that is used to perform a single, related action.
# Functions provide better modularity for your application and a high degree of code reusing.

# 1. Defining a Simple Function
# Use the 'def' keyword to define a function.
# Function names follow the same rules as variable names (snake_case recommended).
# The code block within every function starts with a colon (:) and is indented.

def greet():
    """This function prints a simple greeting."""
    # This is the function body. It contains the code to be executed.
    print("Hello, Python learner!")
    print("Welcome to the world of functions.")

# 2. Calling a Function
# To execute the code inside a function, you need to "call" it.
print("--- Calling the greet() function ---")
greet()
print("-" * 30) # Separator

# 3. Functions with Parameters (Arguments)
# You can pass information into functions as arguments (also called parameters).
# Arguments are specified after the function name, inside the parentheses.
# You can add as many arguments as you want, just separate them with a comma.

def greet_user(username):
    """This function greets the user by name."""
    # 'username' is a parameter. When we call the function, we pass an argument.
    print(f"Hello, {username}!")

# Calling the function with an argument
print("--- Calling greet_user() with an argument ---")
greet_user("Alice")
greet_user("Bob")
print("-" * 30)

# 4. Functions with Multiple Parameters

def add_numbers(num1, num2):
    """This function adds two numbers and prints the result."""
    # num1 and num2 are parameters
    result = num1 + num2
    print(f"The sum of {num1} and {num2} is: {result}")

# Calling the function with two arguments
print("--- Calling add_numbers() with two arguments ---")
add_numbers(5, 3)
add_numbers(100, -50)
print("-" * 30)

# 5. Positional vs. Keyword Arguments
# When you call a function, you can pass arguments in two ways:
# a) Positional arguments: Arguments are matched based on their position.
# b) Keyword arguments: Arguments are matched based on the parameter name.

def describe_pet(animal_type, pet_name):
    """Displays information about a pet."""
    print(f"I have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

print("--- Using Positional Arguments ---")
describe_pet("hamster", "harry") # 'hamster' goes to animal_type, 'harry' to pet_name

print("\n--- Using Keyword Arguments ---")
describe_pet(animal_type="dog", pet_name="willie")
describe_pet(pet_name="lucy", animal_type="cat") # Order doesn't matter with keyword arguments
print("-" * 30)

# 6. Default Parameter Values
# You can define a default value for a parameter.
# If an argument for that parameter is not provided in the function call, the default value is used.
# Parameters with default values must come AFTER parameters without default values.

def describe_pet_default(pet_name, animal_type="dog"): # animal_type has a default value
    """Displays information about a pet, with a default animal type."""
    print(f"I have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

print("--- Using Default Parameter Values ---")
# Calling without specifying animal_type (uses default 'dog')
describe_pet_default(pet_name="willie")
print()
# Calling and overriding the default value
describe_pet_default(pet_name="goldie", animal_type="fish")
print("-" * 30)

# 7. Return Values
# Functions can perform an action (like printing) or compute a value and return it.
# The 'return' statement exits a function and optionally passes back a value to the caller.
# If no return statement is specified, the function implicitly returns None.

def add_numbers_return(num1, num2):
    """This function adds two numbers and returns the result."""
    result = num1 + num2
    return result # The value of 'result' is sent back to where the function was called

print("--- Using Return Values ---")
sum_result = add_numbers_return(10, 25) # Store the returned value in a variable
print(f"The returned sum is: {sum_result}")
print(f"We can use the result directly: {add_numbers_return(-5, 5)}")

# You can return multiple values (they are returned as a tuple)
def get_name_parts(full_name):
    """Splits a full name into first and last name."""
    parts = full_name.split()
    if len(parts) >= 2:
        return parts[0], parts[-1] # Returns a tuple ('John', 'Doe')
    elif len(parts) == 1:
        return parts[0], None # Return None for the missing part
    else:
        return None, None

first, last = get_name_parts("Jane Doe")
print(f"First name: {first}, Last name: {last}")
first, last = get_name_parts("Madonna")
print(f"First name: {first}, Last name: {last}")
print("-" * 30)

# 8. Scope of Variables (Local vs. Global)
# Variables defined inside a function are local to that function.
# They cannot be accessed from outside the function.
# Variables defined outside all functions are global.

global_var = "I am global"

def scope_test():
    local_var = "I am local"
    print(f"Inside function: {local_var}")
    print(f"Inside function, accessing global: {global_var}")

print("--- Variable Scope ---")
scope_test()
print(f"Outside function: {global_var}")
# print(f"Outside function, trying to access local: {local_var}") # This would cause an error (NameError)
print("-" * 30)

# Modifying a global variable inside a function requires the 'global' keyword.
count = 0

def increment_count():
    global count # Declare that we want to use the global 'count' variable
    count += 1
    print(f"Inside increment_count: {count}")

print("--- Modifying Global Variables ---")
print(f"Initial count: {count}")
increment_count()
increment_count()
print(f"Final count: {count}")
print("-" * 30)

# 9. Docstrings (Documentation Strings)
# The string literal right after the function definition is the docstring.
# It's used to explain what the function does.
# Good practice to always include docstrings.
# You can access the docstring using the help() function or the __doc__ attribute.

def well_documented_function(param1, param2):
    """
    This is a detailed docstring explaining the function.

    Args:
        param1: Description of the first parameter.
        param2: Description of the second parameter.

    Returns:
        Description of the return value (e.g., The sum of param1 and param2).
    """
    # Function code goes here
    return param1 + param2

print("--- Docstrings ---")
help(well_documented_function)
print("\nAccessing docstring directly:")
print(well_documented_function.__doc__)
print("-" * 30)

# 10. Arbitrary Number of Arguments (*args)
# If you don't know beforehand how many positional arguments a function needs to accept.
# Use an asterisk (*) before the parameter name.
# Python packs all the extra positional arguments into a tuple.

def make_pizza(size, *toppings):
    """Summarize the pizza we are about to make."""
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    # 'toppings' is a tuple containing all the arguments passed after 'size'
    if toppings:
        for topping in toppings:
            print(f"- {topping}")
    else:
        print("- Plain cheese")

print("--- Arbitrary Positional Arguments (*args) ---")
make_pizza(12, "pepperoni")
make_pizza(16, "mushrooms", "green peppers", "extra cheese")
make_pizza(10) # No extra toppings provided
print("-" * 30)

# 11. Arbitrary Keyword Arguments (**kwargs)
# If you don't know beforehand what kind of information will be passed to the function.
# Use two asterisks (**) before the parameter name.
# Python packs all the extra keyword arguments into a dictionary.

def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    # 'user_info' is a dictionary containing all keyword arguments passed after 'first' and 'last'
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile

print("--- Arbitrary Keyword Arguments (**kwargs) ---")
user_profile = build_profile('albert', 'einstein',
                             location='princeton',
                             field='physics')
print(user_profile)

user_profile_2 = build_profile('marie', 'curie',
                               location='paris',
                               field='chemistry',
                               nobel_prizes=2)
print(user_profile_2)
print("-" * 30)

# 12. Lambda Functions (Anonymous Functions)
# Small, unnamed functions defined using the 'lambda' keyword.
# Syntax: lambda arguments: expression
# The expression is executed and the result is returned.
# Often used when you need a simple function for a short period, e.g., as an argument to higher-order functions like map(), filter(), sorted().

# Regular function
def square(x):
  return x * x

# Equivalent lambda function
square_lambda = lambda x: x * x

print("--- Lambda Functions ---")
print(f"Square (regular function): {square(5)}")
print(f"Square (lambda function): {square_lambda(5)}")

# Using lambda with sorted()
points = [(1, 2), (3, 1), (5, -4), (2, 3)]
# Sort points based on the second element (y-coordinate)
points_sorted_by_y = sorted(points, key=lambda point: point[1])
print(f"Points sorted by y-coordinate: {points_sorted_by_y}")
print("-" * 30)

print("End of Function Examples.")