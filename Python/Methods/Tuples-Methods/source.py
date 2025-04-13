# Tuples in Python are ordered, immutable sequences.
# Immutable means that once a tuple is created, you cannot change its values.
# Tuples are defined using parentheses ().

# Let's create an example tuple
my_tuple = (1, 2, 'a', 'b', 2, 'a', 3, 2, 'c', 'a')
print(f"Original tuple: {my_tuple}")
print("-" * 30) # Separator for clarity

# --- Tuple Methods ---

# Python has two built-in methods that you can use on tuples:

# 1. count() Method
# Description: Returns the number of times a specified value occurs in a tuple.
# Syntax: tuple.count(value)
#   - value: Required. The value to search for.

print("--- 1. count() Method ---")

# Example 1.1: Count the occurrences of the number 2
count_of_2 = my_tuple.count(2)
print(f"The value '2' appears {count_of_2} times in the tuple.")

# Example 1.2: Count the occurrences of the character 'a'
count_of_a = my_tuple.count('a')
print(f"The value 'a' appears {count_of_a} times in the tuple.")

# Example 1.3: Count the occurrences of a value not in the tuple (e.g., 5)
count_of_5 = my_tuple.count(5)
print(f"The value '5' appears {count_of_5} times in the tuple.") # Output will be 0

# Example 1.4: Count the occurrences of 'c'
count_of_c = my_tuple.count('c')
print(f"The value 'c' appears {count_of_c} times in the tuple.")

print("-" * 30) # Separator

# 2. index() Method
# Description: Searches the tuple for a specified value and returns the position (index)
#              of the first occurrence where the value was found.
#              Remember that Python indexing starts from 0.
# Syntax: tuple.index(value, start, end)
#   - value: Required. The value to search for.
#   - start: Optional. The position where to start the search. Default is 0.
#   - end:   Optional. The position where to end the search. Default is the end of the tuple.
# Important: If the value is not found in the tuple, this method raises a ValueError.

print("--- 2. index() Method ---")

# Example 2.1: Find the index of the first occurrence of 'a'
try:
    index_of_a = my_tuple.index('a')
    print(f"The first occurrence of 'a' is at index: {index_of_a}")
except ValueError:
    print("'a' was not found in the tuple.")

# Example 2.2: Find the index of the first occurrence of 2
try:
    index_of_2 = my_tuple.index(2)
    print(f"The first occurrence of '2' is at index: {index_of_2}")
except ValueError:
    print("'2' was not found in the tuple.")

# Example 2.3: Find the index of 'a', starting the search from index 3
# The tuple is: (1, 2, 'a', 'b', 2, 'a', 3, 2, 'c', 'a')
# Indices:       0  1   2    3   4   5    6   7   8    9
# Searching for 'a' starting from index 3 ('b'). The next 'a' is at index 5.
try:
    index_of_a_after_3 = my_tuple.index('a', 3) # Start searching from index 3
    print(f"The first occurrence of 'a' starting from index 3 is at index: {index_of_a_after_3}")
except ValueError:
    print("'a' was not found in the tuple starting from index 3.")

# Example 2.4: Find the index of 'a', searching between index 3 and 8 (exclusive of 8)
# The tuple slice being searched is ('b', 2, 'a', 3, 2) corresponding to indices 3, 4, 5, 6, 7
try:
    index_of_a_between_3_8 = my_tuple.index('a', 3, 8) # Search from index 3 up to (but not including) index 8
    print(f"The first occurrence of 'a' between index 3 and 8 is at index: {index_of_a_between_3_8}")
except ValueError:
    print("'a' was not found in the tuple between index 3 and 8.")


# Example 2.5: Try to find the index of a value that doesn't exist (e.g., 'z')
# This will raise a ValueError, so we use a try-except block to handle it gracefully.
try:
    index_of_z = my_tuple.index('z')
    print(f"The first occurrence of 'z' is at index: {index_of_z}")
except ValueError:
    print("ValueError occurred: 'z' is not in the tuple.")

print("-" * 30) # Separator
print("End of Tuple Methods examples.")

# Note: Since tuples are immutable, there are no methods like append(), remove(), sort(), etc.,
# which would modify the tuple in place. If you need such functionality, you might
# consider converting the tuple to a list, performing the operation, and then
# converting it back to a tuple if necessary.
# Example:
# my_list = list(my_tuple)
# my_list.append('new_item')
# my_new_tuple = tuple(my_list)
# print(f"New tuple after converting to list, appending, and converting back: {my_new_tuple}")