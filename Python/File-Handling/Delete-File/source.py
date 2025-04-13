import os

# Import the 'os' module
# The 'os' module provides functions for interacting with the operating system,
# such as creating, reading, updating, and deleting files and directories.

# Define the name of the file we want to work with
file_name = "my_sample_file_to_delete.txt"

# --- Step 1: Create a dummy file to delete ---
# We need a file to exist before we can delete it.
# This 'try...except' block handles the file creation.
try:
    # 'with open(...) as f:' is a safe way to handle files.
    # It ensures the file is properly closed even if errors occur.
    # 'w' mode means 'write' mode. If the file exists, it will be overwritten.
    # If it doesn't exist, it will be created.
    with open(file_name, "w") as f:
        f.write("This is some content in the file.\n")
        f.write("We will delete this file soon.\n")
    print(f"Successfully created the file: '{file_name}' for demonstration.")
except IOError as e:
    # If there's an error during file creation (e.g., disk full, permissions),
    # print an error message.
    print(f"Error creating file '{file_name}': {e}")
    # Exit the script if we can't create the file, as there's nothing to delete.
    exit() # Stop the script here

# --- Step 2: Check if the file exists before attempting deletion ---
# It's good practice to check if a file exists before trying to delete it.
# Trying to delete a non-existent file will cause an error.
print(f"\nChecking if file '{file_name}' exists...")

if os.path.exists(file_name):
    # os.path.exists(file_name) returns True if the file exists, False otherwise.
    print(f"File '{file_name}' found. Proceeding with deletion.")

    # --- Step 3: Delete the file ---
    # Use a 'try...except' block to handle potential errors during deletion.
    try:
        # os.remove(file_name) is the function that deletes the file.
        os.remove(file_name)
        # If os.remove() executes without error, the file is deleted.
        print(f"Successfully deleted the file: '{file_name}'")

        # Optional: Verify deletion by checking existence again
        print(f"\nVerifying deletion by checking if '{file_name}' still exists...")
        if not os.path.exists(file_name):
            print(f"Verification successful: '{file_name}' no longer exists.")
        else:
            # This case is unlikely if os.remove() succeeded but included for completeness
            print(f"Verification failed: '{file_name}' still seems to exist.")

    except FileNotFoundError:
        # This error *shouldn't* happen if os.path.exists() was True just before,
        # but it's possible in rare cases (e.g., another process deleted it).
        print(f"Error: File '{file_name}' was not found during deletion attempt.")
    except PermissionError:
        # This error occurs if the script doesn't have the necessary permissions
        # to delete the file (e.g., file is read-only, or locked by another program).
        print(f"Error: Permission denied. Could not delete '{file_name}'.")
    except OSError as e:
        # Catch any other potential OS-related errors during deletion.
        print(f"An OS error occurred while trying to delete '{file_name}': {e}")

else:
    # This block executes if os.path.exists(file_name) returned False initially.
    print(f"File '{file_name}' does not exist. No deletion needed.")

print("\n--- Script finished ---")