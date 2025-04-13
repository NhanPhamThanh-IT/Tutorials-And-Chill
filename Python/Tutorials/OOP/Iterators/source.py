# --- Python Iterators Explained ---

# What is an Iterator?
# An iterator is an object that allows you to traverse through all the elements
# of a collection (like a list, tuple, dictionary, set, or string), one element at a time.
# It remembers its state, specifically which element it needs to return next.

# Key Concepts:
# 1. Iterable: An object capable of returning its members one at a time.
#    Examples: lists, tuples, strings, dictionaries, sets.
#    Technically, an object is iterable if it implements the `__iter__()` method,
#    which returns an iterator object.
# 2. Iterator: An object that represents a stream of data.
#    It implements the `__next__()` method, which returns the next item
#    from the stream. When there are no more items, it raises the
#    `StopIteration` exception.
#    An iterator also implements the `__iter__()` method, which usually
#    returns the iterator object itself (`self`).

# --- Using Built-in Iterators ---

# Example 1: Iterating over a list
print("--- Example 1: Iterating over a list ---")
my_list = [10, 20, 30, 40]

# Get an iterator object from the list using the built-in iter() function
my_iterator = iter(my_list)

print(f"Type of my_list: {type(my_list)}")
print(f"Type of my_iterator: {type(my_iterator)}")

# Use the next() function to get the next item from the iterator
print(f"First item: {next(my_iterator)}")  # Output: 10
print(f"Second item: {next(my_iterator)}") # Output: 20
print(f"Third item: {next(my_iterator)}")  # Output: 30
print(f"Fourth item: {next(my_iterator)}") # Output: 40

# If we call next() again after all items are exhausted, it raises StopIteration
try:
    print(next(my_iterator))
except StopIteration:
    print("StopIteration: No more items in the iterator.")

# Example 2: Iterating over a string
print("\n--- Example 2: Iterating over a string ---")
my_string = "Hi"
string_iterator = iter(my_string)

print(f"First char: {next(string_iterator)}")  # Output: H
print(f"Second char: {next(string_iterator)}") # Output: i

try:
    print(next(string_iterator))
except StopIteration:
    print("StopIteration: No more characters.")

# --- The `for` loop and Iterators ---

# The `for` loop in Python automatically handles the iterator protocol.
# When you write `for item in iterable:`, Python does the following behind the scenes:
# 1. Calls `iter(iterable)` to get an iterator object.
# 2. Repeatedly calls `next()` on the iterator object to get the next item.
# 3. Assigns the item to the loop variable (`item`).
# 4. Executes the loop body.
# 5. When `next()` raises `StopIteration`, the loop terminates automatically.

print("\n--- Example 3: Using a for loop (implicit iteration) ---")
my_tuple = (100, 200, 300)

print("Iterating through a tuple using a for loop:")
for number in my_tuple:
    print(number)
# Output:
# 100
# 200
# 300

# --- Creating a Custom Iterator ---

# To create your own iterator, you need to implement two special methods in your class:
# 1. `__iter__(self)`: This method should return the iterator object itself (`self`).
# 2. `__next__(self)`: This method should return the next item in the sequence.
#    When there are no more items, it must raise the `StopIteration` exception.

print("\n--- Example 4: Creating a custom iterator (CountUp) ---")

class CountUp:
    """An iterator that counts up from a start value to an end value."""

    def __init__(self, start, end):
        """Initialize the counter."""
        if start > end:
            raise ValueError("Start value cannot be greater than end value.")
        self.current = start
        self.end = end
        print(f"CountUp initialized: start={start}, end={end}")

    def __iter__(self):
        """Return the iterator object itself."""
        print("CountUp.__iter__() called")
        return self

    def __next__(self):
        """Return the next number in the sequence."""
        print("CountUp.__next__() called")
        if self.current > self.end:
            # No more items, raise StopIteration
            print("Raising StopIteration")
            raise StopIteration
        else:
            # Return the current value and increment for the next call
            value_to_return = self.current
            self.current += 1
            print(f"Returning {value_to_return}")
            return value_to_return

# Using the custom iterator directly with iter() and next()
print("\nUsing CountUp with iter() and next():")
counter_iterator = iter(CountUp(1, 3)) # Calls __init__ and __iter__

try:
    item1 = next(counter_iterator) # Calls __next__
    print(f"Received: {item1}")
    item2 = next(counter_iterator) # Calls __next__
    print(f"Received: {item2}")
    item3 = next(counter_iterator) # Calls __next__
    print(f"Received: {item3}")
    item4 = next(counter_iterator) # Calls __next__, raises StopIteration
    print(f"Received: {item4}") # This line won't be reached
except StopIteration:
    print("Caught StopIteration as expected.")

# Using the custom iterator with a for loop
print("\nUsing CountUp with a for loop:")
my_counter = CountUp(5, 7) # Calls __init__

# The for loop automatically calls iter(my_counter) which calls __iter__
# Then it repeatedly calls next() which calls __next__
for number in my_counter:
    print(f"For loop received: {number}")

print("\n--- Example 5: An iterator for powers of two ---")

class PowersOfTwo:
    """Iterates through powers of two up to a maximum exponent."""

    def __init__(self, max_exponent=5):
        self.max_exponent = max_exponent
        self.current_exponent = 0

    def __iter__(self):
        # Reset exponent for potential re-iteration if needed,
        # though typically iterators are single-use.
        # self.current_exponent = 0 # Optional: uncomment if re-iteration is desired
        return self

    def __next__(self):
        if self.current_exponent > self.max_exponent:
            raise StopIteration
        else:
            result = 2 ** self.current_exponent
            self.current_exponent += 1
            return result

# Using the PowersOfTwo iterator
print("\nPowers of Two up to exponent 4:")
powers = PowersOfTwo(4)
for power in powers:
    print(power)
# Output:
# 1
# 2
# 4
# 8
# 16

# Note: Once an iterator is exhausted (StopIteration is raised), it's generally
# considered empty. Trying to iterate over it again won't yield results unless
# its __iter__ method resets the state (which is less common).
print("\nTrying to iterate over the exhausted 'powers' iterator again:")
for power in powers:
    print(f"Second pass: {power}") # This loop will likely not print anything

print("\nCreating a new PowersOfTwo instance for re-iteration:")
for power in PowersOfTwo(3):
    print(power)
# Output:
# 1
# 2
# 4
# 8

print("\n--- End of Iterator Examples ---")