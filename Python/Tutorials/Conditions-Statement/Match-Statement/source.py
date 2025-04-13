# Python 3.10+ is required for the match statement

print("--- Basic Match Example ---")
def http_status(status):
    match status:
        case 200:
            return "OK"
        case 201:
            return "Created"
        case 400:
            return "Bad Request"
        case 404:
            return "Not Found"
        case 500 | 502 | 503: # OR Pattern (Literals)
            return "Server Error"
        case _: # Wildcard pattern (default case)
            return "Unknown status"

print(f"Status 200: {http_status(200)}")
print(f"Status 404: {http_status(404)}")
print(f"Status 503: {http_status(503)}")
print(f"Status 302: {http_status(302)}")

print("\n--- Variable Capture Example ---")
def describe_value(value):
    match value:
        case str() as s: # Match if value is a string, capture as s
            print(f"It's a string: '{s}'")
        case int() as i: # Match if value is an int, capture as i
            print(f"It's an integer: {i}")
        case x: # Variable pattern (captures anything else)
            print(f"It's something else: {x} (Type: {type(x).__name__})")

describe_value("Hello Python")
describe_value(123)
describe_value([1, 2, 3])
describe_value(None)

print("\n--- Sequence Pattern Example ---")
def process_list(items):
    match items:
        case []:
            print("List is empty")
        case [item1]:
            print(f"List has one item: {item1}")
        case [item1, item2]:
            print(f"List has two items: {item1} and {item2}")
        case [item1, *rest]: # Capture first item and the rest
            print(f"First item: {item1}, remaining: {rest}")
        case (*_, last_item): # Capture only the last item (Python 3.11+)
             print(f"Last item: {last_item}")
        case _:
            print("It's not a list or doesn't match other patterns")

process_list([])
process_list(["apple"])
process_list(["apple", "banana"])
process_list(["apple", "banana", "cherry", "date"])
process_list(tuple(["apple", "banana", "cherry", "date"])) # Also works with tuples

print("\n--- Mapping Pattern Example ---")
def process_command(command):
    match command:
        case {"action": "move", "direction": dir, "speed": speed}:
            print(f"Moving {dir} at speed {speed}")
        case {"action": "move", "direction": dir}: # Speed is optional here
            print(f"Moving {dir} (default speed)")
        case {"action": "shoot", "power": p}:
            print(f"Shooting with power {p}")
        case {"action": "quit"}:
            print("Quitting...")
        case {"action": action, **details}: # Capture action and other details
            print(f"Performing action '{action}' with details: {details}")
        case {}:
            print("Empty command")
        case _:
            print("Unknown command structure or not a dictionary")

process_command({"action": "move", "direction": "north", "speed": 10})
process_command({"action": "move", "direction": "south"})
process_command({"action": "shoot", "power": 95, "target": "enemy"})
process_command({"action": "quit"})
process_command({"operation": "load", "file": "data.txt"})
process_command({})
process_command("move north") # Not a dictionary

print("\n--- Class Pattern Example ---")
class Point:
    # Using __match_args__ helps with positional matching in class patterns
    __match_args__ = ("x", "y")
    def __init__(self, x, y):
        self.x = x
        self.y = y

def locate(p):
    match p:
        # Positional matching (requires __match_args__)
        case Point(0, 0):
            print("The point is at the Origin")
        # Keyword matching (always works)
        case Point(x=0, y=y_pos):
            print(f"The point is on the Y-axis at y={y_pos}")
        case Point(x=x_pos, y=0):
            print(f"The point is on the X-axis at x={x_pos}")
        # Capture attributes
        case Point(x=x_pos, y=y_pos):
            print(f"The point is at ({x_pos}, {y_pos})")
        case _:
            print("Not a Point object or doesn't match")

locate(Point(0, 0))
locate(Point(0, 5))
locate(Point(10, 0))
locate(Point(3, 4))
locate((3, 4)) # This is a tuple, not a Point

print("\n--- Guard Example ---")
def process_guarded_point(p):
    match p:
        case Point(x, y) if x == y: # Guard condition
            print(f"Point ({x},{y}) is on the diagonal y=x")
        case Point(x, y) if x > 0 and y > 0: # Another guard
            print(f"Point ({x},{y}) is in the first quadrant")
        case Point(x, y):
            print(f"Point ({x},{y}) is somewhere else")
        case _:
            print("Input is not a Point")

process_guarded_point(Point(5, 5))
process_guarded_point(Point(2, 8))
process_guarded_point(Point(-1, 3))
process_guarded_point(Point(0, 0)) # Matches the first guard

print("\n--- AS Pattern Example ---")
def check_data(data):
    match data:
        case [x, y] as pair if x == y: # Match a pair and bind it, with a guard
            print(f"Pair with equal elements: {pair}")
        case [_, _] as pair: # Match any pair and bind it
            print(f"Generic pair: {pair}")
        case str() as text: # Match a string and bind it
            print(f"Text data: '{text}'")
        case _:
            print("Other data format")

check_data([10, 10])
check_data([10, 20])
check_data("Hello")
check_data([1, 2, 3])
