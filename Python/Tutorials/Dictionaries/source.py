import copy

# Dictionaries in Python
# A dictionary is an unordered collection of data values, used to store data values like a map,
# which, unlike other Data Types that hold only a single value as an element,
# Dictionary holds key:value pair. Key-value is provided in the dictionary to make it more optimized.

# Note: Dictionary keys must be immutable (like strings, numbers, or tuples with immutable elements).
# Values can be of any data type.
# Dictionaries are mutable, meaning they can be changed after creation.
# As of Python 3.7, dictionaries are ordered. In earlier versions (3.6 and below), they were unordered.

print("--- 1. Creating Dictionaries ---")

# a) Creating an empty dictionary
empty_dict = {}
print(f"Empty dictionary: {empty_dict}, type: {type(empty_dict)}")

empty_dict_constructor = dict()
print(f"Empty dictionary using dict(): {empty_dict_constructor}, type: {type(empty_dict_constructor)}")

# b) Creating a dictionary with initial items
# Keys are typically strings or numbers. Values can be anything.
student = {
    "name": "Alice",
    "age": 20,
    "major": "Computer Science",
    "courses": ["Math", "Physics", "Programming"]
}
print(f"Student dictionary: {student}")

# Dictionary with mixed key types (less common but possible)
mixed_dict = {
    "name": "Bob",
    1: "ID Number",
    ("city", "zip"): ("New York", 10001) # Using a tuple as a key
}
print(f"Mixed key types dictionary: {mixed_dict}")

# c) Creating a dictionary using the dict() constructor
# From keyword arguments (keys must be valid identifiers)
person = dict(name="Charlie", age=30, city="London")
print(f"Dictionary from keyword args: {person}")

# From a list of key-value tuples
pairs = [("fruit", "apple"), ("color", "red")]
fruit_dict = dict(pairs)
print(f"Dictionary from list of tuples: {fruit_dict}")


print("\n--- 2. Accessing Elements ---")

# a) Using square bracket notation []
# If the key exists, it returns the value.
# If the key does NOT exist, it raises a KeyError.
print(f"Student's name: {student['name']}")
print(f"Student's age: {student['age']}")
# print(student['gpa']) # This would cause a KeyError because 'gpa' doesn't exist

# b) Using the .get() method
# If the key exists, it returns the value.
# If the key does NOT exist, it returns None (by default) or a specified default value.
print(f"Student's major using get(): {student.get('major')}")
print(f"Student's GPA using get() (key doesn't exist): {student.get('gpa')}") # Returns None
print(f"Student's GPA using get() with default: {student.get('gpa', 'Not Available')}") # Returns 'Not Available'


print("\n--- 3. Adding and Updating Elements ---")

# a) Using square bracket notation []
# If the key exists, it updates the value.
# If the key does NOT exist, it adds the new key-value pair.
print(f"Original student dict: {student}")

# Add a new key-value pair
student['gpa'] = 3.8
print(f"Student dict after adding GPA: {student}")

# Update an existing value
student['age'] = 21 # Alice had a birthday!
print(f"Student dict after updating age: {student}")

# b) Using the .update() method
# Merges the dictionary with another dictionary or an iterable of key-value pairs.
# If keys overlap, the values from the dictionary being passed to update() will overwrite existing values.
print(f"Original person dict: {person}")

# Update with another dictionary
person_updates = {"city": "Manchester", "occupation": "Engineer"}
person.update(person_updates)
print(f"Person dict after update(): {person}")

# Update with an iterable of key-value pairs (e.g., a list of tuples)
person.update([("email", "charlie@example.com"), ("age", 31)])
print(f"Person dict after update() with list: {person}")


print("\n--- 4. Removing Elements ---")

# a) Using the `del` keyword
# Removes the item with the specified key.
# Raises a KeyError if the key does not exist.
print(f"Original student dict: {student}")
del student['gpa']
print(f"Student dict after deleting GPA: {student}")
# del student['gpa'] # This would now raise a KeyError

# b) Using the .pop() method
# Removes the item with the specified key AND returns its value.
# Raises a KeyError if the key does not exist, unless a default value is provided.
print(f"Original person dict: {person}")
removed_occupation = person.pop("occupation")
print(f"Removed occupation using pop(): {removed_occupation}")
print(f"Person dict after pop('occupation'): {person}")

# Using pop() with a default value for a non-existent key
removed_hobby = person.pop("hobby", "No hobby specified")
print(f"Result of pop('hobby') with default: {removed_hobby}")
print(f"Person dict remains unchanged: {person}")
# removed_hobby_error = person.pop("hobby") # This would raise a KeyError

# c) Using the .popitem() method
# Removes and returns the last inserted key-value pair as a tuple.
# Before Python 3.7, it removed an arbitrary pair.
# Raises a KeyError if the dictionary is empty.
print(f"Original fruit dict: {fruit_dict}")
last_item = fruit_dict.popitem()
print(f"Removed item using popitem(): {last_item}")
print(f"Fruit dict after popitem(): {fruit_dict}")

# Add another item and pop again
fruit_dict['taste'] = 'sweet'
print(f"Fruit dict after adding taste: {fruit_dict}")
last_item_again = fruit_dict.popitem()
print(f"Removed item using popitem() again: {last_item_again}")
print(f"Fruit dict after second popitem(): {fruit_dict}")

# d) Using the .clear() method
# Removes all items from the dictionary, making it empty.
print(f"Original mixed_dict: {mixed_dict}")
mixed_dict.clear()
print(f"Mixed_dict after clear(): {mixed_dict}")


print("\n--- 5. Iterating Through Dictionaries ---")

# Recreate a sample dictionary
inventory = {"apples": 10, "bananas": 5, "oranges": 8}
print(f"Inventory: {inventory}")

# a) Iterating through keys (default iteration behavior)
print("Iterating through keys:")
for item_key in inventory: # Same as iterating over inventory.keys()
    print(f"  Key: {item_key}, Value: {inventory[item_key]}")

# b) Iterating through values using .values()
print("Iterating through values:")
for quantity in inventory.values():
    print(f"  Value: {quantity}")

# c) Iterating through key-value pairs using .items()
print("Iterating through key-value pairs (items):")
for key, value in inventory.items():
    print(f"  Key: {key}, Value: {value}")


print("\n--- 6. Dictionary Methods and Operations ---")

# a) .keys(), .values(), .items() - Return view objects
# View objects reflect changes in the dictionary.
print(f"Inventory keys view: {inventory.keys()}")
print(f"Inventory values view: {inventory.values()}")
print(f"Inventory items view: {inventory.items()}")

# Demonstrate view object updates
keys_view = inventory.keys()
print(f"Keys view before adding 'pears': {keys_view}")
inventory['pears'] = 12
print(f"Keys view after adding 'pears': {keys_view}") # The view updates automatically

# b) len() - Get the number of key-value pairs
print(f"Number of items in inventory: {len(inventory)}")

# c) `in` and `not in` - Check for key existence
print(f"Is 'apples' in inventory? {'apples' in inventory}")
print(f"Is 'grapes' in inventory? {'grapes' in inventory}")
print(f"Is 'bananas' not in inventory? {'bananas' not in inventory}")

# Note: `in` checks for keys, not values. To check for values:
print(f"Is the value 5 in inventory values? {5 in inventory.values()}")

# d) .copy() - Create a shallow copy
# A shallow copy creates a new dictionary, but the values are references to the original objects.
# If values are mutable (like lists), changes in the original list will reflect in the copy.
original_dict = {"a": 1, "b": [10, 20]}
shallow_copy = original_dict.copy()

print(f"Original dictionary: {original_dict}")
print(f"Shallow copy: {shallow_copy}")

# Modify the copy
shallow_copy["a"] = 100
shallow_copy["b"].append(30) # Modify the list within the copy

print(f"Original dictionary after modifying copy: {original_dict}") # Note 'b' changed!
print(f"Shallow copy after modifications: {shallow_copy}")

# To create a deep copy (copying nested mutable objects as well), use the `copy` module:
deep_copy = copy.deepcopy(original_dict)
deep_copy["b"].append(40) # Modify the list within the deep copy
print(f"Original dictionary after modifying deep copy: {original_dict}") # 'b' is unchanged
print(f"Deep copy after modification: {deep_copy}")

# e) dict.fromkeys(iterable, value=None) - Create a new dictionary with keys from iterable and values set to value.
keys = ['x', 'y', 'z']
default_value = 0
new_dict_from_keys = dict.fromkeys(keys, default_value)
print(f"Dictionary from keys with default value: {new_dict_from_keys}")

new_dict_from_keys_none = dict.fromkeys(keys) # Default value is None
print(f"Dictionary from keys with None value: {new_dict_from_keys_none}")


print("\n--- 7. Dictionary Comprehensions ---")
# A concise way to create dictionaries.
# Syntax: {key_expression: value_expression for item in iterable if condition}

# Create a dictionary of squares
numbers = [1, 2, 3, 4, 5]
squares_dict = {num: num**2 for num in numbers}
print(f"Dictionary of squares: {squares_dict}")

# Create a dictionary from two lists
keys = ["name", "age", "city"]
values = ["David", 25, "Paris"]
person_info = {keys[i]: values[i] for i in range(len(keys))}
print(f"Dictionary from two lists: {person_info}")

# Create a dictionary with a condition
original_scores = {"Alice": 85, "Bob": 92, "Charlie": 78, "David": 95}
passing_scores = {name: score for name, score in original_scores.items() if score >= 90}
print(f"Original scores: {original_scores}")
print(f"Passing scores (>= 90): {passing_scores}")


print("\n--- 8. Nested Dictionaries ---")
# Dictionaries can contain other dictionaries as values.

students_data = {
    "student1": {
        "name": "Eve",
        "major": "Biology",
        "grades": {"Math": "A", "Bio": "A+"}
    },
    "student2": {
        "name": "Frank",
        "major": "History",
        "grades": {"History": "B+", "English": "A-"}
    }
}

print(f"Nested students data: {students_data}")

# Accessing nested elements
print(f"Student 1's name: {students_data['student1']['name']}")
print(f"Student 2's Math grade: {students_data['student2']['grades']['English']}")

# Adding data to a nested dictionary
students_data['student1']['grades']['Chemistry'] = 'B'
print(f"Updated Student 1 grades: {students_data['student1']['grades']}")

print("\n--- Dictionary Summary ---")
print("Dictionaries store key-value pairs.")
print("Keys must be immutable.")
print("Values can be any type.")
print("Dictionaries are mutable.")
print("As of Python 3.7+, dictionaries maintain insertion order.")
print("Use [] for access/add/update (KeyError if key missing on access).")
print("Use .get() for safe access (returns None or default if key missing).")
print("Use del, .pop(), .popitem(), .clear() for removal.")
print("Iterate using keys (default), .values(), or .items().")
print("Dictionary comprehensions offer a concise way to create dictionaries.")