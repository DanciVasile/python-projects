"""Tuples
Work with immutable sequences

​
What are tuples?
Tuples are like lists, but they can’t be changed once created. They’re immutable (unchangeable) sequences.
Use tuples for data that shouldn’t change:
Coordinates (x, y)
RGB colors (255, 0, 0)
Database records
Function return values"""

# Creating tuples
# Empty tuple
empty = ()

# Tuple with items
point = (3, 5)
colors = ("red", "green", "blue")

# Single item tuple needs comma!
single = (42,)  # Note the comma
not_tuple = 42  # This is just 42 in parentheses

# Without parentheses
coordinates = 10, 20

""" A single item tuple needs a comma: (42,) not (42). Without the
comma, Python thinks it's just parentheses around a number"""

# Accesing items
# Just like lists, tuples use indexing:
points = (3, 5)
colors = ("red", "green", "blue")

# Get items
print(points[0])  # 3
print(colors[-1])  # blue

# Tuple unpacking
# Python coolest tuple feature
# Unpack values
point = (3, 5)
x, y = point  # x = 3, y = 5
print(point)
print(x, y)

# Mutliple assignment
a, b, c = 1, 2, 3  # Same as (1, 2, 3)
print(a, b, c)

# Swap variables elegantly
x = 20
y = 4
x, y = y, x  # Swaps values!
print(x, y)

# Mistakes in trying to modify tuples
# Wrong - tuples are immutable
point = (4, 5)
point[0] = 4  # TypeError!

# Right - create a new tuple
point = (4, point[1])
print(point)
# Or convert to list, modify, convert back
temp = list(point)
temp[0] = 2
point = tuple(temp)
