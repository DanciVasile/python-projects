"""Functions
Create reusable blocks of code

​
Building with functions
Functions are reusable blocks of code that do specific tasks. Instead of writing the same code multiple times, you write it once as a function and call it whenever needed.
Think of functions like:
A recipe you can follow multiple times
A machine that takes input and produces output
A named shortcut for complex operations
​
Why use functions?
Don’t repeat yourself: Write code once, use it many times
Stay organized: Break complex programs into smaller pieces
Fix bugs easier: Change code in one place, affects everywhere
Test your code: Test each function separately"""


# Define a function
def greet():
    print("Hello World!")
    print("Welcome to Python!")


# Call the function
greet()


# Function syntax
def function_name():
    # Code goes here
    # Must be indented
    pass


"""
Naming functions
Follow these rules for function names:
Use lowercase letters
Separate words with underscores
Be descriptive about what it does"""


def calculate_total():
    pass


def send_email():
    pass


def validate_password():
    pass


# BAD NAMES
def func1():  # NOT DESCRIPTIVE
    pass


def Calculate():  # SHOULD BE LOWERCASE
    pass


# Calling functions
def say_goodbye():
    print("Goodbye")
    print("See you later!")


# Call it multiple times
say_goodbye()
say_goodbye()
say_goodbye()


# Functions with logic
def check_weather():
    temperature = 25
    if temperature > 30:
        print("It's hot!")
    else:
        print("Nice weather!")


# Use the function
check_weather()

# Variable scope: Local vs Global
# Variables in Python have a "scope" - where they can be accessed and used.


# LOCAL VARIABLES
# Varibles created within a function only exist within than function
def calculate_price():
    price = 100
    tax = price * 0.1
    print(f"Total: {price + tax}")


calculate_price()

# This fails - price doesn't exist outside the function
"""print(price) #NameError: name 'price' is not defined"""

# GLOBAL VARIABLES
# Variables outside the function can be accessed anywhere:
discount_rate = 0.15  # Global variable


def apply_discount(price):
    discount = price * discount_rate  # Can read global variable
    return price - discount


result = apply_discount(100)
print(result)  # 85.0

# MODIFYING GLOBAL VARIABLES
# To change a global variable inside a function, use the global keyword:

counter = 0  # Global variable


def increment():
    global counter  # Declare we want to modify the globalvariable
    counter += 1


increment()
increment()
print(counter)  # 2

"""Avoid using global when possible, it makes harder to
understand and debug. Instead, pass values as parameters and return results."""

# BEST PRACTICE: Use parameters and returns

# Bad - using global variable
total = 0


def add_to_total(amount):
    global total
    total += amount


# Good - using parameters and return
def add_amounts(current_total, amount):
    return current_total + amount


total = 0
total = add_amounts(total, 10)
total = add_amounts(total, 20)
print(total)  # 30

"""When a local and global variable have the same name,
the local variable "shadows" the global variable inside the function.
Python will always use the local version first"""
