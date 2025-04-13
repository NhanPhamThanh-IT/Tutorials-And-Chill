# Python `re` Module: Regular Expressions for Beginners

## 1. Introduction to Regular Expressions (Regex)

Regular expressions (often shortened to "regex" or "regexp") are powerful sequences of characters that define a search pattern. They are used to match character combinations in strings. Think of them as a specialized mini-language for describing patterns you want to find within text.

In Python, the `re` module provides support for working with regular expressions. You need to import it before you can use its functions:

```python
import re
```

## 2. Basic Regex Syntax

Understanding the basic building blocks of regex patterns is crucial.

### a. Literal Characters

The simplest patterns match literal characters. For example, the pattern `cat` will match the sequence of characters 'c', 'a', 't' exactly.

### b. Metacharacters

Metacharacters have special meanings in regex. They don't match themselves but affect how the pattern is interpreted. Here are some common ones:

*   `.` (Dot): Matches any single character except a newline (`\n`).
*   `\` (Backslash): Escapes a metacharacter, making it literal. For example, `\.` matches a literal dot. It's also used for special sequences (see below).
*   `[]` (Character Set): Matches any single character *inside* the brackets.
    *   `[abc]` matches 'a', 'b', or 'c'.
    *   `[a-z]` matches any lowercase letter.
    *   `[0-9]` matches any digit.
    *   `[^abc]` (Caret inside): Matches any character *except* 'a', 'b', or 'c'.
*   `|` (Alternation/OR): Matches either the pattern before or the pattern after it. `cat|dog` matches 'cat' or 'dog'.
*   `()` (Grouping): Groups parts of a pattern together. Allows applying quantifiers to the group or capturing the matched text. `(ab)+` matches one or more repetitions of 'ab'.

### c. Quantifiers

Quantifiers specify how many times the preceding character, group, or character set must occur.

*   `*`: Matches 0 or more occurrences. `a*` matches '', 'a', 'aa', 'aaa', etc.
*   `+`: Matches 1 or more occurrences. `a+` matches 'a', 'aa', 'aaa', etc. (but not '').
*   `?`: Matches 0 or 1 occurrence. `a?` matches '' or 'a'.
*   `{n}`: Matches exactly `n` occurrences. `a{3}` matches 'aaa'.
*   `{n,}`: Matches `n` or more occurrences. `a{2,}` matches 'aa', 'aaa', etc.
*   `{n,m}`: Matches between `n` and `m` occurrences (inclusive). `a{2,4}` matches 'aa', 'aaa', or 'aaaa'.

**Greedy vs. Non-Greedy:** By default, quantifiers are *greedy*, meaning they match the longest possible string. Adding a `?` after a quantifier makes it *non-greedy* (or *lazy*), matching the shortest possible string.
    *   `.*` (Greedy): Matches as much as possible.
    *   `.*?` (Non-Greedy): Matches as little as possible.

### d. Anchors

Anchors don't match characters but assert something about the string or the matching process's position.

*   `^`: Matches the beginning of the string (or the beginning of a line in multiline mode).
*   `$`: Matches the end of the string (or the end of a line in multiline mode).
*   `\b`: Matches a word boundary (the position between a word character and a non-word character, or at the start/end of the string if the first/last character is a word character).
*   `\B`: Matches a non-word boundary.

### e. Special Sequences

These start with a backslash `\` and represent predefined sets of characters or special meanings.

*   `\d`: Matches any Unicode decimal digit (equivalent to `[0-9]` in ASCII).
*   `\D`: Matches any character that is not a decimal digit.
*   `\s`: Matches any Unicode whitespace character (space, tab, newline, etc.).
*   `\S`: Matches any character that is not whitespace.
*   `\w`: Matches any Unicode word character (alphanumeric characters plus underscore).
*   `\W`: Matches any character that is not a word character.
*   `\n`, `\t`, `\r`: Match newline, tab, return characters respectively.

## 3. Core `re` Module Functions

Let's explore the most commonly used functions in the `re` module.

### a. `re.search(pattern, string, flags=0)`

*   Scans through `string` looking for the *first* location where the `pattern` produces a match.
*   Returns a `Match` object if found, otherwise returns `None`.
*   Checks the entire string, not just the beginning.

```python
import re

text = "The quick brown fox jumps over the lazy dog."
pattern = r"fox" # r"" denotes a raw string, often used for regex patterns

match = re.search(pattern, text)

if match:
    print("Match found!")
    print("Matched string:", match.group(0)) # group(0) or group() returns the entire match
    print("Start index:", match.start())
    print("End index:", match.end())
    print("Span:", match.span())
else:
    print("No match found.")

# Example with a more complex pattern
text2 = "Contact us at info@example.com or support@test.org"
pattern2 = r"\w+@\w+\.\w+" # Simple email pattern
match2 = re.search(pattern2, text2)
if match2:
    print(f"Found email: {match2.group()}") # Output: Found email: info@example.com
```

### b. `re.match(pattern, string, flags=0)`

*   Similar to `re.search()`, but it only checks for a match *at the beginning* of the `string`.
*   If the pattern matches starting from the first character, it returns a `Match` object; otherwise, it returns `None`.

```python
import re

text = "The quick brown fox"
pattern_start = r"The"
pattern_middle = r"quick"

match_start = re.match(pattern_start, text)
match_middle = re.match(pattern_middle, text)

if match_start:
    print(f"'{pattern_start}' matches at the beginning.") # This will print
else:
    print(f"'{pattern_start}' does not match at the beginning.")

if match_middle:
    print(f"'{pattern_middle}' matches at the beginning.")
else:
    print(f"'{pattern_middle}' does not match at the beginning.") # This will print
```

### c. `re.findall(pattern, string, flags=0)`

*   Finds *all* non-overlapping occurrences of the `pattern` in the `string`.
*   Returns a list of strings. Each string in the list is a match.
*   If the pattern contains capturing groups `()`, it returns a list of tuples, where each tuple contains the strings matched by the groups. If there's only one group, it returns a list of strings matched by that group.

```python
import re

text = "Apples are red, bananas are yellow, apples are green."
pattern = r"apples"

matches = re.findall(pattern, text, re.IGNORECASE) # re.IGNORECASE makes it case-insensitive
print(matches) # Output: ['Apples', 'apples']

text_emails = "Emails: a@b.com, c@d.net, e@f.org"
pattern_emails = r"\w+@\w+\.\w+"
emails = re.findall(pattern_emails, text_emails)
print(emails) # Output: ['a@b.com', 'c@d.net', 'e@f.org']

# Example with capturing groups
text_pairs = "Pairs: key1=value1, key2=value2"
pattern_pairs = r"(\w+)=(\w+)" # Two capturing groups
pairs = re.findall(pattern_pairs, text_pairs)
print(pairs) # Output: [('key1', 'value1'), ('key2', 'value2')]
```

### d. `re.finditer(pattern, string, flags=0)`

*   Similar to `re.findall()`, but returns an *iterator* yielding `Match` objects for each non-overlapping match found.
*   This is more memory-efficient for a large number of matches, as it generates matches one by one.

```python
import re

text = "Event dates: 2023-10-26, 2024-01-15, 2024-05-01"
pattern = r"\d{4}-\d{2}-\d{2}" # Date pattern YYYY-MM-DD

matches_iterator = re.finditer(pattern, text)

print("Found dates:")
for match in matches_iterator:
    print(f"  Date: {match.group()}, Span: {match.span()}")
# Output:
# Found dates:
#   Date: 2023-10-26, Span: (13, 23)
#   Date: 2024-01-15, Span: (25, 35)
#   Date: 2024-05-01, Span: (37, 47)
```

### e. `re.sub(pattern, repl, string, count=0, flags=0)`

*   Replaces occurrences of the `pattern` in the `string` with `repl`.
*   `repl` can be a string or a function.
    *   If `repl` is a string, backreferences like `\1`, `\2` can be used to insert text from captured groups.
    *   If `repl` is a function, it's called for each match, and the `Match` object is passed as an argument. The function's return value is used as the replacement.
*   `count` (optional): Maximum number of replacements to perform. If 0 (default), all occurrences are replaced.
*   Returns the modified string.

```python
import re

text = "Usernames: alice123, bob_45, charlie-7"
pattern = r"[-_]" # Match hyphen or underscore

# Replace with a space
new_text = re.sub(pattern, " ", text)
print(new_text) # Output: Usernames: alice123, bob 45, charlie 7

# Using backreferences with groups
text_names = "Smith, John and Doe, Jane"
pattern_names = r"(\w+), (\w+)" # Group 1: Last name, Group 2: First name
# Swap first and last names using backreferences \2 (first name) and \1 (last name)
swapped_names = re.sub(pattern_names, r"\2 \1", text_names)
print(swapped_names) # Output: John Smith and Jane Doe

# Using a replacement function
text_numbers = "Values: 10, 25, 5"
pattern_numbers = r"\d+"

def double_value(match):
    value = int(match.group(0))
    return str(value * 2)

doubled_text = re.sub(pattern_numbers, double_value, text_numbers)
print(doubled_text) # Output: Values: 20, 50, 10
```

### f. `re.split(pattern, string, maxsplit=0, flags=0)`

*   Splits the `string` by the occurrences of the `pattern`.
*   Returns a list of strings.
*   If the pattern contains capturing groups `()`, the captured text is also included in the result list.
*   `maxsplit` (optional): Maximum number of splits. If 0 (default), splits on all occurrences.

```python
import re

text = "Split,this;string:by-delimiters"
pattern = r"[,;:\-]" # Split by comma, semicolon, colon, or hyphen

parts = re.split(pattern, text)
print(parts) # Output: ['Split', 'this', 'string', 'by', 'delimiters']

# Splitting with capturing groups includes delimiters
text_with_delimiters = "word1,word2;word3"
pattern_capture = r"([,;])" # Capture the delimiter
parts_with_delimiters = re.split(pattern_capture, text_with_delimiters)
print(parts_with_delimiters) # Output: ['word1', ',', 'word2', ';', 'word3']
```

### g. `re.compile(pattern, flags=0)`

*   Compiles a regular expression `pattern` into a `RegexObject`.
*   Using a compiled regex object is more efficient if you use the same pattern multiple times in your code, as the compilation step (parsing the pattern string) is done only once.
*   The compiled object has methods corresponding to the module-level functions (`match()`, `search()`, `findall()`, `sub()`, etc.), but the `string` is passed as the first argument.

```python
import re

# Compile the pattern once
email_pattern = re.compile(r"\w+@\w+\.\w+")

text1 = "Contact: info@example.com"
text2 = "Support: support@test.org"
text3 = "Invalid email here"

match1 = email_pattern.search(text1)
match2 = email_pattern.search(text2)
match3 = email_pattern.search(text3)

if match1: print(f"Found in text1: {match1.group()}")
if match2: print(f"Found in text2: {match2.group()}")
if match3: print(f"Found in text3: {match3.group()}") # No output for text3

# Using findall with the compiled pattern
all_emails = email_pattern.findall(text1 + " " + text2)
print(f"All found emails: {all_emails}")
```

## 4. Match Objects

Functions like `re.search()`, `re.match()`, and `re.finditer()` return `Match` objects when they find a match. These objects contain information about the match.

### Common Match Object Methods:

*   `match.group(num=0)`: Returns the matched string (or a specific captured group if `num` > 0). `group()` or `group(0)` returns the entire match.
*   `match.groups()`: Returns a tuple containing all the captured subgroups' strings.
*   `match.groupdict()`: Returns a dictionary containing named captured subgroups (if `(?P<name>...)` syntax was used in the pattern).
*   `match.start(num=0)`: Returns the starting index of the match (or a specific group).
*   `match.end(num=0)`: Returns the ending index (exclusive) of the match (or a specific group).
*   `match.span(num=0)`: Returns a tuple `(start, end)` for the match (or a specific group).

```python
import re

text = "Log entry: [2023-10-27] User 'admin' logged in from 192.168.1.100"
# Pattern with named capture groups: date, user, ip
pattern = r"\[(?P<date>\d{4}-\d{2}-\d{2})\] User '(?P<user>\w+)' logged in from (?P<ip>[\d\.]+)"

match = re.search(pattern, text)

if match:
    print("Full match:", match.group(0))
    print("Date (group 1 or 'date'):", match.group(1)) # Access by number
    print("User (group 2 or 'user'):", match.group('user')) # Access by name
    print("IP (group 3 or 'ip'):", match.group('ip'))

    print("All groups (tuple):", match.groups())
    print("Named groups (dict):", match.groupdict())

    print("Span of full match:", match.span())
    print("Start index of user:", match.start('user'))
    print("End index of user:", match.end('user'))
    print("Span of IP address:", match.span('ip'))
```

## 5. Flags

Flags modify the behavior of the regex matching. They can be passed as the `flags` argument to most `re` functions or included within the pattern using `(?...)` syntax. Common flags include:

*   `re.IGNORECASE` or `re.I`: Perform case-insensitive matching.
*   `re.MULTILINE` or `re.M`: Make `^` match the start of each line and `$` match the end of each line (in addition to the start/end of the string).
*   `re.DOTALL` or `re.S`: Make the `.` metacharacter match any character, *including* newline (`\n`).
*   `re.VERBOSE` or `re.X`: Allows writing more readable regex patterns by ignoring whitespace and comments within the pattern string.

```python
import re

text = """LINE 1: data
line 2: more data
LINE 3: end"""

# Find lines starting with "LINE" case-insensitively
pattern_multiline = r"^line"
matches_m = re.findall(pattern_multiline, text, re.IGNORECASE | re.MULTILINE)
# Equivalent: matches_m = re.findall(r"(?im)^line", text)
print(matches_m) # Output: ['LINE', 'line', 'LINE']

# Verbose pattern example
pattern_verbose = re.compile(r"""
    \d+      # Match one or more digits (the integer part)
    \.       # Match the literal dot
    \d*      # Match zero or more digits (the fractional part)
""", re.VERBOSE)

print(pattern_verbose.search("Number: 123.45").group()) # Output: 123.45
```

## Conclusion

The `re` module is a fundamental tool for text processing in Python. While regex syntax can seem complex initially, understanding the core concepts and functions (`search`, `match`, `findall`, `sub`, `split`, `compile`) and practicing with different patterns will make you proficient in manipulating and extracting information from strings. Remember to use raw strings (`r"..."`) for your patterns to avoid issues with backslash interpretation.