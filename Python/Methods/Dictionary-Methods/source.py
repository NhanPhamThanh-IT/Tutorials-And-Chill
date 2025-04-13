# Dictionary Methods in Python - Detailed Examples for Beginners

# Dictionaries are used to store data values in key:value pairs.
# A dictionary is a collection which is ordered*, changeable and does not allow duplicate keys.
# *As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.

# Let's start with a sample dictionary
print("--- Initial Dictionary ---")
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print("Original car dictionary:", car)
print("-" * 20)

# 1. clear() - Removes all the elements from the dictionary
print("--- 1. clear() ---")
temp_car_clear = car.copy() # Create a copy to demonstrate clear() without affecting later examples
print("Dictionary before clear():", temp_car_clear)
temp_car_clear.clear()
print("Dictionary after clear():", temp_car_clear)
print("-" * 20)

# 2. copy() - Returns a shallow copy of the dictionary
print("--- 2. copy() ---")
car_copy = car.copy()
print("Original car dictionary:", car)
print("Copied car dictionary:", car_copy)
# Modifying the copy doesn't affect the original
car_copy["year"] = 2023
print("Modified copy:", car_copy)
print("Original after modifying copy:", car)
print("-" * 20)

# 3. fromkeys() - Returns a dictionary with the specified keys and value.
# Creates a new dictionary from the given sequence of keys.
# You can optionally specify a value for all keys (default is None).
print("--- 3. fromkeys() ---")
keys = ('key1', 'key2', 'key3')
value = 0
# Create a dictionary with keys from the 'keys' tuple and value 0 for all
dict_from_keys = dict.fromkeys(keys, value)
print("Keys:", keys)
print("Value:", value)
print("Dictionary created using fromkeys():", dict_from_keys)

# If value is not specified, it defaults to None
dict_from_keys_no_value = dict.fromkeys(keys)
print("Dictionary created using fromkeys() with default value (None):", dict_from_keys_no_value)
print("-" * 20)

# 4. get() - Returns the value of the specified key.
# It's safer than using square brackets [] because it doesn't raise an error
# if the key is not found. Instead, it returns None (or a specified default value).
print("--- 4. get() ---")
print("Original car dictionary:", car)
# Get the value for the key 'model'
model_value = car.get("model")
print("Value for key 'model':", model_value)

# Try to get the value for a key that doesn't exist ('color')
color_value = car.get("color")
print("Value for key 'color' (doesn't exist):", color_value) # Output: None

# Get the value for 'color', but specify a default value if it's not found
color_value_default = car.get("color", "Not specified")
print("Value for key 'color' with default 'Not specified':", color_value_default)

# Compare with using square brackets (will raise KeyError if key not found)
print("Value for key 'brand' using []:", car["brand"])
# print(car["color"]) # This line would cause a KeyError
print("-" * 20)

# 5. items() - Returns a view object that displays a list of a dictionary's key-value tuple pairs.
# This view object updates automatically when the dictionary changes.
print("--- 5. items() ---")
print("Original car dictionary:", car)
car_items = car.items()
print("Items (key-value pairs) in the dictionary:", car_items)
# You can iterate through the items
print("Iterating through items:")
for key, value in car_items:
    print(f"  Key: {key}, Value: {value}")
# If the dictionary changes, the items view reflects the change
car["color"] = "red" # Add a new item
print("Dictionary after adding 'color':", car)
print("Items view after adding 'color':", car_items) # Shows the new item
del car["color"] # Remove the added item for consistency in later examples
print("-" * 20)

# 6. keys() - Returns a view object that displays a list of all the keys in the dictionary.
# This view object updates automatically when the dictionary changes.
print("--- 6. keys() ---")
print("Original car dictionary:", car)
car_keys = car.keys()
print("Keys in the dictionary:", car_keys)
# You can iterate through the keys
print("Iterating through keys:")
for key in car_keys:
    print(f"  Key: {key}")
# If the dictionary changes, the keys view reflects the change
car["owner"] = "John Doe" # Add a new item
print("Dictionary after adding 'owner':", car)
print("Keys view after adding 'owner':", car_keys) # Shows the new key
del car["owner"] # Remove the added item
print("-" * 20)

# 7. pop() - Removes the element with the specified key and returns its value.
# If the key is not found, it raises a KeyError, unless a default value is provided.
print("--- 7. pop() ---")
temp_car_pop = car.copy() # Use a copy for this example
print("Dictionary before pop():", temp_car_pop)
# Remove the item with key 'model' and get its value
popped_value = temp_car_pop.pop("model")
print("Popped value for key 'model':", popped_value)
print("Dictionary after pop('model'):", temp_car_pop)

# Try to pop a key that doesn't exist, providing a default value
popped_nonexistent = temp_car_pop.pop("color", "Key not found")
print("Result of popping non-existent key 'color' with default:", popped_nonexistent)
print("Dictionary remains unchanged:", temp_car_pop)

# Trying to pop a non-existent key without a default would raise KeyError
# temp_car_pop.pop("color") # This would cause a KeyError
print("-" * 20)

# 8. popitem() - Removes the last inserted key-value pair (in Python 3.7+) and returns it as a tuple.
# In earlier Python versions (before 3.7), it removes an arbitrary item.
# Raises KeyError if the dictionary is empty.
print("--- 8. popitem() ---")
temp_car_popitem = car.copy()
temp_car_popitem["added_last"] = "temporary" # Add an item to be the 'last inserted'
print("Dictionary before popitem():", temp_car_popitem)
# Remove and return the last inserted item
last_item = temp_car_popitem.popitem()
print("Popped item (last inserted):", last_item)
print("Dictionary after popitem():", temp_car_popitem)

# Pop another item (which was the last inserted before the previous pop)
next_last_item = temp_car_popitem.popitem()
print("Popped item (next last):", next_last_item)
print("Dictionary after second popitem():", temp_car_popitem)
print("-" * 20)

# 9. setdefault() - Returns the value of the specified key.
# If the key does not exist: insert the key, with the specified value (default is None).
print("--- 9. setdefault() ---")
temp_car_setdefault = car.copy()
print("Dictionary before setdefault():", temp_car_setdefault)

# Get the value for 'model' (key exists)
model_val = temp_car_setdefault.setdefault("model", "F-150")
print("Value returned by setdefault('model', 'F-150'):", model_val) # Returns existing value 'Mustang'
print("Dictionary after setdefault for existing key:", temp_car_setdefault) # Dictionary unchanged

# Try to get value for 'color' (key doesn't exist), set it to 'red'
color_val = temp_car_setdefault.setdefault("color", "red")
print("Value returned by setdefault('color', 'red'):", color_val) # Returns the new value 'red'
print("Dictionary after setdefault for non-existing key:", temp_car_setdefault) # 'color': 'red' is added

# Try to get value for 'mileage' (key doesn't exist), use default value None
mileage_val = temp_car_setdefault.setdefault("mileage")
print("Value returned by setdefault('mileage'):", mileage_val) # Returns None
print("Dictionary after setdefault with default value None:", temp_car_setdefault) # 'mileage': None is added
print("-" * 20)

# 10. update() - Updates the dictionary with the specified key-value pairs.
# It can take another dictionary or an iterable of key-value pairs (like tuples).
# If a key already exists, its value is updated. If the key is new, it's added.
print("--- 10. update() ---")
temp_car_update = car.copy()
print("Dictionary before update():", temp_car_update)

# Update with another dictionary
update_dict = {"year": 2020, "color": "blue"}
print("Updating with dictionary:", update_dict)
temp_car_update.update(update_dict)
print("Dictionary after update() with dict:", temp_car_update) # 'year' updated, 'color' added

# Update with keyword arguments
print("Updating with keyword arguments (owner='Jane Doe', mileage=5000)")
temp_car_update.update(owner="Jane Doe", mileage=5000)
print("Dictionary after update() with kwargs:", temp_car_update) # 'owner' and 'mileage' added/updated
print("-" * 20)

# 11. values() - Returns a view object that displays a list of all the values in the dictionary.
# This view object updates automatically when the dictionary changes.
print("--- 11. values() ---")
print("Original car dictionary:", car) # Back to the original car dict for this example
car_values = car.values()
print("Values in the dictionary:", car_values)
# You can iterate through the values
print("Iterating through values:")
for value in car_values:
    print(f"  Value: {value}")
# If the dictionary changes, the values view reflects the change
car["year"] = 1965 # Modify a value
print("Dictionary after changing 'year':", car)
print("Values view after changing 'year':", car_values) # Shows the updated value
car["year"] = 1964 # Change it back for consistency
print("-" * 20)

print("--- End of Dictionary Methods Examples ---")