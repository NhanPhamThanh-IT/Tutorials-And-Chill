# --- List Basics in Python ---

# 1. Creating Lists
# ------------------
# A list is an ordered collection of items. Items can be of different types.
# Lists are created using square brackets [].

# Empty list
empty_list = []
print(f"1a. Empty list: {empty_list}")

# List of integers
numbers = [1, 2, 3, 4, 5]
print(f"1b. List of numbers: {numbers}")

# List of strings
fruits = ["apple", "banana", "cherry"]
print(f"1c. List of strings: {fruits}")

# List with mixed data types
mixed_list = [1, "hello", 3.14, True]
print(f"1d. List with mixed types: {mixed_list}")

# 2. Accessing Elements
# ---------------------
# You can access list elements using their index.
# Python uses 0-based indexing (the first element is at index 0).
# Negative indexing starts from the end (-1 is the last element).

print(f"\n--- Accessing Elements ---")
print(f"2a. First fruit: {fruits[0]}")  # Output: apple
print(f"2b. Second number: {numbers[1]}") # Output: 2
print(f"2c. Last fruit (using negative index): {fruits[-1]}") # Output: cherry
print(f"2d. Second to last fruit: {fruits[-2]}") # Output: banana

# Trying to access an index outside the list range will cause an IndexError
# print(fruits[3]) # This would cause an error

# 3. Slicing Lists
# ----------------
# Slicing allows you to get a sub-list (a portion) of the list.
# Syntax: list[start:stop:step]
# - start: Index to start the slice (inclusive, default is 0)
# - stop: Index to end the slice (exclusive, default is the end of the list)
# - step: The interval between elements (default is 1)

print(f"\n--- Slicing Lists ---")
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(f"Original numbers list: {numbers}")

# Get elements from index 2 up to (but not including) index 5
print(f"3a. Slice [2:5]: {numbers[2:5]}") # Output: [2, 3, 4]

# Get elements from the beginning up to index 3
print(f"3b. Slice [:3]: {numbers[:3]}") # Output: [0, 1, 2]

# Get elements from index 5 to the end
print(f"3c. Slice [5:]: {numbers[5:]}") # Output: [5, 6, 7, 8, 9]

# Get a copy of the entire list
print(f"3d. Slice [:]: {numbers[:]}") # Output: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Get every second element
print(f"3e. Slice [::2]: {numbers[::2]}") # Output: [0, 2, 4, 6, 8]

# Get elements from index 1 to 7, taking every second element
print(f"3f. Slice [1:8:2]: {numbers[1:8:2]}") # Output: [1, 3, 5, 7]

# Get elements in reverse order
print(f"3g. Slice [::-1]: {numbers[::-1]}") # Output: [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

# 4. Modifying Lists
# ------------------
# Lists are mutable, meaning you can change their content after creation.

print(f"\n--- Modifying Lists ---")
colors = ["red", "green", "blue"]
print(f"Original colors: {colors}")

# Change an element at a specific index
colors[1] = "yellow"
print(f"4a. Changed element at index 1: {colors}") # Output: ['red', 'yellow', 'blue']

# Add an element to the end: append()
colors.append("purple")
print(f"4b. Appended 'purple': {colors}") # Output: ['red', 'yellow', 'blue', 'purple']

# Insert an element at a specific index: insert()
colors.insert(1, "orange") # Insert 'orange' at index 1
print(f"4c. Inserted 'orange' at index 1: {colors}") # Output: ['red', 'orange', 'yellow', 'blue', 'purple']

# Add all elements from another list (or iterable) to the end: extend()
more_colors = ["black", "white"]
colors.extend(more_colors)
print(f"4d. Extended with {more_colors}: {colors}") # Output: ['red', 'orange', 'yellow', 'blue', 'purple', 'black', 'white']

# Remove the first occurrence of a specific value: remove()
colors.remove("yellow")
print(f"4e. Removed 'yellow': {colors}") # Output: ['red', 'orange', 'blue', 'purple', 'black', 'white']
# colors.remove("pink") # This would cause a ValueError if 'pink' is not in the list

# Remove an element at a specific index and return it: pop()
# If no index is specified, it removes and returns the last item.
last_color = colors.pop()
print(f"4f. Popped last element ('{last_color}'): {colors}") # Output: ['red', 'orange', 'blue', 'purple', 'black']
color_at_index_1 = colors.pop(1)
print(f"4g. Popped element at index 1 ('{color_at_index_1}'): {colors}") # Output: ['red', 'blue', 'purple', 'black']

# Remove an element at a specific index (or slice) using del statement
del colors[0]
print(f"4h. Deleted element at index 0: {colors}") # Output: ['blue', 'purple', 'black']
numbers_to_del = [0, 1, 2, 3, 4, 5]
del numbers_to_del[1:4] # Delete elements from index 1 up to 4
print(f"4i. Deleted slice [1:4] from [0, 1, 2, 3, 4, 5]: {numbers_to_del}") # Output: [0, 4, 5]

# Remove all elements from the list: clear()
colors.clear()
print(f"4j. Cleared the list: {colors}") # Output: []

# 5. List Methods
# ---------------
# Python provides several built-in methods for lists.

print(f"\n--- List Methods ---")
numbers = [3, 1, 4, 1, 5, 9, 2, 6]
print(f"Original numbers list: {numbers}")

# Get the number of elements: len() (this is a function, not a method)
print(f"5a. Length of the list: {len(numbers)}") # Output: 8

# Sort the list in ascending order (modifies the original list): sort()
numbers.sort()
print(f"5b. Sorted list (ascending): {numbers}") # Output: [1, 1, 2, 3, 4, 5, 6, 9]

# Sort the list in descending order: sort(reverse=True)
numbers.sort(reverse=True)
print(f"5c. Sorted list (descending): {numbers}") # Output: [9, 6, 5, 4, 3, 2, 1, 1]

# Reverse the order of elements (modifies the original list): reverse()
numbers.reverse()
print(f"5d. Reversed list: {numbers}") # Output: [1, 1, 2, 3, 4, 5, 6, 9]

# Count the number of occurrences of a value: count()
count_of_1 = numbers.count(1)
print(f"5e. Count of '1' in the list: {count_of_1}") # Output: 2

# Find the index of the first occurrence of a value: index()
index_of_5 = numbers.index(5)
print(f"5f. Index of first '5': {index_of_5}") # Output: 5
# numbers.index(10) # This would cause a ValueError if 10 is not in the list

# Create a shallow copy of the list: copy()
numbers_copy = numbers.copy()
print(f"5g. Original list: {numbers}")
print(f"5h. Copied list: {numbers_copy}")
# Modifying the copy doesn't affect the original
numbers_copy.append(100)
print(f"5i. Original list after modifying copy: {numbers}")
print(f"5j. Copied list after appending 100: {numbers_copy}")

# Note: Assigning a list just creates another reference, not a copy
numbers_ref = numbers
numbers_ref.append(200)
print(f"5k. Original list after modifying reference: {numbers}") # Original is changed!
print(f"5l. Reference list after appending 200: {numbers_ref}")

# 6. List Operations
# ------------------

print(f"\n--- List Operations ---")
list1 = [1, 2, 3]
list2 = [4, 5, 6]

# Concatenation (+): Creates a new list by joining two lists
concatenated_list = list1 + list2
print(f"6a. Concatenated list ({list1} + {list2}): {concatenated_list}")

# Repetition (*): Creates a new list by repeating elements
repeated_list = list1 * 3
print(f"6b. Repeated list ({list1} * 3): {repeated_list}")

# 7. Checking Membership
# ----------------------
# Use 'in' and 'not in' to check if an element exists in a list.

print(f"\n--- Checking Membership ---")
fruits = ["apple", "banana", "cherry"]
print(f"Fruits list: {fruits}")

print(f"7a. Is 'banana' in fruits? {'banana' in fruits}")     # Output: True
print(f"7b. Is 'grape' in fruits? {'grape' in fruits}")       # Output: False
print(f"7c. Is 'apple' not in fruits? {'apple' not in fruits}") # Output: False
print(f"7d. Is 'orange' not in fruits? {'orange' not in fruits}")# Output: True

# 8. Iterating Through Lists
# --------------------------
# Use a for loop to go through each element in the list.

print(f"\n--- Iterating Through Lists ---")
print("Printing fruits:")
for fruit in fruits:
    print(f"- {fruit}")

# You can also iterate using index and range()
print("\nPrinting fruits with index:")
for i in range(len(fruits)):
    print(f"- Index {i}: {fruits[i]}")

# Using enumerate to get both index and value
print("\nPrinting fruits with enumerate:")
for index, fruit in enumerate(fruits):
    print(f"- Index {index}: {fruit}")

# 9. List Comprehensions
# ----------------------
# A concise way to create lists based on existing lists or iterables.
# Syntax: [expression for item in iterable if condition]

print(f"\n--- List Comprehensions ---")
numbers = [1, 2, 3, 4, 5, 6]
print(f"Original numbers: {numbers}")

# Create a list of squares for each number
squares = [x**2 for x in numbers]
print(f"9a. Squares: {squares}") # Output: [1, 4, 9, 16, 25, 36]

# Create a list of even numbers from the original list
even_numbers = [x for x in numbers if x % 2 == 0]
print(f"9b. Even numbers: {even_numbers}") # Output: [2, 4, 6]

# Create a list of uppercase fruits
fruits = ["apple", "banana", "cherry"]
uppercase_fruits = [fruit.upper() for fruit in fruits]
print(f"9c. Uppercase fruits: {uppercase_fruits}") # Output: ['APPLE', 'BANANA', 'CHERRY']

print("\n--- End of List Examples ---")