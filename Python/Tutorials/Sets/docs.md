# Sets in Python

## Introduction

A set is an unordered collection of unique items in Python. Sets are mutable, meaning you can add or remove items from them after creation. However, the elements *within* a set must be immutable (like numbers, strings, tuples). Sets are useful when you need to store a collection of items where the order doesn't matter and you want to ensure there are no duplicate entries.

## Key Characteristics

*   **Unordered:** Items in a set do not have a defined order. You cannot access items using an index.
*   **Unique Elements:** Sets automatically discard duplicate elements.
*   **Mutable:** You can add or remove elements from a set after it's created (unless it's a `frozenset`).
*   **Immutable Elements:** The items *inside* a set must be of immutable types (e.g., integers, floats, strings, tuples). You cannot have lists or dictionaries as elements of a set.

## Creating Sets

You can create sets in two main ways:

1.  **Using curly braces `{}`:** Place comma-separated items inside curly braces.
    *   Note: An empty set cannot be created with `{}`, as this creates an empty dictionary. Use `set()` instead.

    ```python
    # Creating a set with elements
    my_set = {1, 2, 3, "hello", 3.14}
    print(my_set)
    # Output might be: {1, 2, 3.14, 3, 'hello'} (order may vary)

    # Duplicates are automatically removed
    another_set = {1, 2, 2, 3, 3, 3}
    print(another_set)
    # Output: {1, 2, 3}
    ```

2.  **Using the `set()` constructor:** Pass an iterable (like a list, tuple, or string) to the `set()` function.

    ```python
    # Creating an empty set
    empty_set = set()
    print(empty_set)
    # Output: set()

    # Creating a set from a list
    list_items = [1, "apple", True, 1]
    set_from_list = set(list_items)
    print(set_from_list)
    # Output: {True, 1, 'apple'} (Note: True is treated as 1)

    # Creating a set from a string
    set_from_string = set("hello")
    print(set_from_string)
    # Output: {'e', 'h', 'l', 'o'} (order may vary)
    ```

## Common Set Operations

### Adding Elements

*   **`add(element)`:** Adds a single element to the set. If the element is already present, the set remains unchanged.

    ```python
    my_set = {1, 2, 3}
    my_set.add(4)
    print(my_set)
    # Output: {1, 2, 3, 4}

    my_set.add(2) # Adding an existing element
    print(my_set)
    # Output: {1, 2, 3, 4}
    ```

*   **`update(iterable)`:** Adds all elements from an iterable (like another set, list, or tuple) to the set.

    ```python
    my_set = {1, 2}
    my_set.update([3, 4, 1])
    print(my_set)
    # Output: {1, 2, 3, 4}

    my_set.update({5, 6}, (7, 8))
    print(my_set)
    # Output: {1, 2, 3, 4, 5, 6, 7, 8}
    ```

### Removing Elements

*   **`remove(element)`:** Removes the specified element. Raises a `KeyError` if the element is not found.

    ```python
    my_set = {1, 2, 3, 4}
    my_set.remove(3)
    print(my_set)
    # Output: {1, 2, 4}

    # my_set.remove(5) # This would cause a KeyError
    ```

*   **`discard(element)`:** Removes the specified element if it is present. Does *not* raise an error if the element is not found.

    ```python
    my_set = {1, 2, 3, 4}
    my_set.discard(2)
    print(my_set)
    # Output: {1, 3, 4}

    my_set.discard(5) # No error raised
    print(my_set)
    # Output: {1, 3, 4}
    ```

*   **`pop()`:** Removes and returns an *arbitrary* element from the set. Raises a `KeyError` if the set is empty. Since sets are unordered, you cannot predict which element will be removed.

    ```python
    my_set = {'a', 'b', 'c', 'd'}
    removed_item = my_set.pop()
    print(f"Removed item: {removed_item}")
    print(f"Set after pop: {my_set}")
    # Output might be:
    # Removed item: c
    # Set after pop: {'b', 'd', 'a'} (order and removed item may vary)
    ```

*   **`clear()`:** Removes all elements from the set.

    ```python
    my_set = {1, 2, 3}
    my_set.clear()
    print(my_set)
    # Output: set()
    ```

### Checking Membership

Use the `in` and `not in` operators to check if an element exists in a set.

```python
my_set = {1, "hello", 3.14}

print(1 in my_set)
# Output: True

print("world" in my_set)
# Output: False

print("hello" not in my_set)
# Output: False
```

### Mathematical Set Operations

Sets support standard mathematical operations:

*   **Union (`|` or `union()`):** Returns a new set containing all unique elements from both sets.

    ```python
    set_a = {1, 2, 3}
    set_b = {3, 4, 5}

    union_set = set_a | set_b
    # or union_set = set_a.union(set_b)
    print(union_set)
    # Output: {1, 2, 3, 4, 5}
    ```

*   **Intersection (`&` or `intersection()`):** Returns a new set containing elements common to both sets.

    ```python
    set_a = {1, 2, 3}
    set_b = {3, 4, 5}

    intersection_set = set_a & set_b
    # or intersection_set = set_a.intersection(set_b)
    print(intersection_set)
    # Output: {3}
    ```

*   **Difference (`-` or `difference()`):** Returns a new set containing elements in the first set but not in the second set.

    ```python
    set_a = {1, 2, 3}
    set_b = {3, 4, 5}

    difference_set = set_a - set_b
    # or difference_set = set_a.difference(set_b)
    print(difference_set)
    # Output: {1, 2}

    difference_set_ba = set_b - set_a
    print(difference_set_ba)
    # Output: {4, 5}
    ```

*   **Symmetric Difference (`^` or `symmetric_difference()`):** Returns a new set containing elements in either set, but not both.

    ```python
    set_a = {1, 2, 3}
    set_b = {3, 4, 5}

    sym_diff_set = set_a ^ set_b
    # or sym_diff_set = set_a.symmetric_difference(set_b)
    print(sym_diff_set)
    # Output: {1, 2, 4, 5}
    ```

## Other Useful Methods

*   **`len(set)`:** Returns the number of elements in the set.
*   **`copy()`:** Returns a shallow copy of the set.
*   **`issubset(other_set)`:** Returns `True` if all elements of the set are present in `other_set`.
*   **`issuperset(other_set)`:** Returns `True` if the set contains all elements of `other_set`.
*   **`isdisjoint(other_set)`:** Returns `True` if the set has no elements in common with `other_set`.

## Frozen Sets (`frozenset`)

A `frozenset` is an immutable version of a set. Once created, you cannot add or remove elements. Because they are immutable and hashable, they can be used as elements in other sets or as keys in dictionaries.

```python
# Create a frozenset
frozen = frozenset([1, 2, 3, 2])
print(frozen)
# Output: frozenset({1, 2, 3})

# Attempting to modify raises an error
# frozen.add(4) # AttributeError: 'frozenset' object has no attribute 'add'
# frozen.remove(1) # AttributeError: 'frozenset' object has no attribute 'remove'

# Frozensets can be elements of other sets
set_of_frozensets = {frozenset({1, 2}), frozenset({3, 4})}
print(set_of_frozensets)
# Output: {frozenset({1, 2}), frozenset({3, 4})}
```

## When to Use Sets

*   Removing duplicates from a sequence (like a list).
*   Membership testing (checking if an item is in a collection) – sets are highly optimized for this.
*   Performing mathematical set operations like union, intersection, difference, etc.

Sets are a powerful and efficient data structure in Python for handling collections of unique items.