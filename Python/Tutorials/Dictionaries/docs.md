# Dictionaries in Python

## 1. Introduction

A dictionary in Python is an unordered (prior to Python 3.7) or ordered (Python 3.7+) collection of items. While other compound data types have only values as their elements, dictionaries store data in **key-value pairs**.

*   **Keys:** Must be unique and immutable (e.g., strings, numbers, tuples with immutable elements). They act as identifiers for values.
*   **Values:** Can be of any data type (even other dictionaries) and can be duplicated.
*   **Mutable:** Dictionaries can be changed after they are created (add, remove, modify items).
*   **Ordered (Python 3.7+):** As of Python 3.7, dictionaries remember the order in which items were inserted. In earlier versions, the order was arbitrary.
*   **Syntax:** Defined using curly braces `{}` with key-value pairs separated by colons `:` and pairs separated by commas `,`. `my_dict = {key1: value1, key2: value2}`.

Dictionaries are optimized for retrieving values when the key is known. They are often used to represent real-world objects (like a person's attributes) or to store configuration settings.

## 2. Creating Dictionaries

There are several ways to create a dictionary:

**a) Using Curly Braces `{}`:**

This is the most common way.

```python
# An empty dictionary
empty_dict = {}
print(f"Empty dictionary: {empty_dict}")
print(f"Type: {type(empty_dict)}")

# Dictionary with integer keys
num_dict = {1: 'one', 2: 'two', 3: 'three'}
print(f"Number dictionary: {num_dict}")

# Dictionary with string keys
person = {
    'name': 'Alice',
    'age': 30,
    'city': 'New York'
}
print(f"Person dictionary: {person}")

# Dictionary with mixed key types (keys must be immutable)
mixed_dict = {
    'name': 'Bob',
    1: [1, 2, 3],
    ('a', 'b'): True
}
print(f"Mixed key dictionary: {mixed_dict}")
```

**b) Using the `dict()` Constructor:**

The `dict()` constructor can build dictionaries directly from sequences of key-value pairs or using keyword arguments.

```python
# Creating an empty dictionary
empty_dict_constructor = dict()
print(f"Empty dict (constructor): {empty_dict_constructor}")

# From keyword arguments (keys must be valid identifiers)
person_constructor = dict(name='Charlie', age=25, city='London')
print(f"Person dict (constructor kwargs): {person_constructor}")

# From a list of tuples (key-value pairs)
pairs = [('fruit', 'apple'), ('color', 'red'), ('count', 5)]
fruit_dict = dict(pairs)
print(f"Fruit dict (constructor from pairs): {fruit_dict}")

# From another dictionary (creates a shallow copy)
original = {'a': 1, 'b': 2}
copy_dict = dict(original)
print(f"Copied dict (constructor): {copy_dict}")
```

**c) Using Dictionary Comprehension:**

A concise way to create dictionaries, similar to list comprehensions.

```python
# Create a dictionary of squares
squares = {x: x*x for x in range(5)}
print(f"Squares dictionary (comprehension): {squares}") # Output: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# Create a dictionary from two lists
keys = ['a', 'b', 'c']
values = [1, 2, 3]
combined_dict = {k: v for k, v in zip(keys, values)}
print(f"Combined dict (comprehension): {combined_dict}") # Output: {'a': 1, 'b': 2, 'c': 3}
```

## 3. Accessing Elements

You can access dictionary values using their corresponding keys.

**a) Using Square Brackets `[]`:**

Provide the key inside square brackets. If the key does not exist, this will raise a `KeyError`.

```python
person = {'name': 'Alice', 'age': 30, 'city': 'New York'}

print(f"Name: {person['name']}")   # Output: Alice
print(f"Age: {person['age']}")     # Output: 30

# Trying to access a non-existent key raises KeyError
# print(person['country']) # Uncommenting this line will cause a KeyError
```

**b) Using the `get()` Method:**

The `get()` method retrieves the value for a given key. Its advantage is that it doesn't raise an error if the key is missing. Instead, it returns `None` (by default) or a specified default value.

```python
person = {'name': 'Alice', 'age': 30, 'city': 'New York'}

# Get existing key
print(f"Name (get): {person.get('name')}") # Output: Alice

# Get non-existent key (returns None)
print(f"Country (get): {person.get('country')}") # Output: None

# Get non-existent key with a default value
print(f"Country (get with default): {person.get('country', 'Unknown')}") # Output: Unknown
```

## 4. Adding and Modifying Elements

Dictionaries are mutable, so you can add new key-value pairs or change the values associated with existing keys.

**a) Using Square Brackets `[]`:**

If the key exists, its value is updated. If the key doesn't exist, a new key-value pair is added.

```python
person = {'name': 'Alice', 'age': 30}
print(f"Original person: {person}")

# Modify an existing value
person['age'] = 31
print(f"Modified person (age): {person}")

# Add a new key-value pair
person['city'] = 'San Francisco'
print(f"Added city: {person}")
```

**b) Using the `update()` Method:**

The `update()` method merges another dictionary or an iterable of key-value pairs into the current dictionary. Existing keys are updated, and new keys are added.

```python
person = {'name': 'Alice', 'age': 30}
print(f"Original person: {person}")

# Update with another dictionary
updates = {'age': 32, 'city': 'Chicago', 'email': 'alice@example.com'}
person.update(updates)
print(f"Updated person (dict): {person}")

# Update with keyword arguments
person.update(age=33, country='USA')
print(f"Updated person (kwargs): {person}")

# Update with a list of tuples
person.update([('zipcode', '12345'), ('name', 'Alice Smith')])
print(f"Updated person (list of tuples): {person}")
```

## 5. Removing Elements

You can remove items from a dictionary using several methods.

**a) Using `pop()`:**

Removes the item with the specified key and returns its value. If the key is not found, it raises a `KeyError`, unless a default value is provided.

```python
person = {'name': 'Bob', 'age': 25, 'city': 'London'}
print(f"Original person: {person}")

# Remove 'age' and get its value
removed_age = person.pop('age')
print(f"Removed age: {removed_age}")
print(f"Person after pop('age'): {person}")

# Remove 'country' (doesn't exist) with a default value
removed_country = person.pop('country', 'Not Found')
print(f"Removed country (default): {removed_country}")
print(f"Person after pop('country', default): {person}")

# Trying to pop a non-existent key without default raises KeyError
# person.pop('zipcode') # Uncommenting causes KeyError
```

**b) Using `popitem()`:**

Removes and returns an arbitrary (key, value) pair before Python 3.7. In Python 3.7+, it removes and returns the *last inserted* (key, value) pair (LIFO - Last In, First Out). Raises `KeyError` if the dictionary is empty.

```python
person = {'name': 'Charlie', 'age': 40, 'city': 'Paris'}
print(f"Original person: {person}")

# Remove the last inserted item
key, value = person.popitem()
print(f"Removed item (popitem): {key}: {value}")
print(f"Person after popitem(): {person}")

key, value = person.popitem()
print(f"Removed item (popitem): {key}: {value}")
print(f"Person after popitem(): {person}")

# Calling popitem() on an empty dictionary raises KeyError
# empty_dict = {}
# empty_dict.popitem() # Uncommenting causes KeyError
```

**c) Using the `del` Keyword:**

Removes the item with the specified key. Raises `KeyError` if the key is not found. Can also be used to delete the entire dictionary object.

```python
person = {'name': 'David', 'age': 50, 'city': 'Tokyo'}
print(f"Original person: {person}")

# Delete the item with key 'city'
del person['city']
print(f"Person after del 'city': {person}")

# Trying to delete a non-existent key raises KeyError
# del person['country'] # Uncommenting causes KeyError

# Delete the entire dictionary object
# del person
# print(person) # Uncommenting causes NameError because 'person' no longer exists
```

**d) Using `clear()`:**

Removes all items from the dictionary, making it empty.

```python
person = {'name': 'Eve', 'age': 22, 'city': 'Berlin'}
print(f"Original person: {person}")

person.clear()
print(f"Person after clear(): {person}") # Output: {}
```

## 6. Iterating Through Dictionaries

You can loop through dictionaries in several ways.

**a) Iterating Through Keys (Default):**

When you iterate directly over a dictionary, you get its keys.

```python
person = {'name': 'Frank', 'age': 35, 'job': 'Engineer'}
print("\nIterating through keys:")
for key in person:
    print(f"Key: {key}, Value: {person[key]}")
```

**b) Iterating Through Values using `.values()`:**

The `.values()` method returns a view object containing the dictionary's values.

```python
person = {'name': 'Grace', 'age': 28, 'hobby': 'Reading'}
print("\nIterating through values:")
for value in person.values():
    print(f"Value: {value}")
```

**c) Iterating Through Key-Value Pairs using `.items()`:**

The `.items()` method returns a view object containing tuples of (key, value) pairs. This is often the most useful way to iterate.

```python
person = {'name': 'Heidi', 'age': 42, 'location': 'Sydney'}
print("\nIterating through items (key-value pairs):")
for key, value in person.items():
    print(f"Key: {key}, Value: {value}")
```

## 7. Dictionary Methods Summary

Here's a summary of common dictionary methods:

*   `clear()`: Removes all items from the dictionary.
*   `copy()`: Returns a shallow copy of the dictionary.
*   `fromkeys(seq[, value])`: Creates a new dictionary with keys from `seq` and values set to `value` (defaults to `None`). (Class method).
*   `get(key[, default])`: Returns the value for `key` if `key` is in the dictionary, else `default`.
*   `items()`: Returns a view object displaying a list of a dictionary's key-value tuple pairs.
*   `keys()`: Returns a view object displaying a list of all the keys.
*   `pop(key[, default])`: Removes the specified key and returns the corresponding value. If the key is not found, `default` is returned if given, otherwise `KeyError` is raised.
*   `popitem()`: Removes and returns a (key, value) pair as a 2-tuple. Pairs are returned in LIFO order (last in, first out) as of Python 3.7. Raises `KeyError` if the dictionary is empty.
*   `setdefault(key[, default])`: If `key` is in the dictionary, return its value. If not, insert `key` with a value of `default` and return `default`. `default` defaults to `None`.
*   `update([other])`: Updates the dictionary with the key/value pairs from `other`, overwriting existing keys. `other` can be another dictionary, an iterable of key-value pairs, or keyword arguments.
*   `values()`: Returns a view object displaying a list of all the values.

```python
# Example of setdefault
person = {'name': 'Ivy', 'age': 29}
city = person.setdefault('city', 'Unknown')
print(f"City (setdefault): {city}") # Output: Unknown
print(f"Person after setdefault: {person}") # Output: {'name': 'Ivy', 'age': 29, 'city': 'Unknown'}

name = person.setdefault('name', 'DefaultName')
print(f"Name (setdefault existing): {name}") # Output: Ivy
print(f"Person after setdefault (existing): {person}") # Output: {'name': 'Ivy', 'age': 29, 'city': 'Unknown'}

# Example of fromkeys
keys = ['a', 'b', 'c']
default_value = 0
new_dict = dict.fromkeys(keys, default_value)
print(f"Dict fromkeys: {new_dict}") # Output: {'a': 0, 'b': 0, 'c': 0}

new_dict_none = dict.fromkeys(keys)
print(f"Dict fromkeys (None): {new_dict_none}") # Output: {'a': None, 'b': None, 'c': None}
```

## 8. Nested Dictionaries

Dictionaries can contain other dictionaries as values. This allows for creating complex, hierarchical data structures.

```python
users = {
    'user1': {
        'name': 'Alice',
        'email': 'alice@example.com',
        'permissions': {'read': True, 'write': False}
    },
    'user2': {
        'name': 'Bob',
        'email': 'bob@example.com',
        'permissions': {'read': True, 'write': True}
    }
}

# Accessing nested elements
print(f"User1 Name: {users['user1']['name']}")
print(f"User2 Write Permission: {users['user2']['permissions']['write']}")

# Modifying a nested value
users['user1']['email'] = 'alice.new@example.com'
print(f"User1 updated email: {users['user1']['email']}")
```

## 9. Key Characteristics and Considerations

*   **Uniqueness of Keys:** Dictionary keys *must* be unique within a single dictionary. If you assign a value to an existing key, it overwrites the previous value.
*   **Immutability of Keys:** Keys must be of an immutable type. This means you can use strings, numbers, or tuples (if the tuple contains only immutable elements) as keys. You cannot use lists or other dictionaries as keys because they are mutable.
*   **Mutability of Dictionaries:** Dictionaries themselves are mutable. You can change them after creation.
*   **Order (Python 3.7+):** Remember that insertion order is preserved in modern Python versions. This can be important if the order of items matters for your application.
*   **Shallow Copies:** The `copy()` method and `dict(other_dict)` create *shallow* copies. This means the new dictionary is a separate object, but if the values are mutable objects (like lists or other dictionaries), both the original and the copy will refer to the *same* mutable objects. Modifying these nested objects in one dictionary will affect the other. For a fully independent copy, use `copy.deepcopy()`.

```python
import copy

original = {'a': 1, 'b': [10, 20]}

# Shallow copy
shallow = original.copy()
shallow['a'] = 2
shallow['b'].append(30)

print(f"Original after shallow copy mod: {original}") # Output: {'a': 1, 'b': [10, 20, 30]} (Note 'b' changed)
print(f"Shallow copy: {shallow}")                   # Output: {'a': 2, 'b': [10, 20, 30]}

# Deep copy
original = {'a': 1, 'b': [10, 20]} # Reset original
deep = copy.deepcopy(original)
deep['a'] = 3
deep['b'].append(40)

print(f"Original after deep copy mod: {original}") # Output: {'a': 1, 'b': [10, 20]} (Unaffected)
print(f"Deep copy: {deep}")                     # Output: {'a': 3, 'b': [10, 20, 40]}
```

## 10. When to Use Dictionaries

Dictionaries are incredibly useful in many programming scenarios:

*   **Representing structured data:** Like JSON objects, configuration files, or database records.
*   **Fast lookups:** When you need to quickly retrieve a value based on a unique identifier (the key).
*   **Counting frequencies:** Using items as keys and their counts as values.
*   **Grouping data:** Using a common attribute as a key and lists of items with that attribute as values.
*   **Implementing caches:** Storing results of expensive computations with input parameters as keys.

Dictionaries are a fundamental and versatile data structure in Python, essential for efficient data management and manipulation.