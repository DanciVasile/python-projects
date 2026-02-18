"""Parameters
Pass data into your functions

​
What are parameters?
Parameters let you pass data into functions.
Instead of hardcoding values, you make functions flexible to work with different inputs.
"""


# Without parameters (inflexible)
def greet_alice():
    print("Hello, Alice!")


greet_alice()


# With parameters (flexible)
def greet(name):
    print(f"Hello, {name}!")


# Now it works for anyone
greet("Alice")
greet("Bob")
greet("Charlie")

# Basic parameters
# Add parameters inside the parentheses when defining a function


def introduce(name, age):
    print(f"My name is {name}")
    print(f"I am {age} years old")


# Call with values
introduce("Alice", 25)
introduce("Bob", 30)

"""The values you pass when calling a function are called "arguments".
The variables in the function definition are "parameters".
Many people use these terms interchangeably"""

# Multiple parameters
# Functions can have multiple parameters:


def calculate_total(price, tax_rate, discount):
    tax = price * tax_rate
    final_price = price + tax - discount
    print(f"Total: ${final_price}")


# Order matters!
calculate_total(100, 0.08, 10)  # $98

# Defining values
# Give parameters default values for optional arguments:


def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}!")


# Use default
greet("Alice")  # Hello Alice!

# Override default
greet("Bob", "Hi")  # Hi, Bob!
greet("Charlie", "Hey")  # Hey, Charlie!

"""Put parameters with defaults at the end. Required parameters
come first, optional ones last."""

# Keyword arguments
# Call functions using parameter names for clarity:


def create_profile(name, age, city):
    print(f"{name}, {age}, from {city}")


# Positional arguments (order matters)
create_profile("Alice", 25, "New York City")

# Keyword arguments (order doesn't matter)
create_profile(city="NYC", age=35, name="Alice")
create_profile(name="Bob", city="Melbourne", age=18)


def greet(name, age):
    print(f"Hi {name}, you're {age}")


# COMMON MISTAKES
# Wrong - too few arguments
greet("Alice")  # TypeError!

# Wrong - too many arguments
greet("Alice", 25, "NYC")  # TypeError!

# Right
greet("Alice", 25)


# Wrong - don't use lists as defaults
# Default values with mutable objects
def add_item(item, list=[]):
    list.append(item)
    return list


# Right - use None and create new list
def add_items(item, list=None):
    if list is None:
        list = []
    list.append(item)
    return list
