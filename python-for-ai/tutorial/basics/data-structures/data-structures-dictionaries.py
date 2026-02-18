"""Dictionaries
Store data with key-value pairs

​
What are dictionaries?
Dictionaries store data in key-value pairs. Think of them like a real dictionary where you look up a word (key) to find its definition (value).
Real-world examples:
Phone book: name > phone number
Menu: dish > price
User profile: username > user info"""

# CREATING DICTIONARIES
# Empty dictionary
my_dict = {}

# Dictionary with data
person = {"name": "Alice", "age": 30, "city": "New York"}

# Different ways to create
scores = dict(math=95, english=87, science=92)

# Accesign values
person = {"name": "Alice", "age": 30, "city": "New York"}
# Get values by key
print(person["name"])  # "Alice"
print(person["age"])  # 30

# Safer with get()
print(person.get("job"))  # None (no error)
print(person.get("job", "Unknown"))  # Unknown (default)

# Changing dictionaries
person = {"name": "Mark", "age": 30}

# Add or update
person["email"] = "mark@gmail.com"  # Add new
person["age"] = 31  # Update existing
print(person)

# Remove items
del person["email"]  # Remove by key
age = person.pop("age")  # Remove and return
person.clear()  # remove all items

# Dictionary methods
person = {"name": "Alice", "age": 30, "city": "New York"}

# Get all keys, values, or items
print(person.keys())  # dict_keys(['name', 'age', 'city'])
print(person.values())  # dict_values(['Alice', 30, 'New York'])
print(
    person.items()
)  # dict_items([('name', 'Alice'), ('age', 30), ('city', 'New York')])

# Check if key exists
if "name" in person:
    print("Name found!")

# Update multiple values
person.update({"age": 31, "job": "Engineer"})

# Nested dictionaries
# Dictionary of dictionaries
students = {
    "Alice": {"age": 31, "grade": "A"},
    "Bob": {"age": 27, "grade": "F"},
    "Mark": {"age": 30, "grade": "D"},
    "James": {"age": 29, "grade": "C"},
}

# Access nested data
print(students["Alice"]["grade"])  # A

# Using mutable keys
# Wrong - lists can't be keys
bad_dict = {[1, 2]: "value"}  # TypeError!

# Rigth - use immutable types
good_dict = {(1, 2): "value"}  # Tuple is OK
good_dict = {"1, 2": "value"}  # String  is OK

print(bad_dict)
print(good_dict)
