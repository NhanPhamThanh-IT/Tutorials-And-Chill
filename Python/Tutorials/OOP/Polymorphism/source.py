# --- Polymorphism in Python ---

# Polymorphism, which means "many forms", is a fundamental concept in
# Object-Oriented Programming (OOP). It allows objects of different classes
# to respond to the same method call in their own specific ways.

# --- 1. Method Overriding (Inheritance-based Polymorphism) ---

# This is the most common form of polymorphism in statically-typed languages,
# and it's also very common in Python. It involves defining a method in a
# subclass that has the same name as a method in its superclass. The subclass's
# method overrides the superclass's method.

print("--- Example 1: Method Overriding ---")

class Animal:
    """A base class for different animals."""
    def __init__(self, name):
        self.name = name
        print(f"Animal '{self.name}' created.")

    def speak(self):
        """A generic sound an animal might make."""
        # This method is intended to be overridden by subclasses.
        # We can raise an error or provide a default implementation.
        print(f"{self.name} makes a generic animal sound.")
        # Alternatively: raise NotImplementedError("Subclass must implement abstract method")

class Dog(Animal):
    """A subclass representing a dog."""
    def speak(self):
        """Overrides the Animal speak method for a dog."""
        print(f"{self.name} says Woof!")

class Cat(Animal):
    """A subclass representing a cat."""
    def speak(self):
        """Overrides the Animal speak method for a cat."""
        print(f"{self.name} says Meow!")

class Bird(Animal):
    """A subclass representing a bird."""
    def speak(self):
        """Overrides the Animal speak method for a bird."""
        print(f"{self.name} says Tweet!")

# Create instances of different animal classes
my_dog = Dog("Buddy")
my_cat = Cat("Whiskers")
my_bird = Bird("Sky")
generic_animal = Animal("Creature")

# Call the 'speak' method on each object.
# Notice that the *same* method call (`.speak()`) results in
# *different* behaviors depending on the object's actual class.
my_dog.speak()
my_cat.speak()
my_bird.speak()
generic_animal.speak() # Calls the base class method

print("\n--- Example 2: Polymorphism with a Function ---")

# We can write functions that work with any object that implements
# a certain method, regardless of its specific class.

def make_animal_speak(animal_object):
    """
    Takes an object and calls its speak() method.
    This function demonstrates polymorphism because it can work
    with any object that has a 'speak' method.
    """
    print(f"Calling speak() on a {type(animal_object).__name__} object:")
    animal_object.speak()

# Pass different types of Animal objects to the function
make_animal_speak(my_dog)
make_animal_speak(my_cat)
make_animal_speak(my_bird)
make_animal_speak(generic_animal)

# --- 2. Duck Typing (Interface-based Polymorphism) ---

# Python follows a principle often called "Duck Typing".
# "If it walks like a duck and quacks like a duck, then it must be a duck."
# This means Python focuses on an object's *behavior* (the methods it has)
# rather than its explicit *type* or *class inheritance*.

# An object doesn't need to inherit from `Animal` to be used by our
# `make_animal_speak` function, as long as it has a `speak()` method.

print("\n--- Example 3: Duck Typing ---")

class Car:
    """A class representing a car. It's not an Animal."""
    def __init__(self, model):
        self.model = model
        print(f"Car '{self.model}' created.")

    def speak(self):
        """A car 'speaks' differently - it honks!"""
        # Note: The method name is the same ('speak'), but the class
        # does NOT inherit from Animal.
        print(f"{self.model} says Honk! Honk!")

my_car = Car("Tesla Model 3")

# We can still pass the Car object to make_animal_speak,
# because it has a 'speak()' method (it "quacks like a duck").
make_animal_speak(my_car)

# --- 3. Polymorphism with Built-in Functions ---

# Many built-in Python functions and operators exhibit polymorphism.
# For example, the `len()` function works on different types of objects
# (strings, lists, tuples, dictionaries, custom objects with __len__)
# as long as they implement the necessary protocol (the `__len__` method).

print("\n--- Example 4: Polymorphism with len() ---")

print(f"Length of string 'hello': {len('hello')}")
print(f"Length of list [1, 2, 3]: {len([1, 2, 3])}")
print(f"Length of dictionary {{'a': 1, 'b': 2}}: {len({'a': 1, 'b': 2})}")

# Similarly, the '+' operator performs addition for numbers and
# concatenation for strings and lists.

print("\n--- Example 5: Polymorphism with '+' operator ---")
print(f"5 + 3 = {5 + 3}")
print(f"'Hello' + ' World' = {'Hello' + ' World'}")
print(f"[1, 2] + [3, 4] = {[1, 2] + [3, 4]}")


# --- Summary ---
# Polymorphism allows us to write more flexible and reusable code.
# - Method Overriding: Subclasses provide specific implementations for methods
#   defined in their superclass.
# - Duck Typing: Focuses on whether an object *can do* something (has the method)
#   rather than what the object *is* (its class).
# This enables functions and methods to operate on objects of various types
# as long as they support the required operations or methods (interface).