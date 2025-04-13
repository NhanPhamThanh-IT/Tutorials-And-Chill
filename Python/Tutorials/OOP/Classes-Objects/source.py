# --- Python Classes and Objects: A Detailed Beginner's Guide ---

# === 1. What is a Class? ===
# A class is like a blueprint or a template for creating objects.
# It defines a set of attributes (data/variables) and methods (functions)
# that the objects created from the class will have.
# We define a class using the `class` keyword.

class Dog:
    """
    This class represents a dog. It serves as a blueprint
    for creating individual dog objects.
    """

    # === 2. Class Attributes ===
    # Class attributes are variables that are shared among ALL instances (objects)
    # of the class. They belong to the class itself, not to any specific object.
    # They are defined directly inside the class definition, but outside any methods.
    species = "Canis familiaris"  # All dogs belong to this species

    # === 3. The Constructor (`__init__` method) ===
    # The `__init__` method is a special method called a constructor.
    # It gets automatically called when you create a new object (instance) of the class.
    # Its primary purpose is to initialize the object's attributes (instance attributes).
    # The `self` parameter is mandatory as the first parameter in instance methods (including `__init__`).
    # `self` refers to the specific instance of the class being created or worked with.
    def __init__(self, name, breed, age):
        """
        Initializes a new Dog object.

        Args:
            name (str): The name of the dog.
            breed (str): The breed of the dog.
            age (int): The age of the dog in years.
        """
        print(f"Creating a new Dog object named {name}...")

        # === 4. Instance Attributes ===
        # Instance attributes are variables that belong to a specific instance (object)
        # of the class. Each object created from the class can have different values
        # for its instance attributes.
        # They are typically defined within the `__init__` method using `self.attribute_name`.
        self.name = name
        self.breed = breed
        self.age = age
        self.is_awake = True # Default state for a new dog object

        print(f"Dog {self.name} initialized.")

    # === 5. Instance Methods ===
    # Instance methods are functions defined inside a class that perform actions
    # related to the object or modify its state.
    # They always take `self` as their first parameter, allowing them to access
    # and modify the object's instance attributes and call other methods.

    def bark(self):
        """Makes the dog bark."""
        if self.is_awake:
            print(f"{self.name} says: Woof! Woof!")
        else:
            print(f"{self.name} is sleeping... zzz...")

    def describe(self):
        """Describes the dog."""
        print(f"Name: {self.name}")
        print(f"Breed: {self.breed}")
        print(f"Age: {self.age} years old")
        print(f"Species: {self.species}") # Accessing the class attribute
        print(f"Awake: {'Yes' if self.is_awake else 'No'}")

    def sleep(self):
        """Puts the dog to sleep."""
        if self.is_awake:
            print(f"{self.name} is going to sleep.")
            self.is_awake = False
        else:
            print(f"{self.name} is already sleeping.")

    def wake_up(self):
        """Wakes the dog up."""
        if not self.is_awake:
            print(f"{self.name} is waking up.")
            self.is_awake = True
        else:
            print(f"{self.name} is already awake.")

    def celebrate_birthday(self):
        """Increases the dog's age by one year."""
        self.age += 1
        print(f"Happy Birthday, {self.name}! You are now {self.age} years old.")


# === 6. Creating Objects (Instances) ===
# To create an object (instance) from a class, you call the class name
# followed by parentheses `()`, passing any required arguments defined
# in the `__init__` method (excluding `self`).

print("--- Creating Dog Objects ---")
dog1 = Dog("Buddy", "Golden Retriever", 3)
print("-" * 20)
dog2 = Dog("Lucy", "Poodle", 5)
print("-" * 20)

# `dog1` and `dog2` are now objects (instances) of the `Dog` class.
# Each object has its own set of instance attributes (`name`, `breed`, `age`, `is_awake`).

# === 7. Accessing Attributes ===
# You can access an object's instance attributes using dot notation (`object.attribute`).
# You can also access class attributes using either the class name or an instance.

print("\n--- Accessing Attributes ---")
print(f"Dog 1's name: {dog1.name}")
print(f"Dog 2's age: {dog2.age}")

# Accessing class attribute via instance
print(f"Dog 1's species: {dog1.species}")
# Accessing class attribute via class name
print(f"Species for all dogs: {Dog.species}")

# Modifying an instance attribute
dog1.age = 4
print(f"Dog 1's updated age: {dog1.age}")

# === 8. Calling Methods ===
# You call an object's methods using dot notation (`object.method()`).
# Remember to include the parentheses `()` even if the method takes no arguments other than `self`.

print("\n--- Calling Methods ---")
dog1.bark()
dog2.sleep()
dog2.bark() # Lucy is sleeping
dog1.describe()
print("-" * 10)
dog2.describe()
print("-" * 10)
dog2.wake_up()
dog2.bark() # Lucy is awake now
dog1.celebrate_birthday()

# === 9. Inheritance ===
# Inheritance allows a new class (called a subclass or derived class)
# to inherit attributes and methods from an existing class (called a superclass or base class).
# This promotes code reuse.
# The subclass can add its own unique attributes and methods, or override inherited ones.
# We define a subclass by putting the superclass name in parentheses after the subclass name.

class GuideDog(Dog): # GuideDog inherits from Dog
    """
    Represents a guide dog, inheriting from the Dog class
    and adding specific attributes and methods for guide dogs.
    """

    def __init__(self, name, breed, age, owner_name):
        """
        Initializes a GuideDog object.

        Args:
            name (str): The name of the dog.
            breed (str): The breed of the dog.
            age (int): The age of the dog in years.
            owner_name (str): The name of the person the guide dog assists.
        """
        print(f"Initializing a GuideDog named {name}...")
        # === 10. Calling the Superclass Constructor (`super().__init__`) ===
        # To initialize the inherited attributes from the superclass (`Dog`),
        # we need to call the superclass's `__init__` method.
        # The `super()` function provides a way to do this.
        super().__init__(name, breed, age) # Calls Dog.__init__(self, name, breed, age)

        # Add attributes specific to GuideDog
        self.owner_name = owner_name
        self.is_working = False # Guide dogs aren't always working

        print(f"GuideDog {self.name} initialized for owner {self.owner_name}.")

    # === 11. Method Overriding ===
    # Subclasses can provide their own implementation of a method
    # that is already defined in the superclass. This is called overriding.
    def bark(self):
        """Guide dogs might bark differently, especially when working."""
        if self.is_working:
            print(f"{self.name} stays quiet while working.")
        else:
            # We can still call the original `bark` method from the superclass
            # using `super()` if needed.
            print(f"{self.name} (Guide Dog) says: ", end="")
            super().bark() # Calls the bark() method from the Dog class

    # Add methods specific to GuideDog
    def lead(self):
        """Simulates the guide dog leading its owner."""
        if self.is_awake and self.is_working:
            print(f"{self.name} is carefully guiding {self.owner_name}.")
        elif not self.is_awake:
            print(f"{self.name} needs to wake up first!")
        else:
             print(f"{self.name} needs to be in working mode to lead.")

    def start_working(self):
        """Puts the guide dog into working mode."""
        if self.is_awake:
            print(f"{self.name} is now working, assisting {self.owner_name}.")
            self.is_working = True
        else:
            print(f"{self.name} needs to wake up before working.")

    def stop_working(self):
        """Takes the guide dog out of working mode."""
        print(f"{self.name} is now off duty.")
        self.is_working = False

    # Overriding describe to include guide dog specific info
    def describe(self):
        """Describes the guide dog, including owner information."""
        super().describe() # Call the original describe method first
        print(f"Owner: {self.owner_name}")
        print(f"Working: {'Yes' if self.is_working else 'No'}")


# === 12. Using the Subclass ===
print("\n--- Creating and Using GuideDog Objects ---")
guide_dog1 = GuideDog("Riley", "Labrador", 4, "Alice")
print("-" * 20)

guide_dog1.describe()
print("-" * 10)

guide_dog1.bark() # Not working, barks normally (using overridden method)
guide_dog1.start_working()
guide_dog1.bark() # Working, stays quiet (using overridden method)
guide_dog1.lead()
guide_dog1.stop_working()
guide_dog1.bark() # Not working again
print("-" * 10)
guide_dog1.describe() # Shows updated working status

# Note: guide_dog1 still has access to methods from the Dog class
guide_dog1.celebrate_birthday()
guide_dog1.sleep()
guide_dog1.lead() # Cannot lead while sleeping

print("\n--- End of Demonstration ---")

# === Key Concepts Summary ===
# *   Class: Blueprint for objects (e.g., `Dog`, `GuideDog`).
# *   Object/Instance: A specific creation based on a class (e.g., `dog1`, `guide_dog1`).
# *   `__init__`: Constructor method to initialize object attributes.
# *   `self`: Refers to the instance itself within methods.
# *   Attribute: Data associated with a class or object.
#     *   Class Attribute: Shared by all instances (e.g., `Dog.species`).
#     *   Instance Attribute: Specific to each instance (e.g., `dog1.name`).
# *   Method: Function defined within a class that operates on objects (e.g., `dog1.bark()`).
# *   Inheritance: Creating a new class (subclass) from an existing class (superclass), inheriting its features (e.g., `GuideDog` inherits from `Dog`).
# *   `super()`: Used in subclasses to call methods from the superclass (e.g., `super().__init__()`, `super().bark()`).
# *   Method Overriding: Providing a specific implementation for a method in a subclass that is already defined in its superclass (e.g., `GuideDog` overrides `bark`).