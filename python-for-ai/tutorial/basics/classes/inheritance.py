"""What is inheritance?
Inheritance lets you create new classes based on existing ones. The new class (child) gets everything from the parent class, plus can add its own stuff.
Think of it like this:
All dogs are animals (dogs inherit from animals)
Dogs have everything animals have, plus dog-specific things"""


# Basic inheritance example
# Parent class - general animal
class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        return f"{self.name} is eating."

    def sleep(self):
        return f"{self.name} is sleeping."


# Child class - specific animal
class Dog(Animal):
    def bark(self):
        return f"{self.name} says woof!"


# Create a dog using positional args
my_dog = Dog("Buddy")
# Or with named args
my_dog2 = Dog(name="Max")

# Dog can do animal things
print(my_dog.eat())  # Buddy is eating.
print(my_dog.sleep())  # Buddy is sleeping.
print(my_dog.bark())  # Buddy says woof!

# Adding attributes in child classes


class Human:
    def __init__(self, name):
        self.name = name
        self.is_alive = True


class Student(Human):
    def __init__(self, name, student_id):
        super().__init__(name)  # Pass name to parent's __init__
        self.student_id = student_id

    def describe(self):
        return f"{self.name} is a student with ID {self.student_id}."


# Create a student with student ID, positional args
student1 = Student("Mike", "S12345")

# Create a student with student ID, named args
student2 = Student(name="Giovanni", student_id="S884930")

print(student1.describe())  # Mike is a student with ID S12345.
print(student2.describe())  # Giovanni is a student with ID S884930.
print(student1.is_alive)  # True (inherited from Human)


"""super().__init__() calls the parent class’s __init__ method.
This ensures the parent class sets up its attributes properly before the child class adds its own."""

# Overriding methods, child classes can change how parents methods work


class Animal:
    def __init__(self, name):
        self.name = name

    def makes_sound(self):
        return f"{self.name} makes a sound."


class Cat(Animal):
    def makes_sound(self):
        return f"{self.name} meows: meow!"  # Overrides the parent method


class Dog(Animal):
    def makes_sounds(self):
        return f"{self.name} barks: woof!"  # Overrides the parent method


# Different animals make different sounds
generic = Animal(name="Something")
dog = Dog(name="Buddy")
cat = Cat(name="Whiskers")

print(generic.makes_sound())  # Something makes a sound.
print(dog.makes_sound())  # Buddy barks: woof!
print(cat.makes_sound())  # Whiskers meows: meow!


# Real-world use case
# Here is a practical example for AI applications:
class BaseModel:
    def __init__(self, model_name):
        self.model_name = model_name
        self.is_loaded = False

    def load(self):
        print(f"Loading model: {self.model_name}...")
        self.is_loaded = True


class TextModel(BaseModel):
    def __init__(self, model_name, max_length):
        super().__init__(model_name)  # Initialize BaseModel
        self.max_length = max_length

    def process_text(self, text):
        if not self.is_loaded:
            self.load()
        # Truncate if needed
        if len(text) > self.max_length:
            text = text[: self.max_length]
        return f"Processed text: {text}"


# Use the model - with named arguments
model = TextModel(model_name="Claude", max_length=1000)

# Call method, notice no "self" parameter needed
result = model.process_text(text="Hello World!" * 100)  # Long text to test truncation
print(
    result
)  # Processed text: Hello World!Hello World!Hello World!... (truncated to 1000 chars)

"""
When to use inheritance
Use inheritance when:
You have an “is a” relationship (Dog is an Animal)
Child classes share most behavior with parent
You want to extend functionality, not replace it
Don’t use inheritance when:
Classes are only slightly related
You just want to reuse one or two methods
The relationship feels forced"""


# Example of wrong inheritance:
# Wrong - Rectangle is not a Square!
class Square:
    def __init__(self, size):
        self.size = size


class Rectangle(Square):  # Doesn't make sense
    def __init__(self, width, height):
        self.width = width
        self.height = height


# Better - they're both shapes
class Shape:
    pass


class Square(Shape):
    def __init__(self, size):
        self.size = size


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height


# When to use classes
# Use classes when you need to:
# Keep track of state between operations
# Group related data and functions together
# Create multiple instances with similar behavior
# Model real-world objects or concepts
# ​
# When to use functions
# Use functions when you have:
# Simple transformations (input → output)
# Stateless operations
# One-off calculations
# Small scripts

"""Start with functions. They’re simpler and often sufficient.
Only add classes when you find yourself passing the same data between 
multiple functions or when you need to maintain state."""


# Common pitfalls
# Over-engineering: Don’t create classes for simple operations. A class with one method is usually better as a function.
# God objects: Classes that do too many things. Keep classes focused on a single responsibility.
# Static method classes: If all methods are static, you probably want a module with functions instead.
