# --- String Formatting in Python ---

# String formatting is the process of creating strings by embedding variables,
# values, or expressions within a predefined string template. This makes it
# easier to generate dynamic output, log messages, or construct complex strings.
# Python offers several ways to achieve this.

# --- 1. Old-Style Formatting (using the % operator) ---
# This method uses the modulo operator (%) as a formatting operator.
# It's similar to the `printf` function in the C programming language.
# While it works, it's generally considered less readable and flexible
# compared to newer methods, especially for complex formatting.

print("--- 1. Old-Style Formatting (%) ---")

# Define some variables to format into strings
student_name = "Charlie"
student_age = 21
student_gpa = 3.758

# Basic Usage:
# Placeholders like %s (string), %d (integer), %f (float) are used in the template string.
# A tuple containing the values to substitute is provided after the % operator.
# The order of values in the tuple must match the order of placeholders.
format_string_1 = "Student Name: %s, Age: %d" % (student_name, student_age)
print("Example 1.1 (Basic):", format_string_1)

# Formatting Floating-Point Numbers:
# You can control the precision (number of decimal places).
# %.2f means format as a float with exactly 2 decimal places.
# %.4f means format as a float with exactly 4 decimal places.
format_string_2 = "Student GPA: %.2f" % student_gpa
print("Example 1.2 (Float Precision):", format_string_2)

format_string_3 = "Student GPA (more precision): %.4f" % student_gpa
print("Example 1.3 (Float More Precision):", format_string_3)

# Combining different types:
format_string_4 = "Summary: %s (%d years old) has a GPA of %.1f" % (student_name, student_age, student_gpa)
print("Example 1.4 (Combined Types):", format_string_4)

# Using named placeholders with a dictionary:
# You can use %(key_name)s syntax and provide a dictionary after the %.
# This can sometimes improve readability if you have many values.
student_data = {"name": "Dana", "age": 23, "gpa": 3.91}
format_string_5 = "Student: %(name)s, Age: %(age)d, GPA: %(gpa).2f" % student_data
print("Example 1.5 (Dictionary/Named Placeholders):", format_string_5)

# Potential Pitfalls:
# - If the number of values in the tuple doesn't match the placeholders, you get a TypeError.
# - If the type of the value doesn't match the placeholder (e.g., %d for a string), you get a TypeError.
# try:
#     error_example = "Error: %d" % "hello" # This will cause a TypeError
# except TypeError as e:
#     print("Example 1.6 (Type Mismatch Error):", e)

print("-" * 30)

# --- 2. String `.format()` Method ---
# Introduced in Python 2.6 and improved later, this method is more powerful
# and flexible than the % operator. It uses curly braces `{}` as placeholders.

print("--- 2. String .format() Method ---")

# Define variables
item = "Coffee Mug"
price = 15.99
quantity = 3

# Basic Usage (Positional Arguments):
# Placeholders {} are filled with arguments passed to .format() in order.
format_string_6 = "Item: {}, Price: ${}, Quantity: {}".format(item, price, quantity)
print("Example 2.1 (Positional):", format_string_6)

# Using Indices:
# You can specify the index of the argument within the braces {index}.
# This allows reordering or reusing arguments.
format_string_7 = "Item: {0}, Quantity: {2}, Price: ${1:.2f}".format(item, price, quantity)
print("Example 2.2 (Indexed):", format_string_7)
format_string_8 = "Repeat Item: {0}, Original Price: ${1:.2f}, Item Again: {0}".format(item, price)
print("Example 2.3 (Reusing Index):", format_string_8)

# Using Keyword Arguments:
# You can name your placeholders {name} and pass arguments using name=value.
# This often makes the format string much more readable.
format_string_9 = "Product: {prod}, Cost: ${cost:.2f}, Available: {qty}".format(prod=item, cost=price, qty=quantity)
print("Example 2.4 (Keyword Arguments):", format_string_9)

# Mixing Positional and Keyword Arguments:
# Positional arguments must come before keyword arguments in the .format() call.
format_string_10 = "Details for {}: Price is ${cost:.2f}".format(item, cost=price)
print("Example 2.5 (Mixed Arguments):", format_string_10)

# Format Specifiers (inside the braces, after a colon `:`):
# These control how the value is presented (similar to % formatting but more extensive).
#   :<15  Left-align within 15 characters
#   :>15  Right-align within 15 characters
#   :^15  Center-align within 15 characters
#   :*^15 Center-align within 15 characters, using '*' as the fill character
#   :.2f  Format as float with 2 decimal places
#   :d    Format as integer
#   :,d   Format as integer with comma as thousands separator
#   :0>5d Format as integer, right-aligned in 5 spaces, padded with leading zeros

format_string_11 = "Item: '{:<15}' | Price: ${:>8.2f} | Quantity: {:0>3d}".format(item, price, quantity)
print("Example 2.6 (Alignment and Padding):", format_string_11)

total_cost = price * quantity
format_string_12 = "Total cost for {qty} '{prod}': ${total:,.2f}".format(qty=quantity, prod=item, total=total_cost)
print("Example 2.7 (Thousands Separator):", format_string_12)

# Using dictionaries with .format() and ** unpacking:
product_info = {"name": "Keyboard", "price": 75.00, "stock": 15}
format_string_13 = "Product: {name}, Price: ${price:.2f}, Stock: {stock}".format(**product_info)
print("Example 2.8 (Dictionary Unpacking):", format_string_13)

print("-" * 30)

# --- 3. f-Strings (Formatted String Literals) ---
# Introduced in Python 3.6, f-strings are generally the preferred method
# for string formatting in modern Python code. They are concise, readable,
# and efficient.
# You create an f-string by prefixing the string literal with 'f' or 'F'.
# You can embed expressions directly inside curly braces `{}`.

print("--- 3. f-Strings (Formatted String Literals) ---")

# Define variables
city = "Paris"
temperature_c = 22.5
population = 2_141_000 # Underscores improve readability of large numbers

# Basic Usage:
# Variables are placed directly inside the braces.
format_string_14 = f"The current temperature in {city} is {temperature_c}°C."
print("Example 3.1 (Basic f-string):", format_string_14)

# Expressions Inside Braces:
# You can put any valid Python expression inside the braces.
temperature_f = (temperature_c * 9/5) + 32
format_string_15 = f"{city}: {temperature_c}°C is equal to {temperature_f:.1f}°F."
print("Example 3.2 (Expression in f-string):", format_string_15)

# Using Format Specifiers (same syntax as .format() after the colon):
#   :<10  Left-align within 10 characters
#   :>10  Right-align within 10 characters
#   :^10  Center-align within 10 characters
#   :.2f  Format float with 2 decimal places
#   :,    Use comma as thousands separator (for numbers)
#   :b    Format integer in binary
#   :x    Format integer in hexadecimal (lowercase)
#   :X    Format integer in hexadecimal (uppercase)

format_string_16 = f"City: {city:<12} | Population: {population:>15,d}"
print("Example 3.3 (f-string Alignment and Formatting):", format_string_16)

discount_percent = 15
original_price = 80.0
discounted_price = original_price * (1 - discount_percent / 100)
format_string_17 = f"Original: ${original_price:.2f}, Discount: {discount_percent}%, Final: ${discounted_price:.2f}"
print("Example 3.4 (f-string Calculation):", format_string_17)

# Multiline f-strings:
format_string_18 = f"""
Report for: {city}
--------------------
Population: {population:10,d}
Temperature: {temperature_c:10.1f}°C
             {temperature_f:10.1f}°F
"""
print("Example 3.5 (Multiline f-string):", format_string_18.strip()) # .strip() removes leading/trailing whitespace

# Debugging with f-strings (Python 3.8+):
# Adding an equals sign `=` after the expression inside the braces will print
# both the expression text and its evaluated value. Very useful for quick debugging!
value_a = 10
value_b = 25
print(f"Example 3.6 (Debugging): {value_a=}, {value_b=}, {value_a * value_b = }")

# Using quotes inside f-string expressions:
# Be mindful of the quotes used for the f-string itself. If the f-string uses
# double quotes, use single quotes inside the expression, and vice-versa.
person_dict = {'name': 'Eva', 'role': 'Developer'}
format_string_19 = f"Person's name: {person_dict['name']}, Role: {person_dict['role']}"
print("Example 3.7 (Quotes inside f-string):", format_string_19)

# You can call functions inside f-strings too
def get_status():
    return "Active"
format_string_20 = f"User: {student_name.upper()}, Status: {get_status()}"
print("Example 3.8 (Function call in f-string):", format_string_20)


print("-" * 30)
print("End of String Formatting examples.")