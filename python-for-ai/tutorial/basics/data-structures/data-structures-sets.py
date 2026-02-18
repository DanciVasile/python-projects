"""Sets
Work with unique collections

​
What are sets?
Sets are collections that only store unique values. They automatically remove duplicates.
Think of sets like:
A bag of unique marbles
Guest list (each person once)
Unique tags or categories
​
Creating sets
You can create sets two ways: with set() or with curly braces {} (but only when it has values).
"""

# Empty set (careful!)
empty_set = set()  # NOT {} - that's a dict

# Set with values - both ways work
numbers = {1, 2, 3, 4, 5}
fruits = set(["apple", "banana", "orange"])

# From a list (removes duplicates)
scores = [85, 90, 85, 92, 90]
unique_scores = set(scores)  # {85, 90, 92}
print(unique_scores)
"""Use set() for empty sets, not {}. Empty curly braces create a dictionary"""

# Basic operations
colors = {"red", "blue"}

# Add items
colors.add("green")
print(colors)  # {'green', 'blue', 'red'}

# Remove items
colors.remove("blue")  # Error if not found
colors.discard("yellow")  # No error if not found

# Check membership
if "red" in colors:
    print("Red is available!")

# Common uses
# Remove duplicates
names = ["Alice", "Bob", "Alice", "Charlie", "Bob"]
unique_names = list(set(names))
print(unique_names)
print(names)

# Fast membership testing
allowed_users = {"Alice", "Bob", "Charlie"}
if "Alice" in allowed_users:  # Very fast!
    print("Access granted")

# Common mistakes
# Wrong - create empty dict
empty = {}

# Right - use set()
empty = set()

# Sets are unordered
# Order is not a guaranteed!
numbers = {3, 1, 4, 1, 5}
print(numbers)

# Use list if order matters
ordered = [3, 1, 4, 1, 5]
print(ordered)

s = {10, 3, 7, 2, 99, 1}
print(s)

"""
🔹 Use sets when you care about uniqueness
🔹 Use lists when you care about order
"""
