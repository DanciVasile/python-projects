# ## 1. Arithmetic Operators

# Arithmetic operators perform mathematical calculations.

# **Available operators:**

# - `+` Addition
# - Subtraction
# - Multiplication
# - `/` Division (always returns float)
# - `//` Floor Division (returns integer)
# - `%` Modulus (returns remainder)
# - `*` Exponentiation (power)

# Real world example
# Calculate the price with tax
price = 99.99
tax_rate = 0.08
total = price + (price * tax_rate)
print(f"Total: ${total:.2f}")


# Split items evenly among people:
total_items = 25
people = 4
items_per_person = total_items // people
leftover = total_items % people
print(f"Each person gets {items_per_person} items, {leftover} leftover")

# Calculate compound interest:
principal = 1000
rate = 0.05
years = 10
amount = principal * (1 + rate) ** years
print(f"Amount: ${amount:.2f}")

# **When to use:**

# - `/` when you need precise decimal results (prices, measurements)
# - `//` when you need whole numbers (splitting items, pagination)
# - `%` for remainders (checking even/odd, wrapping arrays, cycling through options)
# - `*` for powers and roots (compound interest, area calculations)

## 2. Comparison Operators

# Comparison operators compare two values and return True or False.

# **Available operators:**

# - `==` Equal to
# - `!=` Not equal to
# - `<` Less than
# - `>` Greater than
# - `<=` Less than or equal to
# - `>=` Greater than or equal to

# Age verification for voting
age = 19
can_vote = age > 18
print(f"Can vote: {can_vote}")

# Password strength checker:
password = "SecurePass123"
is_long_enough = len(password) >= 8
is_too_short = len(password) < 6
has_minimum_chars = len(password) >= 8

if has_minimum_chars:
    print("Password meets minimum requirements")

# Validate user input:
user_answer = input("Continue? (yes/no): ")

if user_answer.lower() == "yes":
    print("Proceeding...")

elif user_answer != "no":
    print("Invalid input")
else:
    print("You typed no.")


# Grade calculator
score = 85

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
else:
    grade = "F"


print(f"Grade: {grade}")

## 3. Assignment Operators

# Assignment operators assign values to variables. Compound operators combine an operation with assignment.

# **Available operators:**

#  `=` Assign value
#  `+=` Add and assign (x += 3 means x = x + 3)
#  `-=` Subtract and assign
#  `*=` Multiply and assign
#  `/=` Divide and assign
#  `//=` Floor divide and assign
#  `%=` Modulus and assign
#  `**=` Exponent and assign

# Shopping cart total:
cart_total = 0
cart_total += 29.99
cart_total += 15.50
cart_total += 42.00
print(f"Total: ${cart_total}")

# Game score with multiplier:
score = 100
score *= 2  # Double the score for power-up
score += 50  # Bonus points
print(f"Score: {score}")

# Health managent in game:
health = 100
health -= 25  # Take damage
health -= 15  # More damage

if health <= 0:
    print("Game Over")
else:
    print(f"Health remainig: {health}")


# Invetory counter:
inventory = 50
inventory -= 5
inventory += 20
inventory //= 2  # Split inventory in half
print(f"Inventory remaining: {inventory}")


""" 4. Logical Operators """

# Logical operators combine conditional statements and return Boolean values.

# - `and` Returns True only if both conditions are True
# - `or` Returns True if at least one condition is True
# - `not` Reverses the boolean value


# User authentification
username = "admin"
password = "secret123"
is_admin = username == "admin"
correct_password = password == "secret123"

if is_admin and correct_password:
    print("Access granted")
else:
    print("Access denied")


# Loan eligibility checker:
age = 25
credit_score = 720
income = 50000

# Elligible if: (over 21 AND good credit score) OR high income
eligible = (age >= 21 and credit_score >= 650) or income >= 60000
print(f"Loan eligible: {eligible}")


# Weekend or holiday check:
is_weekend = True
is_holiday = False
is_working_day = not (is_weekend or is_holiday)
print(f"Working day: {is_working_day}")


# Form validation
email = "user@example.com"
password = "pass123"
terms_accepted = True

# All conditions must be met
valid_form = len(email) > 0 and len(password) >= 8 and terms_accepted

if valid_form:
    print("Form submitted successfully!")
else:
    print("Form error detected")


""" 5. Membership Operators """

# Membership operators test whether a value exists in a sequence (strings, lists, tuples, sets, dictionaries).

# **Available operators:**

# - `in` Returns True if value is found in sequence
# - `not in` Returns True if value is NOT found in sequence

email = "user@email.com"
has_at = "@" in email
has_dot = "." in email
valid_email = has_at and has_dot
print(f"Valid email: {valid_email}")


# Check user permissions:
user_permissions = ["read", "write", "delete"]
can_delete = "delete" in user_permissions
can_write = "write" in user_permissions
can_delete = "delete" in user_permissions
can_execute = can_write and can_delete
if can_delete:
    print("User can delete files")
if not can_execute:
    print("User cannot execute files.")


# Product availability:
available_sizes = ["S", "M", "L", "XL"]
requested_size = "M"

if requested_size in available_sizes:
    print(f"Size {requested_size} is available.")
else:
    print("Sorry, size not available")


# Search for substring:
message = "Hello, welcome to Python programming"

if "Python" in message:
    print("This message is about Python")

if "Java" not in message:
    print("This message does not metion Java")

# Filtering vulgare words:
banned_words = [
    "fuck",
    "pussy",
    "asshole",
]
user_comment = "This is a great product"
contains_banned = any(word in user_comment.lower() for word in banned_words)
if not contains_banned:
    print("Comment approved.")

""" 6. Identity Operators """

# Identity operators check whether two variables refer to the same object in memory (not just equal values).

# **Available operators:**

# - `is` Returns True if both variables point to the same object
# - `is not` Returns True if variables point to different objects

# Checking for None(most common use)
user_input = None

if user_input is None:
    print("No input provided.")

# ALWAYS use 'is None', not '== None'
# This is the Pythonic way

# Understanding object identity vs equality
# Two lists with the same values but different objects
list1 = [1, 2, 3]
list2 = [1, 2, 3]
list3 = list1  # list3 points to the same object as list1

print(list1 == list2)  # True (same values)
print(list1 is list2)  # False (different objects in memory)
print(list1 is list3)  # True (same object)

# Modifying list1 also affects list3
list1.append(4)
print(list3)

# Checking boolean singletons:
success = True
# You CAN do this:
if success is True:
    print("Operation succeeded")

# But this is more Pythonic:
# Simulate operation success
success = True
if success:
    print("Operation succeeded.")

# In-memory "users" data
users = [
    {"id": 1, "name": "Alice"},
    {"id": 2, "name": "Bob"},
    {"id": 3, "name": "Charlie"},
]

# Simulate a "query" for user with id 5
user_id_to_find = 5
result = next((user for user in users if user["id"] == user_id_to_find), None)

if result is not None:
    print("User found:", result)
else:
    print("User not found.")


"""
**When to use:**

- ALWAYS use `is` when checking for None
- Use `is` for True/False singletons (though `if variable:` is more Pythonic)
- Use `is` when you need to check if two variables reference the exact same object
- DON'T use `is` to compare numbers or strings (use `==` instead)

**Important:** Small integers (-5 to 256) and some strings are cached by Python,
which can make `is` appear to work, but this is unreliable. 
Always use `==` for value comparison. """


# ================================================
""" When to Use What: Quick Decision Guide """
# ================================================

### Use Arithmetic Operators When:

# - Performing calculations (prices, measurements, statistics)
# - Working with counters and accumulators
# - Distributing items evenly (// and %)
# - Computing powers or square roots (**)
# - Building formulas

# ### Use Comparison Operators When:

# - Making decisions in if/elif/else statements
# - Validating input against requirements
# - Sorting or filtering data
# - Checking ranges (age limits, price ranges)
# - Building loop conditions

# ### Use Assignment Operators When:

# - Initializing variables (=)
# - Updating values (+=, -=, *=, etc.)
# - Accumulating totals in loops
# - Applying multipliers to values
# - Makes code cleaner than `x = x + 3`

# ### Use Logical Operators When:

# - Combining multiple conditions
# - Building complex validation rules
# - Implementing business logic
# - Creating filters
# - Short-circuit evaluation needed

# ### Use Membership Operators When:

# - Checking if item exists in collection
# - Validating against allowed values
# - Searching for substrings
# - Implementing permissions/features
# - Working with sets and lists

# ### Use Identity Operators When:

# - Checking for None (always!)
# - Verifying object identity
# - Checking if variables point to same object
# - Performance-critical comparisons (is is faster than ==)

# ================================================
""" Best Practices """
# ================================================

### General

# - Use meaningful variable names to make operator usage clear
# - Add comments for complex operator combinations
# - Break down complex expressions into multiple lines

# ### Arithmetic

# - Always validate divisors before dividing to avoid division by zero
# - Use // when you need integer results, not int(x / y)
# - Remember operator precedence: ** then *, /, //, % then +, -

# ### Comparison

# - Use == for value comparison, not = (assignment)
# - Chain comparisons for readability: `if 0 < x < 100:` instead of `if x > 0 and x < 100:`
# - Be careful comparing floats due to precision issues

# ### Logical

# - Take advantage of short-circuit evaluation by putting simpler conditions first
# - Don't write `if x == True:`, just write `if x:`
# - Don't write `if x == False:`, write `if not x:`

# ### Assignment

# - Use compound operators (+=, -=) instead of `x = x + 3` for clarity
# - Initialize before using compound assignment
# - Be aware that += creates new strings/tuples but modifies lists in place

# ### Identity

# - ALWAYS use `is None` to check for None, never `== None`
# - Don't use `is` to compare numbers or strings
# - Remember: is checks identity, == checks equality


""" Common pitfalls """
# WRONG (can fail due to floating point precision)
if 0.1 + 0.2 == 0.3:  # False!
    pass
# CORRECT
if abs((0.1 + 0.2) - 0.3) < 0.0001:
    pass

# Using is for numbers/strings
# WRONG
x = ""
if x is 1000:  # Unreliable
    pass
# CORRECT
if x == 1000:
    pass

## Summary

# Python operators are essential tools that make your code expressive and powerful.
# By understanding when and how to use each operator type, you can write cleaner,
# more efficient programs.

# **Remember:**

# - **Arithmetic operators** handle all your mathematical needs
# - **Comparison operators** enable smart decision-making
# - **Assignment operators** efficiently update values
# - **Logical operators** combine conditions elegantly
# - **Membership operators** check for presence in collections
# - **Identity operators** verify object identity

# Practice using these operators in real projects, and you'll quickly develop intuition
# for choosing the right tool for each task. Happy coding!
