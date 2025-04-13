import array

# Python Arrays (using Lists)
# In Python, the most common way to work with array-like data structures
# is using the built-in `list` type. Lists are ordered, mutable (changeable),
# and can hold items of different data types.

# 1. Creating Lists
# ------------------

# Create an empty list
empty_list = []
print(f"Empty list: {empty_list}")

# Create a list with initial elements (integers)
numbers = [1, 2, 3, 4, 5]
print(f"List of numbers: {numbers}")

# Create a list with mixed data types
mixed_list = [1, "hello", 3.14, True]
print(f"Mixed data type list: {mixed_list}")

# Create a list using the list() constructor
list_from_tuple = list((10, 20, 30)) # Note the double parentheses
print(f"List created from a tuple: {list_from_tuple}")

# 2. Accessing Elements (Indexing)
# ---------------------------------
# List elements are accessed using zero-based indexing.
# The first element is at index 0, the second at index 1, and so on.

fruits = ["apple", "banana", "cherry", "date"]
print(f"\nList of fruits: {fruits}")

# Get the first element (index 0)
first_fruit = fruits[0]
print(f"First fruit (index 0): {first_fruit}") # Output: apple

# Get the third element (index 2)
third_fruit = fruits[2]
print(f"Third fruit (index 2): {third_fruit}") # Output: cherry

# Negative Indexing: Access elements from the end of the list.
# -1 refers to the last element, -2 to the second last, etc.
last_fruit = fruits[-1]
print(f"Last fruit (index -1): {last_fruit}") # Output: date

second_last_fruit = fruits[-2]
print(f"Second last fruit (index -2): {second_last_fruit}") # Output: cherry

# Trying to access an index outside the list range will raise an IndexError
# print(fruits[10]) # This would cause an IndexError

# 3. Slicing Lists
# ----------------
# Slicing allows you to get a sub-list (a portion) of the original list.
# Syntax: list[start:stop:step]
# - start: The index to start the slice (inclusive). Defaults to 0.
# - stop: The index to end the slice (exclusive). Defaults to the end of the list.
# - step: The interval between elements. Defaults to 1.

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(f"\nNumbers list: {numbers}")

# Get elements from index 2 up to (but not including) index 5
sub_list1 = numbers[2:5]
print(f"Slice [2:5]: {sub_list1}") # Output: [2, 3, 4]

# Get elements from the beginning up to index 4 (exclusive)
sub_list2 = numbers[:4]
print(f"Slice [:4]: {sub_list2}") # Output: [0, 1, 2, 3]

# Get elements from index 6 to the end of the list
sub_list3 = numbers[6:]
print(f"Slice [6:]: {sub_list3}") # Output: [6, 7, 8, 9]

# Get every second element from the list
sub_list4 = numbers[::2]
print(f"Slice [::2]: {sub_list4}") # Output: [0, 2, 4, 6, 8]

# Get elements from index 1 to 7 (exclusive) with a step of 3
sub_list5 = numbers[1:7:3]
print(f"Slice [1:7:3]: {sub_list5}") # Output: [1, 4]

# Create a copy of the entire list
list_copy = numbers[:]
print(f"Copy using slice [:]: {list_copy}")

# Reverse the list using slicing
reversed_list = numbers[::-1]
print(f"Reversed list using slice [::-1]: {reversed_list}")

# 4. Modifying List Elements
# --------------------------
# Lists are mutable, meaning you can change their elements after creation.

colors = ["red", "green", "blue"]
print(f"\nOriginal colors list: {colors}")

# Change the element at index 1
colors[1] = "yellow"
print(f"After changing index 1: {colors}") # Output: ['red', 'yellow', 'blue']

# Change a range of elements using slicing
colors[0:2] = ["orange", "purple"] # Replace elements at index 0 and 1
print(f"After changing slice [0:2]: {colors}") # Output: ['orange', 'purple', 'blue']

# You can replace a slice with a list of different length
colors[1:] = ["cyan", "magenta", "black"] # Replace from index 1 onwards
print(f"After replacing slice [1:] with more elements: {colors}")

# 5. Adding Elements to a List
# ----------------------------

# append(): Adds a single element to the end of the list.
pets = ["dog", "cat"]
print(f"\nInitial pets list: {pets}")
pets.append("hamster")
print(f"After append('hamster'): {pets}") # Output: ['dog', 'cat', 'hamster']

# insert(): Inserts an element at a specific index.
# pets.insert(index, element)
pets.insert(1, "parrot") # Insert "parrot" at index 1
print(f"After insert(1, 'parrot'): {pets}") # Output: ['dog', 'parrot', 'cat', 'hamster']

# extend(): Adds all elements from another iterable (like a list, tuple)
#           to the end of the current list.
more_pets = ["fish", "turtle"]
pets.extend(more_pets)
print(f"After extend(['fish', 'turtle']): {pets}")
# Output: ['dog', 'parrot', 'cat', 'hamster', 'fish', 'turtle']

# You can also use the + operator to concatenate lists (creates a new list)
list1 = [1, 2]
list2 = [3, 4]
combined_list = list1 + list2
print(f"Combined list using +: {combined_list}") # Output: [1, 2, 3, 4]
print(f"Original list1 remains unchanged: {list1}") # Output: [1, 2]

# 6. Removing Elements from a List
# --------------------------------

items = ["book", "pen", "pencil", "eraser", "pen"]
print(f"\nInitial items list: {items}")

# remove(): Removes the first occurrence of a specific value.
# If the value is not found, it raises a ValueError.
items.remove("pen")
print(f"After remove('pen'): {items}") # Output: ['book', 'pencil', 'eraser', 'pen']
# items.remove("stapler") # This would cause a ValueError

# pop(): Removes and returns the element at a specific index.
# If no index is specified, it removes and returns the last element.
removed_item_at_index_2 = items.pop(2) # Remove element at index 2 ('eraser')
print(f"After pop(2): {items}") # Output: ['book', 'pencil', 'pen']
print(f"Removed item using pop(2): {removed_item_at_index_2}") # Output: eraser

last_item = items.pop() # Remove the last element ('pen')
print(f"After pop(): {items}") # Output: ['book', 'pencil']
print(f"Removed item using pop(): {last_item}") # Output: pen

# del: Removes an element at a specific index or a slice.
# It doesn't return the removed element.
numbers_to_del = [10, 20, 30, 40, 50, 60]
print(f"\nInitial numbers_to_del: {numbers_to_del}")

del numbers_to_del[1] # Delete element at index 1 (20)
print(f"After del numbers_to_del[1]: {numbers_to_del}") # Output: [10, 30, 40, 50, 60]

del numbers_to_del[2:4] # Delete elements from index 2 up to 4 (exclusive) (40, 50)
print(f"After del numbers_to_del[2:4]: {numbers_to_del}") # Output: [10, 30, 60]

# clear(): Removes all elements from the list.
numbers_to_del.clear()
print(f"After clear(): {numbers_to_del}") # Output: []

# 7. List Length
# --------------
# Use the built-in `len()` function to find the number of elements in a list.

letters = ['a', 'b', 'c', 'd']
print(f"\nLetters list: {letters}")
length = len(letters)
print(f"Length of the letters list: {length}") # Output: 4

# 8. Iterating Through a List
# ---------------------------
# You can loop through the elements of a list using a `for` loop.

print("\nIterating through fruits:")
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# You can also iterate using index with range() and len()
print("\nIterating through fruits using index:")
for i in range(len(fruits)):
    print(f"Index {i}: {fruits[i]}")

# 9. Checking if an Item Exists
# -----------------------------
# Use the `in` keyword to check if an element is present in the list.

print(f"\nChecking items in {fruits}:")
if "banana" in fruits:
    print("Yes, 'banana' is in the fruits list.")
else:
    print("No, 'banana' is not in the fruits list.")

if "grape" not in fruits:
    print("Yes, 'grape' is not in the fruits list.")

# 10. List Methods Summary (Common ones)
# --------------------------------------
# list.append(x)    - Add item x to the end.
# list.extend(L)    - Extend list by appending all items from iterable L.
# list.insert(i, x) - Insert item x at index i.
# list.remove(x)    - Remove first item equal to x. Raises ValueError if not found.
# list.pop([i])     - Remove and return item at index i (default: last).
# list.clear()      - Remove all items from the list.
# list.index(x)     - Return index of first item equal to x. Raises ValueError if not found.
# list.count(x)     - Return number of times x appears in the list.
# list.sort()       - Sort the items of the list in place.
# list.reverse()    - Reverse the elements of the list in place.
# list.copy()       - Return a shallow copy of the list (equivalent to list[:]).

# Example of count()
grades = ['A', 'B', 'C', 'B', 'A', 'A']
print(f"\nGrades: {grades}")
count_A = grades.count('A')
print(f"Count of 'A' grades: {count_A}") # Output: 3

# Example of sort() (in-place)
numbers_to_sort = [5, 1, 4, 2, 3]
print(f"Original numbers: {numbers_to_sort}")
numbers_to_sort.sort() # Sorts the list directly
print(f"Sorted numbers: {numbers_to_sort}")

# Example of reverse() (in-place)
numbers_to_sort.reverse() # Reverses the list directly
print(f"Reversed numbers: {numbers_to_sort}")

# Example of index()
index_of_4 = numbers_to_sort.index(4)
print(f"Index of 4: {index_of_4}") # Output: 1 (in the reversed list [5, 4, 3, 2, 1])

# 11. The `array` Module (Briefly)
# --------------------------------
# Python also has an `array` module that provides space-efficient storage
# of basic C-style data types like integers and floats.
# Arrays created with this module are typed (all elements must be of the same type).
# They are less flexible than lists but can be more memory-efficient for large
# sequences of numeric data.


# Create an array of integers ('i' is the type code for signed integer)
# See Python docs for other type codes: https://docs.python.org/3/library/array.html
integer_array = array.array('i', [10, 20, 30, 40, 50])
print(f"\nArray from 'array' module: {integer_array}")
print(f"Type code: {integer_array.typecode}")
print(f"Item size (bytes): {integer_array.itemsize}")

# Accessing elements works like lists
print(f"Element at index 1: {integer_array[1]}") # Output: 20

# Arrays from the 'array' module are also mutable
integer_array[0] = 15
print(f"Modified array: {integer_array}")

# Trying to add an element of a different type will raise a TypeError
# integer_array.append(3.14) # This would cause a TypeError

# For most general-purpose programming in Python, especially for beginners,
# lists are the preferred way to handle array-like collections.
# Use the `array` module when you specifically need typed arrays for
# memory efficiency or interfacing with C code.