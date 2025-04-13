# --- For Loops in Python ---

# A 'for' loop is used for iterating over a sequence (that is either a list,
# a tuple, a dictionary, a set, or a string) or other iterable object.
# This is less like the 'for' keyword in other programming languages, and
# works more like an iterator method as found in other object-orientated
# programming languages.

# --- 1. Iterating over Sequences ---

# Example 1.1: Iterating over a list
print("--- Iterating over a list ---")
fruits = ["apple", "banana", "cherry"]
print("Fruits list:", fruits)
for fruit in fruits:
    print(f"Current fruit: {fruit}")
print("-" * 20) # Separator

# Example 1.2: Iterating over a tuple
print("--- Iterating over a tuple ---")
colors = ("red", "green", "blue")
print("Colors tuple:", colors)
for color in colors:
    print(f"Current color: {color}")
print("-" * 20)

# Example 1.3: Iterating over a string
print("--- Iterating over a string ---")
message = "Hello"
print("Message string:", message)
for char in message:
    print(f"Current character: {char}")
print("-" * 20)

# --- 2. Using the range() function ---

# The range() function returns a sequence of numbers, starting from 0 by default,
# and increments by 1 (by default), and stops before a specified number.

# Example 2.1: range(stop) - Iterate from 0 up to (but not including) stop
print("--- Using range(stop) ---")
print("Numbers from 0 to 4:")
for i in range(5): # Generates numbers 0, 1, 2, 3, 4
    print(f"Current number: {i}")
print("-" * 20)

# Example 2.2: range(start, stop) - Iterate from start up to (but not including) stop
print("--- Using range(start, stop) ---")
print("Numbers from 2 to 5:")
for i in range(2, 6): # Generates numbers 2, 3, 4, 5
    print(f"Current number: {i}")
print("-" * 20)

# Example 2.3: range(start, stop, step) - Iterate from start up to stop, incrementing by step
print("--- Using range(start, stop, step) ---")
print("Even numbers from 0 to 10:")
for i in range(0, 11, 2): # Generates 0, 2, 4, 6, 8, 10
    print(f"Current number: {i}")
print("Numbers from 5 down to 1:")
for i in range(5, 0, -1): # Generates 5, 4, 3, 2, 1
    print(f"Current number: {i}")
print("-" * 20)

# --- 3. Iterating over Dictionaries ---

# When iterating over a dictionary, you can loop through its keys, values, or key-value pairs.

my_dict = {"name": "Alice", "age": 30, "city": "New York"}
print("--- Iterating over a dictionary ---")
print("Dictionary:", my_dict)

# Example 3.1: Iterating over keys (default behavior)
print("\nIterating over keys:")
for key in my_dict:
    print(f"Key: {key}, Value: {my_dict[key]}") # Access value using the key

# Example 3.2: Iterating over values using .values()
print("\nIterating over values:")
for value in my_dict.values():
    print(f"Value: {value}")

# Example 3.3: Iterating over key-value pairs using .items()
print("\nIterating over key-value pairs:")
for key, value in my_dict.items():
    print(f"Key: {key}, Value: {value}")
print("-" * 20)

# --- 4. Using enumerate() ---

# Sometimes you need both the index and the item while iterating.
# enumerate() adds a counter to an iterable and returns it as an enumerate object.

print("--- Using enumerate() ---")
animals = ["dog", "cat", "mouse"]
print("Animals list:", animals)
for index, animal in enumerate(animals):
    print(f"Index: {index}, Animal: {animal}")

# You can also specify a starting index for enumerate
print("\nUsing enumerate() with start=1:")
for index, animal in enumerate(animals, start=1):
    print(f"Position: {index}, Animal: {animal}")
print("-" * 20)

# --- 5. Using zip() ---

# zip() is used to iterate over two or more sequences at the same time.
# It pairs up the corresponding elements from each sequence.
# The iteration stops when the shortest sequence is exhausted.

print("--- Using zip() ---")
names = ["Alice", "Bob", "Charlie"]
scores = [85, 92, 78]
cities = ["London", "Paris", "Tokyo", "Berlin"] # Berlin will be ignored

print("Names:", names)
print("Scores:", scores)
print("Cities:", cities)

print("\nPairing names and scores:")
for name, score in zip(names, scores):
    print(f"Name: {name}, Score: {score}")

print("\nPairing names, scores, and cities:")
for name, score, city in zip(names, scores, cities):
    print(f"Name: {name}, Score: {score}, City: {city}")
print("-" * 20)

# --- 6. The 'break' statement ---

# The 'break' statement is used to exit a loop prematurely, regardless
# of whether the loop condition is still true or if there are more items
# to iterate over.

print("--- Using 'break' ---")
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Numbers list:", numbers)
print("Looping until the number 5 is found:")
for num in numbers:
    print(f"Checking number: {num}")
    if num == 5:
        print("Found 5! Breaking the loop.")
        break # Exit the loop immediately
print("Loop finished.")
print("-" * 20)

# --- 7. The 'continue' statement ---

# The 'continue' statement is used to skip the rest of the code inside
# the current iteration of the loop and proceed to the next iteration.

print("--- Using 'continue' ---")
print("Printing only odd numbers from the list:", numbers)
for num in numbers:
    if num % 2 == 0: # Check if the number is even
        continue # Skip the rest of this iteration if even
    print(f"Odd number found: {num}") # This line is skipped for even numbers
print("Loop finished.")
print("-" * 20)

# --- 8. The 'else' clause in a 'for' loop ---

# Python's 'for' loops can have an optional 'else' block.
# The 'else' block is executed only if the loop completes its iterations
# without being terminated by a 'break' statement.

print("--- Using 'else' with 'for' ---")

# Example 8.1: Loop completes normally
print("\nScenario 1: Loop completes without break")
search_list = [1, 3, 7, 9]
value_to_find = 5
print(f"Searching for {value_to_find} in {search_list}")
for item in search_list:
    print(f"Checking {item}...")
    if item == value_to_find:
        print(f"Found {value_to_find}!")
        break
else:
    # This block executes because the loop finished without finding 'value_to_find'
    print(f"{value_to_find} was not found in the list.")

# Example 8.2: Loop is terminated by break
print("\nScenario 2: Loop terminates with break")
search_list = [1, 3, 5, 7, 9]
value_to_find = 5
print(f"Searching for {value_to_find} in {search_list}")
for item in search_list:
    print(f"Checking {item}...")
    if item == value_to_find:
        print(f"Found {value_to_find}!")
        break # The loop terminates here
else:
    # This block does NOT execute because the loop was broken
    print(f"{value_to_find} was not found in the list.")
print("-" * 20)

# --- 9. Nested Loops ---

# You can use one or more loops inside another loop. This is called nesting.

print("--- Nested Loops ---")
print("Example: Printing coordinates (x, y)")
for x in range(3): # Outer loop (0, 1, 2)
    for y in range(2): # Inner loop (0, 1)
        print(f"  (x={x}, y={y})")
    print(f"Finished inner loop for x={x}") # Executes after each inner loop completes
print("Finished outer loop.")
print("-" * 20)

# Example: Generating a multiplication table
print("\nExample: Multiplication Table (up to 3x3)")
for i in range(1, 4): # Rows (1, 2, 3)
    for j in range(1, 4): # Columns (1, 2, 3)
        # print() has an 'end' parameter to control what's printed at the end.
        # Default is '\n' (newline). We use '\t' (tab) for spacing.
        print(f"{i}*{j}={i*j}", end="\t")
    print() # Print a newline after each row is complete
print("-" * 20)

print("For loop examples complete.")