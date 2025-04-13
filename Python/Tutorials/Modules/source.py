# source.py

"""
This file serves as an example module in Python.
A module is simply a Python file (.py) containing Python definitions and statements.
The file name is the module name with the suffix .py appended.

You can import this module into another Python script or into the interactive interpreter
to use the functions and variables defined here.
"""

# Define some variables
module_variable_string = "Hello from the source module!"
module_variable_number = 123
module_variable_list = [1, 2, 3, 4, 5]

# Define some functions
def greet(name):
    """
    This function takes a name as input and prints a greeting.
    Example: greet("Alice") will print "Hello, Alice! Welcome to the source module."
    """
    print(f"Hello, {name}! Welcome to the source module.")

def add_numbers(num1, num2):
    """
    This function takes two numbers as input and returns their sum.
    Example: add_numbers(5, 3) will return 8.
    """
    return num1 + num2

def multiply_numbers(num1, num2):
    """
    This function takes two numbers as input and returns their product.
    Example: multiply_numbers(5, 3) will return 15.
    """
    return num1 * num2

# Define a class (more advanced topic, but good to see in a module)
class SimpleCalculator:
    """
    A simple calculator class that can perform addition and multiplication.
    """
    def __init__(self, initial_value=0):
        """Initializes the calculator with an optional initial value."""
        self.current_value = initial_value
        print(f"Calculator initialized with value: {self.current_value}")

    def add(self, number):
        """Adds a number to the current value."""
        self.current_value += number
        return self.current_value

    def multiply(self, number):
        """Multiplies the current value by a number."""
        self.current_value *= number
        return self.current_value

    def get_value(self):
        """Returns the current value."""
        return self.current_value

# --- How to use this module ---
# 1. Save this file as 'source.py'.
# 2. Create another Python file (e.g., 'main.py') in the SAME directory.
# 3. In 'main.py', you can import this module and use its contents.

# Example content for 'main.py':
# ```python
# # main.py
#
# # Import the entire module
# import source
#
# # Access variables using module_name.variable_name
# print(source.module_variable_string)
# print(source.module_variable_number)
#
# # Call functions using module_name.function_name()
# source.greet("Bob")
# sum_result = source.add_numbers(10, 5)
# print(f"Sum: {sum_result}")
#
# # You can also import specific items from the module
# from source import module_variable_list, multiply_numbers
#
# print(module_variable_list)
# product_result = multiply_numbers(6, 7)
# print(f"Product: {product_result}")
#
# # You can import with an alias
# import source as src
#
# src.greet("Charlie")
# print(src.module_variable_number)
#
# # Using the class defined in the module
# from source import SimpleCalculator
#
# calc = SimpleCalculator(10)
# calc.add(5)
# calc.multiply(2)
# print(f"Calculator final value: {calc.get_value()}")
# ```

# --- The `if __name__ == "__main__":` block ---
# The code inside this block will only run when this script ('source.py')
# is executed directly (e.g., by running `python source.py` in the terminal).
# It will NOT run if this file is imported as a module into another script.
# This is useful for including test code or example usage within the module file itself.

if __name__ == "__main__":
    print("\n--- Running source.py directly ---")
    print("This code runs only when source.py is the main script.")

    # Example usage of the functions and variables defined above
    print(f"Module variable (string): {module_variable_string}")
    print(f"Module variable (number): {module_variable_number}")

    greet("Direct Runner")

    result = add_numbers(20, 22)
    print(f"Result of add_numbers(20, 22): {result}")

    result = multiply_numbers(5, 5)
    print(f"Result of multiply_numbers(5, 5): {result}")

    # Example usage of the class
    print("\nTesting the SimpleCalculator class:")
    my_calc = SimpleCalculator(100)
    my_calc.add(50)
    my_calc.multiply(3)
    print(f"Calculator test result: {my_calc.get_value()}")

    print("\n--- Finished running source.py directly ---")

# End of source.py module example