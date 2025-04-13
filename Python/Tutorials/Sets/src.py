# Sets in Python
# A set is an unordered collection of unique items.
# Sets are mutable, meaning you can change their contents (add/remove items).
# Sets are defined using curly braces {} or the set() constructor.

# -------------------------
# 1. Creating Sets
# -------------------------

# Using curly braces {}
# Note: An empty {} creates an empty dictionary, not an empty set.
my_set = {1, 2, 3, 4, 5}
print(f"Set created with {{}}: {my_set}")
print(f"Type of my_set: {type(my_set)}")

# Creating an empty set - use set()
empty_set = set()
print(f"An empty set: {empty_set}")
print(f"Type of empty_set: {type(empty_set)}")

# Creating a set from a list (duplicates are automatically removed)
list_with_duplicates = [1, 2, 2, 3, 4, 4, 4, 5]
set_from_list = set(list_with_duplicates)
print(f"Set created from list {list_with_duplicates}: {set_from_list}")

# Creating a set from a string (each character becomes an element)
set_from_string = set("hello")
print(f"Set created from string 'hello': {set_from_string}")

# Creating a set from a tuple
set_from_tuple = set((1, 'a', 3.14))
print(f"Set created from tuple (1, 'a', 3.14): {set_from_tuple}")

# Sets cannot contain mutable items like lists or dictionaries
# This will raise a TypeError:
# bad_set = {1, 2, [3, 4]} # Uncommenting this line will cause an error

# -------------------------
# 2. Set Characteristics
# -------------------------

# Unordered: Items have no specific order. You cannot access items by index.
# print(my_set[0]) # This will raise a TypeError

# Unique Elements: Sets automatically discard duplicate values.
set_with_duplicates = {1, 1, 2, 3, 3, 3, 4}
print(f"Set with duplicates { {1, 1, 2, 3, 3, 3, 4} } becomes: {set_with_duplicates}")

# -------------------------
# 3. Adding Elements
# -------------------------

# Use the add() method to add a single element.
fruits = {"apple", "banana"}
print(f"\nOriginal fruits set: {fruits}")
fruits.add("orange")
print(f"After adding 'orange': {fruits}")

# Adding an element that already exists does nothing.
fruits.add("apple")
print(f"After adding 'apple' again: {fruits}")

# Use the update() method to add multiple elements from an iterable (list, tuple, set, string).
more_fruits = ["mango", "grape", "apple"] # 'apple' is a duplicate here
fruits.update(more_fruits)
print(f"After updating with {more_fruits}: {fruits}")

fruits.update(("kiwi", "banana")) # Update with a tuple
print(f"After updating with ('kiwi', 'banana'): {fruits}")

fruits.update("pear") # Update with a string (adds 'p', 'e', 'a', 'r')
print(f"After updating with 'pear': {fruits}")


# -------------------------
# 4. Removing Elements
# -------------------------

# remove(item): Removes the specified item. Raises KeyError if the item is not found.
print(f"\nCurrent set: {fruits}")
fruits.remove("banana")
print(f"After removing 'banana': {fruits}")
# fruits.remove("pineapple") # Uncommenting this line will cause a KeyError

# discard(item): Removes the specified item. Does NOT raise an error if the item is not found.
fruits.discard("apple")
print(f"After discarding 'apple': {fruits}")
fruits.discard("pineapple") # No error raised, even though 'pineapple' isn't there
print(f"After discarding 'pineapple' (which wasn't present): {fruits}")

# pop(): Removes and returns an arbitrary element from the set. Raises KeyError if the set is empty.
# Since sets are unordered, you don't know which item will be removed.
removed_item = fruits.pop()
print(f"Popped item: {removed_item}")
print(f"Set after pop(): {fruits}")

# clear(): Removes all elements from the set.
fruits.clear()
print(f"Set after clear(): {fruits}")
# removed_item = fruits.pop() # Uncommenting this line will cause a KeyError on an empty set

# -------------------------
# 5. Set Operations
# -------------------------

set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}
set_c = {1, 2}

print(f"\nSet A: {set_a}")
print(f"Set B: {set_b}")
print(f"Set C: {set_c}")

# Union (| or union()): Returns a new set with all elements from both sets.
union_set = set_a | set_b
print(f"Union (A | B): {union_set}")
union_set_method = set_a.union(set_b)
print(f"Union (A.union(B)): {union_set_method}")

# Intersection (& or intersection()): Returns a new set with elements common to both sets.
intersection_set = set_a & set_b
print(f"Intersection (A & B): {intersection_set}")
intersection_set_method = set_a.intersection(set_b)
print(f"Intersection (A.intersection(B)): {intersection_set_method}")

# Difference (- or difference()): Returns a new set with elements in the first set but not in the second.
difference_set_ab = set_a - set_b
print(f"Difference (A - B): {difference_set_ab}")
difference_set_ba = set_b - set_a
print(f"Difference (B - A): {difference_set_ba}")
difference_set_method = set_a.difference(set_b)
print(f"Difference (A.difference(B)): {difference_set_method}")

# Symmetric Difference (^ or symmetric_difference()): Returns a new set with elements in either set, but not both.
sym_diff_set = set_a ^ set_b
print(f"Symmetric Difference (A ^ B): {sym_diff_set}")
sym_diff_set_method = set_a.symmetric_difference(set_b)
print(f"Symmetric Difference (A.symmetric_difference(B)): {sym_diff_set_method}")

# -------------------------
# 6. In-place Set Operations (Modify the original set)
# -------------------------

set_d = {10, 20, 30}
set_e = {30, 40, 50}
print(f"\nSet D: {set_d}")
print(f"Set E: {set_e}")

# intersection_update() or &= : Updates the set with the intersection of itself and another.
set_d_copy = set_d.copy() # Work on a copy to show the original
set_d_copy.intersection_update(set_e)
print(f"D after intersection_update(E): {set_d_copy}") # Output: {30}

# difference_update() or -= : Updates the set by removing elements found in another set.
set_d_copy = set_d.copy()
set_d_copy.difference_update(set_e)
print(f"D after difference_update(E): {set_d_copy}") # Output: {10, 20}

# symmetric_difference_update() or ^= : Updates the set with the symmetric difference.
set_d_copy = set_d.copy()
set_d_copy.symmetric_difference_update(set_e)
print(f"D after symmetric_difference_update(E): {set_d_copy}") # Output: {10, 20, 40, 50}

# Note: update() or |= is the in-place version of union(). We saw update() earlier.

# -------------------------
# 7. Set Membership Testing
# -------------------------

numbers = {1, 3, 5, 7, 9}
print(f"\nNumbers set: {numbers}")

# Check if an item exists in the set using 'in'
print(f"Is 5 in numbers? {5 in numbers}")       # True
print(f"Is 2 in numbers? {2 in numbers}")       # False

# Check if an item does not exist using 'not in'
print(f"Is 6 not in numbers? {6 not in numbers}") # True
print(f"Is 9 not in numbers? {9 not in numbers}") # False

# -------------------------
# 8. Set Comparisons
# -------------------------

set_x = {1, 2, 3}
set_y = {1, 2, 3, 4, 5}
set_z = {1, 2}
set_w = {10, 20}

print(f"\nSet X: {set_x}")
print(f"Set Y: {set_y}")
print(f"Set Z: {set_z}")
print(f"Set W: {set_w}")

# issubset() or <= : Check if all elements of one set are present in another.
print(f"Is X subset of Y? (X <= Y): {set_x <= set_y}")         # True
print(f"Is Z subset of X? (Z.issubset(X)): {set_z.issubset(set_x)}") # True
print(f"Is Y subset of X? (Y <= X): {set_y <= set_x}")         # False

# issuperset() or >= : Check if a set contains all elements of another set.
print(f"Is Y superset of X? (Y >= X): {set_y >= set_x}")         # True
print(f"Is X superset of Z? (X.issuperset(Z)): {set_x.issuperset(set_z)}") # True
print(f"Is X superset of Y? (X >= Y): {set_x >= set_y}")         # False

# Proper Subset (<): issubset() is True, and the sets are not equal.
print(f"Is X proper subset of Y? (X < Y): {set_x < set_y}")     # True
print(f"Is X proper subset of X? (X < X): {set_x < set_x}")     # False

# Proper Superset (>): issuperset() is True, and the sets are not equal.
print(f"Is Y proper superset of X? (Y > X): {set_y > set_x}")     # True
print(f"Is Y proper superset of Y? (Y > Y): {set_y > set_y}")     # False

# isdisjoint(): Check if two sets have no elements in common.
print(f"Are X and W disjoint? (X.isdisjoint(W)): {set_x.isdisjoint(set_w)}") # True
print(f"Are X and Y disjoint? (X.isdisjoint(Y)): {set_x.isdisjoint(set_y)}") # False (common elements 1, 2, 3)

# -------------------------
# 9. Iterating Through a Set
# -------------------------

colors = {"red", "green", "blue"}
print("\nIterating through colors set:")
for color in colors:
    print(color) # Note: The order is not guaranteed

# -------------------------
# 10. Set Comprehension (Similar to list comprehension)
# -------------------------

# Create a set of squares of numbers from 0 to 4
squares = {x*x for x in range(5)}
print(f"\nSet comprehension (squares): {squares}")

# Create a set of even numbers from 0 to 9
evens = {x for x in range(10) if x % 2 == 0}
print(f"Set comprehension (evens): {evens}")

# -------------------------
# 11. Frozensets
# -------------------------

# Frozensets are immutable versions of sets.
# Once created, you cannot add or remove elements.
# They can be used as dictionary keys or elements of another set (because they are hashable).

frozen = frozenset([1, 2, 3, 2]) # Duplicates are still removed
print(f"\nFrozenset: {frozen}")
print(f"Type of frozen: {type(frozen)}")

# Attempting to modify a frozenset will raise an AttributeError:
# frozen.add(4)      # Uncommenting this line will cause an error
# frozen.remove(1)   # Uncommenting this line will cause an error
# frozen.update([5]) # Uncommenting this line will cause an error

# Frozensets support regular set operations (union, intersection, etc.),
# but the result is always a frozenset or a regular set depending on the operation.
fs1 = frozenset([1, 2])
fs2 = frozenset([2, 3])
print(f"Union of frozensets: {fs1 | fs2}") # Returns a frozenset
print(f"Intersection of frozensets: {fs1 & fs2}") # Returns a frozenset

# Using frozenset as a dictionary key
dict_with_frozenset_key = {frozenset({1, 2}): "value"}
print(f"Dictionary with frozenset key: {dict_with_frozenset_key}")

# Using frozenset as an element in a regular set
set_containing_frozenset = {10, 20, frozenset({1, 2})}
print(f"Set containing a frozenset: {set_containing_frozenset}")

print("\n--- End of Set Examples ---")