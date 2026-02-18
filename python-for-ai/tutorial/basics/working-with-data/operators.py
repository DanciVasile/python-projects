"""Operators
Math, comparisons, and logic in Python

​
What are operators?
Operators are symbols that perform operations on values. Think of them as the “verbs” of programming - they make things happen!
You already know most operators from math class:
Calculate: +, -, *, /
Compare: >, <, ==
Combine: and, or, not"""

# Arithmetic operators
# Basic math

print(10 + 3)  # Addition
print(10 - 3)  # Substraction
print(10 * 3)  # Multiplication
print(10 / 3)  # Division, always gives float 3.3333

# Special operators
print(10 // 3)  # Floor division (rounds down)
print(10 % 3)  # Modulo (remainder) 1
print(10**3)  # Exponent (power) 1000

# Order of operations
# Python follows math rules (PEMDAS):
result = 2 + 3 * 4  # 14 (not 20!)
result = (2 + 3) * 4  # 20 (parentheses first)

# Comparison oeprators
age = 18

print(age == 18)  # True  - Equal to
print(age != 21)  # True  - Not equal to
print(age > 17)  # True  - Greater than
print(age < 20)  # True  - Less than
print(age >= 18)  # True  - Greather than or equal
print(age <= 18)  # True  - Less than or equal

# Don't confuse = (assignment) with == (comparison)!
# age = 18  stores 18 in age
# age == 18 checks if age equals 18

# Logical operators
# These combine boolean values and conditions

age = 25
has_license = True

# AND - both must be True
can_drive = age >= 16 and has_license
print(can_drive)  # True
# OR - at least one must be true
day = "Saturday"
is_weekend = day == "Saturday" or day == "Sunday"
print(is_weekend)  # True

# NOT - reverse the value
is_adult = age >= 18
is_child = not is_adult
print(is_child)  # False

# Truth tables
# Understanding how 'and', 'or', and 'not' works

# AND: Both must be true
print(True and True)  # True
print(True and False)  # False
print(False and False)  # True

# OR - At least one must be True
print(True and False)  # True
print(False and False)  # False

# NOT - Flips the value
print(not True)  # False
print(not False)  # True

# Assignment shortcuts
# These shortcuts updates variables in place:
# Instead of:
"""score = score + 10"""

# Write:
score = 0
score += 10

# Works with all the operators
x = 10
x += 10
x *= 2
print("number is ", x)
