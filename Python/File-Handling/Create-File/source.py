import os

# Import the 'os' module
# While not strictly required for the basic 'open' function,
# the 'os' module provides useful functions for interacting with the operating system,
# including checking if a file exists (`os.path.exists`).

# --- Introduction to File Creation in Python ---
# The primary way to create files in Python is using the built-in `open()` function.
# This function can open existing files or create new ones depending on the 'mode' specified.

# Key modes for creating/writing to files:
# 'w' (write): Opens a file for writing.
#            - If the file exists, its contents are overwritten (deleted first).
#            - If the file does not exist, it is created.
# 'a' (append): Opens a file for appending.
#            - If the file exists, new data is written to the end of the file.
#            - If the file does not exist, it is created.
# 'x' (exclusive creation): Creates a new file for writing.
#            - If the file already exists, the operation fails with a FileExistsError.
#            - This is useful to avoid accidentally overwriting an existing file.
# '+' (update): Can be added to 'w', 'a', or 'x' (e.g., 'w+', 'a+') to allow both reading and writing.

# The `with open(...) as ...:` statement is the recommended way to work with files.
# It automatically handles closing the file, even if errors occur during processing.

# --- Example 1: Creating a file using 'w' (write) mode ---
file_name_w = "my_new_file_w.txt"
print(f"--- Attempting to create '{file_name_w}' using 'w' mode ---")

try:
    # Open the file in 'w' mode. If it exists, it will be truncated (emptied).
    # If it doesn't exist, it will be created.
    with open(file_name_w, "w") as f:
        # 'f' is the file object. We can use methods like write() on it.
        print(f"Successfully opened/created '{file_name_w}' in 'w' mode.")
        f.write("Hello from Python using 'w' mode!\n")
        f.write("This line will be written to the file.\n")
        # The file is automatically closed when exiting the 'with' block.
    print(f"Successfully wrote content to '{file_name_w}'.")

    # Optional: Verify creation
    if os.path.exists(file_name_w):
        print(f"Verification: '{file_name_w}' exists.")
    else:
        print(f"Verification failed: '{file_name_w}' was not found.")

except IOError as e:
    # Catch potential input/output errors during file operations (e.g., permissions)
    print(f"An error occurred while working with '{file_name_w}': {e}")
except Exception as e:
    # Catch any other unexpected errors
    print(f"An unexpected error occurred: {e}")

print("\n--- Example 1 finished ---\n")


# --- Example 2: Creating/Appending to a file using 'a' (append) mode ---
file_name_a = "my_new_file_a.txt"
print(f"--- Attempting to create/append to '{file_name_a}' using 'a' mode ---")

try:
    # First attempt: Create the file if it doesn't exist
    print(f"Attempt 1: Opening '{file_name_a}' in 'a' mode.")
    with open(file_name_a, "a") as f:
        print(f"Successfully opened/created '{file_name_a}' in 'a' mode.")
        f.write("This is the first line added using 'a' mode.\n")
    print(f"Successfully wrote first line to '{file_name_a}'.")

    # Second attempt: Append more content to the *same* file
    print(f"\nAttempt 2: Opening '{file_name_a}' again in 'a' mode to append.")
    with open(file_name_a, "a") as f:
        print(f"Successfully opened '{file_name_a}' again.")
        f.write("This is a second line, appended to the existing content.\n")
    print(f"Successfully appended second line to '{file_name_a}'.")

    # Optional: Verify creation/existence
    if os.path.exists(file_name_a):
        print(f"\nVerification: '{file_name_a}' exists.")
        # You could also read the file here to verify content, but that's beyond file *creation*.
    else:
        print(f"\nVerification failed: '{file_name_a}' was not found.")

except IOError as e:
    print(f"An error occurred while working with '{file_name_a}': {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

print("\n--- Example 2 finished ---\n")


# --- Example 3: Creating a file using 'x' (exclusive creation) mode ---
file_name_x = "my_new_file_x.txt"
print(f"--- Attempting to create '{file_name_x}' using 'x' mode ---")

# Clean up before trying 'x' mode, in case the file exists from a previous run
if os.path.exists(file_name_x):
    print(f"'{file_name_x}' already exists. Deleting it before 'x' mode test.")
    try:
        os.remove(file_name_x)
    except OSError as e:
        print(f"Error deleting existing '{file_name_x}': {e}")
        # If deletion fails, the 'x' mode test below will likely fail as expected.

# First attempt: Should succeed if the file doesn't exist
print(f"\nAttempt 1: Creating '{file_name_x}' with 'x' mode.")
try:
    with open(file_name_x, "x") as f:
        print(f"Successfully created '{file_name_x}' using 'x' mode.")
        f.write("Created exclusively with 'x' mode.\n")
    print(f"Successfully wrote content to '{file_name_x}'.")

    # Optional: Verify creation
    if os.path.exists(file_name_x):
        print(f"Verification: '{file_name_x}' exists.")
    else:
        print(f"Verification failed: '{file_name_x}' was not found.")

except FileExistsError:
    # This error occurs if the file *already* exists when using 'x' mode.
    print(f"Error: '{file_name_x}' already exists. Cannot create with 'x' mode.")
except IOError as e:
    print(f"An IO error occurred while trying to create '{file_name_x}': {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")


# Second attempt: Should fail because the file now exists
print(f"\nAttempt 2: Trying to create '{file_name_x}' again with 'x' mode (expected to fail).")
try:
    with open(file_name_x, "x") as f:
        # This part should not be reached if the file exists
        print(f"This message should NOT appear if '{file_name_x}' exists.")
        f.write("This should not be written.\n")
except FileExistsError:
    # This is the EXPECTED outcome for the second attempt.
    print(f"Successfully caught FileExistsError: '{file_name_x}' already exists, as expected.")
except IOError as e:
    print(f"An IO error occurred on the second attempt with '{file_name_x}': {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

print("\n--- Example 3 finished ---")

# --- Optional: Clean up created files ---
# You might want to delete the files created by this script afterwards.
# Uncomment the following lines to enable cleanup.

# print("\n--- Cleaning up created files ---")
# for filename in [file_name_w, file_name_a, file_name_x]:
#     try:
#         if os.path.exists(filename):
#             os.remove(filename)
#             print(f"Successfully deleted '{filename}'.")
#         else:
#             print(f"'{filename}' not found, no need to delete.")
#     except OSError as e:
#         print(f"Error deleting '{filename}': {e}")
# print("--- Cleanup finished ---")

print("\n--- Script finished ---")