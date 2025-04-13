# File Methods in Python - Detailed Examples for Beginners

# --- Creating and Writing to a File ---

# 1. open() - Opens a file and returns a file object.
#    Modes:
#    'r' - Read (default). Error if the file doesn't exist.
#    'a' - Append. Creates the file if it doesn't exist. Appends to the end.
#    'w' - Write. Creates the file if it doesn't exist. Truncates (empties) the file if it exists.
#    'x' - Create. Creates the specified file. Error if the file exists.
#    't' - Text mode (default).
#    'b' - Binary mode (e.g., for images).
#    '+' - Open for updating (reading and writing). e.g., 'r+', 'w+', 'a+'

# Let's open a file named 'my_example_file.txt' in write mode ('w').
# If the file exists, its content will be deleted. If not, it will be created.
try:
    # It's good practice to use try...finally or a 'with' statement
    # to ensure the file is closed even if errors occur.
    file_object = open('my_example_file.txt', 'w')
    print(f"File opened in write mode: {file_object.name}")
    print(f"Mode: {file_object.mode}")

    # 2. writable() - Returns True if the file stream allows writing.
    print(f"Is file writable? {file_object.writable()}") # Output: True

    # 3. write() - Writes the specified string to the file.
    #    Returns the number of characters written.
    content1 = "Hello, this is the first line.\n"
    chars_written1 = file_object.write(content1)
    print(f"Wrote {chars_written1} characters: '{content1.strip()}'")

    content2 = "This is the second line.\n"
    chars_written2 = file_object.write(content2)
    print(f"Wrote {chars_written2} characters: '{content2.strip()}'")

    # 4. writelines() - Writes a list of strings (lines) to the file.
    #    Note: It does NOT add newline characters between lines automatically.
    lines_to_write = [
        "This is the third line, written using writelines.\n",
        "And the fourth line.\n"
    ]
    file_object.writelines(lines_to_write)
    print(f"Wrote lines using writelines: {lines_to_write}")

    # 5. flush() - Flushes the internal buffer.
    #    Python buffers writes; flush() forces writing to the disk immediately.
    #    Often not needed explicitly, as close() does this.
    file_object.flush()
    print("File buffer flushed.")

    # 6. fileno() - Returns the integer file descriptor used by the underlying implementation.
    #    This is more of an OS-level concept.
    file_descriptor = file_object.fileno()
    print(f"File descriptor number: {file_descriptor}")

    # 7. isatty() - Returns True if the file stream is interactive (connected to a tty device).
    #    For regular files, this is usually False.
    print(f"Is file connected to a tty? {file_object.isatty()}") # Output: False

finally:
    # 8. close() - Closes the file. Releases system resources.
    #    Always close files after you are done with them!
    if 'file_object' in locals() and not file_object.closed:
        file_object.close()
        print(f"File closed. Is it closed? {file_object.closed}") # Output: True

print("-" * 30)

# --- Reading from a File ---

# Now, let's open the same file in read mode ('r').
try:
    file_object = open('my_example_file.txt', 'r')
    print(f"\nFile opened in read mode: {file_object.name}")
    print(f"Mode: {file_object.mode}")

    # 9. readable() - Returns True if the file stream allows reading.
    print(f"Is file readable? {file_object.readable()}") # Output: True
    print(f"Is file writable? {file_object.writable()}") # Output: False

    # 10. read(size) - Reads 'size' bytes from the file.
    #     If 'size' is omitted or negative, reads the entire file content.
    print("\nReading first 10 characters using read(10):")
    first_10_chars = file_object.read(10)
    print(f"'{first_10_chars}'")

    # 11. tell() - Returns the current position of the file pointer (cursor) in bytes.
    current_position = file_object.tell()
    print(f"Current file pointer position: {current_position} bytes")

    print("\nReading the rest of the file using read():")
    rest_of_content = file_object.read()
    print(rest_of_content)

    # Trying to read again will return an empty string as we are at the end.
    print(f"Reading again after reaching the end: '{file_object.read()}'")

    # 12. seek(offset, whence=0) - Changes the file pointer position.
    #     offset: Number of bytes to move.
    #     whence: Reference point (optional):
    #         0: Absolute positioning (from the beginning, default).
    #         1: Relative to the current position.
    #         2: Relative to the end of the file.
    #     Note: For text files ('t' mode), only seeking with whence=0 is guaranteed
    #           to work reliably (except seek(0, 2) to go to the end).
    #           Use binary mode ('b') for more flexible seeking.

    print("\nMoving pointer to the beginning using seek(0):")
    file_object.seek(0)
    print(f"Current position after seek(0): {file_object.tell()}")

    # 13. readline(size) - Reads one entire line from the file.
    #     If 'size' is specified, reads at most 'size' bytes from that line.
    print("\nReading line by line using readline():")
    line1 = file_object.readline()
    print(f"Line 1: '{line1.strip()}' (Position: {file_object.tell()})")
    line2 = file_object.readline()
    print(f"Line 2: '{line2.strip()}' (Position: {file_object.tell()})")

    # Go back to the beginning
    file_object.seek(0)
    print("\nPointer moved back to the beginning.")

    # 14. readlines(hint) - Reads all lines from the file and returns them as a list of strings.
    #     'hint' (optional): If specified, reads approximately 'hint' bytes and enough more
    #     to complete a line, returning that list. Often not used.
    print("\nReading all lines using readlines():")
    all_lines = file_object.readlines()
    print(all_lines) # Note: Each line includes the newline character '\n'

    # Iterating directly over the file object is often more memory-efficient for large files
    file_object.seek(0) # Go back to the beginning again
    print("\nIterating directly over the file object (recommended):")
    for line_number, line in enumerate(file_object):
        print(f"Line {line_number + 1}: {line.strip()}")

finally:
    if 'file_object' in locals() and not file_object.closed:
        file_object.close()
        print(f"\nFile closed. Is it closed? {file_object.closed}")

print("-" * 30)

# --- Appending to a File ---

# Open in append mode ('a')
try:
    file_object = open('my_example_file.txt', 'a')
    print(f"\nFile opened in append mode: {file_object.name}")
    print(f"Mode: {file_object.mode}")
    print(f"Is file writable? {file_object.writable()}") # Output: True

    # The file pointer starts at the end in append mode.
    print(f"Initial position in append mode: {file_object.tell()}")

    append_content = "This line was appended.\n"
    file_object.write(append_content)
    print(f"Appended: '{append_content.strip()}'")
    print(f"Position after appending: {file_object.tell()}")

finally:
    if 'file_object' in locals() and not file_object.closed:
        file_object.close()
        print(f"File closed. Is it closed? {file_object.closed}")

# Verify the appended content by reading the file again
print("\nReading the file after appending:")
try:
    file_object = open('my_example_file.txt', 'r')
    print(file_object.read())
finally:
    if 'file_object' in locals() and not file_object.closed:
        file_object.close()

print("-" * 30)

# --- Using the 'with' Statement (Recommended Practice) ---

# The 'with' statement automatically handles closing the file,
# even if errors occur within the block. This is safer and cleaner.

print("\nUsing 'with' statement for writing:")
try:
    with open('my_example_file_with.txt', 'w') as f:
        print(f"  File opened: {f.name}, Mode: {f.mode}")
        f.write("This file was created using the 'with' statement.\n")
        f.write("It ensures the file is closed automatically.\n")
        # No need to call f.close() explicitly
        print(f"  Is file closed inside 'with'? {f.closed}") # Output: False
    print(f"File closed outside 'with'? {f.closed}") # Output: True
except IOError as e:
    print(f"An error occurred: {e}")


print("\nUsing 'with' statement for reading:")
try:
    with open('my_example_file_with.txt', 'r') as f:
        print(f"  File opened: {f.name}, Mode: {f.mode}")
        content = f.read()
        print("  File content:")
        print(content)
    print(f"File closed outside 'with'? {f.closed}") # Output: True
except FileNotFoundError:
    print("Error: The file 'my_example_file_with.txt' was not found.")
except IOError as e:
    print(f"An error occurred: {e}")

print("-" * 30)

# --- Truncating a File ---

# 15. truncate(size) - Resizes the file to 'size' bytes.
#     If 'size' is not specified, truncates at the current position.
#     Requires the file to be opened in a mode that allows writing ('w', 'a', 'r+', etc.).

try:
    # Open in read and write mode ('r+')
    with open('my_example_file.txt', 'r+') as f:
        print(f"\nFile opened for truncate: {f.name}, Mode: {f.mode}")
        print("Original content:")
        print(f.read())

        # Truncate the file to the first 20 bytes
        f.seek(0) # Go to the beginning before truncating from a specific size
        f.truncate(20)
        print("\nFile truncated to 20 bytes.")

        # Read the truncated content
        f.seek(0) # Need to go back to the beginning to read
        print("Content after truncate(20):")
        print(f.read())

        # Now truncate at the current position (which is the end after reading)
        # This won't change anything as we are already at the end.
        # Let's seek to position 10 and truncate from there
        f.seek(10)
        print(f"\nCurrent position: {f.tell()}")
        f.truncate() # Truncates from byte 10 onwards
        print("File truncated at current position (10).")

        f.seek(0)
        print("Content after truncate() at position 10:")
        print(f.read())

except IOError as e:
    print(f"An error occurred during truncate: {e}")

print("\n--- End of File Methods Examples ---")

# Note on other methods (less common for basic file I/O):
# - detach(): Separates the underlying raw stream from the buffer. Advanced use.
# - seekable(): Returns True if the file stream supports random access (seek, tell).
# - encoding: The encoding used for text files (e.g., 'utf-8').
# - errors: The error handling scheme used for encoding/decoding errors.
# - newlines: The newline character(s) detected during reading ('\n', '\r', '\r\n').