"""Return values
Get results back from your functions

​
Getting results from functions
So far, our functions have printed output.
But often you want functions to calculate something and give you the result to use elsewhere.
"""


# This function only prints
def add_print(a, b):
    print(a + b)


# This function returns a value
def add_return(a, b):
    return a + b


# Now you can use the result
result = add_return(5, 3)
print(f"The result is {result}")  # The result is 8


# The return statement
# Use return to send a value back from a function:
def calculate_area(width, height):
    area = width * height
    return area


# Store the returned value
room_area = calculate_area(10, 12)
print(f"Room size: {room_area} sq ft")  # Room size: 120 sq ft

"""When Python hits a return statement, it immediately exits the
function. Any code after return won't run"""

# Using returned values
# Returned values can be used in many ways


def double(number):
    return number * 2


# Store in variable
result = double(5)

# Use in expressions
total = double(5) + double(3)  # 10 + 6 = 16

# Pass the other functions
print(double(10))  # 20

# Use in conditions
if double(7) > 10:
    print("Big number!")

# Returning multiple values
# Python can return multiple values as a tuple:


def get_min_max(numbers):
    return min(numbers), max(numbers)


# Get bot values
minimum, maximum = get_min_max([5, 2, 8, 1, 9])
print(f"Min: {minimum}, Max: {maximum}")  # Min: 1, Max 9

# Or as a tuple
result = get_min_max([5, 2, 8, 1, 9])
print(result)  # (1, 9)

# Return vs print
# Understanding the differences is crucial


def get_greeting_print(name):
    print(f"Hello, {name}!")  # Just displays


def get_greeting_return(name):
    return f"Hello {name}!"  # Gives back value


# can't use print version's output
message = get_greeting_print("Alice")  # Prints but returns None
print(message)

# Can use return version's output
message = get_greeting_return("Alice")  # Returns the string
print(message.upper())  # HELLO, ALICE!

"""Use return when you need to use the result elsewhere.
Use print when you jsut want to display information."""


# Functions without return
# Functions without return explicit return statements return None:
def greet(name):
    print(f"Hello, {name}")
    # No return statement


result = greet("Alice")  # Hello, Alice!
print(result)  # None
