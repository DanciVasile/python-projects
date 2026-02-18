age = 27
print(age == 18)
print(age != 18)
print(age > 17)
print(age < 20)
print(age >= 18)
print(age <= 27)


has_license = False

# AND - both must be true
can_drive = age >= 18 and has_license
print(f"Can drive: {can_drive}")  # False

# OR - at least one must be true
day = "Saturday"
is_weekend = day == "Saturday" or day == "Sunday"
print(f"Is weekend: {is_weekend}")  # True

# NOT - reverse the value
is_adult = age >= 18
is_child = not is_adult
print(f"Is child: {is_child}")  # False

# TRUTH TABLES
# AND: Both must be true
print(True and False)  # Output: False
print(True and True)  # Output: True
print(False and False)  # Output: False

# Or: At least one must be true
print(True and False)  # Output: False
print(False and False)  # Output: False

# NOT: Flips the value
print(not True)  # Output: False
print(not False)  # Output: True

# ASSIGNMENT SHORTCUTS
# Instead of:
score = 0
score = score + 10
# write
score = 0
score += 10
print(score)
# Works with operators
x = 10
x += 5
x *= 2
print(x)

# COMMON MSITAKES

# Division always returns float
# Regular division
result = 10 / 2  # Output: 5.0 (float) not 5
print(result)
# Integer division
result = 10 // 2  # Output: 5 (integer)
print(result)

# Order of operations
# Wrong
average = 10 + 20 + 30 / 3  # Output: 40.0 (not 20)
print(average)
# Right
average = (10 + 20 + 30) / 3  # output: 20.0
print(average)

# CONFUSING = AND ==
# = assigns a value
x = 5
# == compares values
is_equal = x == 5  # Output: True
print(is_equal)


# Indentation
# Wrong
if age >= 18:
    print("You are an adult")
else:
    print("You are not an adult")
# Right
if age >= 18:
    print("You are an adult")
else:
    print("You are not an adult")

# Spacing - use spaces around operators and after commas
# Good
x = 1 + 2
numbers = [1, 2, 3, 4]

# Bad
x = 1 + 2
numbers = [1, 2, 3]


# Blank lines = use blank linese to separate functions and logical sections
def first_function():
    pass


def second_functionn():
    pass


# Line length = keep lines under 80-100 characters. Break long lines for readability:
long_string = (
    "This is a very long string that " + "spans multiple lines for readability."
)

print(long_string)
