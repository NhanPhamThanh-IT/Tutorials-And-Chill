import keyword

# String Methods in Python - Examples

# Note: Strings are immutable in Python. String methods return new strings,
# they do not modify the original string.

# 1. capitalize() - Converts the first character to upper case
print("--- capitalize() ---")
txt = "hello, and welcome to my world."
x = txt.capitalize()
print(f"Original: '{txt}'")
print(f"Capitalized: '{x}'")
print()

# 2. casefold() - Converts string into lower case (more aggressive than lower())
print("--- casefold() ---")
txt = "Hello, And Welcome To My World."
x = txt.casefold()
print(f"Original: '{txt}'")
print(f"Casefolded: '{x}'")
# Example showing difference with lower() for specific characters like German ß
txt_german = "Der Fluß"
print(f"Original German: '{txt_german}'")
print(f"casefold(): '{txt_german.casefold()}'") # Output: 'der fluss'
print(f"lower(): '{txt_german.lower()}'")     # Output: 'der fluß'
print()

# 3. center() - Returns a centered string
print("--- center() ---")
txt = "banana"
# Center 'banana' in a string of length 20
x = txt.center(20)
print(f"Original: '{txt}'")
print(f"Centered (20 spaces): '{x}'")
# Center 'banana' using a specific character ('O')
y = txt.center(20, "O")
print(f"Centered (20 'O's): '{y}'")
print()

# 4. count() - Returns the number of times a specified value occurs in a string
print("--- count() ---")
txt = "I love apples, apple are my favorite fruit"
# Count how many times "apple" appears
x = txt.count("apple")
print(f"String: '{txt}'")
print(f"Count of 'apple': {x}")
# Count "apple" starting from position 10 up to 24
y = txt.count("apple", 10, 24)
print(f"Count of 'apple' (index 10-24): {y}")
print()

# 5. encode() - Returns an encoded version of the string
print("--- encode() ---")
txt = "My name is Ståle"
# Default encoding is UTF-8
x = txt.encode()
print(f"Original: '{txt}'")
print(f"Encoded (UTF-8): {x}")
# Specify encoding and error handling
y = txt.encode(encoding="ascii", errors="ignore")
print(f"Encoded (ASCII, ignore errors): {y}")
z = txt.encode(encoding="ascii", errors="replace")
print(f"Encoded (ASCII, replace errors): {z}")
# Other error handlers: 'xmlcharrefreplace', 'backslashreplace'
print()

# 6. endswith() - Returns true if the string ends with the specified value
print("--- endswith() ---")
txt = "Hello, welcome to my world."
# Check if it ends with "."
x = txt.endswith(".")
print(f"String: '{txt}'")
print(f"Ends with '.': {x}")
# Check if the substring from index 5 to 11 ends with "o"
y = txt.endswith("o", 5, 11) # Checks "o, welco"
print(f"Substring 'o, welco' ends with 'o': {y}")
z = txt.endswith("my world.")
print(f"Ends with 'my world.': {z}")
print()

# 7. expandtabs() - Sets the tab size of the string
print("--- expandtabs() ---")
txt = "H\te\tl\tl\to"
print(f"Original with tabs: '{txt}'")
# Default tab size is 8
x = txt.expandtabs()
print(f"Expanded (default tab size 8): '{x}'")
# Set tab size to 2
y = txt.expandtabs(2)
print(f"Expanded (tab size 2): '{y}'")
# Set tab size to 4
z = txt.expandtabs(4)
print(f"Expanded (tab size 4): '{z}'")
print()

# 8. find() - Searches the string for a specified value and returns the position of where it was found
print("--- find() ---")
txt = "Hello, welcome to my world."
# Find the first occurrence of "welcome"
x = txt.find("welcome")
print(f"String: '{txt}'")
print(f"Position of 'welcome': {x}")
# Find "e" starting from index 5 up to 10
y = txt.find("e", 5, 10) # Searches within ", welc"
print(f"Position of 'e' (index 5-10): {y}")
# If the value is not found, find() returns -1
z = txt.find("q")
print(f"Position of 'q': {z}")
# Note: Use 'in' operator for checking presence: 'q' in txt -> False
print()

# 9. format() - Formats specified values in a string
print("--- format() ---")
# Using positional arguments
txt1 = "My name is {fname}, I'm {age}."
print(txt1.format(fname="John", age=36))
# Using numbered placeholders
txt2 = "My name is {0}, I'm {1}."
print(txt2.format("John", 36))
# Using empty placeholders (order matters)
txt3 = "My name is {}, I'm {}."
print(txt3.format("John", 36))
# Formatting numbers
price = 49
txt4 = "The price is {:.2f} dollars." # Format as float with 2 decimal places
print(txt4.format(price))
# More formatting options (alignment, padding, sign, etc.)
txt5 = "Item: {:<10} Price: {:>5.2f}" # Left align item (10 chars), right align price (5 chars, 2 decimals)
print(txt5.format("Apple", 1.5))
print(txt5.format("Banana", 0.75))
print()

# 10. format_map() - Formats specified values in a string using a dictionary
print("--- format_map() ---")
point = {'x': 4, 'y': -5}
print('Coordinates: ({x}, {y})'.format_map(point))
# Can be useful when you have data in a dictionary
person = {'name': 'Alice', 'age': 30}
print("Name: {name}, Age: {age}".format_map(person))
print()

# 11. index() - Searches the string for a specified value and returns the position of where it was found
print("--- index() ---")
txt = "Hello, welcome to my world."
# Find the first occurrence of "welcome"
x = txt.index("welcome")
print(f"String: '{txt}'")
print(f"Position of 'welcome': {x}")
# Find "e" starting from index 5 up to 10
y = txt.index("e", 5, 10) # Searches within ", welc"
print(f"Position of 'e' (index 5-10): {y}")
# If the value is not found, index() raises a ValueError exception
try:
    z = txt.index("q")
    print(f"Position of 'q': {z}")
except ValueError as e:
    print(f"Finding 'q' raised an error: {e}")
# Difference between find() and index(): find() returns -1 on failure, index() raises ValueError.
print()

# 12. isalnum() - Returns True if all characters in the string are alphanumeric (a-z, A-Z, 0-9)
print("--- isalnum() ---")
txt1 = "Company12"
print(f"'{txt1}'.isalnum(): {txt1.isalnum()}") # True
txt2 = "Company 12" # Contains space
print(f"'{txt2}'.isalnum(): {txt2.isalnum()}") # False
txt3 = "Comp@ny" # Contains symbol
print(f"'{txt3}'.isalnum(): {txt3.isalnum()}") # False
print()

# 13. isalpha() - Returns True if all characters in the string are in the alphabet (a-z, A-Z)
print("--- isalpha() ---")
txt1 = "CompanyX"
print(f"'{txt1}'.isalpha(): {txt1.isalpha()}") # True
txt2 = "Company12" # Contains numbers
print(f"'{txt2}'.isalpha(): {txt2.isalpha()}") # False
txt3 = "Company X" # Contains space
print(f"'{txt3}'.isalpha(): {txt3.isalpha()}") # False
print()

# 14. isascii() - Returns True if all characters in the string are ascii characters
print("--- isascii() ---")
txt1 = "Company123"
print(f"'{txt1}'.isascii(): {txt1.isascii()}") # True
txt2 = "My name is Ståle" # Contains non-ASCII 'å'
print(f"'{txt2}'.isascii(): {txt2.isascii()}") # False
print()

# 15. isdecimal() - Returns True if all characters in the string are decimals (0-9)
print("--- isdecimal() ---")
txt1 = "12345"
print(f"'{txt1}'.isdecimal(): {txt1.isdecimal()}") # True
txt2 = "123.45" # Contains '.'
print(f"'{txt2}'.isdecimal(): {txt2.isdecimal()}") # False
txt3 = "\u0030\u0031\u0032" # Unicode for 012
print(f"'{txt3}'.isdecimal(): {txt3.isdecimal()}") # True
txt4 = "\u00B2" # Unicode for ² (superscript two) - not considered decimal
print(f"'{txt4}'.isdecimal(): {txt4.isdecimal()}") # False
print()

# 16. isdigit() - Returns True if all characters in the string are digits (0-9, and some other unicode digits)
print("--- isdigit() ---")
txt1 = "12345"
print(f"'{txt1}'.isdigit(): {txt1.isdigit()}") # True
txt2 = "123.45" # Contains '.'
print(f"'{txt2}'.isdigit(): {txt2.isdigit()}") # False
txt3 = "\u0030\u0031\u0032" # Unicode for 012
print(f"'{txt3}'.isdigit(): {txt3.isdigit()}") # True
txt4 = "\u00B2" # Unicode for ² (superscript two) - considered a digit
print(f"'{txt4}'.isdigit(): {txt4.isdigit()}") # True
print()

# 17. isidentifier() - Returns True if the string is a valid identifier (variable name, etc.)
# Rules: Starts with letter or underscore, followed by letters, numbers, or underscores. Cannot be a keyword.
print("--- isidentifier() ---")
txt1 = "Demo"
print(f"'{txt1}'.isidentifier(): {txt1.isidentifier()}") # True
txt2 = "my_variable"
print(f"'{txt2}'.isidentifier(): {txt2.isidentifier()}") # True
txt3 = "2bring" # Starts with number
print(f"'{txt3}'.isidentifier(): {txt3.isidentifier()}") # False
txt4 = "my-var" # Contains hyphen
print(f"'{txt4}'.isidentifier(): {txt4.isidentifier()}") # False
txt5 = "if" # Is a Python keyword
print(f"'{txt5}'.isidentifier(): {txt5.isidentifier()}") # False (though syntactically valid start, it's reserved)
print(f"Is 'if' a keyword? {keyword.iskeyword('if')}")
print()

# 18. islower() - Returns True if all cased characters in the string are lower case
print("--- islower() ---")
txt1 = "hello world!"
print(f"'{txt1}'.islower(): {txt1.islower()}") # True
txt2 = "Hello world!" # Contains 'H'
print(f"'{txt2}'.islower(): {txt2.islower()}") # False
txt3 = "hello 123" # Numbers and symbols are ignored
print(f"'{txt3}'.islower(): {txt3.islower()}") # True
txt4 = "helloß" # German sharp s is lowercase
print(f"'{txt4}'.islower(): {txt4.islower()}") # True
print()

# 19. isnumeric() - Returns True if all characters in the string are numeric (0-9, unicode numeric chars, fractions, etc.)
print("--- isnumeric() ---")
txt1 = "12345"
print(f"'{txt1}'.isnumeric(): {txt1.isnumeric()}") # True
txt2 = "123.45" # Contains '.'
print(f"'{txt2}'.isnumeric(): {txt2.isnumeric()}") # False
txt3 = "\u0030\u0031\u0032" # Unicode for 012
print(f"'{txt3}'.isnumeric(): {txt3.isnumeric()}") # True
txt4 = "\u00B2" # Unicode for ² (superscript two)
print(f"'{txt4}'.isnumeric(): {txt4.isnumeric()}") # True
txt5 = "\u00BD" # Unicode for ½ (Vulgar fraction one half)
print(f"'{txt5}'.isnumeric(): {txt5.isnumeric()}") # True
txt6 = "one" # Text representation
print(f"'{txt6}'.isnumeric(): {txt6.isnumeric()}") # False
# Key difference: isdecimal() < isdigit() < isnumeric() in terms of what they accept
print()

# 20. isprintable() - Returns True if all characters in the string are printable or if the string is empty
print("--- isprintable() ---")
txt1 = "Hello! Are you #1?"
print(f"'{txt1}'.isprintable(): {txt1.isprintable()}") # True
txt2 = "Hello\nWorld!" # Contains newline '\n' (non-printable)
print(f"'{txt2}'.isprintable(): {txt2.isprintable()}") # False
txt3 = "Hello\tWorld!" # Contains tab '\t' (non-printable control character)
print(f"'{txt3}'.isprintable(): {txt3.isprintable()}") # False
txt4 = "" # Empty string
print(f"'' (empty string).isprintable(): {txt4.isprintable()}") # True
print()

# 21. isspace() - Returns True if all characters in the string are whitespaces
print("--- isspace() ---")
txt1 = "   " # Only spaces
print(f"'{txt1}'.isspace(): {txt1.isspace()}") # True
txt2 = " \n\t " # Space, newline, tab, space
print(f"'{txt2}'.isspace(): {txt2.isspace()}") # True
txt3 = "   s   " # Contains 's'
print(f"'{txt3}'.isspace(): {txt3.isspace()}") # False
txt4 = "" # Empty string is not considered space
print(f"'' (empty string).isspace(): {txt4.isspace()}") # False
print()

# 22. istitle() - Returns True if the string follows the rules of a title
# Rules: First character of each word is uppercase, rest are lowercase. Symbols/numbers ignored.
print("--- istitle() ---")
txt1 = "Hello, And Welcome To My World!"
print(f"'{txt1}'.istitle(): {txt1.istitle()}") # True
txt2 = "HELLO, AND WELCOME..."
print(f"'{txt2}'.istitle(): {txt2.istitle()}") # False (all uppercase)
txt3 = "Hello, and Welcome..." # 'and' is not capitalized
print(f"'{txt3}'.istitle(): {txt3.istitle()}") # False
txt4 = "This Is Title 1" # Numbers are ignored
print(f"'{txt4}'.istitle(): {txt4.istitle()}") # True
txt5 = "This Is A Title With An Apostrophe's"
print(f"'{txt5}'.istitle(): {txt5.istitle()}") # True (apostrophe doesn't break the rule)
txt6 = "This Is A Title With Hyphenated-Word"
print(f"'{txt6}'.istitle(): {txt6.istitle()}") # False ('Word' should start uppercase)
print()

# 23. isupper() - Returns True if all cased characters in the string are upper case
print("--- isupper() ---")
txt1 = "HELLO WORLD!"
print(f"'{txt1}'.isupper(): {txt1.isupper()}") # True
txt2 = "Hello world!" # Contains lowercase
print(f"'{txt2}'.isupper(): {txt2.isupper()}") # False
txt3 = "HELLO 123" # Numbers and symbols are ignored
print(f"'{txt3}'.isupper(): {txt3.isupper()}") # True
txt4 = "HELLOß" # German sharp s has no uppercase equivalent in some contexts, treated as lowercase
print(f"'{txt4}'.isupper(): {txt4.isupper()}") # False
print()

# 24. join() - Joins the elements of an iterable (like list, tuple) into a string, using the string as a separator
print("--- join() ---")
my_tuple = ("John", "Peter", "Vicky")
separator = "#"
x = separator.join(my_tuple)
print(f"Tuple: {my_tuple}")
print(f"Joined with '#': '{x}'")

my_list = ["apple", "banana", "cherry"]
separator = ", "
y = separator.join(my_list)
print(f"List: {my_list}")
print(f"Joined with ', ': '{y}'")

my_dict = {"name": "John", "country": "Norway"} # Joins the keys by default
separator = " TEST "
z = separator.join(my_dict)
print(f"Dictionary: {my_dict}")
print(f"Joined keys with ' TEST ': '{z}'")

# Joining characters of a string
separator = "-"
w = separator.join("hello")
print(f"String: 'hello'")
print(f"Joined with '-': '{w}'")
print()

# 25. ljust() - Returns a left justified version of the string
print("--- ljust() ---")
txt = "banana"
# Justify 'banana' in a string of length 20 (padded with spaces on the right)
x = txt.ljust(20)
print(f"Original: '{txt}'")
print(f"Left justified (20 spaces): '{x}'")
# Justify using a specific character ('O')
y = txt.ljust(20, "O")
print(f"Left justified (20 'O's): '{y}'")
# If length is less than or equal to original string length, returns original
z = txt.ljust(4)
print(f"Left justified (4 spaces): '{z}'")
print()

# 26. lower() - Converts a string into lower case
print("--- lower() ---")
txt = "Hello, And Welcome To My World."
x = txt.lower()
print(f"Original: '{txt}'")
print(f"Lowercased: '{x}'")
# See casefold() for comparison with specific characters like German ß
print()

# 27. lstrip() - Returns a left trim version of the string (removes leading whitespace by default)
print("--- lstrip() ---")
txt = "     banana     "
x = txt.lstrip()
print(f"Original: '{txt}'")
print(f"Left stripped (whitespace): '{x}'")
# Remove specific leading characters
txt2 = ",,,ssaaww.....banana"
y = txt2.lstrip(",saw.") # Removes any combination of ',', 's', 'a', 'w', '.' from the left
print(f"Original: '{txt2}'")
print(f"Left stripped (',saw.'): '{y}'")
print()

# 28. maketrans() - Returns a translation table to be used in translations
print("--- maketrans() ---")
# Create a mapping table: 'S' maps to 'P', 'a' maps to 'o'
map_from = "Sa"
map_to = "Po"
my_table = str.maketrans(map_from, map_to)
print(f"Mapping '{map_from}' to '{map_to}'")
print(f"Translation table: {my_table}") # Shows ASCII code mappings

# Example usage with translate()
txt = "Hello Sam!"
translated_txt = txt.translate(my_table)
print(f"Original: '{txt}'")
print(f"Translated: '{translated_txt}'")

# Can also specify characters to delete (third argument)
map_from2 = "aeiou"
map_to2 = "12345"
delete_chars = "l"
my_table2 = str.maketrans(map_from2, map_to2, delete_chars)
txt2 = "hello world"
translated_txt2 = txt2.translate(my_table2)
print(f"Original: '{txt2}'")
print(f"Mapping vowels to numbers, deleting 'l': '{translated_txt2}'")
print()

# 29. partition() - Returns a tuple where the string is parted into three parts based on the first occurrence of the separator
print("--- partition() ---")
txt = "I could eat bananas all day"
# Partition based on "bananas"
x = txt.partition("bananas")
print(f"String: '{txt}'")
print(f"Partitioned by 'bananas': {x}") # Output: ('I could eat ', 'bananas', ' all day')
# Partition based on a separator that appears multiple times
y = txt.partition("a")
print(f"Partitioned by 'a' (first occurrence): {y}") # Output: ('I could e', 'a', 't bananas all day')
# If the separator is not found
z = txt.partition("apples")
print(f"Partitioned by 'apples': {z}") # Output: ('I could eat bananas all day', '', '')
print()

# 30. replace() - Returns a string where a specified value is replaced with a specified value
print("--- replace() ---")
txt = "I like bananas"
# Replace "bananas" with "apples"
x = txt.replace("bananas", "apples")
print(f"Original: '{txt}'")
print(f"Replaced 'bananas' with 'apples': '{x}'")
# Replace only the first occurrence (or specified number of occurrences)
txt2 = "one one was a race horse, two two was one too."
y = txt2.replace("one", "three") # Replace all occurrences
print(f"Original: '{txt2}'")
print(f"Replaced all 'one' with 'three': '{y}'")
z = txt2.replace("one", "three", 2) # Replace only the first 2 occurrences
print(f"Replaced first 2 'one' with 'three': '{z}'")
print()

# 31. rfind() - Searches the string for a specified value and returns the last position of where it was found
print("--- rfind() ---")
txt = "Mi casa, su casa."
# Find the last occurrence of "casa"
x = txt.rfind("casa")
print(f"String: '{txt}'")
print(f"Last position of 'casa': {x}")
# Find the last "a" between index 5 and 10 ("a, su ")
y = txt.rfind("a", 5, 10)
print(f"Last position of 'a' (index 5-10): {y}")
# If the value is not found, rfind() returns -1
z = txt.rfind("q")
print(f"Last position of 'q': {z}")
print()

# 32. rindex() - Searches the string for a specified value and returns the last position of where it was found
print("--- rindex() ---")
txt = "Mi casa, su casa."
# Find the last occurrence of "casa"
x = txt.rindex("casa")
print(f"String: '{txt}'")
print(f"Last position of 'casa': {x}")
# Find the last "a" between index 5 and 10 ("a, su ")
y = txt.rindex("a", 5, 10)
print(f"Last position of 'a' (index 5-10): {y}")
# If the value is not found, rindex() raises a ValueError exception
try:
    z = txt.rindex("q")
    print(f"Last position of 'q': {z}")
except ValueError as e:
    print(f"Finding 'q' with rindex() raised an error: {e}")
# Difference between rfind() and rindex(): rfind() returns -1 on failure, rindex() raises ValueError.
print()

# 33. rjust() - Returns a right justified version of the string
print("--- rjust() ---")
txt = "banana"
# Justify 'banana' in a string of length 20 (padded with spaces on the left)
x = txt.rjust(20)
print(f"Original: '{txt}'")
print(f"Right justified (20 spaces): '{x}'")
# Justify using a specific character ('O')
y = txt.rjust(20, "O")
print(f"Right justified (20 'O's): '{y}'")
# If length is less than or equal to original string length, returns original
z = txt.rjust(4)
print(f"Right justified (4 spaces): '{z}'")
print()

# 34. rpartition() - Returns a tuple where the string is parted into three parts based on the last occurrence of the separator
print("--- rpartition() ---")
txt = "I could eat bananas all day, bananas are great"
# Partition based on the last occurrence of "bananas"
x = txt.rpartition("bananas")
print(f"String: '{txt}'")
print(f"Right partitioned by 'bananas': {x}") # Output: ('I could eat bananas all day, ', 'bananas', ' are great')
# Partition based on the last occurrence of "a"
y = txt.rpartition("a")
print(f"Right partitioned by 'a': {y}") # Output: ('I could eat bananas all day, bananas are gre', 'a', 't')
# If the separator is not found
z = txt.rpartition("apples")
print(f"Right partitioned by 'apples': {z}") # Output: ('', '', 'I could eat bananas all day, bananas are great')
print()

# 35. rsplit() - Splits the string at the specified separator, starting from the right, and returns a list
print("--- rsplit() ---")
txt = "apple, banana, cherry"
# Split from the right, default separator is whitespace (none here, so no split)
x = txt.rsplit()
print(f"String: '{txt}'")
print(f"Right split (default whitespace): {x}") # Output: ['apple, banana, cherry']
# Split using ", " as separator
y = txt.rsplit(", ")
print(f"Right split by ', ': {y}") # Output: ['apple', 'banana', 'cherry']
# Split using ", " but only make maxsplit=1 split (from the right)
z = txt.rsplit(", ", 1)
print(f"Right split by ', ' (maxsplit=1): {z}") # Output: ['apple, banana', 'cherry']

txt2 = "a b c d e"
w = txt2.rsplit(None, 2) # Split by whitespace, max 2 splits from right
print(f"String: '{txt2}'")
print(f"Right split by whitespace (maxsplit=2): {w}") # Output: ['a b c', 'd', 'e']
print()

# 36. rstrip() - Returns a right trim version of the string (removes trailing whitespace by default)
print("--- rstrip() ---")
txt = "     banana     "
x = txt.rstrip()
print(f"Original: '{txt}'")
print(f"Right stripped (whitespace): '{x}'")
# Remove specific trailing characters
txt2 = "banana,,,,,ssaaww....."
y = txt2.rstrip(",saw.") # Removes any combination of ',', 's', 'a', 'w', '.' from the right
print(f"Original: '{txt2}'")
print(f"Right stripped (',saw.'): '{y}'")
print()

# 37. split() - Splits the string at the specified separator and returns a list
print("--- split() ---")
txt = "welcome to the jungle"
# Split by default separator (whitespace)
x = txt.split()
print(f"String: '{txt}'")
print(f"Split (default whitespace): {x}") # Output: ['welcome', 'to', 'the', 'jungle']

txt2 = "hello, my name is Peter, I am 26 years old"
# Split using ", " as separator
y = txt2.split(", ")
print(f"String: '{txt2}'")
print(f"Split by ', ': {y}") # Output: ['hello', 'my name is Peter', 'I am 26 years old']
# Split using ", " but only make maxsplit=1 split (from the left)
z = txt2.split(", ", 1)
print(f"Split by ', ' (maxsplit=1): {z}") # Output: ['hello', 'my name is Peter, I am 26 years old']
print()

# 38. splitlines() - Splits the string at line breaks and returns a list
print("--- splitlines() ---")
txt = "Thank you for the music\nWelcome to the jungle"
x = txt.splitlines()
print(f"String with newline: '{txt}'")
print(f"Split lines: {x}") # Output: ['Thank you for the music', 'Welcome to the jungle']
# Keep line breaks? (optional argument)
y = txt.splitlines(keepends=True)
print(f"Split lines (keepends=True): {y}") # Output: ['Thank you for the music\n', 'Welcome to the jungle']
# Works with various line endings like \r, \r\n
txt2 = "Line1\rLine2\r\nLine3"
z = txt2.splitlines()
print(f"String with mixed line endings: '{txt2}'")
print(f"Split lines: {z}") # Output: ['Line1', 'Line2', 'Line3']
print()

# 39. startswith() - Returns true if the string starts with the specified value
print("--- startswith() ---")
txt = "Hello, welcome to my world."
# Check if it starts with "Hello"
x = txt.startswith("Hello")
print(f"String: '{txt}'")
print(f"Starts with 'Hello': {x}")
# Check if the substring from index 7 to 20 ("welcome to my") starts with "wel"
y = txt.startswith("wel", 7, 20)
print(f"Substring 'welcome to my' starts with 'wel': {y}")
z = txt.startswith("hello") # Case sensitive
print(f"Starts with 'hello': {z}")
print()

# 40. strip() - Returns a trimmed version of the string (removes leading and trailing whitespace by default)
print("--- strip() ---")
txt = "     banana     "
x = txt.strip()
print(f"Original: '{txt}'")
print(f"Stripped (whitespace): '{x}'")
# Remove specific leading/trailing characters
txt2 = ",,,ssaaww.....banana.....rrrqqq,,,,"
y = txt2.strip(",.sawrq") # Removes any combination from both ends
print(f"Original: '{txt2}'")
print(f"Stripped (',.sawrq'): '{y}'")
print()

# 41. swapcase() - Swaps cases, lower case becomes upper case and vice versa
print("--- swapcase() ---")
txt = "Hello My Name Is PETER"
x = txt.swapcase()
print(f"Original: '{txt}'")
print(f"Swapped case: '{x}'")
print()

# 42. title() - Converts the first character of each word to upper case
print("--- title() ---")
txt = "Welcome to my world"
x = txt.title()
print(f"Original: '{txt}'")
print(f"Title cased: '{x}'")
txt2 = "hello b2b2b2 and 3g3g3g"
y = txt2.title() # Numbers/symbols act as word separators
print(f"Original: '{txt2}'")
print(f"Title cased: '{y}'") # Output: 'Hello B2B2B2 And 3G3G3G'
txt3 = "they're bill's friends."
z = txt3.title() # Apostrophes are handled correctly within words
print(f"Original: '{txt3}'")
print(f"Title cased: '{z}'") # Output: "They'Re Bill'S Friends." (Note 'R' and 'S')
# Compare with istitle() which checks if a string *is* title cased.
print()

# 43. translate() - Returns a translated string using a translation table (see maketrans())
print("--- translate() ---")
# Using table created with maketrans() earlier
map_from = "Sam"
map_to = "Joe"
delete_chars = "l"
my_table = str.maketrans(map_from, map_to, delete_chars)
txt = "Hello Sam! How are you Sam?"
print(f"Original: '{txt}'")
print(f"Using table: {my_table}")
print(f"Translated: '{txt.translate(my_table)}'") # Output: 'Heo Joe! How are y45 Joe?'

# Can also use a dictionary for direct mapping (only supports Unicode ordinals)
# This is less common than maketrans for simple replacements
translation_dict = {72: 80, 101: None, 108: None, 111: 65} # H->P, e->delete, l->delete, o->A
txt2 = "Hello"
print(f"Original: '{txt2}'")
print(f"Using dict {translation_dict}: '{txt2.translate(translation_dict)}'") # Output: 'PA'
print()

# 44. upper() - Converts a string into upper case
print("--- upper() ---")
txt = "Hello my friends"
x = txt.upper()
print(f"Original: '{txt}'")
print(f"Uppercased: '{x}'")
print()

# 45. zfill() - Pads the string with zeros (0) at the beginning, to fill a specified width
print("--- zfill() ---")
txt = "50"
x = txt.zfill(4) # Pad '50' to a length of 4
print(f"Original: '{txt}'")
print(f"zfill(4): '{x}'") # Output: '0050'

txt2 = "hello"
y = txt2.zfill(10)
print(f"Original: '{txt2}'")
print(f"zfill(10): '{y}'") # Output: '00000hello'

txt3 = "-25" # Handles sign correctly
z = txt3.zfill(6)
print(f"Original: '{txt3}'")
print(f"zfill(6): '{z}'") # Output: '-00025'

# If width is less than or equal to original length, no change
w = txt.zfill(2)
print(f"Original: '{txt}'")
print(f"zfill(2): '{w}'") # Output: '50'
print()

print("--- End of String Methods ---")