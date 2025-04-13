import json

import datetime # Import datetime to demonstrate handling non-serializable types

print("--- JSON Module Examples ---")

# JSON (JavaScript Object Notation) is a lightweight data-interchange format.
# It is easy for humans to read and write and easy for machines to parse and generate.
# The `json` module in Python provides the necessary tools to work with JSON data.

# --- Python Data Types and their JSON Equivalents ---
# Python          | JSON
# ----------------|-----------------
# dict            | object
# list, tuple     | array
# str             | string
# int, float      | number
# True            | true
# False           | false
# None            | null

# --- 1. Encoding Python Objects to JSON Strings (Serialization) ---
print("\n--- 1. Encoding Python Objects to JSON (Serialization) ---")

# Example Python dictionary
python_dict = {
    "name": "Alice",
    "age": 30,
    "isStudent": False,
    "courses": ["Math", "Science"],
    "address": {
        "street": "123 Main St",
        "city": "Anytown"
    },
    "grades": None
}
print(f"Original Python Dictionary:\n{python_dict}")

# Use json.dumps() to convert a Python object into a JSON formatted string.
# 'dumps' stands for "dump string".
json_string = json.dumps(python_dict)
print(f"\nConverted JSON String (compact):\n{json_string}")
print(f"Type of json_string: {type(json_string)}") # It's a string!

# --- Pretty-Printing JSON with Indentation ---
# You can make the JSON string more readable using the 'indent' parameter.
# It specifies the number of spaces for indentation.
json_string_pretty = json.dumps(python_dict, indent=4)
print(f"\nConverted JSON String (pretty-printed with indent=4):\n{json_string_pretty}")

# --- Sorting Keys ---
# You can sort the keys of the JSON object alphabetically using 'sort_keys=True'.
json_string_sorted = json.dumps(python_dict, indent=4, sort_keys=True)
print(f"\nConverted JSON String (pretty-printed, keys sorted):\n{json_string_sorted}")

# Example Python list
python_list = [1, "hello", 3.14, True, None, {"key": "value"}]
print(f"\nOriginal Python List:\n{python_list}")

json_array_string = json.dumps(python_list, indent=2) # Indent arrays too
print(f"\nConverted JSON Array String (pretty-printed):\n{json_array_string}")

# --- 2. Decoding JSON Strings to Python Objects (Deserialization) ---
print("\n--- 2. Decoding JSON to Python Objects (Deserialization) ---")

# Use json.loads() to parse a JSON string and convert it back into a Python object.
# 'loads' stands for "load string".
json_data_string = '{"name": "Bob", "age": 25, "city": "Otherville", "hobbies": ["Reading", "Hiking"]}'
print(f"\nJSON String to decode:\n{json_data_string}")

python_object = json.loads(json_data_string)
print(f"\nDecoded Python Object:\n{python_object}")
print(f"Type of decoded object: {type(python_object)}") # It's a dict
print(f"Accessing data: Name = {python_object['name']}")

json_array_str = '[10, 20, "apple", false, null]'
print(f"\nJSON Array String to decode:\n{json_array_str}")
python_list_obj = json.loads(json_array_str)
print(f"\nDecoded Python List:\n{python_list_obj}")
print(f"Type of decoded object: {type(python_list_obj)}") # It's a list
print(f"Accessing data: First element = {python_list_obj[0]}")


# --- 3. Working with JSON Files ---
print("\n--- 3. Working with JSON Files ---")

# --- Writing Python data to a JSON file (json.dump) ---
# Use json.dump() to write a Python object directly to a file-like object (e.g., a file).
# 'dump' (without 's') works with file objects.
file_path = 'data.json'
data_to_write = {
    "id": "user123",
    "timestamp": "2023-10-27T10:00:00Z",
    "data": [15, 25, 35],
    "metadata": {"source": "sensorA", "valid": True}
}

try:
    with open(file_path, 'w', encoding='utf-8') as f:
        # Write data_to_write to the file 'f' as JSON
        # Use indent for readability in the file
        json.dump(data_to_write, f, indent=4)
    print(f"\nSuccessfully wrote Python data to '{file_path}'")
except IOError as e:
    print(f"Error writing to file {file_path}: {e}")

# --- Reading JSON data from a file (json.load) ---
# Use json.load() to read JSON data from a file-like object and parse it into a Python object.
# 'load' (without 's') works with file objects.
try:
    with open(file_path, 'r', encoding='utf-8') as f:
        # Load the JSON data from file 'f' into a Python object
        loaded_data = json.load(f)
    print(f"\nSuccessfully loaded data from '{file_path}':")
    print(loaded_data)
    print(f"Type of loaded data: {type(loaded_data)}")
    print(f"Accessing loaded data: ID = {loaded_data.get('id', 'N/A')}") # Use .get for safer access
except FileNotFoundError:
    print(f"Error: File '{file_path}' not found.")
except json.JSONDecodeError as e:
    print(f"Error decoding JSON from file {file_path}: {e}")
except IOError as e:
    print(f"Error reading file {file_path}: {e}")


# --- 4. Handling Errors ---
print("\n--- 4. Handling Errors ---")

# --- Invalid JSON String ---
invalid_json_string = '{"name": "Charlie", "age": 40,}' # Trailing comma is invalid in standard JSON
print(f"\nAttempting to decode invalid JSON: {invalid_json_string}")
try:
    python_obj_error = json.loads(invalid_json_string)
    print(f"Decoded object: {python_obj_error}")
except json.JSONDecodeError as e:
    # This block will execute because the JSON is invalid
    print(f"Caught JSONDecodeError: {e}")

# --- Non-Serializable Types ---
# Some Python objects (like sets, complex numbers, datetime objects) are not directly serializable to JSON by default.
non_serializable_data = {
    "name": "David",
    "meeting_time": datetime.datetime.now(), # datetime objects are not JSON serializable
    "unique_numbers": {1, 2, 3} # sets are not JSON serializable
}
print(f"\nAttempting to serialize non-standard types: {non_serializable_data}")
try:
    json_string_error = json.dumps(non_serializable_data, indent=4)
    print(json_string_error)
except TypeError as e:
    # This block will execute
    print(f"Caught TypeError: {e}")
    print("Hint: You might need a custom encoder/decoder or convert types manually (e.g., datetime to string).")

# --- Simple workaround for datetime (convert to string) ---
serializable_data = {
    "name": "David",
    "meeting_time": str(datetime.datetime.now()), # Convert datetime to string
    "unique_numbers": list({1, 2, 3}) # Convert set to list
}
print(f"\nAttempting to serialize converted types: {serializable_data}")
try:
    json_string_fixed = json.dumps(serializable_data, indent=4)
    print(f"Successfully serialized after conversion:\n{json_string_fixed}")
except TypeError as e:
    print(f"Caught TypeError even after conversion: {e}") # Should not happen now


# For more complex scenarios involving custom objects, you might explore the `default`
# parameter in `json.dumps` and the `object_hook` parameter in `json.loads`.

print("\n--- End of JSON Module Examples ---")