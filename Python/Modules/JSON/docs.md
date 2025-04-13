# Python `json` Module: Working with JSON Data

## 1. Introduction to JSON

**What is JSON?**

JSON stands for **J**ava**S**cript **O**bject **N**otation. It's a lightweight, text-based data interchange format that is easy for humans to read and write, and easy for machines to parse and generate.

Even though it originated from JavaScript, JSON is language-independent and widely used across different programming languages and platforms for:

*   **Configuration files:** Storing application settings.
*   **APIs (Application Programming Interfaces):** Exchanging data between web servers and clients (like web browsers or mobile apps).
*   **Data Storage:** Storing structured data in files or databases.

**JSON Structure:**

JSON data is built on two main structures:

1.  **Objects:** An unordered collection of key/value pairs.
    *   Keys must be strings (enclosed in double quotes).
    *   Values can be strings, numbers, booleans (`true`/`false`), `null`, arrays, or other JSON objects.
    *   Enclosed in curly braces `{}`.
    *   Example: `{"name": "Alice", "age": 30, "isStudent": false}`
2.  **Arrays:** An ordered list of values.
    *   Values can be any valid JSON data type (strings, numbers, booleans, `null`, objects, or other arrays).
    *   Enclosed in square brackets `[]`.
    *   Example: `["apple", "banana", "cherry"]` or `[1, {"id": 2}, true]`

**JSON Data Types vs. Python Data Types:**

| JSON Type     | Python Type        |
| :------------ | :----------------- |
| object        | `dict`             |
| array         | `list`             |
| string        | `str`              |
| number (int)  | `int`              |
| number (real) | `float`            |
| `true`        | `True`             |
| `false`       | `False`            |
| `null`        | `None`             |

## 2. The Python `json` Module

Python has a built-in module called `json` that makes it very easy to work with JSON data. You don't need to install anything extra; just import it:

```python
import json
```

The `json` module primarily provides two sets of functions:

1.  **Serialization (Encoding):** Converting Python objects into JSON formatted strings or writing them to files.
    *   `json.dumps()`: Serializes a Python object to a JSON formatted string.
    *   `json.dump()`: Serializes a Python object and writes it to a file-like object (e.g., a file).
2.  **Deserialization (Decoding):** Parsing JSON formatted strings or reading JSON data from files and converting them back into Python objects.
    *   `json.loads()`: Deserializes a JSON formatted string into a Python object.
    *   `json.load()`: Reads JSON data from a file-like object and deserializes it into a Python object.

## 3. Serialization: Python to JSON

### `json.dumps()` - Python Object to JSON String

This function takes a Python object (like a dictionary or list) and returns its JSON string representation.

```python
import json

# Example Python dictionary
python_dict = {
    "name": "Bob",
    "age": 25,
    "city": "New York",
    "isProgrammer": True,
    "skills": ["Python", "JavaScript", "SQL"],
    "projects": None
}

# Convert the Python dictionary to a JSON string
json_string = json.dumps(python_dict)

print("--- Original Python Dictionary ---")
print(python_dict)
print(type(python_dict))

print("\n--- JSON String Representation ---")
print(json_string)
print(type(json_string))
```

**Output:**

```
--- Original Python Dictionary ---
{'name': 'Bob', 'age': 25, 'city': 'New York', 'isProgrammer': True, 'skills': ['Python', 'JavaScript', 'SQL'], 'projects': None}
<class 'dict'>

--- JSON String Representation ---
{"name": "Bob", "age": 25, "city": "New York", "isProgrammer": true, "skills": ["Python", "JavaScript", "SQL"], "projects": null}
<class 'str'>
```

Notice the differences:
*   `True` becomes `true`.
*   `None` becomes `null`.
*   The output is a single string.

**Making JSON Readable with `indent` and `sort_keys`:**

The default output of `json.dumps()` is compact but hard to read. You can use arguments to format it nicely:

*   `indent`: Specifies the number of spaces for indentation per level.
*   `sort_keys=True`: Sorts the keys in JSON objects alphabetically.

```python
import json

python_dict = {
    "name": "Bob",
    "age": 25,
    "city": "New York",
    "isProgrammer": True,
    "skills": ["Python", "JavaScript", "SQL"],
    "projects": None
}

# Convert with indentation and sorted keys
readable_json_string = json.dumps(python_dict, indent=4, sort_keys=True)

print("\n--- Readable JSON String ---")
print(readable_json_string)
```

**Output:**

```
--- Readable JSON String ---
{
    "age": 25,
    "city": "New York",
    "isProgrammer": true,
    "name": "Bob",
    "projects": null,
    "skills": [
        "Python",
        "JavaScript",
        "SQL"
    ]
}
```

### `json.dump()` - Python Object to JSON File

This function is similar to `dumps()`, but instead of returning a string, it writes the JSON data directly to a *file-like object*. This is useful for saving configurations or data.

```python
import json

python_data = {
    "id": "user123",
    "preferences": {
        "theme": "dark",
        "notifications": True
    },
    "last_login": "2023-10-27T10:00:00Z"
}

# Open a file in write mode ('w')
# 'with' ensures the file is automatically closed even if errors occur
with open("config.json", "w") as json_file:
    # Write the python_data to the file as JSON, with indentation
    json.dump(python_data, json_file, indent=4)

print("Data successfully written to config.json")
```

After running this code, a file named `config.json` will be created (or overwritten) in the same directory with the following content:

```json
{
    "id": "user123",
    "preferences": {
        "theme": "dark",
        "notifications": true
    },
    "last_login": "2023-10-27T10:00:00Z"
}
```

## 4. Deserialization: JSON to Python

### `json.loads()` - JSON String to Python Object

This function takes a JSON formatted string and parses it, returning the corresponding Python object.

```python
import json

# Example JSON string (often received from APIs or read from simple sources)
json_data_string = '''
{
    "productName": "Laptop",
    "price": 1200.50,
    "inStock": true,
    "specs": {
        "cpu": "Intel i7",
        "ram": 16
    },
    "tags": ["electronics", "computer", "office"]
}
'''

# Convert the JSON string back into a Python object (usually a dictionary)
python_object = json.loads(json_data_string)

print("--- Original JSON String ---")
print(json_data_string)
print(type(json_data_string))

print("\n--- Deserialized Python Object ---")
print(python_object)
print(type(python_object))

# You can now access data like a normal Python dictionary/list
print("\n--- Accessing Data ---")
print(f"Product Name: {python_object['productName']}")
print(f"Price: {python_object['price']}")
print(f"CPU: {python_object['specs']['cpu']}")
print(f"First Tag: {python_object['tags'][0]}")
```

**Output:**

```
--- Original JSON String ---

{
    "productName": "Laptop",
    "price": 1200.50,
    "inStock": true,
    "specs": {
        "cpu": "Intel i7",
        "ram": 16
    },
    "tags": ["electronics", "computer", "office"]
}

<class 'str'>

--- Deserialized Python Object ---
{'productName': 'Laptop', 'price': 1200.5, 'inStock': True, 'specs': {'cpu': 'Intel i7', 'ram': 16}, 'tags': ['electronics', 'computer', 'office']}
<class 'dict'>

--- Accessing Data ---
Product Name: Laptop
Price: 1200.5
CPU: Intel i7
First Tag: electronics
```

Notice the conversions:
*   `true` becomes `True`.
*   `null` (if present) would become `None`.
*   Numbers become `int` or `float`.
*   JSON objects become Python `dict`.
*   JSON arrays become Python `list`.

### `json.load()` - JSON File to Python Object

This function reads JSON data from a *file-like object* and deserializes it into a Python object. It's the counterpart to `json.dump()`.

Let's read the `config.json` file we created earlier:

```python
import json

# Make sure 'config.json' exists from the previous json.dump() example

try:
    # Open the file in read mode ('r')
    with open("config.json", "r") as json_file:
        # Load the JSON data from the file into a Python object
        loaded_data = json.load(json_file)

    print("--- Data loaded from config.json ---")
    print(loaded_data)
    print(type(loaded_data))

    # Access the loaded data
    print("\n--- Accessing Loaded Data ---")
    print(f"User ID: {loaded_data['id']}")
    print(f"Theme Preference: {loaded_data['preferences']['theme']}")

except FileNotFoundError:
    print("Error: config.json not found. Make sure you ran the json.dump() example first.")
except json.JSONDecodeError as e:
    print(f"Error decoding JSON from the file: {e}")

```

**Output (assuming `config.json` exists and is valid):**

```
--- Data loaded from config.json ---
{'id': 'user123', 'preferences': {'theme': 'dark', 'notifications': True}, 'last_login': '2023-10-27T10:00:00Z'}
<class 'dict'>

--- Accessing Loaded Data ---
User ID: user123
Theme Preference: dark
```

**Error Handling:** It's good practice to wrap `json.load()` and `json.loads()` in `try...except` blocks to handle potential errors like the file not existing (`FileNotFoundError`) or the file containing invalid JSON (`json.JSONDecodeError`).

## 5. Handling Non-Serializable Types

The `json` module can only directly serialize basic Python types (dict, list, tuple, str, int, float, bool, None). If you try to serialize other types like sets, custom objects, or dates, you'll get a `TypeError`.

```python
import json
import datetime

my_set = {1, 2, 3}
now = datetime.datetime.now()

data_with_unsupported_types = {
    "a_set": my_set,
    "current_time": now
}

try:
    json_string = json.dumps(data_with_unsupported_types, indent=4)
    print(json_string)
except TypeError as e:
    print(f"TypeError: {e}")
    # Output: TypeError: Object of type set is not JSON serializable (or similar for datetime)
```

For beginners, the simplest way to handle this is to convert unsupported types to supported types *before* serialization:

```python
import json
import datetime

my_set = {1, 2, 3}
now = datetime.datetime.now()

# Convert unsupported types manually
data_prepared_for_json = {
    "a_list_from_set": list(my_set),  # Convert set to list
    "current_time_iso": now.isoformat() # Convert datetime to ISO string
}

json_string = json.dumps(data_prepared_for_json, indent=4)
print(json_string)
```

**Output:**

```json
{
    "a_list_from_set": [
        1,
        2,
        3
    ],
    "current_time_iso": "2023-10-27T12:34:56.789012" # Example timestamp
}
```

(Note: More advanced techniques involve using the `default` argument in `dumps`/`dump` or creating custom JSON encoders/decoders, but manual conversion is often sufficient for simple cases.)

## 6. Summary

*   **JSON** is a human-readable text format for data exchange.
*   Python's `json` module provides tools to work with JSON.
*   **Serialization (Python -> JSON):**
    *   `json.dumps(obj)`: Converts a Python object `obj` to a JSON string.
    *   `json.dump(obj, file)`: Writes the Python object `obj` as JSON to a `file`.
    *   Use `indent` and `sort_keys` arguments for readability.
*   **Deserialization (JSON -> Python):**
    *   `json.loads(json_string)`: Parses a `json_string` into a Python object.
    *   `json.load(file)`: Reads JSON data from a `file` and parses it into a Python object.
*   Handle potential `FileNotFoundError` and `json.JSONDecodeError` when working with files and parsing.
*   Convert non-standard Python types (like sets or datetimes) to JSON-compatible types (like lists or strings) before serializing.