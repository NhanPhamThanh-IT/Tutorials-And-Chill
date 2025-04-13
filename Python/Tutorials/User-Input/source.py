# --- User Input in Python ---

# The `input()` function is used to get input from the user via the console.
# It always returns the user's input as a string.

# 1. Basic Input:
#    When you call `input()`, the program pauses and waits for the user to type something
#    and press Enter.
print("Example 1: Basic Input")
user_text = input()
print("You entered:", user_text)
print("The type of the input is:", type(user_text)) # This will always show <class 'str'>
print("-" * 20)

# 2. Input with a Prompt:
#    It's good practice to provide a message (a "prompt") to the user,
#    telling them what kind of input you expect. You pass this message as an
#    argument to the `input()` function.
print("Example 2: Input with a Prompt")
user_name = input("Please enter your name: ")
print("Hello,", user_name + "!")
print("-" * 20)

# 3. Input is Always a String:
#    Even if the user types numbers, `input()` returns them as a string.
print("Example 3: Input is Always a String")
user_number_str = input("Enter a number: ")
print("You entered:", user_number_str)
print("Type of input:", type(user_number_str))

# If you try to do math directly with the input string, you might get an error
# or unexpected behavior (like string concatenation instead of addition).
# For example, uncommenting the next line would likely cause an error:
# result = user_number_str + 5
# print(result)

# Concatenation example:
print("Adding '5' as a string:", user_number_str + "5") # Joins the strings
print("-" * 20)

# 4. Converting Input Types (Type Casting):
#    To use the user's input as a number (integer, float, etc.), you need to
#    convert it from a string to the desired numeric type using functions like
#    `int()` or `float()`.

print("Example 4: Converting Input to Integer")
age_str = input("Enter your age: ")
try:
    # Attempt to convert the input string to an integer
    age_int = int(age_str)
    print("Your age is:", age_int)
    print("Type after conversion:", type(age_int))
    # Now you can perform calculations
    next_year_age = age_int + 1
    print("Next year, you will be:", next_year_age)
except ValueError:
    # Handle the case where the user enters something that cannot be converted to an integer
    print(f"Error: '{age_str}' is not a valid whole number.")
print("-" * 20)


print("Example 5: Converting Input to Float")
price_str = input("Enter the price of an item: ")
try:
    # Attempt to convert the input string to a floating-point number
    price_float = float(price_str)
    print("The price is:", price_float)
    print("Type after conversion:", type(price_float))
    # Now you can perform calculations
    price_with_tax = price_float * 1.1 # Example: adding 10% tax
    print(f"Price with 10% tax: {price_with_tax:.2f}") # Format to 2 decimal places
except ValueError:
    # Handle the case where the user enters something that cannot be converted to a float
    print(f"Error: '{price_str}' is not a valid number.")
print("-" * 20)

# 5. Combining Input and Conversion in One Step:
#    You can often wrap the `input()` call directly within the conversion function.
print("Example 6: Combined Input and Conversion")
try:
    quantity = int(input("Enter the quantity: "))
    print("Quantity entered:", quantity)
    print("Type:", type(quantity))
    # Use the integer directly
    total_cost = price_float * quantity # Assuming price_float is still valid from Example 5
    print(f"Total cost for {quantity} items: {total_cost:.2f}")
except NameError:
    print("Cannot calculate total cost because price was not entered correctly earlier.")
except ValueError:
    print("Error: Please enter a valid whole number for the quantity.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
print("-" * 20)

print("End of User Input examples.")