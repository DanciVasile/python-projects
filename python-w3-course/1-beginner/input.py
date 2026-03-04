# The input() function is Python's built-in way to get information from users.
# It pauses your program,
# waits for the user to type something, and returns what they typed.

name = input("What is your name?")
print("You typed: " + name)
print("Hello")

# Goldn rule: input() always returns a string
age = input("What is your age?")
print(type(age))  # This will show <class 'str'>, meaning it's a string

# Why does this matter?
# ✅ Example 1: Math won't work
age = input("What is your age?")
next_year_age = (
    age + 1
)  # ❌ This will cause an error because you can't add an integer to a string
print(next_year_age)


# ✅ Example 2: Comparisons behave unexpectedly
num = input("Enter a number:")
if num > 10:  # String comparison, not numeric
    print("Greater than 10")
else:
    print(
        "Not greater than 10"
    )  # ❌ TypeError: '>' not supported between instances of 'str' and 'int'

# ✅ Example 3:  String concatenation instead of math
x = input("First number:")  # 5
y = input("Second number:")  # 3
print(x + y)  # Prints "53" not 8!

""" Coverting input types"""

# Method 1: convert after input
age_str = input("Enter your age:")
age = int(age_str)

# Method 2: convert immediately (more common)
age = int(input("Enter your age:"))

# Now you can do math
next_year_age = age + 1
print(f"Next year you will be {next_year_age}.")


""" Coonverting to float """
# Python doesn't have a bool() converter that works intuitively
# You need to implement your own logic

response = input("Do you agree? (yes/no): ")
agrees = response.lower() == "yes"  # True or False

# Or more sophisticated
response = input("Continue? (yes/no): ").lower()
if response.lower() in ["yes", "y", "true", "1"]:
    continues = True
else:
    continues = False

print(continues)

""" VALIDATION INPUT"""
while True:
    try:
        age = int(input("Enter your age: "))
        break  # Exit the loop if conversion is successful
    except ValueError:
        print("Invalid input. Please enter a number.")

print(f"Your age is {age}.")


""" Validation with conditions"""
# Validate range
while True:
    try:
        age = int(input("Enter your age (0-120): "))
        if 0 <= age <= 120:
            print(f"Your age is {age}.")
            break
        else:
            print("Age must be between 0 and 120.")
    except ValueError:
        print("Invalid input. Please enter a number.")


""" Advanced validation example """


def get_positive_integer(prompt):
    """Get a positive integer from the user with validation."""
    while True:
        try:
            value = int(input(prompt))
            if value > 0:
                return value
            else:
                print("Please enter a positive number!")
        except ValueError:
            print("Please enter a valid integer!")


# Usage
quantity = get_positive_integer("How many items?")
print(f"You entered: {quantity}")

""" Validating String input """
# Example: Only accept yes/no
while True:
    answer = input("Do you want to continue? (yes/no): ").lower()
    if answer in ["yes", "no"]:
        print(f"You answered: {answer}")
        break
    else:
        print("Please answer 'yes' or 'no'.")

# Example: non-empty String
while True:
    name = input("Enter your name: ").strip()
    if name:  # Check if String is not empty
        print(f"Hello, {name}!")
        break
    else:
        print("Name cannot be empty. Please try again.")


""" Validation pattern template """


def get_validated_input(prompt, validation_func, error_message):
    """Generic validation pattern."""
    while True:
        user_input = input(prompt)
        if validation_func(user_input):
            return user_input
        else:
            print(error_message)


# Usage example
def is_valid_email(email):
    return "@" in email and "." in email


email = get_validated_input(
    "Enter your email: :", is_valid_email, "Please enter a valid email address."
)
print(f"Your email is: {email}")

# ❌❌❌ Common mistakes:
# ❌ multiple inputs on a single line doesn't work.
x, y = input(
    "Enter two numbers: "
)  # This will not work as expected, it will treat the entire input as a single string
print(x, y)

# ✅ CORRECT WAY method 1: separate inputs
x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
print(x, y)

# ✅ CORRECT WAY method 2: Split a single input
values = input(
    "Enter two numbers separated by a space: "
).split()  # This will split the input into a list of strings
x = int(values[0])
y = int(values[1])
print(x, y)

# ✅ CORRECT WAY method 3: More elegant split and convert
x, y = map(
    int, input("Enter two numbers separated by a space: ").split()
)  # This will split the input and convert each part to an integer
print(x, y)


# ❌ MISTAKE: not stripping the whitespace
name = input("Enter your name: ")  # User types " John " with extra spaces
if name == "John":  # False! name is " John " not "John"
    print("Hello, Jonh!")

# ✅ CORRECT WAY: strip any whitespace
name = input("Enter your name: ").strip()  # User types " John " with extra spaces
if name == "John":  # True! name is "John" after stripping
    print("Hello, John!")

    """ Infintite loops without exit """
while True:
    age = int(input("Age: "))  # Crashes on invalid input
    if age > 0:
        break

# ✅ CORRECT WAY: graceful error handling
attempts = 0
max_attempts = 3
while attempts < max_attempts:
    try:
        age = int(input("Age: "))
        if age > 0:
            print(f"Your age is {age}.")
            break
        else:
            print("Age must be positive.")
    except ValueError:
        print("Please enter a valid number.")
    attempts += 1
else:
    print("Too many invalid attempts. Exiting.")
    age = None  # or handle as needed


### Exercise 1: Age Calculator

# Write a program that:

# - Asks for the user's birth year
# - Calculates their age in 2024
# - Validates the input


def get_birth_year():
    while True:
        try:
            birth_year = int(input("Enter your birth year:"))
            if 1900 <= birth_year <= 2024:
                age = 2024 - birth_year
                print(f"You are {age} years old in 2024.")
                break
            else:
                print("Please enter a birth year between 1900 and 2024.")
        except ValueError:
            print("Invalid input. Please enter a valid year.")


get_birth_year()


### Exercise 2: Age Calculator

### Exercise 2: Temperature Converter

# Create a program that:

# - Asks if user wants to convert from C to F or F to C
# - Gets the temperature
# - Performs the conversion
# - Validates all inputs


def convert_temperature():
    while True:
        choice = input(
            "Convert from (C)elsius to Fahrenheit or (F)ahrenheit to Celsius? (C/F):"
        ).upper()
        if choice in ["C", "F"]:
            break
        print("Please enter 'C' or 'F'.")

    while True:
        try:
            temp = float(input("Enter the temperature to convert: "))
            break
        except ValueError:
            print("Please enter a valid number.")

    if choice == "C":
        result = (temp * 9 / 5) + 32
        print(f"{temp} degrees Celsius is {result} degrees Fahrenheit.")
    else:
        result = (temp - 32) * 5 / 9
        print(f"{temp} degrees Fahrenheit is {result} degrees Celsius.")


convert_temperature()


### Exercise 3: Simple Calculator

# Build a calculator that:

# - Gets two numbers from the user
# - Asks what operation to perform (+, -, *, /)
# - Performs the calculation
# - Handles division by zero


def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number.")


num1 = get_number("Enter the first number: ")
num2 = get_number("Enter the second number: ")

while True:
    operation = input("Choose an operation (+, -, *, /): ")
    if operation in ["+", "-", "*", "/"]:
        break
    print("Invalid operation.")

if operation == "+":
    result = num1 + num2
elif operation == "-":
    result = num1 - num2
elif operation == "*":
    result = num1 * num2
elif operation == "/":
    result = num1 / num2 if num2 != 0 else "Error: Division by zero is not allowed."

print(f"{num1} {operation} {num2} = {result}")
