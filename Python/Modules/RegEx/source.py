import re

# source.py
# This file demonstrates the basics of the 're' module in Python for regular expressions.


# --- 1. Basic Matching Functions ---

# Sample text for demonstrations
text = "The quick brown fox jumps over the lazy dog. The dog barks."
email_text = "Contact us at support@example.com or sales.support@company.co.uk"
multiline_text = """Line 1: Some text
Line 2: More text here
Line 3: Final line"""

# --- 1.1. re.search(pattern, string, flags=0) ---
# Scans through the string looking for the *first* location where the pattern matches.
# Returns a match object if found, otherwise None.

print("--- 1.1. re.search() ---")
pattern_fox = r"fox" # 'r' before the string indicates a raw string, useful for regex
match_fox = re.search(pattern_fox, text)

if match_fox:
    print(f"Found '{pattern_fox}' using search(): {match_fox}")
    # Match objects have useful methods:
    print(f"  Match starts at index: {match_fox.start()}")
    print(f"  Match ends at index: {match_fox.end()}")
    print(f"  Match span (start, end): {match_fox.span()}")
    print(f"  The matched string: {match_fox.group(0)}") # group(0) or group() returns the whole match
else:
    print(f"'{pattern_fox}' not found using search().")

pattern_cat = r"cat"
match_cat = re.search(pattern_cat, text)
if not match_cat:
    print(f"'{pattern_cat}' not found using search(), returned: {match_cat}")
print("-" * 20)


# --- 1.2. re.match(pattern, string, flags=0) ---
# Tries to match the pattern *only* at the beginning of the string.
# Returns a match object if the beginning matches, otherwise None.

print("--- 1.2. re.match() ---")
pattern_the = r"The"
match_start = re.match(pattern_the, text)

if match_start:
    print(f"Found '{pattern_the}' at the start using match(): {match_start}")
    print(f"  Matched string: {match_start.group()}")
else:
    print(f"'{pattern_the}' not found at the start using match().")

pattern_quick = r"quick"
match_quick_start = re.match(pattern_quick, text) # 'quick' is not at the start
if not match_quick_start:
    print(f"'{pattern_quick}' not found at the start using match(), returned: {match_quick_start}")
print("-" * 20)


# --- 1.3. re.findall(pattern, string, flags=0) ---
# Finds *all* non-overlapping matches of the pattern in the string.
# Returns a list of strings. If the pattern has groups, returns a list of tuples.

print("--- 1.3. re.findall() ---")
pattern_the_all = r"The"
all_the = re.findall(pattern_the_all, text) # Case-sensitive by default
print(f"Found all '{pattern_the_all}' using findall(): {all_the}")

pattern_the_case_insensitive = r"the"
all_the_insensitive = re.findall(pattern_the_case_insensitive, text, re.IGNORECASE) # Use a flag
print(f"Found all '{pattern_the_case_insensitive}' (case-insensitive) using findall(): {all_the_insensitive}")

# Example with groups: find all words starting with 'b'
pattern_b_words = r"\b(b\w+)\b" # \b is word boundary, \w+ is one or more word chars
b_words = re.findall(pattern_b_words, text)
print(f"Found all words starting with 'b': {b_words}") # Returns only the captured group content

# If you want the full match when groups are present, use non-capturing groups (?:...)
pattern_b_words_full = r"\b(?:b\w+)\b"
b_words_full = re.findall(pattern_b_words_full, text)
print(f"Found all full words starting with 'b' (using non-capturing group): {b_words_full}")
print("-" * 20)


# --- 1.4. re.finditer(pattern, string, flags=0) ---
# Similar to findall(), but returns an *iterator* yielding match objects for each match.
# This is more memory-efficient for a large number of matches.

print("--- 1.4. re.finditer() ---")
pattern_o = r"o"
iterator_o = re.finditer(pattern_o, text)
print(f"Finding all '{pattern_o}' using finditer():")
for match in iterator_o:
    print(f"  Found '{match.group()}' at index {match.start()}")
print("-" * 20)


# --- 1.5. re.sub(pattern, repl, string, count=0, flags=0) ---
# Replaces occurrences of the pattern in the string with 'repl'.
# 'repl' can be a string or a function.
# 'count' limits the number of replacements (0 means replace all).
# Returns the modified string.

print("--- 1.5. re.sub() ---")
pattern_dog = r"dog"
replacement = "cat"
substituted_text = re.sub(pattern_dog, replacement, text)
print(f"Original text: {text}")
print(f"Substituted '{pattern_dog}' with '{replacement}': {substituted_text}")

# Replace only the first occurrence
substituted_first_text = re.sub(pattern_dog, replacement, text, count=1)
print(f"Substituted only the first '{pattern_dog}': {substituted_first_text}")

# Using a function for replacement
def uppercase_match(match_obj):
    """Converts the matched word to uppercase."""
    word = match_obj.group(0)
    return word.upper()

pattern_jumps = r"jumps"
substituted_func_text = re.sub(pattern_jumps, uppercase_match, text)
print(f"Substituted using a function: {substituted_func_text}")
print("-" * 20)


# --- 2. Metacharacters and Special Sequences ---
# These give patterns more power.

print("--- 2. Metacharacters & Special Sequences ---")

# .     - Matches any character except a newline (unless re.DOTALL flag is used)
pattern_dot = r"f.x" # Matches 'fox'
print(f"Matching '{pattern_dot}': {re.search(pattern_dot, text).group()}")

# ^     - Matches the beginning of the string (or line if re.MULTILINE)
pattern_start = r"^The"
print(f"Matching '{pattern_start}' at start: {re.match(pattern_start, text).group()}")

# $     - Matches the end of the string (or line if re.MULTILINE)
pattern_end = r"barks\.$" # Need to escape the literal '.' with '\'
print(f"Matching '{pattern_end}' at end: {re.search(pattern_end, text).group()}")

# *     - Matches 0 or more repetitions of the preceding character/group
pattern_star = r"o*" # Matches '', 'o', 'oo', etc.
print(f"Matching 'go*d': {re.search(r'go*d', 'gd')}") # Matches 'gd' (0 'o's)
print(f"Matching 'go*d': {re.search(r'go*d', 'god')}") # Matches 'god' (1 'o')
print(f"Matching 'go*d': {re.search(r'go*d', 'good')}") # Matches 'good' (2 'o's)

# +     - Matches 1 or more repetitions of the preceding character/group
pattern_plus = r"o+" # Matches 'o', 'oo', etc. (but not empty string)
print(f"Matching 'go+d': {re.search(r'go+d', 'gd')}") # No match
print(f"Matching 'go+d': {re.search(r'go+d', 'god').group()}") # Matches 'god'
print(f"Matching 'go+d': {re.search(r'go+d', 'good').group()}") # Matches 'good'

# ?     - Matches 0 or 1 repetition of the preceding character/group (makes it optional)
pattern_qmark = r"colou?r" # Matches 'color' or 'colour'
print(f"Matching '{pattern_qmark}': {re.search(pattern_qmark, 'color').group()}")
print(f"Matching '{pattern_qmark}': {re.search(pattern_qmark, 'colour').group()}")

# {m}   - Matches exactly m repetitions
# {m,n} - Matches from m to n repetitions
# {m,}  - Matches m or more repetitions
# {,n}  - Matches up to n repetitions
pattern_rep = r"o{2}" # Matches exactly 'oo'
print(f"Matching '{pattern_rep}' in 'good': {re.search(pattern_rep, 'good').group()}")
pattern_rep_range = r"o{1,2}" # Matches 'o' or 'oo'
print(f"Matching '{pattern_rep_range}' in 'fox': {re.search(pattern_rep_range, 'fox').group()}")
print(f"Matching '{pattern_rep_range}' in 'good': {re.search(pattern_rep_range, 'good').group()}")

# []    - Character set. Matches any single character within the brackets.
pattern_set = r"[aeiou]" # Matches any vowel
print(f"Matching vowels '{pattern_set}' in 'quick': {re.findall(pattern_set, 'quick')}")
pattern_range = r"[a-zA-Z]" # Matches any letter (lowercase or uppercase)
print(f"Matching letters '{pattern_range}' in 'fox123': {re.findall(pattern_range, 'fox123')}")
pattern_neg_set = r"[^0-9]" # Matches any character that is NOT a digit
print(f"Matching non-digits '{pattern_neg_set}' in 'fox123': {re.findall(pattern_neg_set, 'fox123')}")

# |     - Alternation (OR). Matches either the expression before or after the pipe.
pattern_or = r"fox|dog"
print(f"Matching '{pattern_or}': {re.findall(pattern_or, text)}")

# ()    - Grouping. Captures the matched substring. Also used for applying quantifiers (*,+,?,{}) to a group.
pattern_group = r"(qu\w+)\s(br\w+)" # Capture 'quick' and 'brown'
match_groups = re.search(pattern_group, text)
if match_groups:
    print(f"Matching groups '{pattern_group}':")
    print(f"  Full match (group 0): {match_groups.group(0)}")
    print(f"  Group 1: {match_groups.group(1)}")
    print(f"  Group 2: {match_groups.group(2)}")
    print(f"  All groups (tuple): {match_groups.groups()}")

# \     - Escape special characters (like ., *, +, ?, $, ^, etc.) or signal a special sequence.
pattern_literal_dot = r"dog\." # Matches 'dog.' literally
print(f"Matching literal dot '{pattern_literal_dot}': {re.search(pattern_literal_dot, text).group()}")

# --- Special Sequences (start with \) ---
# \d    - Matches any Unicode digit (equivalent to [0-9] in ASCII patterns)
# \D    - Matches any non-digit character.
# \s    - Matches any Unicode whitespace character (space, tab, newline, etc.)
# \S    - Matches any non-whitespace character.
# \w    - Matches any Unicode word character (letters, digits, underscore).
# \W    - Matches any non-word character.
# \b    - Matches a word boundary (the position between a \w and \W character, or start/end of string).
# \B    - Matches a non-word boundary.

pattern_digits = r"\d+" # Matches one or more digits
print(f"Matching digits '{pattern_digits}' in 'Year 2024': {re.search(pattern_digits, 'Year 2024').group()}")
pattern_non_digits = r"\D+" # Matches one or more non-digits
print(f"Matching non-digits '{pattern_non_digits}' in 'Year 2024': {re.search(pattern_non_digits, 'Year 2024').group()}")
pattern_whitespace = r"\s+" # Matches one or more whitespace chars
print(f"Matching whitespace '{pattern_whitespace}' in 'quick brown': {re.search(pattern_whitespace, 'quick brown').group()!r}") # !r shows quotes
pattern_word_chars = r"\w+" # Matches one or more word characters
print(f"Matching word chars '{pattern_word_chars}' in 'fox!': {re.search(pattern_word_chars, 'fox!').group()}")
pattern_non_word_chars = r"\W+" # Matches one or more non-word characters
print(f"Matching non-word chars '{pattern_non_word_chars}' in 'fox!': {re.search(pattern_non_word_chars, 'fox!').group()}")
pattern_word_boundary = r"\bfox\b" # Matches 'fox' as a whole word
print(f"Matching word boundary '{pattern_word_boundary}': {re.search(pattern_word_boundary, text).group()}")
print(f"Matching word boundary '{pattern_word_boundary}' in 'firefox': {re.search(pattern_word_boundary, 'firefox')}") # No match

print("-" * 20)


# --- 3. Flags ---
# Modifiers that change how the pattern is interpreted.

print("--- 3. Flags ---")

# re.IGNORECASE (or re.I): Perform case-insensitive matching.
print(f"Case-sensitive search for 'the': {re.findall(r'the', text)}")
print(f"Case-insensitive search for 'the': {re.findall(r'the', text, re.IGNORECASE)}")

# re.MULTILINE (or re.M): Makes ^ match start of line and $ match end of line (in addition to string start/end).
print(f"\nMultiline text:\n{multiline_text}")
print(f"Finding lines starting with 'Line': {re.findall(r'^Line', multiline_text)}") # Only matches first line without M
print(f"Finding lines starting with 'Line' (MULTILINE): {re.findall(r'^Line', multiline_text, re.MULTILINE)}")
print(f"Finding lines ending with 'here': {re.findall(r'here$', multiline_text)}") # No match without M
print(f"Finding lines ending with 'here' (MULTILINE): {re.findall(r'here$', multiline_text, re.MULTILINE)}")

# re.DOTALL (or re.S): Makes the '.' special character match any character at all, including a newline.
pattern_dotall_test = r"text.More"
print(f"Matching across newline without DOTALL: {re.search(pattern_dotall_test, multiline_text)}") # No match
print(f"Matching across newline with DOTALL: {re.search(pattern_dotall_test, multiline_text, re.DOTALL)}")

# Multiple flags can be combined using the bitwise OR operator (|)
print(f"Finding 'line' case-insensitive at start of lines: {re.findall(r'^line', multiline_text, re.IGNORECASE | re.MULTILINE)}")

print("-" * 20)


# --- 4. Compiling Patterns ---
# If you use a regex pattern multiple times, compiling it first can improve performance.
# re.compile(pattern, flags=0) returns a pattern object.

print("--- 4. Compiling Patterns ---")

# Compile a pattern to find email addresses
email_pattern_str = r"[\w\.-]+@[\w\.-]+\.\w+"
compiled_email_pattern = re.compile(email_pattern_str)

print(f"Using compiled pattern on: {email_text}")

# Use methods directly on the compiled pattern object
matches = compiled_email_pattern.findall(email_text)
print(f"findall() with compiled pattern: {matches}")

search_result = compiled_email_pattern.search(email_text)
if search_result:
    print(f"search() with compiled pattern: {search_result.group()}")

# You can still pass flags during compilation
compiled_case_insensitive = re.compile(r"the", re.IGNORECASE)
print(f"findall() with compiled case-insensitive pattern: {compiled_case_insensitive.findall(text)}")

print("-" * 20)

# --- 5. Example: Extracting data ---
log_line = "INFO:2024-07-27 10:30:15:User 'admin' logged in from 192.168.1.100"
# Extract timestamp, user, and IP address
log_pattern = re.compile(r"(\d{4}-\d{2}-\d{2}\s\d{2}:\d{2}:\d{2}):User\s'(\w+)'\slogged\sin\sfrom\s([\d\.]+)")

match = log_pattern.search(log_line)
if match:
    timestamp = match.group(1)
    user = match.group(2)
    ip_address = match.group(3)
    print("--- 5. Example: Extracting Data ---")
    print(f"Log Line: {log_line}")
    print(f"  Timestamp: {timestamp}")
    print(f"  User: {user}")
    print(f"  IP Address: {ip_address}")
    print("-" * 20)

print("End of re module examples.")