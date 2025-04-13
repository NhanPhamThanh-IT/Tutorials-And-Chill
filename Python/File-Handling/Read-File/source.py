import os

# -*- coding: utf-8 -*-
"""
This script demonstrates various ways to read a text file in Python.
We will assume there is a file named 'sample.txt' in the same directory
as this script.

Let's first create a sample file named 'sample.txt' with the following content:

Line 1: Hello Python!
Line 2: This is the second line.
Line 3: Reading files is fun.
Line 4: End of file.

You should create this 'sample.txt' file manually before running this script.
"""


# Define the filename
filename = 'sample.txt'
file_content = """Line 1: Hello Python!
Line 2: This is the second line.
Line 3: Reading files is fun.
Line 4: End of file."""

# --- Create the sample file for demonstration ---
# This part creates the file if it doesn't exist.
# In a real scenario, the file you want to read would already exist.
try:
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(file_content)
    print(f"'{filename}' created successfully for demonstration.")
except IOError as e:
    print(f"Error creating sample file: {e}")
    # If we can't create the sample file, exit because reading will fail.
    exit()

print("\n--- Reading Files in Python ---")

# --- Method 1: Using `with open()` and `read()` ---
# This is the recommended way to open files.
# The `with` statement ensures the file is automatically closed
# even if errors occur.
# `read()` reads the entire content of the file into a single string.
print("\nMethod 1: Reading the entire file with read()")
try:
    # 'r' mode is for reading (this is the default mode)
    # 'encoding='utf-8'' is recommended for handling various characters
    with open(filename, 'r', encoding='utf-8') as file:
        content = file.read()
        print("File content:")
        print(content)
        print("Type of content:", type(content))
except FileNotFoundError:
    print(f"Error: The file '{filename}' was not found.")
except IOError as e:
    print(f"Error reading file: {e}")

# --- Method 2: Using `with open()` and `readline()` ---
# `readline()` reads a single line from the file, including the newline
# character ('\n') at the end.
# You can call it multiple times to read subsequent lines.
# It returns an empty string ('') when the end of the file (EOF) is reached.
print("\nMethod 2: Reading the file line by line with readline()")
try:
    with open(filename, 'r', encoding='utf-8') as file:
        print("Reading lines one by one:")
        line1 = file.readline()
        print("Line 1:", repr(line1)) # repr() shows hidden characters like '\n'
        line2 = file.readline()
        print("Line 2:", repr(line2))
        # You can also use a loop to read all lines
        print("\nReading remaining lines using a loop:")
        while True:
            line = file.readline()
            if not line: # An empty string means end of file
                break
            print(repr(line.strip())) # strip() removes leading/trailing whitespace (like '\n')
except FileNotFoundError:
    print(f"Error: The file '{filename}' was not found.")
except IOError as e:
    print(f"Error reading file: {e}")

# --- Method 3: Using `with open()` and `readlines()` ---
# `readlines()` reads all lines from the file and returns them as a list
# of strings. Each string in the list includes the newline character ('\n').
# Be cautious with very large files, as this loads the entire file into memory.
print("\nMethod 3: Reading all lines into a list with readlines()")
try:
    with open(filename, 'r', encoding='utf-8') as file:
        lines_list = file.readlines()
        print("File content as a list of lines:")
        print(lines_list)
        print("Type of lines_list:", type(lines_list))
        print("\nIterating through the list:")
        for i, line in enumerate(lines_list):
            print(f"List item {i}: {repr(line)}")
except FileNotFoundError:
    print(f"Error: The file '{filename}' was not found.")
except IOError as e:
    print(f"Error reading file: {e}")

# --- Method 4: Iterating directly over the file object (Recommended for line-by-line processing) ---
# This is the most Pythonic and memory-efficient way to read a file line by line.
# The `with open()` statement provides a file object that can be iterated over directly.
# Each iteration yields one line from the file, including the newline character.
print("\nMethod 4: Iterating directly over the file object (Recommended)")
try:
    with open(filename, 'r', encoding='utf-8') as file:
        print("Reading lines using direct iteration:")
        for i, line in enumerate(file): # The file object itself is iterable
            print(f"Line {i+1}: {repr(line.strip())}") # strip() for cleaner output
except FileNotFoundError:
    print(f"Error: The file '{filename}' was not found.")
except IOError as e:
    print(f"Error reading file: {e}")

# --- Important Note on File Closing ---
# Using the `with` statement (as shown in all methods above) is crucial because
# it automatically handles closing the file. If you don't use `with`, you
# *must* manually close the file using `file.close()` to free up system resources
# and ensure data is written correctly (though less critical in read mode).

# Example without `with` (less recommended):
# print("\nManual file opening and closing (less recommended)")
# try:
#     file = open(filename, 'r', encoding='utf-8')
#     content = file.read()
#     print("Content read without 'with':")
#     print(content)
# except FileNotFoundError:
#     print(f"Error: The file '{filename}' was not found.")
# except IOError as e:
#     print(f"Error reading file: {e}")
# finally:
#     # Ensure the file is closed even if errors occurred
#     if 'file' in locals() and not file.closed:
#         file.close()
#         print("File closed manually.")


# --- Clean up the sample file (optional) ---
# try:
#     os.remove(filename)
#     print(f"\n'{filename}' removed.")
# except OSError as e:
#     print(f"Error removing sample file: {e}")

print("\n--- End of Demonstration ---")