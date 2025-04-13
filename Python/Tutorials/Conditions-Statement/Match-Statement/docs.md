# Python Match Statement (Structural Pattern Matching)

Introduced in Python 3.10, the `match` statement provides a way to implement structural pattern matching, similar to `switch` statements found in other languages like C++ or Java, but much more powerful. It allows you to compare a value (the "subject") against several patterns and execute code based on the first pattern that matches.

## Basic Syntax

The basic structure of a `match` statement is:

```python
match subject:
    case <pattern_1>:
        <action_1>
    case <pattern_2>:
        <action_2>
    case <pattern_3> if <guard>: # Optional guard
        <action_3>
    case _: # Wildcard pattern (optional, matches anything)
        <default_action>
```

-   `subject`: The value you want to match.
-   `case <pattern>`: Defines a pattern to compare against the `subject`.
-   `<action>`: The block of code to execute if the corresponding pattern matches.
-   `if <guard>`: An optional condition that must also be true for the pattern to match.
-   `case _`: A wildcard pattern that matches anything if no other pattern matches. It's often used for default cases.

**Important:** Only the code block corresponding to the *first* matching pattern is executed.

## Pattern Types

### 1. Literal Patterns

Match exact values like numbers, strings, `True`, `False`, and `None`.

```python
status_code = 200
match status_code:
    case 200:
        print("OK")
    case 404:
        print("Not Found")
    case 500:
        print("Internal Server Error")
    case _:
        print("Unknown status")
```

### 2. Variable Patterns (Capture Patterns)

A single variable name acts as a pattern. It always matches and binds the subject's value to that variable name within the `case` block.

```python
value = "hello"
match value:
    case x: # Matches anything and binds it to x
        print(f"Captured value: {x}")
```
*Note:* `_` is also a variable pattern, but it's special – it's the "wildcard" and doesn't bind the value.

### 3. Wildcard Pattern (`_`)

The underscore `_` acts as a wildcard. It matches any subject but doesn't bind the value to a variable. It's commonly used as a default case when placed last.

```python
value = (1, 2, 3)
match value:
    case (0, y):
        print("Starts with 0")
    case _: # Matches anything else
        print("Doesn't start with 0")
```

### 4. OR Patterns (`|`)

Combine multiple patterns using the `|` (OR) operator. If the subject matches *any* of the patterns separated by `|`, the case block executes. All sub-patterns in an OR pattern must bind the same set of variables.

```python
http_status = 418
match http_status:
    case 200 | 201 | 204:
        print("Success")
    case 400 | 401 | 403 | 404:
        print("Client Error")
    case 500 | 502 | 503:
        print("Server Error")
    case _:
        print("Other")
```

### 5. AS Patterns (`pattern as name`)

Match a pattern and bind the matched value (or part of it) to a variable name using the `as` keyword.

```python
point = (10, 20)
match point:
    case (0, 0):
        print("Origin")
    case (x, 0) as p: # Match points on the x-axis
        print(f"X-axis point {p} at x={x}")
    case (0, y) as p: # Match points on the y-axis
        print(f"Y-axis point {p} at y={y}")
    case (x, y) as p: # Match any other point
        print(f"Point {p} at ({x}, {y})")
    case _:
        print("Not a point")
```

### 6. Sequence Patterns (`[]` or `()`)

Match sequences like lists or tuples. You can match fixed-length sequences, variable-length sequences using `*`, and capture elements.

```python
data = [1, 2, 3]
match data:
    case []: # Empty list
        print("Empty list")
    case [x]: # List with one element
        print(f"Single element: {x}")
    case [x, y]: # List with two elements
        print(f"Two elements: {x}, {y}")
    case [x, *rest]: # List with at least one element
        print(f"First: {x}, Rest: {rest}")
    case (*_, y, z): # Match last two elements (Python 3.11+)
        print(f"Last two: {y}, {z}")
    case _:
        print("Other sequence")
```

### 7. Mapping Patterns (`{}`)

Match dictionary-like objects (mappings). You can match specific keys, capture values associated with keys, and use `**rest` to capture remaining key-value pairs.

```python
command = {"action": "move", "direction": "north", "speed": 10}
match command:
    case {"action": "quit"}:
        print("Quitting...")
    case {"action": "move", "direction": dir}: # Match action and capture direction
        print(f"Moving {dir}")
    case {"action": action, **details}: # Capture action and remaining details
        print(f"Action: {action}, Details: {details}")
    case {}: # Empty dictionary
        print("Empty command")
    case _:
        print("Unknown command structure")
```
*Note:* Only specified keys are checked. Extra keys in the subject are ignored unless `**rest` is used.

### 8. Class Patterns

Match objects based on their class type and attributes.

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def locate(p):
    match p:
        case Point(x=0, y=0): # Match specific attribute values
            print("Origin")
        case Point(x=x, y=0): # Match type and capture attribute x
            print(f"On X-axis at {x}")
        case Point(x=0, y=y): # Match type and capture attribute y
            print(f"On Y-axis at {y}")
        case Point(x=x, y=y): # Match type and capture both attributes
            print(f"Point at ({x}, {y})")
        case _:
            print("Not a Point object")

locate(Point(5, 0))
locate(Point(0, 10))
locate("hello")
```

### 9. Guards (`if condition`)

Add an `if` condition to a `case` pattern. The pattern only matches if both the pattern structure matches *and* the guard condition evaluates to `True`. Variables captured in the pattern are available in the guard expression.

```python
point = (10, 20)
match point:
    case (x, y) if x == y:
        print(f"On the diagonal y=x at ({x},{y})")
    case (x, y) if x > 0 and y > 0:
        print(f"In the first quadrant at ({x},{y})")
    case (x, y):
        print(f"Somewhere else at ({x},{y})")
```

## Summary

The `match` statement is a powerful control flow structure in Python 3.10+ that allows for sophisticated matching based on the *structure* of data, not just its value. It makes code cleaner and more readable when dealing with complex conditional logic based on data types and structures. Remember that only the first matching `case` block is executed.
