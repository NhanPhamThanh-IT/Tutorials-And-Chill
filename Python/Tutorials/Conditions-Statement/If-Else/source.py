# --- Basic If Statement ---
print("--- Basic If ---")
temperature = 30
# Check if the temperature is greater than 25
if temperature > 25:
    # This block executes only if the condition is True
    print(f"Temperature ({temperature}°C) is greater than 25°C. It's warm!")
# This line executes regardless, as it's outside the if block
print("Weather check complete.")
print("-" * 20) # Separator

# --- Basic If-Else Statement ---
print("--- Basic If-Else ---")
age = 17
# Check if age is 18 or greater
if age >= 18:
    # This block runs if age is 18 or more
    print(f"Age {age}: You are eligible to vote.")
else:
    # This block runs if age is less than 18
    print(f"Age {age}: You are not eligible to vote yet.")
print("-" * 20)

# --- Nested If-Else Statement ---
print("--- Nested If-Else ---")
number = 10
print(f"Checking number: {number}")
# First level check: is the number positive?
if number > 0:
    print("Number is positive.")
    # Second level check (nested): is the positive number even?
    if number % 2 == 0:
        # This runs if number > 0 AND number is even
        print("And it's an even number.")
    else:
        # This runs if number > 0 AND number is odd
        print("And it's an odd number.")
elif number == 0:
     print("Number is zero.")
else:
    # This runs if number is not positive (i.e., negative)
    print("Number is negative.")
print("-" * 20)

# --- If-Elif-Else Statement (Chain) ---
print("--- If-Elif-Else ---")
marks = 72
print(f"Marks obtained: {marks}")
# Check grades based on marks
if marks >= 90:
    grade = "A"
elif marks >= 75: # Checked only if marks < 90
    grade = "B"
elif marks >= 60: # Checked only if marks < 75
    grade = "C"
elif marks >= 40: # Checked only if marks < 60
    grade = "D"
else: # Runs only if marks < 40
    grade = "F"
print(f"Calculated Grade: {grade}")
print("-" * 20)

# --- Logical Operators (and, or, not) ---
print("--- Logical Operators ---")
user_age = 25
has_permission = False
print(f"User Age: {user_age}, Has Permission: {has_permission}")

# Example using 'and'
if user_age >= 18 and has_permission:
    print("Access granted (using 'and').")
else:
    print("Access denied (using 'and'). Needs to be >= 18 AND have permission.")

# Example using 'or'
if user_age >= 65 or has_permission:
    print("Eligible for discount or special access (using 'or').")
else:
    print("Not eligible for discount or special access (using 'or'). Needs to be >= 65 OR have permission.")

# Example using 'not'
if not has_permission:
    print("User does NOT have permission (using 'not').")
else:
    print("User HAS permission (using 'not').")
print("-" * 20)

# --- Truthy and Falsy Values ---
print("--- Truthy/Falsy ---")
empty_string = ""
non_empty_string = "Hello"
zero_number = 0
non_zero_number = 10
empty_list = []
non_empty_list = [1, 2]
none_value = None

print(f"Checking empty string ('{empty_string}'):")
if empty_string: # Evaluates to False
    print("  String is truthy.")
else:
    print("  String is falsy.")

print(f"Checking non-empty string ('{non_empty_string}'):")
if non_empty_string: # Evaluates to True
    print("  String is truthy.")
else:
    print("  String is falsy.")

print(f"Checking zero number ({zero_number}):")
if zero_number: # Evaluates to False
    print("  Number is truthy.")
else:
    print("  Number is falsy.")

print(f"Checking non-zero number ({non_zero_number}):")
if non_zero_number: # Evaluates to True
    print("  Number is truthy.")
else:
    print("  Number is falsy.")

print(f"Checking empty list ({empty_list}):")
if empty_list: # Evaluates to False
    print("  List is truthy.")
else:
    print("  List is falsy.")

print(f"Checking non-empty list ({non_empty_list}):")
if non_empty_list: # Evaluates to True
    print("  List is truthy.")
else:
    print("  List is falsy.")

print(f"Checking None value ({none_value}):")
if none_value: # Evaluates to False
    print("  None is truthy.")
else:
    print("  None is falsy.")
print("-" * 20)

# --- Ternary Conditional Operator ---
print("--- Ternary Operator ---")
check_age = 22
# Assign 'Adult' if check_age >= 18, otherwise assign 'Minor'
status = "Adult" if check_age >= 18 else "Minor"
print(f"Age {check_age} is considered: {status}")

check_num = 7
# Assign 'Even' if check_num is divisible by 2, otherwise assign 'Odd'
parity = "Even" if check_num % 2 == 0 else "Odd"
print(f"Number {check_num} is: {parity}")
print("-" * 20)


# --- Practice Problems Examples ---
print("--- Practice Problems ---")

# 1. Positive, Negative, or Zero
num_check = -5
print(f"Checking number {num_check}:")
if num_check > 0:
    print("  Positive.")
elif num_check == 0:
    print("  Zero.")
else:
    print("  Negative.")

# 2. Leap Year
year = 2024
print(f"Checking year {year}:")
# A year is a leap year if:
# - it is divisible by 4 AND not divisible by 100
# - OR it is divisible by 400
is_leap = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
if is_leap:
    print(f"  {year} is a leap year.")
else:
    print(f"  {year} is not a leap year.")

# 3. Largest of Three
a, b, c = 15, 8, 22
print(f"Finding largest among {a}, {b}, {c}:")
if a >= b and a >= c:
    largest = a
elif b >= a and b >= c: # Technically only need b >= c here, as a >= b was false
    largest = b
else:
    largest = c
print(f"  The largest number is {largest}.")

# 4. Username Check (Truthy/Falsy)
username = "" # Try also with "Bob"
print(f"Checking username: '{username}'")
if username: # Checks if the string is not empty (truthy)
    print(f"  Welcome, {username}!")
else: # Runs if the string is empty (falsy)
    print("  Username cannot be empty.")

# 5. Even/Odd with Ternary
number_to_test = 9
print(f"Checking parity of {number_to_test} using ternary:")
result = "Even" if number_to_test % 2 == 0 else "Odd"
print(f"  The number {number_to_test} is {result}.")

print("-" * 20)
print("End of examples.")
