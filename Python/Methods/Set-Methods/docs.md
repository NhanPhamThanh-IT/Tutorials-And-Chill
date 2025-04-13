# Python Set Methods

Sets are used to store multiple items in a single variable. A set is a collection which is both **unordered** and **unindexed**. Sets are written with curly brackets `{}`.

Sets are useful for storing unique items and performing mathematical set operations like union, intersection, difference, etc.

This document covers the built-in methods available for Python sets.

---

## 1. `add()`

Adds an element to the set. If the element is already present, the set remains unchanged.

**Syntax:**

```python
set.add(element)
```

**Parameters:**

*   `element`: The element to add to the set. This element must be immutable (e.g., number, string, tuple).

**Return Value:**

*   None

**Example:**

```python
fruits = {"apple", "banana", "cherry"}
print("Original set:", fruits)

fruits.add("orange")
print("Set after adding 'orange':", fruits)

# Adding an existing element
fruits.add("apple")
print("Set after adding 'apple' again:", fruits)
```

**Output:**

```
Original set: {'banana', 'cherry', 'apple'}
Set after adding 'orange': {'banana', 'cherry', 'orange', 'apple'}
Set after adding 'apple' again: {'banana', 'cherry', 'orange', 'apple'}
```

---

## 2. `clear()`

Removes all elements from the set, making it empty.

**Syntax:**

```python
set.clear()
```

**Parameters:**

*   None

**Return Value:**

*   None

**Example:**

```python
fruits = {"apple", "banana", "cherry"}
print("Original set:", fruits)

fruits.clear()
print("Set after clear():", fruits)
```

**Output:**

```
Original set: {'banana', 'cherry', 'apple'}
Set after clear(): set()
```

---

## 3. `copy()`

Returns a shallow copy of the set. Changes made to the original set will not affect the copy, and vice versa (for immutable elements).

**Syntax:**

```python
new_set = set.copy()
```

**Parameters:**

*   None

**Return Value:**

*   A new set which is a copy of the original set.

**Example:**

```python
original_set = {"apple", "banana", "cherry"}
copied_set = original_set.copy()

print("Original set:", original_set)
print("Copied set:", copied_set)

# Modify the original set
original_set.add("orange")

print("Original set after modification:", original_set)
print("Copied set (unaffected):", copied_set)
```

**Output:**

```
Original set: {'banana', 'cherry', 'apple'}
Copied set: {'banana', 'cherry', 'apple'}
Original set after modification: {'banana', 'cherry', 'orange', 'apple'}
Copied set (unaffected): {'banana', 'cherry', 'apple'}
```

---

## 4. `difference()`

Returns a new set containing the difference between two or more sets. The difference is the set of elements that are in the original set but not in the other specified set(s).

**Syntax:**

```python
new_set = set1.difference(set2, set3, ...)
```

**Parameters:**

*   `set2`, `set3`, ...: One or more sets to compare against `set1`.

**Return Value:**

*   A new set containing elements present only in `set1`.

**Example:**

```python
set_a = {"apple", "banana", "cherry"}
set_b = {"google", "microsoft", "apple"}

# Elements in set_a but not in set_b
diff_set = set_a.difference(set_b)
print("Difference (set_a - set_b):", diff_set)

# Elements in set_b but not in set_a
diff_set_2 = set_b.difference(set_a)
print("Difference (set_b - set_a):", diff_set_2)

# Using the '-' operator (equivalent to difference())
diff_set_operator = set_a - set_b
print("Difference using '-' operator:", diff_set_operator)
```

**Output:**

```
Difference (set_a - set_b): {'banana', 'cherry'}
Difference (set_b - set_a): {'google', 'microsoft'}
Difference using '-' operator: {'banana', 'cherry'}
```

---

## 5. `difference_update()`

Removes the items in this set that are also included in another specified set(s). This method modifies the original set directly.

**Syntax:**

```python
set1.difference_update(set2, set3, ...)
```

**Parameters:**

*   `set2`, `set3`, ...: One or more sets whose elements will be removed from `set1`.

**Return Value:**

*   None

**Example:**

```python
set_a = {"apple", "banana", "cherry"}
set_b = {"google", "microsoft", "apple"}

print("Original set_a:", set_a)

# Remove elements from set_a that are also in set_b
set_a.difference_update(set_b)

print("set_a after difference_update(set_b):", set_a)
```

**Output:**

```
Original set_a: {'banana', 'cherry', 'apple'}
set_a after difference_update(set_b): {'banana', 'cherry'}
```

---

## 6. `discard()`

Removes the specified element from the set. If the element is not present in the set, this method does nothing (it does not raise an error).

**Syntax:**

```python
set.discard(element)
```

**Parameters:**

*   `element`: The element to remove from the set.

**Return Value:**

*   None

**Example:**

```python
fruits = {"apple", "banana", "cherry"}
print("Original set:", fruits)

# Remove "banana"
fruits.discard("banana")
print("Set after discarding 'banana':", fruits)

# Try to discard an element not in the set
fruits.discard("grape")
print("Set after discarding 'grape' (no change):", fruits)
```

**Output:**

```
Original set: {'banana', 'cherry', 'apple'}
Set after discarding 'banana': {'cherry', 'apple'}
Set after discarding 'grape' (no change): {'cherry', 'apple'}
```

---

## 7. `intersection()`

Returns a new set containing the intersection of two or more sets. The intersection is the set of elements that are common to all the specified sets.

**Syntax:**

```python
new_set = set1.intersection(set2, set3, ...)
```

**Parameters:**

*   `set2`, `set3`, ...: One or more sets to find the intersection with `set1`.

**Return Value:**

*   A new set containing elements present in all specified sets.

**Example:**

```python
set_a = {"apple", "banana", "cherry"}
set_b = {"google", "microsoft", "apple"}
set_c = {"facebook", "apple", "amazon"}

# Intersection of set_a and set_b
intersect_set = set_a.intersection(set_b)
print("Intersection (set_a & set_b):", intersect_set)

# Intersection of set_a, set_b, and set_c
intersect_all = set_a.intersection(set_b, set_c)
print("Intersection (set_a & set_b & set_c):", intersect_all)

# Using the '&' operator (equivalent to intersection())
intersect_operator = set_a & set_b
print("Intersection using '&' operator:", intersect_operator)
```

**Output:**

```
Intersection (set_a & set_b): {'apple'}
Intersection (set_a & set_b & set_c): {'apple'}
Intersection using '&' operator: {'apple'}
```

---

## 8. `intersection_update()`

Updates the original set by keeping only the elements that are also present in all other specified sets. This method modifies the original set directly.

**Syntax:**

```python
set1.intersection_update(set2, set3, ...)
```

**Parameters:**

*   `set2`, `set3`, ...: One or more sets to intersect with `set1`.

**Return Value:**

*   None

**Example:**

```python
set_a = {"apple", "banana", "cherry"}
set_b = {"google", "microsoft", "apple"}
set_c = {"facebook", "apple", "amazon"}

print("Original set_a:", set_a)

# Update set_a to keep only elements common with set_b
set_a.intersection_update(set_b)
print("set_a after intersection_update(set_b):", set_a)

# Reset set_a and update with intersection of set_b and set_c
set_a = {"apple", "banana", "cherry"}
set_a.intersection_update(set_b, set_c)
print("set_a after intersection_update(set_b, set_c):", set_a)
```

**Output:**

```
Original set_a: {'banana', 'cherry', 'apple'}
set_a after intersection_update(set_b): {'apple'}
set_a after intersection_update(set_b, set_c): {'apple'}
```

---

## 9. `isdisjoint()`

Returns `True` if the two sets have no elements in common (i.e., their intersection is empty). Otherwise, it returns `False`.

**Syntax:**

```python
result = set1.isdisjoint(set2)
```

**Parameters:**

*   `set2`: The set to compare with `set1`.

**Return Value:**

*   `True` if the sets have no common elements, `False` otherwise.

**Example:**

```python
set_a = {"apple", "banana", "cherry"}
set_b = {"google", "microsoft", "facebook"}
set_c = {"apple", "google"}

# Check if set_a and set_b are disjoint
print("Are set_a and set_b disjoint?", set_a.isdisjoint(set_b))

# Check if set_a and set_c are disjoint
print("Are set_a and set_c disjoint?", set_a.isdisjoint(set_c))
```

**Output:**

```
Are set_a and set_b disjoint? True
Are set_a and set_c disjoint? False
```

---

## 10. `issubset()`

Returns `True` if all elements of this set are present in the specified set. Otherwise, it returns `False`. A set is considered a subset of itself.

**Syntax:**

```python
result = set1.issubset(set2)
```

**Parameters:**

*   `set2`: The set to check if `set1` is a subset of.

**Return Value:**

*   `True` if `set1` is a subset of `set2`, `False` otherwise.

**Example:**

```python
set_a = {"a", "b", "c"}
set_b = {"f", "e", "d", "c", "b", "a"}
set_c = {"a", "b"}

# Check if set_a is a subset of set_b
print("Is set_a a subset of set_b?", set_a.issubset(set_b))

# Check if set_b is a subset of set_a
print("Is set_b a subset of set_a?", set_b.issubset(set_a))

# Check if set_c is a subset of set_a
print("Is set_c a subset of set_a?", set_c.issubset(set_a))

# Using the '<=' operator (equivalent to issubset())
print("Is set_a <= set_b?", set_a <= set_b)
print("Is set_c <= set_a?", set_c <= set_a)
```

**Output:**

```
Is set_a a subset of set_b? True
Is set_b a subset of set_a? False
Is set_c a subset of set_a? True
Is set_a <= set_b? True
Is set_c <= set_a? True
```

---

## 11. `issuperset()`

Returns `True` if this set contains all elements of the specified set. Otherwise, it returns `False`. A set is considered a superset of itself.

**Syntax:**

```python
result = set1.issuperset(set2)
```

**Parameters:**

*   `set2`: The set to check if `set1` is a superset of.

**Return Value:**

*   `True` if `set1` is a superset of `set2`, `False` otherwise.

**Example:**

```python
set_a = {"f", "e", "d", "c", "b", "a"}
set_b = {"a", "b", "c"}
set_c = {"a", "g"}

# Check if set_a is a superset of set_b
print("Is set_a a superset of set_b?", set_a.issuperset(set_b))

# Check if set_b is a superset of set_a
print("Is set_b a superset of set_a?", set_b.issuperset(set_a))

# Check if set_a is a superset of set_c
print("Is set_a a superset of set_c?", set_a.issuperset(set_c))

# Using the '>=' operator (equivalent to issuperset())
print("Is set_a >= set_b?", set_a >= set_b)
print("Is set_a >= set_c?", set_a >= set_c)
```

**Output:**

```
Is set_a a superset of set_b? True
Is set_b a superset of set_a? False
Is set_a a superset of set_c? False
Is set_a >= set_b? True
Is set_a >= set_c? False
```

---

## 12. `pop()`

Removes and returns an arbitrary element from the set. Since sets are unordered, you cannot predict which element will be removed. If the set is empty, calling `pop()` raises a `KeyError`.

**Syntax:**

```python
removed_element = set.pop()
```

**Parameters:**

*   None

**Return Value:**

*   An arbitrary element removed from the set.

**Example:**

```python
fruits = {"apple", "banana", "cherry"}
print("Original set:", fruits)

# Remove and return an arbitrary element
removed = fruits.pop()
print("Removed element:", removed)
print("Set after pop():", fruits)

removed = fruits.pop()
print("Removed element:", removed)
print("Set after pop():", fruits)

removed = fruits.pop()
print("Removed element:", removed)
print("Set after pop():", fruits)

# Trying to pop from an empty set will raise KeyError
# empty_set = set()
# empty_set.pop() # Raises KeyError
```

**Output (Note: the order of popped elements may vary):**

```
Original set: {'banana', 'cherry', 'apple'}
Removed element: banana
Set after pop(): {'cherry', 'apple'}
Removed element: cherry
Set after pop(): {'apple'}
Removed element: apple
Set after pop(): set()
```

---

## 13. `remove()`

Removes the specified element from the set. If the element is not present in the set, this method raises a `KeyError`.

**Syntax:**

```python
set.remove(element)
```

**Parameters:**

*   `element`: The element to remove from the set.

**Return Value:**

*   None

**Example:**

```python
fruits = {"apple", "banana", "cherry"}
print("Original set:", fruits)

# Remove "banana"
fruits.remove("banana")
print("Set after removing 'banana':", fruits)

# Try to remove an element not in the set (will raise KeyError)
try:
    fruits.remove("grape")
except KeyError as e:
    print(f"Error removing 'grape': {e}")

print("Set remains:", fruits)
```

**Output:**

```
Original set: {'banana', 'cherry', 'apple'}
Set after removing 'banana': {'cherry', 'apple'}
Error removing 'grape': 'grape'
Set remains: {'cherry', 'apple'}
```

**Difference between `remove()` and `discard()`:**

*   `remove(element)`: Raises `KeyError` if `element` is not found.
*   `discard(element)`: Does nothing if `element` is not found.

---

## 14. `symmetric_difference()`

Returns a new set containing the symmetric difference of two sets. The symmetric difference is the set of elements that are in either of the sets, but not in both (i.e., elements unique to each set).

**Syntax:**

```python
new_set = set1.symmetric_difference(set2)
```

**Parameters:**

*   `set2`: The set to compute the symmetric difference with `set1`.

**Return Value:**

*   A new set containing elements present in exactly one of the sets.

**Example:**

```python
set_a = {"apple", "banana", "cherry"}
set_b = {"google", "microsoft", "apple"}

# Symmetric difference of set_a and set_b
sym_diff_set = set_a.symmetric_difference(set_b)
print("Symmetric difference (set_a ^ set_b):", sym_diff_set)

# Using the '^' operator (equivalent to symmetric_difference())
sym_diff_operator = set_a ^ set_b
print("Symmetric difference using '^' operator:", sym_diff_operator)
```

**Output:**

```
Symmetric difference (set_a ^ set_b): {'banana', 'cherry', 'google', 'microsoft'}
Symmetric difference using '^' operator: {'banana', 'cherry', 'google', 'microsoft'}
```

---

## 15. `symmetric_difference_update()`

Updates the original set with the symmetric difference of itself and another specified set. This method modifies the original set directly.

**Syntax:**

```python
set1.symmetric_difference_update(set2)
```

**Parameters:**

*   `set2`: The set to compute the symmetric difference with `set1`.

**Return Value:**

*   None

**Example:**

```python
set_a = {"apple", "banana", "cherry"}
set_b = {"google", "microsoft", "apple"}

print("Original set_a:", set_a)

# Update set_a with the symmetric difference of set_a and set_b
set_a.symmetric_difference_update(set_b)

print("set_a after symmetric_difference_update(set_b):", set_a)
```

**Output:**

```
Original set_a: {'banana', 'cherry', 'apple'}
set_a after symmetric_difference_update(set_b): {'banana', 'cherry', 'google', 'microsoft'}
```

---

## 16. `union()`

Returns a new set containing the union of two or more sets. The union is the set of all elements that are present in any of the specified sets. Duplicate elements are automatically handled (only one instance is kept).

**Syntax:**

```python
new_set = set1.union(set2, set3, ...)
```

**Parameters:**

*   `set2`, `set3`, ...: One or more sets to combine with `set1`.

**Return Value:**

*   A new set containing all unique elements from all specified sets.

**Example:**

```python
set_a = {"apple", "banana", "cherry"}
set_b = {"google", "microsoft", "apple"}
set_c = {"facebook", "amazon"}

# Union of set_a and set_b
union_set = set_a.union(set_b)
print("Union (set_a | set_b):", union_set)

# Union of set_a, set_b, and set_c
union_all = set_a.union(set_b, set_c)
print("Union (set_a | set_b | set_c):", union_all)

# Using the '|' operator (equivalent to union())
union_operator = set_a | set_b
print("Union using '|' operator:", union_operator)
```

**Output:**

```
Union (set_a | set_b): {'banana', 'cherry', 'google', 'microsoft', 'apple'}
Union (set_a | set_b | set_c): {'banana', 'cherry', 'google', 'microsoft', 'apple', 'facebook', 'amazon'}
Union using '|' operator: {'banana', 'cherry', 'google', 'microsoft', 'apple'}
```

---

## 17. `update()`

Updates the current set by adding elements from another set (or any other iterable like lists, tuples, strings). Duplicate elements are ignored. This method modifies the original set directly.

**Syntax:**

```python
set1.update(iterable)
```

**Parameters:**

*   `iterable`: An iterable (e.g., set, list, tuple, string) whose elements will be added to `set1`.

**Return Value:**

*   None

**Example:**

```python
set_a = {"apple", "banana", "cherry"}
set_b = {"google", "microsoft", "apple"}
my_list = ["orange", "banana"]

print("Original set_a:", set_a)

# Update set_a with elements from set_b
set_a.update(set_b)
print("set_a after update(set_b):", set_a)

# Update set_a with elements from my_list
set_a.update(my_list)
print("set_a after update(my_list):", set_a)

# Update set_a with characters from a string
set_a.update("grape")
print("set_a after update('grape'):", set_a)
```

**Output:**

```
Original set_a: {'banana', 'cherry', 'apple'}
set_a after update(set_b): {'banana', 'cherry', 'google', 'microsoft', 'apple'}
set_a after update(my_list): {'banana', 'cherry', 'google', 'microsoft', 'apple', 'orange'}
set_a after update('grape'): {'banana', 'cherry', 'google', 'microsoft', 'apple', 'orange', 'g', 'r', 'a', 'p', 'e'}
```

**Note:** `update()` is similar to `union()`, but `update()` modifies the original set, while `union()` returns a new set.