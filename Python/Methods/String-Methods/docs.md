```markdown
# Python String Methods

In Python, strings are sequences of characters. They are immutable, meaning once a string is created, it cannot be changed. However, Python provides a rich set of built-in methods that you can use to perform various operations on strings. These methods return *new* strings or other values, leaving the original string unchanged.

Let's explore some of the most common and useful string methods.

---

## `capitalize()`

Converts the first character of the string to uppercase and the rest to lowercase.

**Syntax:**
```python
string.capitalize()
```

**Parameters:**
None

**Returns:**
A new string where the first character is uppercase and the rest are lowercase.

**Example:**
```python
text = "hello world"
capitalized_text = text.capitalize()
print(capitalized_text)  # Output: Hello world

text2 = "PYTHON IS FUN"
capitalized_text2 = text2.capitalize()
print(capitalized_text2) # Output: Python is fun
```

---

## `casefold()`

Converts the string into lowercase. This method is similar to `lower()`, but `casefold()` is more aggressive because it aims to remove all case distinctions in a string, making it suitable for caseless comparisons.

**Syntax:**
```python
string.casefold()
```

**Parameters:**
None

**Returns:**
A new string in lowercase, suitable for caseless matching.

**Example:**
```python
text = "Hello World"
folded_text = text.casefold()
print(folded_text)  # Output: hello world

# Difference from lower() with German ß
text_german = "Straße"
print(text_german.lower())    # Output: straße
print(text_german.casefold()) # Output: strasse
```

---

## `center()`

Returns a centered string of a specified width. Padding is done using a specified fill character (default is space).

**Syntax:**
```python
string.center(width, fillchar)
```

**Parameters:**
*   `width`: (Required) The total width of the resulting string.
*   `fillchar`: (Optional) The character used for padding. Defaults to a space ' '.

**Returns:**
A new string centered within the specified width.

**Example:**
```python
text = "Python"
centered_text = text.center(20)
print(f"'{centered_text}'")  # Output: '       Python       '

centered_text_filled = text.center(20, '-')
print(f"'{centered_text_filled}'") # Output: '-------Python-------'
```

---

## `count()`

Returns the number of non-overlapping occurrences of a substring in the string. You can optionally specify start and end indices to search within a slice of the string.

**Syntax:**
```python
string.count(substring, start, end)
```

**Parameters:**
*   `substring`: (Required) The substring to search for.
*   `start`: (Optional) The starting index of the search. Defaults to 0.
*   `end`: (Optional) The ending index of the search. Defaults to the end of the string.

**Returns:**
An integer representing the number of occurrences.

**Example:**
```python
text = "hello world, hello universe"
count_hello = text.count("hello")
print(count_hello)  # Output: 2

count_hello_partial = text.count("hello", 15) # Search starting from index 15
print(count_hello_partial) # Output: 1
```

---

## `encode()`

Returns an encoded version of the string as a bytes object.

**Syntax:**
```python
string.encode(encoding="utf-8", errors="strict")
```

**Parameters:**
*   `encoding`: (Optional) The encoding to use. Defaults to "utf-8". Common encodings include "ascii", "utf-16", etc.
*   `errors`: (Optional) Specifies how to handle encoding errors. Defaults to "strict" (raises an error). Other options include "ignore" (skips problematic characters), "replace" (replaces with a placeholder, often '?'), etc.

**Returns:**
A `bytes` object representing the encoded string.

**Example:**
```python
text = "Hello World"
encoded_utf8 = text.encode() # Default is utf-8
print(encoded_utf8)  # Output: b'Hello World'

encoded_ascii = text.encode("ascii", errors="ignore")
print(encoded_ascii) # Output: b'Hello World'

text_special = "H€llo"
# encoded_special_strict = text_special.encode("ascii") # This would raise UnicodeEncodeError
encoded_special_replace = text_special.encode("ascii", errors="replace")
print(encoded_special_replace) # Output: b'H?llo'
```

---

## `endswith()`

Returns `True` if the string ends with the specified suffix, otherwise returns `False`. You can optionally specify start and end indices to check within a slice of the string.

**Syntax:**
```python
string.endswith(suffix, start, end)
```

**Parameters:**
*   `suffix`: (Required) The suffix (string or tuple of strings) to check for.
*   `start`: (Optional) The starting index for the check. Defaults to 0.
*   `end`: (Optional) The ending index for the check. Defaults to the end of the string.

**Returns:**
`True` or `False`.

**Example:**
```python
text = "Hello, welcome to my world."
ends_with_world = text.endswith("world.")
print(ends_with_world)  # Output: True

ends_with_my = text.endswith("my", 0, 20) # Check if the slice text[0:20] ends with "my"
print(ends_with_my) # Output: True

ends_with_options = text.endswith(("world.", "universe.")) # Check if it ends with either
print(ends_with_options) # Output: True
```

---

## `expandtabs()`

Sets the tab size of the string. Replaces tab characters (`\t`) with one or more spaces, depending on the current column and the given tab size.

**Syntax:**
```python
string.expandtabs(tabsize=8)
```

**Parameters:**
*   `tabsize`: (Optional) The number of spaces for each tab character. Defaults to 8.

**Returns:**
A new string where tab characters are replaced by spaces.

**Example:**
```python
text = "H\te\tl\tl\to"
expanded_default = text.expandtabs()
print(expanded_default)  # Output: 'H       e       l       l       o' (assuming default tabsize 8)

expanded_custom = text.expandtabs(4)
print(expanded_custom)   # Output: 'H   e   l   l   o'
```

---

## `find()`

Searches the string for a specified value and returns the lowest index of the first occurrence. Returns -1 if the value is not found. You can optionally specify start and end indices.

**Syntax:**
```python
string.find(substring, start, end)
```

**Parameters:**
*   `substring`: (Required) The value to search for.
*   `start`: (Optional) The starting index of the search. Defaults to 0.
*   `end`: (Optional) The ending index of the search. Defaults to the end of the string.

**Returns:**
The lowest index where the substring is found, or -1 if not found.

**Example:**
```python
text = "Hello, welcome to my world."
index_welcome = text.find("welcome")
print(index_welcome)  # Output: 7

index_o = text.find("o")
print(index_o) # Output: 4 (finds the first 'o')

index_o_later = text.find("o", 5) # Start searching from index 5
print(index_o_later) # Output: 8

index_not_found = text.find("planet")
print(index_not_found) # Output: -1
```
*See also `index()` which is similar but raises an error if not found.*

---

## `format()`

Formats specified values in a string using placeholders defined by curly braces `{}`.

**Syntax:**
```python
string.format(value1, value2...)
```
Placeholders can be empty `{}`, numbered `{0}`, `{1}`, or named `{name}`.

**Parameters:**
*   `value1, value2...`: (Required) The values to be inserted into the string's placeholders. Can be positional or keyword arguments.

**Returns:**
A new formatted string.

**Example:**
```python
# Positional arguments
text1 = "Hello {}, welcome to {}."
formatted_text1 = text1.format("Alice", "Python")
print(formatted_text1) # Output: Hello Alice, welcome to Python.

# Numbered arguments
text2 = "The price is {1:.2f} dollars for {0} items."
formatted_text2 = text2.format(5, 99.95)
print(formatted_text2) # Output: The price is 99.95 dollars for 5 items.

# Named arguments
text3 = "My name is {fname}, I'm {age}."
formatted_text3 = text3.format(fname = "Bob", age = 30)
print(formatted_text3) # Output: My name is Bob, I'm 30.

# Mixed arguments
text4 = "Coordinates: {0}, {y}"
formatted_text4 = text4.format(10, y=25)
print(formatted_text4) # Output: Coordinates: 10, 25
```
*Note: F-strings (formatted string literals) introduced in Python 3.6 offer a more concise way to achieve similar results: `name = "Alice"; age = 30; print(f"My name is {name}, I'm {age}.")`*

---

## `format_map()`

Similar to `format()`, but takes a dictionary (or other mapping object) as the argument. The keys of the dictionary are used to substitute the named placeholders.

**Syntax:**
```python
string.format_map(mapping)
```

**Parameters:**
*   `mapping`: (Required) A dictionary or other mapping object containing the values.

**Returns:**
A new formatted string.

**Example:**
```python
point = {'x': 4, 'y': -5}
text = 'The point is at ({x}, {y})'
formatted_text = text.format_map(point)
print(formatted_text) # Output: The point is at (4, -5)

# Using __getitem__ object
class Coordinate:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __getitem__(self, key):
        if key == 'x':
            return self.x
        if key == 'y':
            return self.y
        raise KeyError(key)

coord = Coordinate(10, 20)
text = 'Coordinates: ({x}, {y})'
formatted_text = text.format_map(coord)
print(formatted_text) # Output: Coordinates: (10, 20)
```

---

## `index()`

Searches the string for a specified value and returns the lowest index of the first occurrence. Similar to `find()`, but raises a `ValueError` if the value is not found.

**Syntax:**
```python
string.index(substring, start, end)
```

**Parameters:**
*   `substring`: (Required) The value to search for.
*   `start`: (Optional) The starting index of the search. Defaults to 0.
*   `end`: (Optional) The ending index of the search. Defaults to the end of the string.

**Returns:**
The lowest index where the substring is found.

**Raises:**
`ValueError` if the substring is not found.

**Example:**
```python
text = "Hello, welcome to my world."
index_welcome = text.index("welcome")
print(index_welcome)  # Output: 7

index_o = text.index("o")
print(index_o) # Output: 4

# This would raise ValueError: substring not found
# index_not_found = text.index("planet")
# print(index_not_found)
```

---

## `isalnum()`

Returns `True` if all characters in the string are alphanumeric (either letters a-z/A-Z or numbers 0-9), and there is at least one character. Returns `False` otherwise.

**Syntax:**
```python
string.isalnum()
```

**Parameters:**
None

**Returns:**
`True` or `False`.

**Example:**
```python
text1 = "Python3"
print(text1.isalnum()) # Output: True

text2 = "Hello World" # Contains space
print(text2.isalnum()) # Output: False

text3 = "12345"
print(text3.isalnum()) # Output: True

text4 = "" # Empty string
print(text4.isalnum()) # Output: False

text5 = "Company_XYZ" # Contains underscore
print(text5.isalnum()) # Output: False
```

---

## `isalpha()`

Returns `True` if all characters in the string are alphabetic (a-z/A-Z) and there is at least one character. Returns `False` otherwise.

**Syntax:**
```python
string.isalpha()
```

**Parameters:**
None

**Returns:**
`True` or `False`.

**Example:**
```python
text1 = "Python"
print(text1.isalpha()) # Output: True

text2 = "HelloWorld"
print(text2.isalpha()) # Output: True

text3 = "Hello World" # Contains space
print(text3.isalpha()) # Output: False

text4 = "Python3" # Contains digit
print(text4.isalpha()) # Output: False

text5 = "" # Empty string
print(text5.isalpha()) # Output: False
```

---

## `isascii()`

Returns `True` if all characters in the string are ASCII characters (ordinal values 0-127). Returns `False` otherwise. Also returns `False` for an empty string.

**Syntax:**
```python
string.isascii()
```

**Parameters:**
None

**Returns:**
`True` or `False`.

**Example:**
```python
text1 = "Hello123!@#"
print(text1.isascii()) # Output: True

text2 = "H€llo" # Contains non-ASCII character €
print(text2.isascii()) # Output: False

text3 = "" # Empty string
print(text3.isascii()) # Output: False
```

---

## `isdecimal()`

Returns `True` if all characters in the string are decimal characters (0-9) and there is at least one character. Returns `False` otherwise. This method is stricter than `isdigit()` and `isnumeric()`.

**Syntax:**
```python
string.isdecimal()
```

**Parameters:**
None

**Returns:**
`True` or `False`.

**Example:**
```python
text1 = "12345"
print(text1.isdecimal()) # Output: True

text2 = "123.45" # Contains decimal point
print(text2.isdecimal()) # Output: False

text3 = "\u0030\u0031\u0032" # Unicode for 012
print(text3.isdecimal()) # Output: True

text4 = "³" # Superscript three (not a decimal character)
print(text4.isdecimal()) # Output: False

text5 = "一二三" # Chinese numerals (not decimal characters)
print(text5.isdecimal()) # Output: False

text6 = "" # Empty string
print(text6.isdecimal()) # Output: False
```

---

## `isdigit()`

Returns `True` if all characters in the string are digits (0-9, and some other digit characters like superscripts) and there is at least one character. Returns `False` otherwise.

**Syntax:**
```python
string.isdigit()
```

**Parameters:**
None

**Returns:**
`True` or `False`.

**Example:**
```python
text1 = "12345"
print(text1.isdigit()) # Output: True

text2 = "123.45" # Contains decimal point
print(text2.isdigit()) # Output: False

text3 = "\u0030\u0031\u0032" # Unicode for 012
print(text3.isdigit()) # Output: True

text4 = "³" # Unicode for superscript three U+00B3
print(text4.isdigit()) # Output: True

text5 = "一二三" # Chinese numerals (not considered digits by isdigit)
print(text5.isdigit()) # Output: False

text6 = "" # Empty string
print(text6.isdigit()) # Output: False
```

---

## `isidentifier()`

Returns `True` if the string is a valid Python identifier (according to Python's rules for variable/function names: starts with a letter or underscore, followed by letters, numbers, or underscores). Also checks if it's not a Python keyword.

**Syntax:**
```python
string.isidentifier()
```

**Parameters:**
None

**Returns:**
`True` or `False`.

**Example:**
```python
text1 = "my_variable"
print(text1.isidentifier()) # Output: True

text2 = "variable123"
print(text2.isidentifier()) # Output: True

text3 = "_privateVar"
print(text3.isidentifier()) # Output: True

text4 = "123variable" # Starts with a number
print(text4.isidentifier()) # Output: False

text5 = "my-variable" # Contains hyphen
print(text5.isidentifier()) # Output: False

text6 = "for" # Python keyword
print(text6.isidentifier()) # Output: False (even though it looks like a valid name structure)

text7 = "class" # Python keyword
print(text7.isidentifier()) # Output: False
```
*Note: To check if a string is a keyword, you can use `keyword.iskeyword(string)` after importing the `keyword` module.*

---

## `islower()`

Returns `True` if all cased characters (letters) in the string are lowercase and there is at least one cased character. Returns `False` otherwise. Symbols and numbers are ignored.

**Syntax:**
```python
string.islower()
```

**Parameters:**
None

**Returns:**
`True` or `False`.

**Example:**
```python
text1 = "hello world"
print(text1.islower()) # Output: True

text2 = "hello 123" # Numbers are ignored
print(text2.islower()) # Output: True

text3 = "Hello world" # Contains uppercase 'H'
print(text3.islower()) # Output: False

text4 = "HELLO WORLD"
print(text4.islower()) # Output: False

text5 = "123 !@#" # No cased characters
print(text5.islower()) # Output: False

text6 = "" # Empty string
print(text6.islower()) # Output: False
```

---

## `isnumeric()`

Returns `True` if all characters in the string are numeric characters (including digits 0-9, fractions, subscripts, superscripts, Roman numerals, etc.) and there is at least one character. Returns `False` otherwise. This is the most inclusive check among `isdecimal()`, `isdigit()`, and `isnumeric()`.

**Syntax:**
```python
string.isnumeric()
```

**Parameters:**
None

**Returns:**
`True` or `False`.

**Example:**
```python
text1 = "12345"
print(text1.isnumeric()) # Output: True

text2 = "123.45" # Contains decimal point
print(text2.isnumeric()) # Output: False

text3 = "\u0030\u0031\u0032" # Unicode for 012
print(text3.isnumeric()) # Output: True

text4 = "³" # Unicode for superscript three U+00B3
print(text4.isnumeric()) # Output: True

text5 = "½" # Unicode for fraction one half U+00BD
print(text5.isnumeric()) # Output: True

text6 = "一二三" # Chinese numerals
print(text6.isnumeric()) # Output: True

text7 = "IV" # Roman numerals (alphabetic)
print(text7.isnumeric()) # Output: False

text8 = "" # Empty string
print(text8.isnumeric()) # Output: False
```

---

## `isprintable()`

Returns `True` if all characters in the string are printable or if the string is empty. Returns `False` if the string contains non-printable characters (like `\n`, `\t`).

**Syntax:**
```python
string.isprintable()
```

**Parameters:**
None

**Returns:**
`True` or `False`.

**Example:**
```python
text1 = "Hello! Are you #1?"
print(text1.isprintable()) # Output: True

text2 = "Hello\nWorld" # Contains newline character \n
print(text2.isprintable()) # Output: False

text3 = "Hello\tWorld" # Contains tab character \t
print(text3.isprintable()) # Output: False

text4 = "" # Empty string is considered printable
print(text4.isprintable()) # Output: True

text5 = " " # Space is printable
print(text5.isprintable()) # Output: True
```

---

## `isspace()`

Returns `True` if all characters in the string are whitespace characters (like space, tab `\t`, newline `\n`, carriage return `\r`, etc.) and there is at least one character. Returns `False` otherwise.

**Syntax:**
```python
string.isspace()
```

**Parameters:**
None

**Returns:**
`True` or `False`.

**Example:**
```python
text1 = "   " # Only spaces
print(text1.isspace()) # Output: True

text2 = " \t\n\r " # Mix of whitespace
print(text2.isspace()) # Output: True

text3 = "   s   " # Contains non-whitespace 's'
print(text3.isspace()) # Output: False

text4 = "" # Empty string
print(text4.isspace()) # Output: False
```

---

## `istitle()`

Returns `True` if the string follows the rules of a title (first character of each word is uppercase, rest are lowercase) and there is at least one character. Symbols and numbers are ignored. Returns `False` otherwise.

**Syntax:**
```python
string.istitle()
```

**Parameters:**
None

**Returns:**
`True` or `False`.

**Example:**
```python
text1 = "Hello World"
print(text1.istitle()) # Output: True

text2 = "Hello And Welcome To Python 3"
print(text2.istitle()) # Output: True

text3 = "HELLO world" # Second word starts lowercase
print(text3.istitle()) # Output: False

text4 = "HelloWorld" # Not separated words
print(text4.istitle()) # Output: False (only first char is upper)

text5 = "Hello world" # 'w' is lowercase
print(text5.istitle()) # Output: False

text6 = "This Is A Title With 'Quotes'" # Apostrophe handled correctly
print(text6.istitle()) # Output: True

text7 = "99 Bottles" # Numbers ignored
print(text7.istitle()) # Output: True

text8 = "" # Empty string
print(text8.istitle()) # Output: False
```

---

## `isupper()`

Returns `True` if all cased characters (letters) in the string are uppercase and there is at least one cased character. Returns `False` otherwise. Symbols and numbers are ignored.

**Syntax:**
```python
string.isupper()
```

**Parameters:**
None

**Returns:**
`True` or `False`.

**Example:**
```python
text1 = "HELLO WORLD"
print(text1.isupper()) # Output: True

text2 = "HELLO 123" # Numbers are ignored
print(text2.isupper()) # Output: True

text3 = "Hello world" # Contains lowercase
print(text3.isupper()) # Output: False

text4 = "hello world"
print(text4.isupper()) # Output: False

text5 = "123 !@#" # No cased characters
print(text5.isupper()) # Output: False

text6 = "" # Empty string
print(text6.isupper()) # Output: False
```

---

## `join()`

Joins the elements of an iterable (like a list, tuple, set) into a single string, with the string itself as the separator between elements.

**Syntax:**
```python
separator_string.join(iterable)
```

**Parameters:**
*   `iterable`: (Required) An iterable whose elements (which must be strings) will be joined.

**Returns:**
A new string which is the concatenation of the elements in the iterable, separated by the `separator_string`.

**Raises:**
`TypeError` if the iterable contains non-string elements.

**Example:**
```python
my_list = ["apple", "banana", "cherry"]
separator = ", "
joined_string = separator.join(my_list)
print(joined_string) # Output: apple, banana, cherry

my_tuple = ("John", "Peter", "Vicky")
separator = " and "
joined_string = separator.join(my_tuple)
print(joined_string) # Output: John and Peter and Vicky

my_dict = {"name": "John", "country": "Norway"} # Joins the keys by default
separator = "-"
joined_string = separator.join(my_dict)
print(joined_string) # Output: name-country

# Joining list with non-string element will raise TypeError
# my_list_mixed = ["a", "b", 1]
# joined_string = "-".join(my_list_mixed) # Raises TypeError
```

---

## `ljust()`

Returns a left-justified string of a specified width. Padding is done using a specified fill character (default is space) on the right.

**Syntax:**
```python
string.ljust(width, fillchar)
```

**Parameters:**
*   `width`: (Required) The total width of the resulting string.
*   `fillchar`: (Optional) The character used for padding. Defaults to a space ' '.

**Returns:**
A new string left-justified within the specified width. If `width` is less than or equal to the length of the string, the original string is returned.

**Example:**
```python
text = "Python"
left_justified = text.ljust(20)
print(f"'{left_justified}'")  # Output: 'Python              '

left_justified_filled = text.ljust(20, '*')
print(f"'{left_justified_filled}'") # Output: 'Python**************'

short_width = text.ljust(4)
print(f"'{short_width}'") # Output: 'Python' (width <= len(text))
```

---

## `lower()`

Converts all uppercase characters in the string to lowercase.

**Syntax:**
```python
string.lower()
```

**Parameters:**
None

**Returns:**
A new string with all cased characters converted to lowercase.

**Example:**
```python
text = "Hello World"
lower_text = text.lower()
print(lower_text)  # Output: hello world

text2 = "PYTHON IS FUN 123!"
lower_text2 = text2.lower()
print(lower_text2) # Output: python is fun 123!
```
*See also `casefold()` for more aggressive lowercasing suitable for caseless comparisons.*

---

## `lstrip()`

Returns a copy of the string with leading characters removed (based on the specified characters argument). If no argument is provided, it removes leading whitespace.

**Syntax:**
```python
string.lstrip(characters)
```

**Parameters:**
*   `characters`: (Optional) A string specifying the set of characters to remove from the left. If omitted or `None`, removes leading whitespace.

**Returns:**
A new string with leading characters removed.

**Example:**
```python
text1 = "     banana     "
stripped_text1 = text1.lstrip()
print(f"'{stripped_text1}'") # Output: 'banana     ' (leading whitespace removed)

text2 = ",,,ssaaww.....banana"
stripped_text2 = text2.lstrip(",.saw") # Remove any leading ',', '.', 's', 'a', or 'w'
print(stripped_text2) # Output: banana
```

---

## `maketrans()`

Returns a translation table (a dictionary mapping Unicode ordinals to other ordinals, strings, or `None`) that can be used with the `translate()` method. It's a static method often called as `str.maketrans()`.

**Syntax (3 forms):**
1.  `str.maketrans(fromstr, tostr)`: Creates a table mapping each character in `fromstr` to the character at the same position in `tostr`. Both strings must be of equal length.
2.  `str.maketrans(fromstr, tostr, removestr)`: Same as above, but also maps characters in `removestr` to `None` (meaning they will be deleted by `translate()`).
3.  `str.maketrans(mapping)`: Takes a dictionary `mapping` where keys are Unicode ordinals (integers) or characters, and values are replacement ordinals, strings, or `None`.

**Parameters:**
*   `fromstr`: String of characters to replace.
*   `tostr`: String of replacement characters.
*   `removestr`: String of characters to delete.
*   `mapping`: Dictionary defining the translation.

**Returns:**
A translation table (dictionary).

**Example:**
```python
# Form 1: Replace 'S' with 'P', 'm' with 'b'
table1 = str.maketrans("Sm", "Pb")
text = "Simple Sample"
print(text.translate(table1)) # Output: Piple Pample

# Form 2: Replace 'a' with 'o', remove 'e'
table2 = str.maketrans("a", "o", "e")
text = "banana example"
print(text.translate(table2)) # Output: bonono xomplo

# Form 3: Using a dictionary
mapping = {ord('l'): ord('X'), ord('o'): '---'}
table3 = str.maketrans(mapping)
text = "hello world"
print(text.translate(table3)) # Output: heXXX--- w---rXd
```
*This method creates the rules; `translate()` applies them.*

---

## `partition()`

Searches for the first occurrence of a specified separator and splits the string into a tuple containing three parts: the part before the separator, the separator itself, and the part after the separator. If the separator is not found, it returns a tuple containing the original string and two empty strings.

**Syntax:**
```python
string.partition(separator)
```

**Parameters:**
*   `separator`: (Required) The string to search for and split by.

**Returns:**
A tuple of three strings.

**Example:**
```python
text = "I could eat bananas all day"
parts = text.partition("bananas")
print(parts) # Output: ('I could eat ', 'bananas', ' all day')

parts_not_found = text.partition("apples")
print(parts_not_found) # Output: ('I could eat bananas all day', '', '')

text_multiple = "apple,banana,apple,cherry"
parts_first = text_multiple.partition(",")
print(parts_first) # Output: ('apple', ',', 'banana,apple,cherry')
```
*See also `rpartition()` for splitting from the right.*

---

## `replace()`

Returns a new string where all occurrences of a specified substring are replaced with another substring. An optional count argument limits the number of replacements.

**Syntax:**
```python
string.replace(oldvalue, newvalue, count)
```

**Parameters:**
*   `oldvalue`: (Required) The substring to search for and replace.
*   `newvalue`: (Required) The substring to replace `oldvalue` with.
*   `count`: (Optional) The maximum number of replacements to perform. Defaults to replacing all occurrences.

**Returns:**
A new string with replacements made.

**Example:**
```python
text = "I like cats. Cats are cool."
replaced_text = text.replace("cats", "dogs")
print(replaced_text) # Output: I like dogs. Dogs are cool.

replaced_once = text.replace("cats", "dogs", 1) # Replace only the first occurrence
print(replaced_once) # Output: I like dogs. Cats are cool.
```

---

## `rfind()`

Searches the string for a specified value and returns the highest index of the last occurrence. Returns -1 if the value is not found. You can optionally specify start and end indices. Searches from right to left.

**Syntax:**
```python
string.rfind(substring, start, end)
```

**Parameters:**
*   `substring`: (Required) The value to search for.
*   `start`: (Optional) The starting index of the search range (search still proceeds right-to-left within this range). Defaults to 0.
*   `end`: (Optional) The ending index of the search range. Defaults to the end of the string.

**Returns:**
The highest index where the substring is found, or -1 if not found.

**Example:**
```python
text = "Hello, welcome to my world. Hello again."
index_hello_last = text.rfind("Hello")
print(index_hello_last)  # Output: 28

index_o_last = text.rfind("o")
print(index_o_last) # Output: 33

index_o_range = text.rfind("o", 5, 20) # Search for 'o' within text[5:20] from the right
print(index_o_range) # Output: 18 ('o' in 'to')

index_not_found = text.rfind("planet")
print(index_not_found) # Output: -1
```
*See also `rindex()` which is similar but raises an error if not found.*

---

## `rindex()`

Searches the string for a specified value and returns the highest index of the last occurrence. Similar to `rfind()`, but raises a `ValueError` if the value is not found. Searches from right to left.

**Syntax:**
```python
string.rindex(substring, start, end)
```

**Parameters:**
*   `substring`: (Required) The value to search for.
*   `start`: (Optional) The starting index of the search range. Defaults to 0.
*   `end`: (Optional) The ending index of the search range. Defaults to the end of the string.

**Returns:**
The highest index where the substring is found.

**Raises:**
`ValueError` if the substring is not found.

**Example:**
```python
text = "Hello, welcome to my world. Hello again."
index_hello_last = text.rindex("Hello")
print(index_hello_last)  # Output: 28

index_o_last = text.rindex("o")
print(index_o_last) # Output: 33

# This would raise ValueError: substring not found
# index_not_found = text.rindex("planet")
# print(index_not_found)
```

---

## `rjust()`

Returns a right-justified string of a specified width. Padding is done using a specified fill character (default is space) on the left.

**Syntax:**
```python
string.rjust(width, fillchar)
```

**Parameters:**
*   `width`: (Required) The total width of the resulting string.
*   `fillchar`: (Optional) The character used for padding. Defaults to a space ' '.

**Returns:**
A new string right-justified within the specified width. If `width` is less than or equal to the length of the string, the original string is returned.

**Example:**
```python
text = "Python"
right_justified = text.rjust(20)
print(f"'{right_justified}'")  # Output: '              Python'

right_justified_filled = text.rjust(20, '0')
print(f"'{right_justified_filled}'") # Output: '00000000000000Python'

short_width = text.rjust(4)
print(f"'{short_width}'") # Output: 'Python' (width <= len(text))
```

---

## `rpartition()`

Searches for the last occurrence of a specified separator and splits the string into a tuple containing three parts: the part before the separator, the separator itself, and the part after the separator. If the separator is not found, it returns a tuple containing two empty strings and the original string.

**Syntax:**
```python
string.rpartition(separator)
```

**Parameters:**
*   `separator`: (Required) The string to search for (from the right) and split by.

**Returns:**
A tuple of three strings.

**Example:**
```python
text = "I could eat bananas all day, yes bananas"
parts = text.rpartition("bananas")
print(parts) # Output: ('I could eat bananas all day, yes ', 'bananas', '')

parts_not_found = text.rpartition("apples")
print(parts_not_found) # Output: ('', '', 'I could eat bananas all day, yes bananas')

text_multiple = "apple,banana,apple,cherry"
parts_last = text_multiple.rpartition(",")
print(parts_last) # Output: ('apple,banana,apple', ',', 'cherry')
```
*See also `partition()` for splitting from the left.*

---

## `rsplit()`

Splits the string at the specified separator, starting from the right, and returns a list of the words. An optional `maxsplit` argument limits the number of splits.

**Syntax:**
```python
string.rsplit(separator=None, maxsplit=-1)
```

**Parameters:**
*   `separator`: (Optional) The delimiter string to split by. If `None` (default), splits by any whitespace and empty strings are discarded.
*   `maxsplit`: (Optional) Maximum number of splits to do, starting from the right. Default is -1 (no limit).

**Returns:**
A list of strings.

**Example:**
```python
text = "apple, banana, cherry, orange"

# Split by comma and space, default maxsplit
words = text.rsplit(", ")
print(words) # Output: ['apple', 'banana', 'cherry', 'orange']

# Split by comma and space, maxsplit=1 (one split from the right)
words_split1 = text.rsplit(", ", 1)
print(words_split1) # Output: ['apple, banana, cherry', 'orange']

# Split by comma and space, maxsplit=2 (two splits from the right)
words_split2 = text.rsplit(", ", 2)
print(words_split2) # Output: ['apple, banana', 'cherry', 'orange']

text_whitespace = "   apple   banana cherry  "
# Split by whitespace (default separator), no limit
words_ws = text_whitespace.rsplit()
print(words_ws) # Output: ['apple', 'banana', 'cherry']

# Split by whitespace, maxsplit=1
words_ws_split1 = text_whitespace.rsplit(None, 1)
print(words_ws_split1) # Output: ['   apple   banana', 'cherry']
```
*See also `split()` for splitting from the left.*

---

## `rstrip()`

Returns a copy of the string with trailing characters removed (based on the specified characters argument). If no argument is provided, it removes trailing whitespace.

**Syntax:**
```python
string.rstrip(characters)
```

**Parameters:**
*   `characters`: (Optional) A string specifying the set of characters to remove from the right. If omitted or `None`, removes trailing whitespace.

**Returns:**
A new string with trailing characters removed.

**Example:**
```python
text1 = "     banana     "
stripped_text1 = text1.rstrip()
print(f"'{stripped_text1}'") # Output: '     banana' (trailing whitespace removed)

text2 = "banana,,,,,ssaaww....."
stripped_text2 = text2.rstrip(",.saw") # Remove any trailing ',', '.', 's', 'a', or 'w'
print(stripped_text2) # Output: banana
```

---

## `split()`

Splits the string at the specified separator and returns a list of the words. An optional `maxsplit` argument limits the number of splits.

**Syntax:**
```python
string.split(separator=None, maxsplit=-1)
```

**Parameters:**
*   `separator`: (Optional) The delimiter string to split by. If `None` (default), splits by any whitespace and empty strings are discarded.
*   `maxsplit`: (Optional) Maximum number of splits to do. Default is -1 (no limit).

**Returns:**
A list of strings.

**Example:**
```python
text = "welcome to the jungle"

# Split by space (default separator)
words = text.split()
print(words) # Output: ['welcome', 'to', 'the', 'jungle']

text_csv = "apple,banana,cherry"
# Split by comma
items = text_csv.split(",")
print(items) # Output: ['apple', 'banana', 'cherry']

# Split by comma, maxsplit=1
items_split1 = text_csv.split(",", 1)
print(items_split1) # Output: ['apple', 'banana,cherry']

text_whitespace = "   apple   banana cherry  "
# Split by whitespace (default separator), handles multiple spaces
words_ws = text_whitespace.split()
print(words_ws) # Output: ['apple', 'banana', 'cherry']
```
*See also `rsplit()` for splitting from the right.*

---

## `splitlines()`

Splits the string at line breaks (`\n`, `\r`, `\r\n`) and returns a list of the lines. An optional `keepends` argument specifies whether to include the line breaks in the resulting list elements.

**Syntax:**
```python
string.splitlines(keepends=False)
```

**Parameters:**
*   `keepends`: (Optional) If `True`, line breaks are included in the list elements. Defaults to `False`.

**Returns:**
A list of strings (lines).

**Example:**
```python
text = "Hello\nWorld\rWelcome\r\nto Python"
lines = text.splitlines()
print(lines) # Output: ['Hello', 'World', 'Welcome', 'to Python']

lines_with_ends = text.splitlines(keepends=True)
print(lines_with_ends) # Output: ['Hello\n', 'World\r', 'Welcome\r\n', 'to Python']

text_no_breaks = "Single line"
lines_no_breaks = text_no_breaks.splitlines()
print(lines_no_breaks) # Output: ['Single line']
```

---

## `startswith()`

Returns `True` if the string starts with the specified prefix, otherwise returns `False`. You can optionally specify start and end indices to check within a slice of the string.

**Syntax:**
```python
string.startswith(prefix, start, end)
```

**Parameters:**
*   `prefix`: (Required) The prefix (string or tuple of strings) to check for.
*   `start`: (Optional) The starting index for the check. Defaults to 0.
*   `end`: (Optional) The ending index for the check. Defaults to the end of the string.

**Returns:**
`True` or `False`.

**Example:**
```python
text = "Hello, welcome to my world."
starts_with_hello = text.startswith("Hello")
print(starts_with_hello)  # Output: True

starts_with_wel = text.startswith("wel", 7) # Check if slice text[7:] starts with "wel"
print(starts_with_wel) # Output: True

starts_with_options = text.startswith(("Hi", "Hello", "Greetings")) # Check if it starts with any
print(starts_with_options) # Output: True
```

---

## `strip()`

Returns a copy of the string with both leading and trailing characters removed (based on the specified characters argument). If no argument is provided, it removes leading and trailing whitespace.

**Syntax:**
```python
string.strip(characters)
```

**Parameters:**
*   `characters`: (Optional) A string specifying the set of characters to remove from both ends. If omitted or `None`, removes whitespace.

**Returns:**
A new string with leading and trailing characters removed.

**Example:**
```python
text1 = "     banana     "
stripped_text1 = text1.strip()
print(f"'{stripped_text1}'") # Output: 'banana' (leading/trailing whitespace removed)

text2 = ",,,ssaaww.....banana.....rrrqqq,,,,"
# Remove any leading/trailing ',', '.', 's', 'a', 'w', 'r', or 'q'
stripped_text2 = text2.strip(",.sawrq")
print(stripped_text2) # Output: banana
```
*Combines the behavior of `lstrip()` and `rstrip()`.*

---

## `swapcase()`

Returns a new string where uppercase characters are converted to lowercase and lowercase characters are converted to uppercase.

**Syntax:**
```python
string.swapcase()
```

**Parameters:**
None

**Returns:**
A new string with the case of all letters swapped.

**Example:**
```python
text = "Hello World"
swapped_text = text.swapcase()
print(swapped_text) # Output: hELLO wORLD

text2 = "PYTHON is Fun 123!"
swapped_text2 = text2.swapcase()
print(swapped_text2) # Output: python IS fUN 123!
```

---

## `title()`

Returns a "titlecased" version of the string, where the first character of each word is uppercase and all remaining characters in the word are lowercase. It handles apostrophes and other separators intelligently.

**Syntax:**
```python
string.title()
```

**Parameters:**
None

**Returns:**
A new titlecased string.

**Example:**
```python
text = "welcome to the jungle"
title_text = text.title()
print(title_text) # Output: Welcome To The Jungle

text2 = "they're bill's friends"
title_text2 = text2.title()
print(title_text2) # Output: They'Re Bill'S Friends (Note the 'R' and 'S' after apostrophes)

text3 = "HELLO world 123"
title_text3 = text3.title()
print(title_text3) # Output: Hello World 123
```
*Compare with `capitalize()` which only affects the very first character of the string, and `istitle()` which checks if a string is already titlecased.*

---

## `translate()`

Returns a copy of the string where each character has been mapped through the given translation table. The table must be a dictionary mapping Unicode ordinals to ordinals, strings, or `None` (for deletion). Use `str.maketrans()` to create translation tables easily.

**Syntax:**
```python
string.translate(table)
```

**Parameters:**
*   `table`: (Required) A translation table created by `str.maketrans()`.

**Returns:**
A new string with translations applied.

**Example:**
```python
# Create a table: 'H' -> 'J', 'l' -> None (delete), 'o' -> '***'
table = str.maketrans({ord('H'): ord('J'), ord('l'): None, ord('o'): '***'})

text = "Hello World"
translated_text = text.translate(table)
print(translated_text) # Output: Je*** W***rd
```

---

## `upper()`

Converts all lowercase characters in the string to uppercase.

**Syntax:**
```python
string.upper()
```

**Parameters:**
None

**Returns:**
A new string with all cased characters converted to uppercase.

**Example:**
```python
text = "Hello World"
upper_text = text.upper()
print(upper_text)  # Output: HELLO WORLD

text2 = "python is fun 123!"
upper_text2 = text2.upper()
print(upper_text2) # Output: PYTHON IS FUN 123!
```

---

## `zfill()`

Pads the string on the left with '0' characters to fill a specified width. If the string starts with a sign character (`+` or `-`), the padding is added after the sign.

**Syntax:**
```python
string.zfill(width)
```

**Parameters:**
*   `width`: (Required) The total desired width of the string.

**Returns:**
A new string padded with leading zeros. If `width` is less than or equal to the length of the string, the original string is returned.

**Example:**
```python
num_str = "50"
filled_str = num_str.zfill(5)
print(filled_str) # Output: 00050

neg_num_str = "-12"
filled_neg = neg_num_str.zfill(6)
print(filled_neg) # Output: -00012

text = "hello"
filled_text = text.zfill(10)
print(filled_text) # Output: 00000hello

short_width = "12345"
filled_short = short_width.zfill(3)
print(filled_short) # Output: 12345 (width <= len(string))
```

---

Remember that all these methods return *new* strings. The original string remains unchanged.
```