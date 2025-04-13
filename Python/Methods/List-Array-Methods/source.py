# Python List/Array Methods Examples

# Lists are used to store multiple items in a single variable.
# Lists are one of 4 built-in data types in Python used to store collections of data,
# the other 3 are Tuple, Set, and Dictionary, all with different qualities and usage.
# Lists are created using square brackets: []

# Let's start with an example list
fruits = ["apple", "banana", "cherry"]
print(f"Initial list: {fruits}")
print("-" * 20)

# 1. append() - Adds an element at the end of the list
print("1. append('orange')")
# Adds 'orange' to the end of the fruits list
fruits.append("orange")
print(f"List after append: {fruits}")
print("-" * 20)

# 2. clear() - Removes all the elements from the list
print("2. clear()")
# Create a temporary list to demonstrate clear
temp_list_for_clear = fruits.copy()
print(f"Temporary list before clear: {temp_list_for_clear}")
# Removes all elements from temp_list_for_clear
temp_list_for_clear.clear()
print(f"Temporary list after clear: {temp_list_for_clear}")
# Note: The original 'fruits' list remains unchanged
print(f"Original 'fruits' list is still: {fruits}")
print("-" * 20)

# 3. copy() - Returns a shallow copy of the list
print("3. copy()")
# Creates a new list that is a copy of the 'fruits' list
fruits_copy = fruits.copy()
print(f"Original list: {fruits}")
print(f"Copied list: {fruits_copy}")
# Modifying the copy doesn't affect the original
fruits_copy.append("kiwi")
print(f"Modified copy: {fruits_copy}")
print(f"Original list remains unchanged: {fruits}")
# Important Note: copy() creates a shallow copy. If the list contains other mutable objects (like other lists),
# changes to those inner objects will be reflected in both the original and the copy.
nested_list = [1, 2, [3, 4]]
nested_copy = nested_list.copy()
nested_list[2].append(5) # Modify the inner list in the original
print(f"Original nested list after inner modification: {nested_list}")
print(f"Shallow copy reflects inner modification: {nested_copy}")
print("-" * 20)

# 4. count() - Returns the number of elements with the specified value
print("4. count('apple')")
fruits.append("apple") # Add another 'apple' to demonstrate count
print(f"List now: {fruits}")
# Counts how many times 'apple' appears in the list
apple_count = fruits.count("apple")
print(f"The count of 'apple' is: {apple_count}")
banana_count = fruits.count("banana")
print(f"The count of 'banana' is: {banana_count}")
grape_count = fruits.count("grape") # Count an item not in the list
print(f"The count of 'grape' is: {grape_count}")
# Remove the extra 'apple' added for this example
fruits.remove("apple") # Removes the first occurrence
print(f"List after removing one 'apple': {fruits}")
print("-" * 20)

# 5. extend() - Add the elements of a list (or any iterable), to the end of the current list
print("5. extend(['mango', 'pineapple'])")
more_fruits = ["mango", "pineapple", "papaya"]
print(f"Original list: {fruits}")
print(f"List to extend with: {more_fruits}")
# Adds each element from more_fruits to the end of fruits
fruits.extend(more_fruits)
print(f"List after extend: {fruits}")
# You can also extend with other iterables like tuples or sets
vegetables_tuple = ("carrot", "broccoli")
fruits.extend(vegetables_tuple)
print(f"List after extending with a tuple: {fruits}")
print("-" * 20)

# 6. index() - Returns the index (position) of the first element with the specified value
print("6. index('cherry')")
print(f"Current list: {fruits}")
# Finds the index of the first occurrence of 'cherry'
# Note: List indices start at 0
cherry_index = fruits.index("cherry")
print(f"The index of 'cherry' is: {cherry_index}")
# You can also specify a start and end position to search within
# Let's add another 'banana' to demonstrate this
fruits.insert(5, "banana")
print(f"List with added 'banana': {fruits}")
first_banana_index = fruits.index("banana") # Finds the first one
print(f"Index of the first 'banana': {first_banana_index}")
# Find 'banana' starting the search *after* index 1 (where the first banana is)
second_banana_index = fruits.index("banana", first_banana_index + 1)
print(f"Index of the second 'banana' (searching after index {first_banana_index}): {second_banana_index}")
# If the value is not found, it raises a ValueError
try:
    grape_index = fruits.index("grape")
    print(f"The index of 'grape' is: {grape_index}")
except ValueError:
    print("'grape' is not in the list.")
# Clean up the extra banana
fruits.pop(second_banana_index) # Remove the second banana by its index
print(f"List after removing second banana: {fruits}")
print("-" * 20)

# 7. insert() - Adds an element at the specified position
print("7. insert(1, 'lemon')")
print(f"List before insert: {fruits}")
# Inserts 'lemon' at index 1 (the second position)
# Existing elements from index 1 onwards are shifted to the right
fruits.insert(1, "lemon")
print(f"List after inserting 'lemon' at index 1: {fruits}")
# Insert at the beginning (index 0)
fruits.insert(0, "strawberry")
print(f"List after inserting 'strawberry' at index 0: {fruits}")
# Insert at the end (equivalent to append if index is len(list) or greater)
fruits.insert(len(fruits), "melon")
print(f"List after inserting 'melon' at the end: {fruits}")
print("-" * 20)

# 8. pop() - Removes the element at the specified position (and returns it)
print("8. pop()")
print(f"List before pop: {fruits}")
# If no index is specified, pop() removes and returns the *last* item
last_item = fruits.pop()
print(f"Removed item (last): {last_item}")
print(f"List after pop(): {fruits}")
# Remove the item at index 1 ('lemon' in this case)
item_at_index_1 = fruits.pop(1)
print(f"Removed item at index 1: {item_at_index_1}")
print(f"List after pop(1): {fruits}")
# Trying to pop an index that doesn't exist will raise an IndexError
# print(fruits.pop(100)) # This would cause an error
print("-" * 20)

# 9. remove() - Removes the *first* item with the specified value
print("9. remove('banana')")
# Let's add another 'banana' to show it removes only the first one
fruits.insert(3, "banana")
print(f"List before remove ('banana' added): {fruits}")
# Removes the first occurrence of 'banana'
fruits.remove("banana")
print(f"List after remove('banana'): {fruits}")
# If the value is not found, it raises a ValueError
try:
    fruits.remove("grape")
    print("Removed 'grape'.") # This won't be printed
except ValueError:
    print("'grape' was not found to remove.")
print("-" * 20)

# 10. reverse() - Reverses the order of the list *in-place*
print("10. reverse()")
print(f"List before reverse: {fruits}")
# Reverses the elements of the list itself
fruits.reverse()
print(f"List after reverse: {fruits}")
# Note: reverse() modifies the original list and returns None
result_of_reverse = fruits.reverse() # Reverse it back
print(f"Result of calling reverse() again: {result_of_reverse}")
print(f"List after second reverse (back to original order): {fruits}")
print("-" * 20)

# 11. sort() - Sorts the list *in-place*
print("11. sort()")
# Note: sort() only works if all elements are comparable (e.g., all strings or all numbers)
# Let's create a list that needs sorting
unsorted_fruits = fruits.copy() # Work on a copy
unsorted_fruits.append("apricot")
unsorted_fruits.append("blueberry")
print(f"Unsorted list: {unsorted_fruits}")
# Sorts the list alphabetically (ascending) by default
unsorted_fruits.sort()
print(f"List after sort() (ascending): {unsorted_fruits}")
# Sort in descending order using the reverse=True argument
unsorted_fruits.sort(reverse=True)
print(f"List after sort(reverse=True) (descending): {unsorted_fruits}")

# Sorting based on a key function (e.g., length of the string)
print("Sorting by length using key=len")
unsorted_fruits.sort(key=len) # Sorts based on the return value of len() for each item
print(f"List after sort(key=len): {unsorted_fruits}")

# Sorting numbers
numbers = [5, 1, 4, 1, 5, 9, 2, 6]
print(f"Unsorted numbers: {numbers}")
numbers.sort()
print(f"Sorted numbers (ascending): {numbers}")
numbers.sort(reverse=True)
print(f"Sorted numbers (descending): {numbers}")

# Trying to sort a list with mixed types (e.g., strings and numbers) will usually raise a TypeError
mixed_list = [1, "apple", 3, "banana"]
print(f"Mixed list: {mixed_list}")
try:
    mixed_list.sort()
    print(f"Sorted mixed list: {mixed_list}") # This won't be printed
except TypeError as e:
    print(f"Could not sort mixed list: {e}")

# Note: sort() modifies the original list and returns None
result_of_sort = numbers.sort()
print(f"Result of calling sort(): {result_of_sort}")
print(f"Numbers list is still sorted: {numbers}")
print("-" * 20)

print("End of List Methods Examples")