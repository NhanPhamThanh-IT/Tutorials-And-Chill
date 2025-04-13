# While Loops in Python

## Introduction

In programming, we often need to repeat a block of code multiple times. A `while` loop is one way to achieve this in Python. It repeatedly executes a target statement as long as a given condition remains true.

Think of it like saying, "While this condition is true, keep doing this task." Once the condition becomes false, the loop stops, and the program continues with the code that comes after the loop.

## Basic Syntax

The basic structure of a `while` loop looks like this:

```python
while condition:
    # Code block to be executed
    # This code runs as long as 'condition' is True
    # Make sure something inside the loop eventually makes the condition False!
# Code here runs after the loop finishes (when condition becomes False)
```

*   **`while` keyword:** Starts the loop.
*   **`condition`:** An expression that evaluates to either `True` or `False`. The loop continues as long as this is `True`.
*   **`:`:** A colon marks the end of the `while` statement.
*   **Indented code block:** The statements inside the loop that are executed repeatedly. Indentation (usually 4 spaces) is crucial in Python to define the scope of the loop.

## Simple Example: Counting

Let's look at a simple example that prints numbers from 0 up to (but not including) 5.

```python
# Initialize a counter variable
count = 0

# Loop as long as count is less than 5
print("Starting the loop...")
while count < 5:
    print(f"Inside the loop: Count is {count}")
    # IMPORTANT: Update the counter variable
    # If we don't do this, count will always be 0, and the loop will never end!
    count = count + 1  # Or use the shorthand: count += 1

print(f"Loop finished! Final count value is {count}")
```

**Explanation:**

1.  **Initialization:** We start by setting `count` to `0`. This happens *before* the loop begins.
2.  **Condition Check:** The loop checks if `count < 5`. Initially, `0 < 5` is `True`, so the loop body executes.
3.  **Execution:** The code inside the loop runs:
    *   It prints the current value of `count`.
    *   It increments `count` by 1 (`count = count + 1`).
4.  **Repeat:** The loop goes back to step 2 (Condition Check).
    *   Is `1 < 5`? Yes. Execute the loop body (`count` becomes 2).
    *   Is `2 < 5`? Yes. Execute the loop body (`count` becomes 3).
    *   Is `3 < 5`? Yes. Execute the loop body (`count` becomes 4).
    *   Is `4 < 5`? Yes. Execute the loop body (`count` becomes 5).
5.  **Condition Check (Exit):** The loop checks again: Is `5 < 5`? No, this is `False`.
6.  **Termination:** Since the condition is `False`, the loop terminates. The program execution jumps to the first statement *after* the indented loop block.
7.  **After Loop:** The final `print` statement outside the loop executes.

## Infinite Loops

A common pitfall is creating an *infinite loop* – a loop whose condition *never* becomes `False`. This usually happens if you forget to include code inside the loop that changes the variables involved in the condition.

```python
# WARNING: This is an infinite loop! Do not run without knowing how to stop it.
# Press Ctrl+C in the terminal to stop execution.

# counter = 0
# while counter < 5:
#     print("This will print forever!")
#     # We forgot to increment the counter! It will always be 0.
```

**Always ensure that something within your `while` loop will eventually make the condition `False` to avoid infinite loops.**

## Controlling Loop Flow: `break` and `continue`

Sometimes you need more control over when a loop stops or skips an iteration.

### The `break` Statement

The `break` statement immediately terminates the *current* loop, regardless of whether the loop's condition is still `True`. Execution continues at the first statement *after* the loop.

```python
count = 0
while True:  # Often used with break for loops that check conditions inside
    print(f"Checking count: {count}")
    if count >= 3:
        print("Condition met, breaking out of the loop!")
        break  # Exit the loop immediately
    count += 1
print(f"Loop finished after break. Count is {count}")
```

### The `continue` Statement

The `continue` statement skips the *rest* of the current iteration of the loop and jumps directly back to the condition check at the top of the loop to start the next iteration (if the condition is still `True`).

```python
number = 0
print("Printing odd numbers less than 10:")
while number < 10:
    number += 1
    # If the number is even, skip the print statement for this iteration
    if number % 2 == 0:
        continue  # Go back to the 'while number < 10' check
    # This print statement only runs if 'continue' was not executed (i.e., for odd numbers)
    print(number)
print("Loop finished.")
```

## The `else` Clause with `while` Loops

Python's `while` loops (and `for` loops) have an optional `else` clause that might seem unusual at first. The `else` block executes *only* if the loop completes normally (i.e., the `while` condition becomes `False`). It does **not** execute if the loop is terminated by a `break` statement.

```python
attempts = 0
max_attempts = 3

while attempts < max_attempts:
    print(f"Attempt {attempts + 1}")
    # Simulate some task
    # Let's say the task succeeds on the 2nd attempt for this example
    if attempts == 1:
         print("Task succeeded!")
         # break # Uncomment this break to see the 'else' block skipped

    attempts += 1
else:
    # This block runs ONLY if the loop finished because 'attempts < max_attempts' became False
    print("Loop completed all attempts without an early break.")

print("Continuing after the loop structure.")

print("\n--- Example with break ---")
attempts = 0
while attempts < max_attempts:
    print(f"Attempt {attempts + 1}")
    if attempts == 1:
         print("Task succeeded! Breaking early.")
         break # Exit the loop prematurely
    attempts += 1
else:
    # This block will NOT run because the loop was terminated by 'break'
    print("Loop completed all attempts without an early break.")
print("Continuing after the loop structure.")
```

## Common Use Cases

*   **User Input:** Keep asking for input until valid input is received.
*   **Game Loops:** Keep the game running until the player chooses to quit.
*   **Processing Data:** Read data from a source (like a file or network) until there's no more data.
*   **Waiting:** Pause execution until a certain condition is met (e.g., waiting for a file to appear).

## Summary

*   `while` loops execute a block of code as long as a condition is `True`.
*   The condition is checked *before* each iteration.
*   You **must** ensure the condition eventually becomes `False` within the loop to avoid infinite loops.
*   `break` exits the loop immediately.
*   `continue` skips the current iteration and goes to the next condition check.
*   The optional `else` block runs only if the loop finishes normally (not via `break`).