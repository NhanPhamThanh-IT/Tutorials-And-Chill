# While Loops in Python

# A while loop repeatedly executes a block of code as long as a given condition is True.

# --- Basic While Loop ---
# This loop prints numbers from 0 up to (but not including) 5.
print("--- Basic While Loop ---")
count = 0
while count < 5:
    print(f"Count is: {count}")
    count = count + 1  # Increment count by 1 in each iteration
    # This is crucial! Without changing the variable used in the condition,
    # the loop might run forever (infinite loop).

print("Loop finished.\n")

# --- Using 'break' to exit a loop ---
# Sometimes you need to exit the loop early, even if the condition is still True.
# The 'break' statement terminates the current loop.
print("--- Using 'break' ---")
number = 0
while True:  # This condition is always True, creating an infinite loop potential
    print(f"Checking number: {number}")
    if number >= 3:
        print("Number is 3 or greater, breaking the loop.")
        break  # Exit the loop immediately
    number += 1 # Increment number

print("Loop broken.\n")

# --- Using 'continue' to skip an iteration ---
# The 'continue' statement skips the rest of the code inside the current
# iteration and proceeds to the next iteration of the loop.
print("--- Using 'continue' ---")
value = 0
while value < 5:
    value += 1
    if value == 3:
        print("Value is 3, skipping this iteration.")
        continue  # Skip the print statement below for this iteration
    print(f"Current value: {value}")

print("Loop finished.\n")

# --- While loop with an 'else' block ---
# The 'else' block associated with a while loop executes only if the loop
# completes normally (i.e., the condition becomes False).
# It does *not* execute if the loop is terminated by a 'break' statement.
print("--- While loop with 'else' ---")

# Example 1: Loop finishes normally
attempts = 0
while attempts < 3:
    print(f"Attempt {attempts + 1}")
    attempts += 1
else:
    # This will be executed because the loop condition (attempts < 3) eventually becomes False.
    print("Else block executed: Loop completed all attempts.")

print("-" * 10)

# Example 2: Loop terminated by 'break'
attempts_with_break = 0
while attempts_with_break < 3:
    print(f"Attempt {attempts_with_break + 1}")
    if attempts_with_break == 1:
        print("Breaking the loop early.")
        break # Exit the loop
    attempts_with_break += 1
else:
    # This will *not* be executed because the loop was terminated by 'break'.
    print("Else block executed: Loop completed all attempts.")

print("Loop finished.\n")


# --- Practical Example: Input validation ---
# Keep asking the user for input until they provide a positive number.
print("--- Input Validation Example ---")
user_input = ""
while not user_input.isdigit() or int(user_input) <= 0:
    user_input = input("Please enter a positive number: ")
    if not user_input.isdigit():
        print("That's not a valid number.")
    elif int(user_input) <= 0:
        print("The number must be positive.")

# The loop only exits when user_input contains digits AND represents a number > 0
positive_number = int(user_input)
print(f"Thank you! You entered the positive number: {positive_number}")
print("Input validation finished.\n")

# --- Common Pitfalls ---
# 1. Infinite Loops: Forgetting to update the variable in the condition.
#    Example (don't run this without knowing how to stop it - usually Ctrl+C):
#    i = 0
#    while i < 5:
#        print("This will run forever!")
#        # Missing i = i + 1

# 2. Off-by-one errors: Getting the condition slightly wrong (e.g., < vs <=).
#    Carefully consider whether the boundary value should be included.