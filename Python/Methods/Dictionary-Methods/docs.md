# Python Dictionary Methods

Dictionaries are used to store data values in key:value pairs. They are unordered (in Python versions before 3.7), mutable (changeable), and do not allow duplicate keys. Python provides several built-in methods to work with dictionaries effectively.

Here's a breakdown of common dictionary methods:

---

## 1. `clear()`

*   **Purpose:** Removes all items (key-value pairs) from the dictionary, making it empty.
*   **Syntax:** `dictionary.clear()`
*   **Parameters:** None
*   **Returns:** `None`

*   **Example:**

    ```python
    car = {
      "brand": "Ford",
      "model": "Mustang",
      "year": 1964
    }
    print("Original dictionary:", car)

    car.clear()
    print("Dictionary after clear():", car)
    ```

*   **Output:**

    ```
    Original dictionary: {'brand': 'Ford', 'model': 'Mustang', 'year': 1964}
    Dictionary after clear(): {}
    ```

---

## 2. `copy()`

*   **Purpose:** Creates a shallow copy of the dictionary. This means changes made to the original dictionary *after* the copy is made will not affect the copied dictionary, and vice versa (for immutable values). However, if the dictionary contains mutable objects (like lists), changes to those objects will be reflected in both the original and the copy.
*   **Syntax:** `dictionary.copy()`
*   **Parameters:** None
*   **Returns:** A shallow copy of the dictionary.

*   **Example:**

    ```python
    original = {
      "brand": "Ford",
      "model": "Mustang",
      "year": 1964
    }
    print("Original dictionary:", original)

    copied_dict = original.copy()
    print("Copied dictionary:", copied_dict)

    # Modify the original dictionary
    original["year"] = 2023
    print("Original after modification:", original)
    print("Copied dictionary after original modification:", copied_dict)
    ```

*   **Output:**

    ```
    Original dictionary: {'brand': 'Ford', 'model': 'Mustang', 'year': 1964}
    Copied dictionary: {'brand': 'Ford', 'model': 'Mustang', 'year': 1964}
    Original after modification: {'brand': 'Ford', 'model': 'Mustang', 'year': 2023}
    Copied dictionary after original modification: {'brand': 'Ford', 'model': 'Mustang', 'year': 1964}
    ```

---

## 3. `fromkeys()`

*   **Purpose:** Creates a new dictionary with keys from a specified sequence (like a tuple or list) and assigns a specified value to all of them. If the value is not provided, it defaults to `None`.
*   **Syntax:** `dict.fromkeys(keys, value)`
*   **Parameters:**
    *   `keys`: Required. An iterable (like a list, tuple, string) containing the keys for the new dictionary.
    *   `value`: Optional. The value to assign to all keys. Defaults to `None`.
*   **Returns:** A new dictionary.

*   **Example 1 (with value):**

    ```python
    keys = ('key1', 'key2', 'key3')
    value = 0

    new_dict = dict.fromkeys(keys, value)
    print("Dictionary created with value:", new_dict)
    ```

*   **Output 1:**

    ```
    Dictionary created with value: {'key1': 0, 'key2': 0, 'key3': 0}
    ```

*   **Example 2 (without value):**

    ```python
    keys = ('key1', 'key2', 'key3')

    new_dict_none = dict.fromkeys(keys)
    print("Dictionary created without value:", new_dict_none)
    ```

*   **Output 2:**

    ```
    Dictionary created without value: {'key1': None, 'key2': None, 'key3': None}
    ```

---

## 4. `get()`

*   **Purpose:** Returns the value associated with a specified key. If the key is not found, it returns a default value (`None` if not specified) instead of raising a `KeyError`.
*   **Syntax:** `dictionary.get(keyname, value)`
*   **Parameters:**
    *   `keyname`: Required. The key whose value you want to retrieve.
    *   `value`: Optional. The value to return if the specified key does not exist. Defaults to `None`.
*   **Returns:** The value of the specified key, or the default value if the key is not found.

*   **Example:**

    ```python
    car = {
      "brand": "Ford",
      "model": "Mustang",
      "year": 1964
    }

    # Get value for existing key
    model_value = car.get("model")
    print("Value for 'model':", model_value)

    # Get value for non-existent key (returns None)
    color_value = car.get("color")
    print("Value for 'color':", color_value)

    # Get value for non-existent key with default value
    price_value = car.get("price", "Not available")
    print("Value for 'price':", price_value)
    ```

*   **Output:**

    ```
    Value for 'model': Mustang
    Value for 'color': None
    Value for 'price': Not available
    ```

---

## 5. `items()`

*   **Purpose:** Returns a *view object* that displays a list of a dictionary's key-value tuple pairs. The view object reflects changes made to the dictionary.
*   **Syntax:** `dictionary.items()`
*   **Parameters:** None
*   **Returns:** A view object containing the dictionary's key-value pairs as tuples.

*   **Example:**

    ```python
    car = {
      "brand": "Ford",
      "model": "Mustang",
      "year": 1964
    }

    items_view = car.items()
    print("Original items view:", items_view) # Output shows dict_items object

    # Convert view to list for clearer display
    print("Items as list:", list(items_view))

    # Modify the dictionary
    car["color"] = "red"
    print("Items view after adding 'color':", items_view) # View reflects the change
    ```

*   **Output:**

    ```
    Original items view: dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 1964)])
    Items as list: [('brand', 'Ford'), ('model', 'Mustang'), ('year', 1964)]
    Items view after adding 'color': dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 1964), ('color', 'red')])
    ```

---

## 6. `keys()`

*   **Purpose:** Returns a *view object* that displays a list of all the keys in the dictionary. The view object reflects changes made to the dictionary.
*   **Syntax:** `dictionary.keys()`
*   **Parameters:** None
*   **Returns:** A view object containing the dictionary's keys.

*   **Example:**

    ```python
    car = {
      "brand": "Ford",
      "model": "Mustang",
      "year": 1964
    }

    keys_view = car.keys()
    print("Original keys view:", keys_view) # Output shows dict_keys object

    # Convert view to list for clearer display
    print("Keys as list:", list(keys_view))

    # Modify the dictionary
    car["color"] = "red"
    print("Keys view after adding 'color':", keys_view) # View reflects the change
    ```

*   **Output:**

    ```
    Original keys view: dict_keys(['brand', 'model', 'year'])
    Keys as list: ['brand', 'model', 'year']
    Keys view after adding 'color': dict_keys(['brand', 'model', 'year', 'color'])
    ```

---

## 7. `pop()`

*   **Purpose:** Removes the item with the specified key name and returns its associated value. If the key is not found, it raises a `KeyError` unless a default value is provided.
*   **Syntax:** `dictionary.pop(keyname, defaultvalue)`
*   **Parameters:**
    *   `keyname`: Required. The key of the item to remove.
    *   `defaultvalue`: Optional. The value to return if the specified key does not exist. If not provided and the key is not found, a `KeyError` is raised.
*   **Returns:** The value of the removed item, or the `defaultvalue` if specified and the key is not found.

*   **Example:**

    ```python
    car = {
      "brand": "Ford",
      "model": "Mustang",
      "year": 1964
    }
    print("Original dictionary:", car)

    # Pop an existing key
    removed_model = car.pop("model")
    print("Removed value:", removed_model)
    print("Dictionary after pop('model'):", car)

    # Try to pop a non-existent key with a default value
    removed_color = car.pop("color", "No color specified")
    print("Removed value (default):", removed_color)
    print("Dictionary after pop('color', ...):", car)

    # Try to pop a non-existent key without default (will raise KeyError)
    # removed_price = car.pop("price") # Uncommenting this line causes an error
    ```

*   **Output:**

    ```
    Original dictionary: {'brand': 'Ford', 'model': 'Mustang', 'year': 1964}
    Removed value: Mustang
    Dictionary after pop('model'): {'brand': 'Ford', 'year': 1964}
    Removed value (default): No color specified
    Dictionary after pop('color', ...): {'brand': 'Ford', 'year': 1964}
    ```

---

## 8. `popitem()`

*   **Purpose:** Removes the *last inserted* key-value pair (in Python 3.7+) and returns it as a tuple. In versions before 3.7, it removes an arbitrary item. If the dictionary is empty, it raises a `KeyError`.
*   **Syntax:** `dictionary.popitem()`
*   **Parameters:** None
*   **Returns:** A tuple containing the removed key-value pair.

*   **Example:**

    ```python
    car = {
      "brand": "Ford",
      "model": "Mustang",
      "year": 1964
    }
    print("Original dictionary:", car)

    # Add a new item (which becomes the last inserted)
    car["color"] = "red"
    print("Dictionary after adding color:", car)

    # Pop the last inserted item
    removed_item = car.popitem()
    print("Removed item (key, value):", removed_item)
    print("Dictionary after popitem():", car)

    removed_item_2 = car.popitem()
    print("Removed item 2 (key, value):", removed_item_2)
    print("Dictionary after second popitem():", car)
    ```

*   **Output:**

    ```
    Original dictionary: {'brand': 'Ford', 'model': 'Mustang', 'year': 1964}
    Dictionary after adding color: {'brand': 'Ford', 'model': 'Mustang', 'year': 1964, 'color': 'red'}
    Removed item (key, value): ('color', 'red')
    Dictionary after popitem(): {'brand': 'Ford', 'model': 'Mustang', 'year': 1964}
    Removed item 2 (key, value): ('year', 1964)
    Dictionary after second popitem(): {'brand': 'Ford', 'model': 'Mustang'}
    ```

---

## 9. `setdefault()`

*   **Purpose:** Returns the value of the item with the specified key. If the key does not exist, it inserts the key with a specified default value (or `None` if no value is given) and then returns that default value.
*   **Syntax:** `dictionary.setdefault(keyname, value)`
*   **Parameters:**
    *   `keyname`: Required. The key of the item to search for or insert.
    *   `value`: Optional. The value to insert if the key does not exist. Defaults to `None`.
*   **Returns:** The value of the specified key (either existing or newly inserted).

*   **Example:**

    ```python
    car = {
      "brand": "Ford",
      "model": "Mustang",
      "year": 1964
    }
    print("Original dictionary:", car)

    # Get value for existing key 'model'
    model_value = car.setdefault("model", "Bronco")
    print("Value for 'model':", model_value)
    print("Dictionary after setdefault('model'):", car) # Dictionary unchanged

    # Try to get value for non-existent key 'color', insert default 'red'
    color_value = car.setdefault("color", "red")
    print("Value for 'color':", color_value)
    print("Dictionary after setdefault('color'):", car) # 'color':'red' was added

    # Try to get value for non-existent key 'price', insert default None
    price_value = car.setdefault("price")
    print("Value for 'price':", price_value)
    print("Dictionary after setdefault('price'):", car) # 'price':None was added
    ```

*   **Output:**

    ```
    Original dictionary: {'brand': 'Ford', 'model': 'Mustang', 'year': 1964}
    Value for 'model': Mustang
    Dictionary after setdefault('model'): {'brand': 'Ford', 'model': 'Mustang', 'year': 1964}
    Value for 'color': red
    Dictionary after setdefault('color'): {'brand': 'Ford', 'model': 'Mustang', 'year': 1964, 'color': 'red'}
    Value for 'price': None
    Dictionary after setdefault('price'): {'brand': 'Ford', 'model': 'Mustang', 'year': 1964, 'color': 'red', 'price': None}
    ```

---

## 10. `update()`

*   **Purpose:** Updates the dictionary with the key-value pairs from another dictionary or from an iterable of key-value pairs (like tuples). If a key already exists, its value is overwritten. If a key doesn't exist, it's added.
*   **Syntax:** `dictionary.update(iterable)`
*   **Parameters:**
    *   `iterable`: Required. A dictionary or an iterable object (e.g., a list of tuples) with key-value pairs to insert into the dictionary.
*   **Returns:** `None`

*   **Example:**

    ```python
    car = {
      "brand": "Ford",
      "model": "Mustang",
      "year": 1964
    }
    print("Original dictionary:", car)

    # Update with new key-value pairs and overwrite existing key 'year'
    update_info = {"year": 2024, "color": "red", "electric": False}
    car.update(update_info)

    print("Dictionary after update():", car)
    ```

*   **Output:**

    ```
    Original dictionary: {'brand': 'Ford', 'model': 'Mustang', 'year': 1964}
    Dictionary after update(): {'brand': 'Ford', 'model': 'Mustang', 'year': 2024, 'color': 'red', 'electric': False}
    ```

---

## 11. `values()`

*   **Purpose:** Returns a *view object* that displays a list of all the values in the dictionary. The view object reflects changes made to the dictionary.
*   **Syntax:** `dictionary.values()`
*   **Parameters:** None
*   **Returns:** A view object containing the dictionary's values.

*   **Example:**

    ```python
    car = {
      "brand": "Ford",
      "model": "Mustang",
      "year": 1964
    }

    values_view = car.values()
    print("Original values view:", values_view) # Output shows dict_values object

    # Convert view to list for clearer display
    print("Values as list:", list(values_view))

    # Modify the dictionary
    car["year"] = 2024
    print("Values view after changing 'year':", values_view) # View reflects the change
    ```

*   **Output:**

    ```
    Original values view: dict_values(['Ford', 'Mustang', 1964])
    Values as list: ['Ford', 'Mustang', 1964]
    Values view after changing 'year': dict_values(['Ford', 'Mustang', 2024])
    ```

---