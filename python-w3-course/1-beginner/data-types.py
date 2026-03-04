"""
In Python, there are 5 main categories of data types:
- Numeric types: Integer, Float, Complex
- Sequence types: List, Tuple, String
- Dictionary
- Boolean
- Set
"""

# =================================== #
""" Numeric types """
# =================================== #

""" Integer """
# Can be positive, negative or zero.
x = 10
x = 45
x = -5
x = 0


""" Float """
# Numbers with decimal points.
# Careful with floats, they can have precision issues.
y = 3.14
z = 0.1 + 0.2  # This will not equal 0.3 due to precision issues.
print(z)  # Output: 0.30000000000000004

# Always better to use the decimal module for precise decimal arithmetic.
from decimal import Decimal

a = Decimal("0.2")
b = Decimal("0.1")
c = a + b
print(c)  # Output: 0.3


""" Complex """
# Complex numbers have a real part and an imaginary part.
d = 2 + 3j
e = complex(2, 3)  # This is another way to create a complex number.
print(d)  # Output: (2+3j)
print(e)  # Output: (2+3j)


""" Dictionary """
# Dictionaries are collections of key-value pairs.
# Keys must be unique and immutable
# They work like real dictionary where you look up a word
# to find its meaning, in a Python dictionary you look up a jey to find its
# value.
my_dict = {"name": "Alice", "age": 44, "city": "New York"}

print(my_dict)
print(my_dict["age"])  # Output: 44
print(my_dict.get("name"))  # Output: Alice


""" Boolean """
# Boolean values can be either True or False.
is_raining = True
is_sunny = False
print(is_raining)  # Output: True
print(is_sunny)  # Output: False

""" Set """
# An unordered collection of unique items.
my_set = {1, 2, 3, 4, 5}  # Declared wiht curly braces like a dictionary
print(my_set)  # Output: {1, 2, 3, 4, 5}
# The special thing about sets is that they automatically remove duplicates.
my_set.add(3)  # Adding a duplicate value will not change the set.
print(my_set)  # Output: {1, 2, 3, 4, 5}

# =================================== #
""" Sequence types """
# =================================== #

""" List """
# A list is an ordered collection of items that can be of different types."""
my_list = [1, "hello", 3.14, True]  # Declared with square brackets.
print(my_list)  # Output: [1, 'hello', 3.14, True]

""" Tuple """
# A tuplr is similar to a list but it is immutable, meaning you cannot
# change its contents after it is created."""
my_tuple = (1, "hello", 3.14, True)  # Declared with parentheses.
print(my_tuple)  # Output: (1, 'hello', 3.14, True)

""" String """
# A string is a sequence of characters enclosed in quotes.
my_string = "Hello, World!"  # Can be declared with single or double quotes.
print(my_string)  # Output: Hello, World!

# -------------------------------------------------------------------------------
# | Data Type  | Example            | Mutable? | Ordered? | Use Case              |
# -------------------------------------------------------------------------------
# | Integer    | 42                 | No       | N/A      | Whole numbers         |
# | Float      | 3.14               | No       | N/A      | Decimal numbers       |
# | Complex    | 2+3j               | No       | N/A      | Complex numbers       |
# | Dictionary | {"key": "value"}   | Yes      | Yes*     | Key-value pairs       |
# | Boolean    | True, False        | No       | N/A      | True/False logic      |
# | Set        | {1, 2, 3}          | Yes      | No       | Unique items          |
# | String     | "hello"            | No       | Yes      | Text                  |
# | List       | [1, 2, 3]          | Yes      | Yes      | Changeable collection |
# | Tuple      | (1, 2, 3)          | No       | Yes      | Fixed collection      |
# -------------------------------------------------------------------------------
#
# * Dictionaries preserve insertion order in Python 3.7+


""" Checking data types """
print(type(x))  # Output: <class 'int'>
print(type(y))  # Output: <class 'float'>
print(type(d))  # Output: <class 'complex'>
print(type(my_dict))  # Output: <class 'dict'>
print(type(is_raining))  # Output: <class 'bool'>
print(type(my_set))  # Output: <class 'set'>
print(type(my_list))  # Output: <class 'list'>
print(type(my_tuple))  # Output: <class 'tuple'>
print(type(my_string))  # Output: <class 'str'>


""" Type conversion"""
# String to Integer
age = int("30")
print(age)  # Output: 30

# Integer to String
age_str = str(40)
print(age_str)  # Output: '40'

# String to Float
pi = float("3.14")
print(pi)  # Output: 3.14

# Float to Integer
pi_int = int(pi)
print(pi_int)  # Output: 3 (Note: this truncates the decimal part)

# Integer to Float
age_float = float(age)
print(age_float)  # Output: 30.0

# List to  Tuple
my_list = [1, 2, 3]
my_tuple = tuple(my_list)
print(my_tuple)  # Output: (1, 2, 3)

# List to Set
numbers = [1, 2, 3, 4, 5]
unique = set(numbers)
print(unique)  # Output: {1, 2, 3, 4, 5}

"""
Summary

Python data types are the building blocks of every program:

- **Numeric types** (`int`, `float`, `complex`) for numbers
- **Dictionary** (`dict`) for key-value pairs and fast lookups
- **Boolean** (`bool`) for True/False logic
- **Set** (`set`) for unique collections
- **Sequence types**:
    - **String** (`str`) for text
    - **List** (`list`) for changeable ordered collections
    - **Tuple** (`tuple`) for fixed ordered collections

Choose the right data type based on what you need to store and how you need to use it!"""
