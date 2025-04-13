# --- Python Inheritance Explained for Beginners ---

# Inheritance is a fundamental concept in Object-Oriented Programming (OOP).
# It allows a new class (called the Derived or Child class) to inherit
# attributes (data) and methods (functions) from an existing class
# (called the Base or Parent class).

# Benefits of Inheritance:
# 1. Code Reusability: Avoids writing the same code multiple times.
# 2. Extensibility: Easily add new features to existing code.
# 3. Organization: Creates a logical hierarchy ("is-a" relationship, e.g., a Dog "is-a" Animal).

# --------------------------------------------------------------------------
# 1. Base Class (Parent Class)
# --------------------------------------------------------------------------
# This is the class that provides the core attributes and methods.
# Other classes will inherit from this one.

print("--- 1. Defining the Base Class (Animal) ---")

class Animal:
    """
    This is the base class representing a generic animal.
    It defines common properties and behaviors shared by all animals.
    """
    def __init__(self, name, species):
        """
        Constructor method (__init__) for the Animal class.
        It's called automatically when you create a new Animal object.
        'self' refers to the instance being created.
        'name' and 'species' are arguments passed during object creation.
        """
        print(f"  [Animal __init__] Initializing an Animal.")
        self.name = name        # Attribute: Stores the animal's name
        self.species = species  # Attribute: Stores the animal's species
        self.is_alive = True    # Attribute: Default status

    def speak(self):
        """
        A method representing the sound the animal makes.
        This is a generic version for the base class.
        """
        print(f"  [Animal speak] {self.name} the {self.species} makes a generic sound.")

    def move(self, distance_meters=1):
        """
        A method representing the animal's movement.
        """
        print(f"  [Animal move] {self.name} the {self.species} moves {distance_meters} meter(s).")

    def display_info(self):
        """
        Displays the basic information about the animal.
        """
        status = "alive" if self.is_alive else "not alive"
        print(f"  [Animal display_info] Name: {self.name}, Species: {self.species}, Status: {status}")

# --- Creating and using an instance of the Base Class ---
print("\n--- Creating an instance of Animal ---")
generic_creature = Animal("Creature", "Unknown") # Creates an Animal object
generic_creature.display_info()
generic_creature.speak()
generic_creature.move(5)
print("-" * 30)


# --------------------------------------------------------------------------
# 2. Derived Class (Child Class) - Simple Inheritance
# --------------------------------------------------------------------------
# This class inherits from the Animal class.
# Syntax: class ChildClassName(ParentClassName):

print("\n--- 2. Defining a Derived Class (Dog) inheriting from Animal ---")

class Dog(Animal): # Dog inherits from Animal
    """
    This is a derived class representing a Dog.
    It inherits from the Animal class and adds dog-specific features.
    A Dog "is-a" type of Animal.
    """
    def __init__(self, name, breed):
        """
        Constructor for the Dog class.
        """
        print(f"  [Dog __init__] Initializing a Dog.")
        # --- Calling the Parent Class Constructor ---
        # It's crucial to initialize the parent class part of the object.
        # We use super() to refer to the parent class (Animal).
        # This calls Animal's __init__ method.
        super().__init__(name=name, species="Canine") # Pass name, specify species for all dogs
        print(f"  [Dog __init__] Parent (Animal) __init__ called via super().")

        # --- Adding Child-Specific Attributes ---
        self.breed = breed # Attribute specific to Dog

    # --- Inherited Methods ---
    # Dog objects automatically have access to 'move()' and 'display_info()'
    # methods from the Animal class because Dog inherits from Animal.

    # --- Method Overriding ---
    # We can provide a specific version of a method that already exists
    # in the parent class. This is called overriding.
    def speak(self):
        """
        Overrides the speak() method inherited from Animal.
        Provides a dog-specific implementation.
        """
        print(f"  [Dog speak] {self.name} the {self.breed} barks: Woof! Woof!")

    # --- Adding Child-Specific Methods ---
    def fetch(self, item="ball"):
        """
        A method unique to the Dog class.
        """
        print(f"  [Dog fetch] {self.name} fetches the {item}.")

# --- Creating and using an instance of the Derived Class ---
print("\n--- Creating an instance of Dog ---")
my_dog = Dog("Buddy", "Golden Retriever") # Creates a Dog object

# Accessing attributes (inherited and specific)
print(f"  Dog's name (from Animal): {my_dog.name}")
print(f"  Dog's species (from Animal): {my_dog.species}")
print(f"  Dog's breed (from Dog): {my_dog.breed}")

# Calling methods
my_dog.display_info() # Calls the inherited Animal display_info() method
my_dog.move(3)        # Calls the inherited Animal move() method
my_dog.speak()        # Calls the overridden Dog speak() method
my_dog.fetch("stick") # Calls the Dog-specific fetch() method
print("-" * 30)


# --------------------------------------------------------------------------
# 3. Using super() in Overridden Methods
# --------------------------------------------------------------------------
# Sometimes, you want to execute the parent class's version of a method
# *in addition* to the child class's specific logic. `super()` is used for this.

print("\n--- 3. Defining another Derived Class (Cat) using super() in methods ---")

class Cat(Animal):
    """
    Another derived class representing a Cat.
    Demonstrates using super() within an overridden method.
    """
    def __init__(self, name, color):
        """Constructor for Cat."""
        print(f"  [Cat __init__] Initializing a Cat.")
        super().__init__(name=name, species="Feline") # Initialize the Animal part
        self.color = color # Cat-specific attribute

    def speak(self):
        """Overrides speak, but also calls the parent's speak."""
        print(f"  [Cat speak] {self.name} the Cat looks around...")
        # Call the speak() method from the parent class (Animal)
        super().speak()
        # Add Cat-specific behavior after the parent's behavior
        print(f"  [Cat speak] ...and then {self.name} meows: Meow!")

    def groom(self):
        """A method specific to Cat."""
        print(f"  [Cat groom] {self.name} the {self.color} cat grooms itself meticulously.")

# --- Creating and using an instance of Cat ---
print("\n--- Creating an instance of Cat ---")
my_cat = Cat("Whiskers", "Tabby")
my_cat.display_info()
my_cat.move(2)
my_cat.speak() # This will execute both Animal's speak (via super()) and Cat's additions
my_cat.groom()
print("-" * 30)


# --------------------------------------------------------------------------
# 4. Multiple Inheritance (Advanced Topic)
# --------------------------------------------------------------------------
# A class can inherit from more than one parent class.
# Syntax: class ChildClassName(Parent1, Parent2, ...):
# Note: Multiple inheritance can sometimes lead to complexity (e.g., the
# "Diamond Problem" if multiple parents provide methods with the same name).
# Python uses Method Resolution Order (MRO) to decide which parent method to call.

print("\n--- 4. Multiple Inheritance Example (Flyer, Swimmer, FlyingFish) ---")

class Flyer:
    """A class representing the ability to fly."""
    def __init__(self, max_altitude):
        print(f"  [Flyer __init__] Initializing Flyer capability (Max Altitude: {max_altitude}m).")
        self.max_altitude = max_altitude

    def fly(self):
        print(f"  [Flyer fly] Flying up towards {self.max_altitude} meters.")

class Swimmer:
    """A class representing the ability to swim."""
    def __init__(self, max_depth):
        print(f"  [Swimmer __init__] Initializing Swimmer capability (Max Depth: {max_depth}m).")
        self.max_depth = max_depth

    def swim(self):
        print(f"  [Swimmer swim] Swimming down towards {self.max_depth} meters.")

# This class inherits from Animal, Flyer, and Swimmer
class FlyingFish(Animal, Flyer, Swimmer):
    """
    Represents a Flying Fish, inheriting behaviors from multiple parents.
    """
    def __init__(self, name, max_altitude, max_depth):
        print(f"  [FlyingFish __init__] Initializing a FlyingFish.")
        # --- Calling Multiple Parent Constructors ---
        # When using multiple inheritance, calling parent __init__ methods
        # needs careful handling. Calling each explicitly is often clearest.
        Animal.__init__(self, name=name, species="Exocoetidae")
        Flyer.__init__(self, max_altitude=max_altitude)
        Swimmer.__init__(self, max_depth=max_depth)
        # Note: Using super() in complex multiple inheritance requires understanding MRO.
        # super().__init__(...) might only call the __init__ of the *first* parent
        # listed in the inheritance order, depending on how the parent classes are defined.

    # Override speak for FlyingFish
    def speak(self):
        print(f"  [FlyingFish speak] {self.name} the Flying Fish makes bubbly noises.")

    # It inherits move() from Animal, fly() from Flyer, swim() from Swimmer

# --- Creating and using an instance of FlyingFish ---
print("\n--- Creating an instance of FlyingFish ---")
fifi = FlyingFish("Fifi", max_altitude=5, max_depth=50)
fifi.display_info() # From Animal
fifi.speak()        # Overridden in FlyingFish
fifi.move(0.5)      # From Animal
fifi.fly()          # From Flyer
fifi.swim()         # From Swimmer
print("-" * 30)


# --------------------------------------------------------------------------
# 5. Checking Inheritance Relationships: isinstance() and issubclass()
# --------------------------------------------------------------------------
# Python provides built-in functions to check relationships between objects and classes.

print("\n--- 5. Checking Relationships with isinstance() and issubclass() ---")

# isinstance(object, classinfo): Checks if an object is an instance of a class
# or an instance of a subclass thereof.
print("--- isinstance() checks ---")
print(f"Is my_dog an instance of Dog? {isinstance(my_dog, Dog)}")       # True
print(f"Is my_dog an instance of Animal? {isinstance(my_dog, Animal)}")   # True (Dog is a subclass of Animal)
print(f"Is my_dog an instance of Cat? {isinstance(my_dog, Cat)}")       # False
print(f"Is my_cat an instance of Animal? {isinstance(my_cat, Animal)}")   # True
print(f"Is fifi an instance of Flyer? {isinstance(fifi, Flyer)}")       # True
print(f"Is fifi an instance of Swimmer? {isinstance(fifi, Swimmer)}")   # True
print(f"Is fifi an instance of Animal? {isinstance(fifi, Animal)}")     # True
print(f"Is generic_creature an instance of Dog? {isinstance(generic_creature, Dog)}") # False

print("\n--- issubclass() checks ---")
# issubclass(class, classinfo): Checks if a class is a subclass of another class.
print(f"Is Dog a subclass of Animal? {issubclass(Dog, Animal)}")     # True
print(f"Is Cat a subclass of Animal? {issubclass(Cat, Animal)}")     # True
print(f"Is Animal a subclass of Dog? {issubclass(Animal, Dog)}")     # False (It's the other way around)
print(f"Is FlyingFish a subclass of Flyer? {issubclass(FlyingFish, Flyer)}") # True
print(f"Is FlyingFish a subclass of Swimmer? {issubclass(FlyingFish, Swimmer)}")# True
print(f"Is FlyingFish a subclass of Animal? {issubclass(FlyingFish, Animal)}")# True
print(f"Is Dog a subclass of object? {issubclass(Dog, object)}")       # True (All classes implicitly inherit from 'object')
print(f"Is Animal a subclass of object? {issubclass(Animal, object)}") # True
print("-" * 30)

print("\nInheritance demonstration complete.")