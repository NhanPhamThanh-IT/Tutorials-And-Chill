import sys
from importlib import metadata
import pkg_resources

# -*- coding: utf-8 -*-
"""
source.py

This file serves as a conceptual example related to PIP (Pip Installs Packages),
the standard package manager for Python.

PIP is a command-line tool, not typically used directly *within* Python code itself.
Instead, you use PIP in your terminal or command prompt to manage external
libraries (packages) that your Python scripts might need.

This script will demonstrate:
1.  How to check if a package is installed using Python code.
2.  Provide comments explaining common PIP commands you would run in your terminal.
"""

import importlib.util
import subprocess # Used to demonstrate *calling* pip, though direct terminal use is standard

# --- What is PIP? ---
# PIP is the package installer for Python. You can use pip to install packages
# from the Python Package Index (PyPI) and other indexes.
#
# Why use packages?
# Packages contain pre-written code that provides specific functionality.
# Instead of writing everything from scratch, you can install packages to:
#   - Make HTTP requests (like the 'requests' package)
#   - Work with data (like 'pandas', 'numpy')
#   - Build web applications (like 'Flask', 'Django')
#   - And much more!
#
# Where do you run PIP commands?
# You run PIP commands in your system's terminal or command prompt,
# NOT inside a Python interpreter or script (usually).

# --- Common PIP Commands (Run these in your Terminal/Command Prompt) ---

# 1. Installing a package:
#    Syntax: pip install <package_name>
#    Example: pip install requests
#    This downloads and installs the 'requests' library from PyPI.
#    You can install specific versions:
#    Example: pip install requests==2.25.1
#    Install from a requirements file:
#    Example: pip install -r requirements.txt
#             (where requirements.txt lists packages line by line)

# 2. Uninstalling a package:
#    Syntax: pip uninstall <package_name>
#    Example: pip uninstall requests
#    This removes the 'requests' library from your environment.
#    It will usually ask for confirmation (y/n).

# 3. Listing installed packages:
#    Syntax: pip list
#    This shows all the packages installed in your current Python environment,
#    along with their versions.

# 4. Saving installed packages to a file (requirements.txt):
#    Syntax: pip freeze > requirements.txt
#    This command is very useful for sharing your project with others.
#    It creates a file named 'requirements.txt' listing all installed packages
#    and their exact versions. Others can then use `pip install -r requirements.txt`
#    to replicate your environment. `pip list` provides a more readable format,
#    while `pip freeze` provides the format needed for requirements files.

# 5. Showing information about an installed package:
#    Syntax: pip show <package_name>
#    Example: pip show requests
#    This displays details like the package's version, author, location,
#    and dependencies.

# 6. Checking for broken dependencies:
#    Syntax: pip check
#    This verifies that installed packages have compatible dependencies.

# 7. Upgrading a package:
#    Syntax: pip install --upgrade <package_name>
#    Example: pip install --upgrade requests
#    This upgrades the 'requests' library to the latest version available on PyPI.

# 8. Searching for packages on PyPI:
#    Syntax: pip search <query>
#    Example: pip search http client
#    This searches PyPI for packages matching the query terms.
#    Note: This command can sometimes be slow or disabled due to server load.
#          It's often easier to search directly on the PyPI website (https://pypi.org/).

# --- Checking if a package is installed using Python ---

def is_package_installed(package_name):
    """
    Checks if a given package is installed in the current Python environment.

    Args:
        package_name (str): The name of the package to check (e.g., 'requests').

    Returns:
        bool: True if the package is installed, False otherwise.
    """
    package_spec = importlib.util.find_spec(package_name)
    if package_spec is None:
        print(f"Package '{package_name}' is NOT installed.")
        return False
    else:
        # If you need the version, you can use importlib.metadata (Python 3.8+)
        try:
            version = metadata.version(package_name)
            print(f"Package '{package_name}' is installed (Version: {version}).")
        except ImportError:
            # Fallback for older Python versions (less reliable)
            try:
                # Note: pkg_resources can be slow to import
                version = pkg_resources.get_distribution(package_name).version
                print(f"Package '{package_name}' is installed (Version: {version}).")
            except ImportError:
                 print(f"Package '{package_name}' is installed (Could not determine version - importlib.metadata or pkg_resources not available).")
            except pkg_resources.DistributionNotFound:
                 # This case should ideally be caught by find_spec, but added for robustness
                 print(f"Package '{package_name}' seems found by find_spec but pkg_resources couldn't find its distribution.")
                 return False # Treat as not installed if version check fails this way
        except Exception as e:
            print(f"Package '{package_name}' is installed, but an error occurred getting version: {e}")

        return True

# --- Example Usage within Python ---

print("--- Checking for installed packages using Python ---")

# Check for a package that is likely installed (like 'pip' itself)
is_package_installed("pip")

# Check for a common package (try running 'pip install requests' in your terminal first)
is_package_installed("requests")

# Check for a package that is likely *not* installed
is_package_installed("non_existent_package_abc123")

print("\n--- Demonstrating calling PIP from Python (Informational Only) ---")
# IMPORTANT: It's generally better practice to manage packages directly
# from your terminal rather than calling pip using subprocess within a script.
# This is shown for demonstration purposes only.

def install_package_from_script(package_name):
    """
    Attempts to install a package using pip via subprocess.
    Use with caution and prefer terminal commands.
    """
    print(f"\nAttempting to install '{package_name}' using subprocess...")
    try:
        # sys.executable ensures we use the pip associated with the current Python interpreter
        subprocess.check_call([sys.executable, "-m", "pip", "install", package_name])
        print(f"Successfully called pip to install '{package_name}'.")
        # Verify installation
        is_package_installed(package_name)
    except subprocess.CalledProcessError as e:
        print(f"Failed to install '{package_name}'. Error: {e}")
    except FileNotFoundError:
        print("Error: 'pip' command not found. Is Python/pip in your system's PATH?")

# Example: Try installing a small, harmless package like 'python-dateutil'
# You might need to run this script with administrator privileges depending on your setup.
# install_package_from_script("python-dateutil") # Uncomment to try

print("\n--- End of Script ---")
print("Remember to run PIP commands like 'pip install <package>' in your terminal!")