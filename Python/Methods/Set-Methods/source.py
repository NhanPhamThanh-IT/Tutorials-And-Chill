# Python Set Methods Examples

# Sets are unordered collections of unique elements.
# Let's explore the various methods available for sets.

# --------------------------------------------------
# 1. add() - Adds an element to the set
# --------------------------------------------------
print("--- 1. add() ---")
my_set = {"apple", "banana", "cherry"}
print("Initial set:", my_set)
my_set.add("orange") # Add 'orange' to the set
print("Set after add('orange'):", my_set)
my_set.add("apple") # Adding an existing element has no effect
print("Set after add('apple') again:", my_set)
print("-" * 20)

# --------------------------------------------------
# 2. clear() - Removes all the elements from the set
# --------------------------------------------------
print("--- 2. clear() ---")
set_to_clear = {1, 2, 3}
print("Set before clear():", set_to_clear)
set_to_clear.clear()
print("Set after clear():", set_to_clear) # Output: set() which means an empty set
print("-" * 20)

# --------------------------------------------------
# 3. copy() - Returns a shallow copy of the set
# --------------------------------------------------
print("--- 3. copy() ---")
original_set = {"red", "green", "blue"}
print("Original set:", original_set)
copied_set = original_set.copy()
print("Copied set:", copied_set)
# Modifying the copy doesn't affect the original
copied_set.add("yellow")
print("Copied set after adding 'yellow':", copied_set)
print("Original set remains unchanged:", original_set)
print("-" * 20)

# --------------------------------------------------
# 4. difference() - Returns a set containing the difference between two or more sets
#                   (elements present in the first set but not in the others)
# --------------------------------------------------
print("--- 4. difference() ---")
set_a = {"apple", "banana", "cherry", "date"}
set_b = {"banana", "date", "fig"}
print("Set A:", set_a)
print("Set B:", set_b)
difference_set = set_a.difference(set_b) # Elements in A but not in B
print("A.difference(B):", difference_set)
# Using the '-' operator achieves the same result
difference_set_operator = set_a - set_b
print("A - B:", difference_set_operator)
# Difference with multiple sets
set_c = {"cherry"}
print("Set C:", set_c)
difference_multiple = set_a.difference(set_b, set_c) # Elements in A but not in B or C
print("A.difference(B, C):", difference_multiple)
print("-" * 20)

# --------------------------------------------------
# 5. difference_update() - Removes the items in this set that are also included in another, specified set(s)
#                          (Modifies the original set in-place)
# --------------------------------------------------
print("--- 5. difference_update() ---")
set_x = {"apple", "banana", "cherry", "date"}
set_y = {"banana", "date", "fig"}
print("Set X before update:", set_x)
print("Set Y:", set_y)
set_x.difference_update(set_y) # Remove elements from X that are also in Y
print("Set X after difference_update(Y):", set_x)
# Using the '-=' operator achieves the same result
set_p = {1, 2, 3, 4}
set_q = {3, 4, 5}
print("Set P before update:", set_p)
print("Set Q:", set_q)
set_p -= set_q
print("Set P after -= Q:", set_p)
print("-" * 20)

# --------------------------------------------------
# 6. discard() - Remove the specified item from the set.
#                If the item is not present, it does nothing (no error).
# --------------------------------------------------
print("--- 6. discard() ---")
discard_set = {"cat", "dog", "bird"}
print("Set before discard:", discard_set)
discard_set.discard("dog") # Remove 'dog'
print("Set after discard('dog'):", discard_set)
discard_set.discard("fish") # Try to discard 'fish' (not in the set)
print("Set after discard('fish'):", discard_set) # No change, no error
print("-" * 20)

# --------------------------------------------------
# 7. intersection() - Returns a set, that is the intersection of two or more sets
#                     (elements present in all sets)
# --------------------------------------------------
print("--- 7. intersection() ---")
set1 = {"apple", "banana", "cherry"}
set2 = {"banana", "cherry", "date"}
set3 = {"cherry", "fig"}
print("Set 1:", set1)
print("Set 2:", set2)
print("Set 3:", set3)
intersection_result = set1.intersection(set2) # Common elements in set1 and set2
print("set1.intersection(set2):", intersection_result)
# Using the '&' operator achieves the same result for two sets
intersection_operator = set1 & set2
print("set1 & set2:", intersection_operator)
# Intersection of multiple sets
intersection_multiple = set1.intersection(set2, set3) # Common elements in set1, set2, and set3
print("set1.intersection(set2, set3):", intersection_multiple)
print("-" * 20)

# --------------------------------------------------
# 8. intersection_update() - Removes the items in this set that are not present in other, specified set(s)
#                            (Modifies the original set in-place to keep only common elements)
# --------------------------------------------------
print("--- 8. intersection_update() ---")
set_m = {"apple", "banana", "cherry"}
set_n = {"banana", "cherry", "date"}
print("Set M before update:", set_m)
print("Set N:", set_n)
set_m.intersection_update(set_n) # Keep only elements present in both M and N
print("Set M after intersection_update(N):", set_m)
# Using the '&=' operator achieves the same result
set_u = {10, 20, 30, 40}
set_v = {30, 40, 50}
print("Set U before update:", set_u)
print("Set V:", set_v)
set_u &= set_v
print("Set U after &= V:", set_u)
print("-" * 20)

# --------------------------------------------------
# 9. isdisjoint() - Returns True if two sets have no elements in common, False otherwise.
# --------------------------------------------------
print("--- 9. isdisjoint() ---")
set_d1 = {1, 2, 3}
set_d2 = {4, 5, 6}
set_d3 = {3, 7, 8}
print("Set D1:", set_d1)
print("Set D2:", set_d2)
print("Set D3:", set_d3)
print("D1 isdisjoint D2:", set_d1.isdisjoint(set_d2)) # True, no common elements
print("D1 isdisjoint D3:", set_d1.isdisjoint(set_d3)) # False, '3' is common
print("-" * 20)

# --------------------------------------------------
# 10. issubset() - Returns True if all elements of this set are present in another specified set, False otherwise.
# --------------------------------------------------
print("--- 10. issubset() ---")
superset = {"a", "b", "c", "d", "e"}
subset1 = {"b", "c"}
subset2 = {"a", "f"}
subset3 = {"a", "b", "c", "d", "e"} # A set is a subset of itself
print("Superset:", superset)
print("Subset 1:", subset1)
print("Subset 2:", subset2)
print("Subset 3:", subset3)
print("subset1 issubset superset:", subset1.issubset(superset)) # True
print("subset2 issubset superset:", subset2.issubset(superset)) # False ('f' is not in superset)
print("subset3 issubset superset:", subset3.issubset(superset)) # True
# Using the '<=' operator achieves the same result
print("subset1 <= superset:", subset1 <= superset) # True
# Use '<' for proper subset (must be a subset and not equal)
print("subset1 < superset:", subset1 < superset) # True
print("subset3 < superset:", subset3 < superset) # False (they are equal)
print("-" * 20)

# --------------------------------------------------
# 11. issuperset() - Returns True if this set contains all elements of another specified set, False otherwise.
# --------------------------------------------------
print("--- 11. issuperset() ---")
# Using the same sets as issubset example
print("Superset:", superset)
print("Subset 1:", subset1)
print("Subset 2:", subset2)
print("Subset 3:", subset3)
print("superset issuperset subset1:", superset.issuperset(subset1)) # True
print("superset issuperset subset2:", superset.issuperset(subset2)) # False
print("superset issuperset subset3:", superset.issuperset(subset3)) # True
print("subset1 issuperset superset:", subset1.issuperset(superset)) # False
# Using the '>=' operator achieves the same result
print("superset >= subset1:", superset >= subset1) # True
# Use '>' for proper superset (must be a superset and not equal)
print("superset > subset1:", superset > subset1) # True
print("superset > subset3:", superset > subset3) # False (they are equal)
print("-" * 20)

# --------------------------------------------------
# 12. pop() - Removes and returns an arbitrary element from the set.
#             Raises KeyError if the set is empty.
#             Since sets are unordered, you don't know which item will be removed.
# --------------------------------------------------
print("--- 12. pop() ---")
pop_set = {"one", "two", "three", "four"}
print("Set before pop:", pop_set)
removed_item = pop_set.pop()
print("Removed item:", removed_item)
print("Set after pop:", pop_set)
removed_item_2 = pop_set.pop()
print("Removed item 2:", removed_item_2)
print("Set after second pop:", pop_set)
# Popping from an empty set raises an error
empty_set_for_pop = set()
try:
    empty_set_for_pop.pop()
except KeyError as e:
    print("Error when popping from empty set:", e)
print("-" * 20)

# --------------------------------------------------
# 13. remove() - Removes the specified element from the set.
#                Raises KeyError if the element is not found.
# --------------------------------------------------
print("--- 13. remove() ---")
remove_set = {"red", "green", "blue"}
print("Set before remove:", remove_set)
remove_set.remove("green") # Remove 'green'
print("Set after remove('green'):", remove_set)
# Trying to remove an element that doesn't exist raises an error
try:
    remove_set.remove("yellow")
except KeyError as e:
    print("Error when removing 'yellow' (not found):", e)
print("Use discard() if you don't want an error for non-existent elements.")
print("-" * 20)

# --------------------------------------------------
# 14. symmetric_difference() - Returns a set with elements that are in exactly one of the sets.
#                              (elements in either set, but not both)
# --------------------------------------------------
print("--- 14. symmetric_difference() ---")
set_sym1 = {"apple", "banana", "cherry"}
set_sym2 = {"banana", "date", "fig"}
print("Set Sym1:", set_sym1)
print("Set Sym2:", set_sym2)
sym_diff_set = set_sym1.symmetric_difference(set_sym2)
print("Sym1 symmetric_difference Sym2:", sym_diff_set)
# Using the '^' operator achieves the same result
sym_diff_operator = set_sym1 ^ set_sym2
print("Sym1 ^ Sym2:", sym_diff_operator)
print("-" * 20)

# --------------------------------------------------
# 15. symmetric_difference_update() - Updates the set with the symmetric difference of itself and another set.
#                                     (Keeps elements that are in exactly one of the sets, modifies in-place)
# --------------------------------------------------
print("--- 15. symmetric_difference_update() ---")
set_sym_up1 = {"apple", "banana", "cherry"}
set_sym_up2 = {"banana", "date", "fig"}
print("Set SymUp1 before update:", set_sym_up1)
print("Set SymUp2:", set_sym_up2)
set_sym_up1.symmetric_difference_update(set_sym_up2) # Update SymUp1
print("Set SymUp1 after symmetric_difference_update(SymUp2):", set_sym_up1)
# Using the '^=' operator achieves the same result
set_k1 = {10, 20, 30}
set_k2 = {20, 40, 50}
print("Set K1 before update:", set_k1)
print("Set K2:", set_k2)
set_k1 ^= set_k2
print("Set K1 after ^= K2:", set_k1)
print("-" * 20)

# --------------------------------------------------
# 16. union() - Returns a set containing all items from the original set and all items from the specified set(s).
#               Duplicates are automatically removed.
# --------------------------------------------------
print("--- 16. union() ---")
set_u1 = {"a", "b", "c"}
set_u2 = {"c", "d", "e"}
set_u3 = {"e", "f"}
print("Set U1:", set_u1)
print("Set U2:", set_u2)
print("Set U3:", set_u3)
union_result = set_u1.union(set_u2) # Union of U1 and U2
print("U1.union(U2):", union_result)
# Using the '|' operator achieves the same result for two sets
union_operator = set_u1 | set_u2
print("U1 | U2:", union_operator)
# Union of multiple sets
union_multiple = set_u1.union(set_u2, set_u3) # Union of U1, U2, and U3
print("U1.union(U2, U3):", union_multiple)
print("-" * 20)

# --------------------------------------------------
# 17. update() - Update the set with the union of itself and others.
#                (Adds elements from other iterables to the set, modifies in-place)
#                The 'others' can be sets, lists, tuples, etc.
# --------------------------------------------------
print("--- 17. update() ---")
set_upd1 = {"apple", "banana"}
set_upd2 = {"banana", "cherry"}
list_upd = ["cherry", "date"]
tuple_upd = ("date", "fig")
print("Set Upd1 before update:", set_upd1)
print("Set Upd2:", set_upd2)
print("List Upd:", list_upd)
print("Tuple Upd:", tuple_upd)
# Update with another set
set_upd1.update(set_upd2)
print("Set Upd1 after update(set_upd2):", set_upd1)
# Update with a list
set_upd1.update(list_upd)
print("Set Upd1 after update(list_upd):", set_upd1)
# Update with a tuple
set_upd1.update(tuple_upd)
print("Set Upd1 after update(tuple_upd):", set_upd1)
# Update with multiple iterables at once
set_upd_multi = {1, 2}
set_upd_multi.update([2, 3], {3, 4}, (4, 5))
print("Set UpdMulti after multiple updates:", set_upd_multi)
# Using the '|=' operator achieves the same result when updating with another set
set_z1 = {10, 20}
set_z2 = {20, 30}
print("Set Z1 before update:", set_z1)
print("Set Z2:", set_z2)
set_z1 |= set_z2
print("Set Z1 after |= Z2:", set_z1)
print("-" * 20)

print("Finished demonstrating Python set methods.")