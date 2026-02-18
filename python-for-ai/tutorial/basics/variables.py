"""Variables
Learn to store and name your data

​
What are variables?
A variable is like a labeled box where you can store information. You give it a name and put a value inside. Later, you can use that name to get the value back.
In real life:
Your name is a “variable” that stores what people call you
Your age is a “variable” that stores a number
Your favorite color is a “variable” that stores text
In Python, we create variables to store data our programs need to remember."""

# Simple variables
name = "Alice"  # must be in quotes because it's a string
age = 30  # numbers don't need quotes
is_student = True  # booleans are True or False, always capitalized

# Naming rules
user_name = "Bob"  # lowercase with underscore (Python style)
userName = "Charlie"  # camelCase (works but not Python style)
age2 = 30  # numbers are allowed but not at the start of the name
_private = "secret"  # underscore at start is OK

# NOT ALLOWED
# 2age = 25             # can't start with a number
# my-name = "Dave"      # No hyphens (Python thinks it's subtraction)
# my name = "Dave"      # No spaces
# class = "Python"        # Can't use Python keywords

"""Python naming convention
In Python, we use lowercase letters with underscores between words. This is called “snake_case” 
and it’s the standard way to name variables in Python.  
"""
# Good Python style
first_name = "Alice"
user_age = 25
is_logged_in = True
shopping_cart_total = 49.99

# Avoid camelCase (This is for other languages)
firstName = "Bob"
userAge = 30
isLoggedIn = False

"""Changing variables
Variables can change (that’s why they’re called variables!):"""

# Start with one value
score = 0
print(score)  # Shows: 0

# Change it
score = 10
print(score)  # Shows: 10

# Change it again
score = 20
print(score)  # Shows: 20
