import os

# -*- coding: utf-8 -*-
"""
This script demonstrates various ways to write to a text file in Python.
We will create and write to a file named 'output.txt' in the same directory
as this script.
"""

# Define the filename we will write to
filename = 'output.txt'

print("--- Writing Files in Python ---")

# --- Method 1: Using `open()` with 'w' mode (Write) ---
# The 'w' mode is used for writing.
# IMPORTANT: If the file already exists, its contents will be ERASED (overwritten).
# If the file does not exist, it will be created.
# Using `with open(...)` is highly recommended because it automatically
# handles closing the file, even if errors occur.
print("\nMethod 1: Writing to a file using 'w' mode (overwrites existing file)")
try:
    # Open the file in write mode ('w') with UTF-8 encoding
    # 'encoding='utf-8'' is good practice for handling diverse characters.
    with open(filename, 'w', encoding='utf-8') as file:
        print(f"Opened '{filename}' in 'w' mode.")

        # Write a single string to the file using file.write()
        file.write("Hello from Python!\n") # '\n' is the newline character

        # Write another line
        file.write("This is the second line written using 'w' mode.\n")

        # You can write variables too
        number = 123
        file.write(f"Here is a number: {number}\n")

        print(f"Successfully wrote initial content to '{filename}'.")
        # The file is automatically closed when exiting the 'with' block

except IOError as e:
    # Handle potential errors during file operations (e.g., permission issues)
    print(f"Error writing to file '{filename}': {e}")

# --- Verify Content after Method 1 ---
# Let's read the file to see what was written (optional, for demonstration)
try:
    with open(filename, 'r', encoding='utf-8') as file:
        print(f"\n--- Content of '{filename}' after 'w' mode: ---")
        print(file.read().strip()) # read() gets the whole content, strip() removes leading/trailing whitespace
        print("--- End of content ---")
except FileNotFoundError:
    print(f"Error: File '{filename}' not found for verification.")
except IOError as e:
    print(f"Error reading file for verification: {e}")


# --- Method 2: Using `open()` with 'a' mode (Append) ---
# The 'a' mode is used for appending.
# If the file exists, new data will be added to the END of the file.
# Existing content will NOT be erased.
# If the file does not exist, it will be created.
print("\nMethod 2: Appending to a file using 'a' mode")
try:
    # Open the file in append mode ('a')
    with open(filename, 'a', encoding='utf-8') as file:
        print(f"Opened '{filename}' in 'a' mode.")

        # Append a new line
        file.write("This line is appended using 'a' mode.\n")

        # Append another line
        file.write("Appending keeps the original content intact.\n")

        print(f"Successfully appended content to '{filename}'.")
        # File is automatically closed here

except IOError as e:
    print(f"Error appending to file '{filename}': {e}")

# --- Verify Content after Method 2 ---
try:
    with open(filename, 'r', encoding='utf-8') as file:
        print(f"\n--- Content of '{filename}' after 'a' mode: ---")
        print(file.read().strip())
        print("--- End of content ---")
except FileNotFoundError:
    print(f"Error: File '{filename}' not found for verification.")
except IOError as e:
    print(f"Error reading file for verification: {e}")


# --- Method 3: Using `writelines()` ---
# `writelines()` writes the items of an iterable (like a list or tuple) to the file.
# IMPORTANT: `writelines()` does NOT automatically add newline characters ('\n')
# between the items. You need to include them in your strings if you want new lines.
print("\nMethod 3: Writing a list of lines using writelines()")

lines_to_write = [
    "First line using writelines.\n", # Include '\n' for a new line
    "Second line using writelines.\n",
    "Third and final line from the list." # No '\n' here, so next write will be on same line
]

# Example using 'w' mode (overwrites the file again)
try:
    with open(filename, 'w', encoding='utf-8') as file:
        print(f"Opened '{filename}' in 'w' mode for writelines().")
        file.writelines(lines_to_write)
        print(f"Successfully wrote list content to '{filename}' using writelines().")
except IOError as e:
    print(f"Error writing list to file '{filename}': {e}")

# --- Verify Content after Method 3 ('w' mode) ---
try:
    with open(filename, 'r', encoding='utf-8') as file:
        print(f"\n--- Content of '{filename}' after writelines() with 'w' mode: ---")
        print(file.read().strip())
        print("--- End of content ---")
except FileNotFoundError:
    print(f"Error: File '{filename}' not found for verification.")
except IOError as e:
    print(f"Error reading file for verification: {e}")

# Example using 'a' mode (appends the list)
more_lines = [
    "\nAppending another list.\n", # Start with '\n' to ensure it's on a new line
    "This is the second item appended from a list.\n"
]
try:
    with open(filename, 'a', encoding='utf-8') as file:
        print(f"\nOpened '{filename}' in 'a' mode for writelines().")
        file.writelines(more_lines)
        print(f"Successfully appended list content to '{filename}' using writelines().")
except IOError as e:
    print(f"Error appending list to file '{filename}': {e}")

# --- Verify Content after Method 3 ('a' mode) ---
try:
    with open(filename, 'r', encoding='utf-8') as file:
        print(f"\n--- Content of '{filename}' after writelines() with 'a' mode: ---")
        print(file.read().strip())
        print("--- End of content ---")
except FileNotFoundError:
    print(f"Error: File '{filename}' not found for verification.")
except IOError as e:
    print(f"Error reading file for verification: {e}")


# --- Important Note on File Closing ---
# As mentioned, using the `with` statement is the best practice because
# it guarantees the file is closed properly, releasing system resources
# and ensuring all data is flushed (written) to the disk.
# If you don't use `with`, you MUST manually call `file.close()`.

# Example without `with` (less recommended):
# print("\nManual file opening and closing (less recommended)")
# file_handle = None # Initialize variable
# try:
#     # Open manually
#     file_handle = open(filename + "_manual.txt", 'w', encoding='utf-8')
#     file_handle.write("Writing manually requires explicit close().\n")
#     print("Wrote using manual open.")
# except IOError as e:
#     print(f"Error during manual write: {e}")
# finally:
#     # This block executes whether an error occurred or not
#     if file_handle and not file_handle.closed:
#         file_handle.close() # Crucial step!
#         print("File closed manually.")


# --- Clean up the created file (optional) ---
# You might want to remove the file created by the script
# try:
#     os.remove(filename)
#     print(f"\n'{filename}' removed.")
#     # os.remove(filename + "_manual.txt") # Remove the manually created one too if used
#     # print(f"'{filename}_manual.txt' removed.")
# except OSError as e:
#     print(f"Error removing file: {e}")

print("\n--- End of Demonstration ---")