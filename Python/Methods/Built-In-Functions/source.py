import datetime

# Python Built-in Functions Examples

# abs(): Returns the absolute value of a number.
print("--- abs() ---")
negative_number = -15.5
absolute_value = abs(negative_number)
print(f"The absolute value of {negative_number} is: {absolute_value}") # Output: 15.5
print("-" * 20)

# all(): Returns True if all items in an iterable are true, otherwise False.
# If the iterable object is empty, the all() function also returns True.
print("--- all() ---")
list1 = [True, True, True]
list2 = [True, False, True]
list3 = [1, 1, 1] # Non-zero numbers are considered True
list4 = [1, 0, 1] # Zero is considered False
list5 = [] # Empty list
print(f"all({list1}) is: {all(list1)}") # Output: True
print(f"all({list2}) is: {all(list2)}") # Output: False
print(f"all({list3}) is: {all(list3)}") # Output: True
print(f"all({list4}) is: {all(list4)}") # Output: False
print(f"all({list5}) is: {all(list5)}") # Output: True
print("-" * 20)

# any(): Returns True if any item in an iterable is true.
# If the iterable object is empty, the any() function returns False.
print("--- any() ---")
list6 = [False, False, False]
list7 = [True, False, False]
list8 = [0, 0, 0] # Zero is considered False
list9 = [0, 1, 0] # Non-zero numbers are considered True
list10 = [] # Empty list
print(f"any({list6}) is: {any(list6)}") # Output: False
print(f"any({list7}) is: {any(list7)}") # Output: True
print(f"any({list8}) is: {any(list8)}") # Output: False
print(f"any({list9}) is: {any(list9)}") # Output: True
print(f"any({list10}) is: {any(list10)}") # Output: False
print("-" * 20)

# ascii(): Returns a readable version of an object, replacing non-ASCII characters with escape characters.
print("--- ascii() ---")
text_with_special_chars = "Hello Wörld"
ascii_text = ascii(text_with_special_chars)
print(f"Original text: {text_with_special_chars}")
print(f"ASCII representation: {ascii_text}") # Output: 'Hello W\xf6rld'
print("-" * 20)

# bin(): Converts an integer to a binary string prefixed with "0b".
print("--- bin() ---")
number = 10
binary_representation = bin(number)
print(f"The binary representation of {number} is: {binary_representation}") # Output: 0b1010
print("-" * 20)

# bool(): Converts a value to a Boolean (True or False).
# 0, None, empty sequences (list, tuple, string, dict, set) are False.
# All other values are True.
print("--- bool() ---")
print(f"bool(1) is: {bool(1)}")       # Output: True
print(f"bool(0) is: {bool(0)}")       # Output: False
print(f"bool([]) is: {bool([])}")     # Output: False
print(f"bool([1, 2]) is: {bool([1, 2])}") # Output: True
print(f"bool('') is: {bool('')}")     # Output: False
print(f"bool('Hi') is: {bool('Hi')}")   # Output: True
print(f"bool(None) is: {bool(None)}")   # Output: False
print("-" * 20)

# bytearray(): Returns a new array of bytes. It's a mutable sequence.
print("--- bytearray() ---")
byte_array_from_int = bytearray(5) # Creates a zero-filled bytearray of size 5
print(f"bytearray(5): {byte_array_from_int}") # Output: bytearray(b'\x00\x00\x00\x00\x00')
byte_array_from_str = bytearray("Hello", "utf-8") # Creates from string with encoding
print(f"bytearray('Hello', 'utf-8'): {byte_array_from_str}") # Output: bytearray(b'Hello')
byte_array_from_str[0] = 74 # Modify the first byte (H -> J)
print(f"Modified bytearray: {byte_array_from_str}") # Output: bytearray(b'Jello')
print("-" * 20)

# bytes(): Returns an immutable bytes object.
print("--- bytes() ---")
bytes_from_int = bytes(5) # Creates a zero-filled bytes object of size 5
print(f"bytes(5): {bytes_from_int}") # Output: b'\x00\x00\x00\x00\x00'
bytes_from_str = bytes("Hello", "utf-8") # Creates from string with encoding
print(f"bytes('Hello', 'utf-8'): {bytes_from_str}") # Output: b'Hello'
# bytes_from_str[0] = 74 # This would cause a TypeError because bytes are immutable
print("-" * 20)

# callable(): Returns True if the specified object is callable (like a function), False if not.
print("--- callable() ---")
def my_function():
    pass
x = 10
print(f"Is my_function callable? {callable(my_function)}") # Output: True
print(f"Is x callable? {callable(x)}")                   # Output: False
print("-" * 20)

# chr(): Returns the character that represents the specified unicode code point.
print("--- chr() ---")
unicode_code_point = 65
character = chr(unicode_code_point)
print(f"The character for unicode {unicode_code_point} is: '{character}'") # Output: 'A'
unicode_code_point_2 = 97
character_2 = chr(unicode_code_point_2)
print(f"The character for unicode {unicode_code_point_2} is: '{character_2}'") # Output: 'a'
print("-" * 20)

# complex(): Returns a complex number with the value real + imag*1j or converts a string or number to a complex number.
print("--- complex() ---")
complex_num1 = complex(3, 5) # real = 3, imaginary = 5
complex_num2 = complex("4+2j") # from string
complex_num3 = complex(6)    # real = 6, imaginary = 0
print(f"complex(3, 5) is: {complex_num1}") # Output: (3+5j)
print(f"complex('4+2j') is: {complex_num2}") # Output: (4+2j)
print(f"complex(6) is: {complex_num3}")    # Output: (6+0j)
print("-" * 20)

# dict(): Creates a dictionary.
print("--- dict() ---")
# Method 1: Using keyword arguments
my_dict1 = dict(name="Alice", age=30, city="New York")
print(f"dict(name='Alice', age=30, city='New York'): {my_dict1}")
# Method 2: Using an iterable of key-value pairs (e.g., a list of tuples)
my_dict2 = dict([('name', 'Bob'), ('age', 25)])
print(f"dict([('name', 'Bob'), ('age', 25)]): {my_dict2}")
# Method 3: Empty dictionary
my_dict3 = dict()
print(f"dict(): {my_dict3}")
print("-" * 20)

# dir(): Returns a list of the specified object's properties and methods.
# Without an argument, it returns the list of names in the current local scope.
print("--- dir() ---")
my_list = [1, 2, 3]
print("Methods and attributes for a list object (partial):")
print(dir(my_list)[-5:]) # Print last 5 items for brevity
print("\nNames in the current local scope (partial):")
print(dir()[-10:]) # Print last 10 items for brevity
print("-" * 20)

# divmod(): Returns a tuple containing the quotient and the remainder when argument1 (dividend) is divided by argument2 (divisor).
print("--- divmod() ---")
dividend = 10
divisor = 3
quotient, remainder = divmod(dividend, divisor)
print(f"divmod({dividend}, {divisor}) is: ({quotient}, {remainder})") # Output: (3, 1)
print(f"Quotient: {quotient}")
print(f"Remainder: {remainder}")
print("-" * 20)

# enumerate(): Takes an iterable and returns an enumerate object.
# It adds a counter to an iterable and returns it as tuples (index, element).
print("--- enumerate() ---")
fruits = ["apple", "banana", "cherry"]
print("Enumerating fruits:")
for index, fruit in enumerate(fruits):
        print(f"Index {index}: {fruit}")
# Starting index can be specified
print("\nEnumerating fruits starting from index 1:")
for index, fruit in enumerate(fruits, start=1):
        print(f"Index {index}: {fruit}")
print("-" * 20)

# filter(): Constructs an iterator from elements of an iterable for which a function returns true.
print("--- filter() ---")
ages = [5, 12, 17, 18, 24, 32]
def is_adult(age):
    return age >= 18
# The filter object itself is an iterator, convert to list to see results
adult_ages = list(filter(is_adult, ages))
print(f"Original ages: {ages}")
print(f"Adult ages (>= 18): {adult_ages}") # Output: [18, 24, 32]
# Using lambda function
adult_ages_lambda = list(filter(lambda age: age >= 18, ages))
print(f"Adult ages (using lambda): {adult_ages_lambda}") # Output: [18, 24, 32]
print("-" * 20)

# float(): Converts a number or a string containing a number to a floating point number.
print("--- float() ---")
integer_num = 10
string_num = "12.5"
string_int = "5"
print(f"float({integer_num}) is: {float(integer_num)}") # Output: 10.0
print(f"float('{string_num}') is: {float(string_num)}") # Output: 12.5
print(f"float('{string_int}') is: {float(string_int)}") # Output: 5.0
print("-" * 20)

# format(): Formats a specified value into a specified format.
print("--- format() ---")
price = 49.956
# Format price to 2 decimal places
formatted_price = format(price, ".2f")
print(f"Original price: {price}")
print(f"Formatted price ('.2f'): {formatted_price}") # Output: 49.96
# Format as percentage
percentage = 0.25
formatted_percentage = format(percentage, "%")
print(f"Original percentage: {percentage}")
print(f"Formatted percentage ('%'): {formatted_percentage}") # Output: 25.000000%
# Format as binary
number_to_format = 10
formatted_binary = format(number_to_format, "b")
print(f"Original number: {number_to_format}")
print(f"Formatted binary ('b'): {formatted_binary}") # Output: 1010
print("-" * 20)

# frozenset(): Returns an immutable frozenset object (like a set, but immutable).
print("--- frozenset() ---")
my_list_for_set = [1, 2, 2, 3, 4, 4, 4]
frozen_s = frozenset(my_list_for_set)
print(f"Original list: {my_list_for_set}")
print(f"Frozenset: {frozen_s}") # Output: frozenset({1, 2, 3, 4})
# frozen_s.add(5) # This would cause an AttributeError because frozensets are immutable
print("-" * 20)

# hash(): Returns the hash value of an object (if it has one).
# Hash values are integers used to quickly compare dictionary keys during a dictionary lookup.
# Only immutable objects (like strings, numbers, tuples, frozensets) are hashable.
print("--- hash() ---")
text = "Hello Python"
number_val = 12345
tuple_val = (1, 2, 3)
# list_val = [1, 2, 3] # Lists are mutable, so they are not hashable (will raise TypeError)
print(f"hash('{text}') is: {hash(text)}")
print(f"hash({number_val}) is: {hash(number_val)}")
print(f"hash({tuple_val}) is: {hash(tuple_val)}")
# print(f"hash({list_val}) is: {hash(list_val)}") # Raises TypeError
print("-" * 20)

# hex(): Converts an integer to a lowercase hexadecimal string prefixed with "0x".
print("--- hex() ---")
number_hex = 255
hex_representation = hex(number_hex)
print(f"The hexadecimal representation of {number_hex} is: {hex_representation}") # Output: 0xff
number_hex_2 = 10
hex_representation_2 = hex(number_hex_2)
print(f"The hexadecimal representation of {number_hex_2} is: {hex_representation_2}") # Output: 0xa
print("-" * 20)

# id(): Returns the unique id (memory address) of an object.
print("--- id() ---")
var1 = "hello"
var2 = 100
var3 = [1, 2]
print(f"id of var1 ('{var1}') is: {id(var1)}")
print(f"id of var2 ({var2}) is: {id(var2)}")
print(f"id of var3 ({var3}) is: {id(var3)}")
print("-" * 20)

# input(): Allows user input. Returns the input as a string.
# print("--- input() ---")
# user_name = input("Enter your name: ")
# print(f"Hello, {user_name}!")
# user_age_str = input("Enter your age: ")
# # Input is always string, convert if needed
# try:
#     user_age_int = int(user_age_str)
#     print(f"You will be {user_age_int + 1} next year.")
# except ValueError:
#     print("Invalid age entered. Please enter a number.")
# print("-" * 20)
# Note: Uncomment the input() section to run it interactively.

# int(): Converts a value to an integer number.
print("--- int() ---")
float_num = 12.8
string_num_int = "100"
string_num_float = "25.5" # Cannot directly convert float string with decimal part
binary_string = "1011" # Binary string (base 2)
hex_string = "FF"      # Hexadecimal string (base 16)
print(f"int({float_num}) is: {int(float_num)}") # Output: 12 (truncates decimal)
print(f"int('{string_num_int}') is: {int(string_num_int)}") # Output: 100
# print(f"int('{string_num_float}') is: {int(string_num_float)}") # Raises ValueError
print(f"int('{binary_string}', 2) is: {int(binary_string, 2)}") # Output: 11
print(f"int('{hex_string}', 16) is: {int(hex_string, 16)}")   # Output: 255
print("-" * 20)

# isinstance(): Returns True if the specified object is of the specified type, otherwise False.
print("--- isinstance() ---")
my_num = 5
my_str = "Hello"
my_list_instance = [1, 2]
print(f"Is my_num an int? {isinstance(my_num, int)}")     # Output: True
print(f"Is my_num a str? {isinstance(my_num, str)}")     # Output: False
print(f"Is my_str a str? {isinstance(my_str, str)}")     # Output: True
print(f"Is my_list_instance a list? {isinstance(my_list_instance, list)}") # Output: True
print(f"Is my_num an int or str? {isinstance(my_num, (int, str))}") # Can check multiple types
print("-" * 20)

# issubclass(): Returns True if the specified class is a subclass of the specified class, otherwise False.
print("--- issubclass() ---")
class Parent:
    pass
class Child(Parent):
    pass
class GrandChild(Child):
    pass
class Other:
    pass
print(f"Is Child a subclass of Parent? {issubclass(Child, Parent)}")     # Output: True
print(f"Is GrandChild a subclass of Parent? {issubclass(GrandChild, Parent)}") # Output: True
print(f"Is Parent a subclass of Child? {issubclass(Parent, Child)}")     # Output: False
print(f"Is Child a subclass of object? {issubclass(Child, object)}")   # All classes inherit from object
print(f"Is Child a subclass of Other? {issubclass(Child, Other)}")     # Output: False
print("-" * 20)

# iter(): Returns an iterator object from an iterable.
print("--- iter() ---")
my_tuple = ("apple", "banana", "cherry")
my_iterator = iter(my_tuple)
print(f"Type of my_iterator: {type(my_iterator)}")
# We can get items using next()
print(f"First item: {next(my_iterator)}")  # Output: apple
print(f"Second item: {next(my_iterator)}") # Output: banana
print(f"Third item: {next(my_iterator)}")  # Output: cherry
# print(next(my_iterator)) # This would raise StopIteration error as there are no more items
print("-" * 20)

# len(): Returns the number of items in an object (string, list, tuple, dict, set, etc.).
print("--- len() ---")
my_string_len = "Hello World"
my_list_len = [1, 2, 3, 4, 5]
my_tuple_len = (10, 20)
my_dict_len = {"a": 1, "b": 2}
print(f"Length of '{my_string_len}' is: {len(my_string_len)}") # Output: 11
print(f"Length of {my_list_len} is: {len(my_list_len)}")     # Output: 5
print(f"Length of {my_tuple_len} is: {len(my_tuple_len)}")    # Output: 2
print(f"Length of {my_dict_len} is: {len(my_dict_len)}")     # Output: 2 (number of key-value pairs)
print("-" * 20)

# list(): Creates a list. Can convert other iterables (tuples, strings, sets, dict keys) to lists.
print("--- list() ---")
my_tuple_to_list = (1, 2, 3)
my_string_to_list = "abc"
my_set_to_list = {10, 20, 30}
my_dict_to_list = {"x": 1, "y": 2} # Converts keys by default
list_from_tuple = list(my_tuple_to_list)
list_from_string = list(my_string_to_list)
list_from_set = list(my_set_to_list)
list_from_dict = list(my_dict_to_list)
empty_list = list()
print(f"list({my_tuple_to_list}) is: {list_from_tuple}") # Output: [1, 2, 3]
print(f"list('{my_string_to_list}') is: {list_from_string}") # Output: ['a', 'b', 'c']
print(f"list({my_set_to_list}) is: {list_from_set}") # Output: [10, 20, 30] (order may vary)
print(f"list({my_dict_to_list}) is: {list_from_dict}") # Output: ['x', 'y'] (keys)
print(f"list() is: {empty_list}") # Output: []
print("-" * 20)

# map(): Executes a specified function for each item in an iterable. The item is sent to the function as a parameter. Returns a map object (iterator).
print("--- map() ---")
numbers_to_map = [1, 2, 3, 4]
def square(n):
    return n * n
# The map object is an iterator, convert to list to see results
squared_numbers = list(map(square, numbers_to_map))
print(f"Original numbers: {numbers_to_map}")
print(f"Squared numbers: {squared_numbers}") # Output: [1, 4, 9, 16]
# Using lambda function
cubed_numbers = list(map(lambda n: n * n * n, numbers_to_map))
print(f"Cubed numbers (using lambda): {cubed_numbers}") # Output: [1, 8, 27, 64]
print("-" * 20)

# max(): Returns the largest item in an iterable or the largest of two or more arguments.
print("--- max() ---")
numbers_max = [1, 5, 2, 9, 3]
strings_max = ["apple", "banana", "cherry"] # Compares lexicographically
print(f"Max of {numbers_max} is: {max(numbers_max)}") # Output: 9
print(f"Max of {strings_max} is: {max(strings_max)}") # Output: cherry
print(f"Max of 10, 20, 5 is: {max(10, 20, 5)}") # Output: 20
print("-" * 20)

# min(): Returns the smallest item in an iterable or the smallest of two or more arguments.
print("--- min() ---")
numbers_min = [1, 5, 2, 9, 3, -2]
strings_min = ["apple", "banana", "cherry"] # Compares lexicographically
print(f"Min of {numbers_min} is: {min(numbers_min)}") # Output: -2
print(f"Min of {strings_min} is: {min(strings_min)}") # Output: apple
print(f"Min of 10, 20, 5 is: {min(10, 20, 5)}") # Output: 5
print("-" * 20)

# next(): Returns the next item from an iterator.
print("--- next() ---")
my_list_next = ["A", "B", "C"]
my_iterator_next = iter(my_list_next)
print("Getting items using next():")
item1 = next(my_iterator_next)
print(f"Item 1: {item1}") # Output: A
item2 = next(my_iterator_next)
print(f"Item 2: {item2}") # Output: B
# Providing a default value if iterator is exhausted
item3 = next(my_iterator_next, "End")
print(f"Item 3: {item3}") # Output: C
item4 = next(my_iterator_next, "End") # Iterator is now exhausted
print(f"Item 4 (default): {item4}") # Output: End
# next(my_iterator_next) # This would raise StopIteration without a default value
print("-" * 20)

# oct(): Converts an integer to an octal string prefixed with "0o".
print("--- oct() ---")
number_oct = 10
octal_representation = oct(number_oct)
print(f"The octal representation of {number_oct} is: {octal_representation}") # Output: 0o12
number_oct_2 = 8
octal_representation_2 = oct(number_oct_2)
print(f"The octal representation of {number_oct_2} is: {octal_representation_2}") # Output: 0o10
print("-" * 20)

# ord(): Returns the integer representing the Unicode code point of the given Unicode character.
print("--- ord() ---")
character_ord = 'A'
unicode_code = ord(character_ord)
print(f"The Unicode code point for '{character_ord}' is: {unicode_code}") # Output: 65
character_ord_2 = 'a'
unicode_code_2 = ord(character_ord_2)
print(f"The Unicode code point for '{character_ord_2}' is: {unicode_code_2}") # Output: 97
character_ord_3 = '€' # Euro sign
unicode_code_3 = ord(character_ord_3)
print(f"The Unicode code point for '{character_ord_3}' is: {unicode_code_3}") # Output: 8364
print("-" * 20)

# pow(): Returns the value of x to the power of y (x^y).
# pow(x, y, z) is equivalent to (x^y) % z, but potentially more efficient.
print("--- pow() ---")
base = 2
exponent = 3
result_pow = pow(base, exponent)
print(f"{base} to the power of {exponent} is: {result_pow}") # Output: 8
base_mod = 3
exponent_mod = 4
modulus = 5
result_pow_mod = pow(base_mod, exponent_mod, modulus) # (3^4) % 5 = 81 % 5
print(f"({base_mod}^{exponent_mod}) % {modulus} is: {result_pow_mod}") # Output: 1
print("-" * 20)

# print(): Prints the specified message to the screen, or other standard output device.
print("--- print() ---")
print("Hello, Beginner!") # Basic usage
name = "Python"
version = 3.10
print("Welcome to", name, version) # Multiple arguments, separated by space by default
print("Item 1", "Item 2", sep="---") # Custom separator
print("First line", end=" ") # Custom end character (default is newline \n)
print("Second line (on the same line as first)")
print("-" * 20)

# range(): Returns a sequence of numbers, starting from 0 by default, increments by 1 by default, and stops before a specified number.
print("--- range() ---")
# range(stop)
print("range(5):")
for i in range(5):
        print(i, end=" ") # Output: 0 1 2 3 4
print("\n")
# range(start, stop)
print("range(2, 6):")
for i in range(2, 6):
        print(i, end=" ") # Output: 2 3 4 5
print("\n")
# range(start, stop, step)
print("range(1, 10, 2):")
for i in range(1, 10, 2):
        print(i, end=" ") # Output: 1 3 5 7 9
print("\n")
# Convert range to list to see the sequence
range_list = list(range(3))
print(f"list(range(3)): {range_list}") # Output: [0, 1, 2]
print("-" * 20)

# repr(): Returns a printable representation string of the given object.
# Often the same as str(), but repr() aims to be unambiguous, often showing how the object could be created.
print("--- repr() ---")
my_string_repr = "Hello\nWorld"
my_number_repr = 100
my_list_repr = [1, 2, 3]
print(f"str('{my_string_repr}') is: {str(my_string_repr)}") # Interprets newline
print(f"repr('{my_string_repr}') is: {repr(my_string_repr)}") # Shows literal newline '\n'
print(f"str({my_number_repr}) is: {str(my_number_repr)}")
print(f"repr({my_number_repr}) is: {repr(my_number_repr)}")
print(f"str({my_list_repr}) is: {str(my_list_repr)}")
print(f"repr({my_list_repr}) is: {repr(my_list_repr)}")
today = datetime.datetime.now()
print(f"str(today) is: {str(today)}") # User-friendly date/time
print(f"repr(today) is: {repr(today)}") # Object representation
print("-" * 20)

# reversed(): Returns a reversed iterator for a sequence (like list, tuple, string, range).
print("--- reversed() ---")
my_list_rev = [1, 2, 3, 4, 5]
my_string_rev = "abcde"
# reversed() returns an iterator, convert to list or loop through it
reversed_list = list(reversed(my_list_rev))
reversed_string_list = list(reversed(my_string_rev))
print(f"Original list: {my_list_rev}")
print(f"Reversed list: {reversed_list}") # Output: [5, 4, 3, 2, 1]
print(f"Original string: {my_string_rev}")
print(f"Reversed string (as list): {reversed_string_list}") # Output: ['e', 'd', 'c', 'b', 'a']
print("Looping through reversed string:")
for char in reversed(my_string_rev):
        print(char, end=" ") # Output: e d c b a
print("\n" + "-" * 20)

# round(): Rounds a number to a specified number of decimal places.
# If the number of decimals is not specified, it rounds to the nearest integer.
# Note: Behavior for numbers exactly halfway between two integers (e.g., 2.5) rounds to the nearest even integer in Python 3 (round half to even).
print("--- round() ---")
num1 = 10.7
num2 = 10.3
num3 = 10.5 # Rounds to nearest even integer (10)
num4 = 11.5 # Rounds to nearest even integer (12)
num5 = 3.14159
print(f"round({num1}) is: {round(num1)}") # Output: 11
print(f"round({num2}) is: {round(num2)}") # Output: 10
print(f"round({num3}) is: {round(num3)}") # Output: 10
print(f"round({num4}) is: {round(num4)}") # Output: 12
print(f"round({num5}, 2) is: {round(num5, 2)}") # Output: 3.14 (rounds to 2 decimal places)
print(f"round({num5}, 3) is: {round(num5, 3)}") # Output: 3.142 (rounds to 3 decimal places)
print("-" * 20)

# set(): Creates a new set object. Sets contain unique, unordered items.
# Can convert other iterables to sets (duplicates are removed).
print("--- set() ---")
my_list_to_set = [1, 2, 2, 3, 4, 4, 4]
my_string_to_set = "hello"
set_from_list = set(my_list_to_set)
set_from_string = set(my_string_to_set)
empty_set = set()
print(f"set({my_list_to_set}) is: {set_from_list}") # Output: {1, 2, 3, 4} (order may vary)
print(f"set('{my_string_to_set}') is: {set_from_string}") # Output: {'h', 'e', 'l', 'o'} (order may vary)
print(f"set() is: {empty_set}") # Output: set()
print("-" * 20)

# sorted(): Returns a new sorted list from the items in an iterable.
print("--- sorted() ---")
numbers_sort = [3, 1, 4, 1, 5, 9, 2]
strings_sort = ["banana", "apple", "cherry"]
tuple_sort = (50, 10, 30)
# Basic sort (ascending)
sorted_numbers = sorted(numbers_sort)
sorted_strings = sorted(strings_sort)
sorted_tuple = sorted(tuple_sort)
print(f"Original numbers: {numbers_sort}")
print(f"Sorted numbers: {sorted_numbers}") # Output: [1, 1, 2, 3, 4, 5, 9]
print(f"Original strings: {strings_sort}")
print(f"Sorted strings: {sorted_strings}") # Output: ['apple', 'banana', 'cherry']
print(f"Original tuple: {tuple_sort}")
print(f"Sorted tuple (as list): {sorted_tuple}") # Output: [10, 30, 50]
# Sort in descending order
sorted_numbers_desc = sorted(numbers_sort, reverse=True)
print(f"Sorted numbers (descending): {sorted_numbers_desc}") # Output: [9, 5, 4, 3, 2, 1, 1]
# Sort based on length of string
sorted_strings_len = sorted(strings_sort, key=len)
print(f"Sorted strings (by length): {sorted_strings_len}") # Output: ['apple', 'banana', 'cherry'] (depends on stability if lengths equal)
print("-" * 20)

# str(): Returns a string version of an object.
print("--- str() ---")
number_str = 123
float_str = 45.67
list_str = [1, 2, 3]
bool_str = True
print(f"str({number_str}) is: '{str(number_str)}'") # Output: '123'
print(f"str({float_str}) is: '{str(float_str)}'") # Output: '45.67'
print(f"str({list_str}) is: '{str(list_str)}'") # Output: '[1, 2, 3]'
print(f"str({bool_str}) is: '{str(bool_str)}'") # Output: 'True'
print("-" * 20)

# sum(): Sums the items of an iterable (e.g., list, tuple) from left to right and returns the total.
# The items must be numbers.
print("--- sum() ---")
numbers_sum = [1, 2, 3, 4, 5]
tuple_sum = (10, 20, 30.5)
# strings_sum = ["a", "b"] # This would cause a TypeError
total = sum(numbers_sum)
print(f"Sum of {numbers_sum} is: {total}") # Output: 15
total_tuple = sum(tuple_sum)
print(f"Sum of {tuple_sum} is: {total_tuple}") # Output: 60.5
# Optional start value
total_with_start = sum(numbers_sum, 100) # Adds 100 to the sum of the list
print(f"Sum of {numbers_sum} with start=100 is: {total_with_start}") # Output: 115
print("-" * 20)

# tuple(): Creates a tuple object. Tuples are immutable sequences.
# Can convert other iterables (lists, strings, sets) to tuples.
print("--- tuple() ---")
my_list_to_tuple = [1, 2, 3]
my_string_to_tuple = "abc"
my_set_to_tuple = {10, 20, 30}
tuple_from_list = tuple(my_list_to_tuple)
tuple_from_string = tuple(my_string_to_tuple)
tuple_from_set = tuple(my_set_to_tuple)
empty_tuple = tuple()
print(f"tuple({my_list_to_tuple}) is: {tuple_from_list}") # Output: (1, 2, 3)
print(f"tuple('{my_string_to_tuple}') is: {tuple_from_string}") # Output: ('a', 'b', 'c')
print(f"tuple({my_set_to_tuple}) is: {tuple_from_set}") # Output: (10, 20, 30) (order may vary based on set)
print(f"tuple() is: {empty_tuple}") # Output: ()
print("-" * 20)

# type(): Returns the type of an object or creates a new type object.
print("--- type() ---")
var_int = 10
var_str = "Hello"
var_list = [1, 2]
var_func = my_function # Defined earlier
print(f"Type of {var_int} is: {type(var_int)}")     # Output: <class 'int'>
print(f"Type of '{var_str}' is: {type(var_str)}")    # Output: <class 'str'>
print(f"Type of {var_list} is: {type(var_list)}")    # Output: <class 'list'>
print(f"Type of my_function is: {type(var_func)}") # Output: <class 'function'>
print("-" * 20)

# zip(): Returns a zip object, which is an iterator of tuples where the first item in each passed iterator is paired together,
# and then the second item in each passed iterator are paired together etc.
# If the passed iterators have different lengths, the iterator with the least items decides the length of the new iterator.
print("--- zip() ---")
names = ["Alice", "Bob", "Charlie"]
ages_zip = [30, 25, 35]
cities = ["New York", "Paris", "London", "Tokyo"] # Tokyo will be ignored
# zip object is an iterator, convert to list to see results
zipped_data = list(zip(names, ages_zip, cities))
print(f"Names: {names}")
print(f"Ages: {ages_zip}")
print(f"Cities: {cities}")
print(f"Zipped data: {zipped_data}")
# Output: [('Alice', 30, 'New York'), ('Bob', 25, 'Paris'), ('Charlie', 35, 'London')]
print("\nLooping through zipped data:")
for name, age, city in zip(names, ages_zip, cities):
        print(f"{name} is {age} years old and lives in {city}.")
print("-" * 20)

print("Finished demonstrating built-in functions!")