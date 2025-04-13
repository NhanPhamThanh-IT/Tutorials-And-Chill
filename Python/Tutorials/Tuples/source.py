# --- Tuples in Python ---
# A tuple is a collection of items that are ordered and *immutable*.
# Immutable means that once a tuple is created, you cannot change, add, or remove items.
# Tuples are often used to store related pieces of information together.
# They are defined using parentheses ().

# --- 1. Creating Tuples ---

# Method 1: Using parentheses ()
# You can put different data types in a tuple.
my_tuple = (1, 2, 3, "hello", True, 3.14)
print("1a. Created tuple using ():", my_tuple)
print("1a. The type is:", type(my_tuple))

# Method 2: Using the tuple() constructor
# You can convert other iterable objects (like lists) into tuples.
my_list = [4, 5, 6, "world"]
tuple_from_list = tuple(my_list)
print("1b. Created tuple from list:", tuple_from_list)
print("1b. The type is:", type(tuple_from_list))

# Method 3: Creating an empty tuple
empty_tuple = ()
print("1c. An empty tuple:", empty_tuple)
print("1c. Length of empty tuple:", len(empty_tuple))

# Method 4: Creating a tuple with a single element
# IMPORTANT: You need a comma after the element, otherwise Python won't recognize it as a tuple.
single_item_tuple = (42,) # Note the comma!
not_a_tuple = (42)      # This is just the integer 42 inside parentheses
print("1d. Single item tuple:", single_item_tuple)
print("1d. Type:", type(single_item_tuple))
print("1e. This is NOT a tuple:", not_a_tuple)
print("1e. Type:", type(not_a_tuple))

# Parentheses are sometimes optional when defining tuples (tuple packing)
packed_tuple = 10, 20, "packed" # Python understands this as a tuple
print("1f. Packed tuple (optional parentheses):", packed_tuple)
print("1f. Type:", type(packed_tuple))

print("-" * 30)

# --- 2. Accessing Tuple Elements ---
# You access elements using their index, starting from 0.
fruits = ("apple", "banana", "cherry", "date", "elderberry")
print("2a. Fruits tuple:", fruits)

# Get the first element (index 0)
first_fruit = fruits[0]
print("2b. First fruit (index 0):", first_fruit)

# Get the third element (index 2)
third_fruit = fruits[2]
print("2c. Third fruit (index 2):", third_fruit)

# Negative indexing: Access elements from the end (-1 is the last element)
last_fruit = fruits[-1]
print("2d. Last fruit (index -1):", last_fruit)

second_last_fruit = fruits[-2]
print("2e. Second last fruit (index -2):", second_last_fruit)

# Trying to access an index outside the tuple's range will cause an IndexError
# print(fruits[10]) # Uncommenting this line would cause an error

print("-" * 30)

# --- 3. Slicing Tuples ---
# Slicing allows you to get a sub-section (a new tuple) from the original tuple.
# Syntax: tuple[start:stop:step]
# start: The index to start the slice (inclusive). Defaults to 0.
# stop: The index to end the slice (exclusive). Defaults to the end of the tuple.
# step: The amount to jump between elements. Defaults to 1.
numbers = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
print("3a. Numbers tuple:", numbers)

# Get elements from index 2 up to (but not including) index 5
slice1 = numbers[2:5]
print("3b. Slice [2:5]:", slice1) # Output: (2, 3, 4)

# Get elements from the beginning up to (but not including) index 4
slice2 = numbers[:4]
print("3c. Slice [:4]:", slice2) # Output: (0, 1, 2, 3)

# Get elements from index 6 to the end
slice3 = numbers[6:]
print("3d. Slice [6:]:", slice3) # Output: (6, 7, 8, 9)

# Get every second element
slice4 = numbers[::2]
print("3e. Slice [::2] (every second element):", slice4) # Output: (0, 2, 4, 6, 8)

# Get a reversed copy of the tuple
reversed_tuple = numbers[::-1]
print("3f. Slice [::-1] (reversed):", reversed_tuple)

print("-" * 30)

# --- 4. Immutability of Tuples ---
# This is a key characteristic: you CANNOT change a tuple after it's created.
immutable_tuple = (10, 20, 30)
print("4a. Original tuple:", immutable_tuple)

# Attempting to change an element will result in a TypeError
try:
    immutable_tuple[0] = 100 # This line will cause an error
except TypeError as e:
    print(f"4b. Error when trying to change element: {e}")

# You also cannot add or remove elements directly.
# Methods like append() or remove() (found in lists) do not exist for tuples.

# However, you can create *new* tuples based on existing ones.
new_tuple_from_old = immutable_tuple + (40, 50) # Concatenation creates a new tuple
print("4c. New tuple created by adding (40, 50):", new_tuple_from_old)
print("4d. Original tuple remains unchanged:", immutable_tuple)

print("-" * 30)

# --- 5. Tuple Packing and Unpacking ---

# Packing: Combining multiple values into one tuple (we saw this in creation).
student = "Alice", 22, "Computer Science" # Packing values into the 'student' tuple
print("5a. Packed tuple (student):", student)

# Unpacking: Assigning the elements of a tuple to individual variables.
# The number of variables on the left must match the number of elements in the tuple.
name, age, major = student # Unpacking the 'student' tuple
print("5b. Unpacked values:")
print("   Name:", name)
print("   Age:", age)
print("   Major:", major)

# Using '*' to capture multiple items during unpacking
# The variable with '*' will receive a list of the remaining items.
first, second, *remaining_items = (10, 20, 30, 40, 50)
print("5c. Unpacking with *:")
print("   First:", first)
print("   Second:", second)
print("   Remaining items (as a list):", remaining_items)

# A common use case for unpacking: swapping variable values easily
a = 5
b = 10
print(f"5d. Before swap: a = {a}, b = {b}")
a, b = b, a # Tuple packing and unpacking in one step!
print(f"5e. After swap: a = {a}, b = {b}")

print("-" * 30)

# --- 6. Tuple Methods ---
# Tuples have very few built-in methods because they are immutable.
# The two main methods are count() and index().

data_tuple = (1, 2, 'a', 'b', 2, 'a', 2, 3, 'a')
print("6a. Data tuple:", data_tuple)

# count(value): Returns the number of times 'value' appears in the tuple.
count_of_2 = data_tuple.count(2)
print(f"6b. Count of '2': {count_of_2}")

count_of_a = data_tuple.count('a')
print(f"6c. Count of 'a': {count_of_a}")

count_of_z = data_tuple.count('z') # Value not in the tuple
print(f"6d. Count of 'z': {count_of_z}")

# index(value): Returns the index of the *first* occurrence of 'value'.
# If the value is not found, it raises a ValueError.
index_of_b = data_tuple.index('b')
print(f"6e. Index of first 'b': {index_of_b}")

index_of_first_2 = data_tuple.index(2)
print(f"6f. Index of first '2': {index_of_first_2}")

# Trying to find the index of a value not present will cause an error
try:
    index_of_z = data_tuple.index('z')
except ValueError as e:
    print(f"6g. Error finding index of 'z': {e}")

print("-" * 30)

# --- 7. Tuple Concatenation and Repetition ---

tuple1 = (1, 2, 3)
tuple2 = ('x', 'y', 'z')
print("7a. Tuple 1:", tuple1)
print("7b. Tuple 2:", tuple2)

# Concatenation (+): Creates a *new* tuple by joining two or more tuples.
combined_tuple = tuple1 + tuple2
print("7c. Concatenated tuple (tuple1 + tuple2):", combined_tuple)

# Repetition (*): Creates a *new* tuple by repeating the elements of a tuple.
repeated_tuple = tuple1 * 3
print("7d. Repeated tuple (tuple1 * 3):", repeated_tuple)

print("-" * 30)

# --- 8. Checking Membership (in / not in) ---
# You can check if an item exists within a tuple.

elements = ("red", 100, False, None)
print("8a. Elements tuple:", elements)

# Check using 'in'
is_red_present = "red" in elements
print(f"8b. Is 'red' in elements? {is_red_present}")

is_99_present = 99 in elements
print(f"8c. Is 99 in elements? {is_99_present}")

# Check using 'not in'
is_blue_absent = "blue" not in elements
print(f"8d. Is 'blue' not in elements? {is_blue_absent}")

is_100_absent = 100 not in elements
print(f"8e. Is 100 not in elements? {is_100_absent}")

print("-" * 30)

# --- 9. Iterating Through a Tuple ---
# You can loop through the items in a tuple using a for loop.

colors = ("cyan", "magenta", "yellow", "black")
print("9a. Colors tuple:", colors)

print("9b. Iterating through colors:")
for color in colors:
    print(f"  - {color}")

# If you need the index as well, use enumerate()
print("9c. Iterating with index using enumerate():")
for index, color in enumerate(colors):
    print(f"  - Index {index}: {color}")

print("-" * 30)

# --- 10. Tuple Length ---
# Use the built-in len() function to find the number of items in a tuple.
coordinates = (10.5, -5.2, 8.0)
print("10a. Coordinates tuple:", coordinates)
length = len(coordinates)
print("10b. Length of coordinates tuple:", length)

print("-" * 30)

# --- 11. Nested Tuples ---
# Tuples can contain other tuples (or other collection types like lists).
person = (
    "John Doe",
    30,
    ("123 Main St", "Anytown", "CA", 12345), # Address tuple
    ["Python", "JavaScript"]                 # List of skills
)
print("11a. Nested tuple (person):", person)

# Accessing nested elements
print("11b. Person's name:", person[0])
print("11c. Person's address tuple:", person[2])
print("11d. Person's city:", person[2][1]) # Access element 1 of the tuple at index 2
print("11e. Person's first skill:", person[3][0]) # Access element 0 of the list at index 3

# Note: Even if a tuple contains a mutable item (like a list), the tuple itself is still immutable.
# You cannot replace the list with something else, but you *can* modify the list *in place*.
print("11f. Original skills list:", person[3])
person[3].append("SQL") # Modifying the list inside the tuple
print("11g. Modified skills list (still inside the tuple):", person[3])
print("11h. The person tuple now looks like this:", person)
# person[3] = ["New Skill"] # This would raise a TypeError because you can't replace the list object

print("-" * 30)

# --- When to Use Tuples vs. Lists ---
# Use Tuples when:
# 1. Data should not change: Coordinates, RGB color values, configuration settings.
# 2. Performance: Tuples can be slightly faster to create and iterate over than lists (in some cases).
# 3. Dictionary Keys: Tuples can be used as keys in dictionaries because they are immutable and hashable. Lists cannot.
# 4. Returning multiple values from functions: It's common practice to return multiple results as a tuple.

# Use Lists when:
# 1. Data needs to change: You need to add, remove, or modify items frequently.
# 2. Order matters and you need modification capabilities.

# Example: Tuple as dictionary key
city_coordinates = {
    ("New York", "USA"): (40.7128, -74.0060),
    ("London", "UK"): (51.5074, -0.1278),
    ("Tokyo", "Japan"): (35.6895, 139.6917),
}
print("12a. Dictionary with tuple keys:", city_coordinates)
print("12b. Coordinates for London, UK:", city_coordinates[("London", "UK")])

print("-" * 30)
print("End of Tuple Examples")