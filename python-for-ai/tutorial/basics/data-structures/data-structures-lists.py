"""Data structures
Store multiple values together

​
Beyond single values
So far, you’ve stored one value per variable. But what if you need to store multiple values? That’s where data structures come in.
Think of data structures as containers:
Lists: Like a shopping list (ordered items)
Dictionaries: Like a phone book (name > number)
Tuples: Like coordinates (fixed values)
Sets: Like a bag of unique items"""

# LISTS
# Work with ordered collections

# What are lists?
# Lists are Python’s most versatile data structure. They’re like containers that can hold multiple items in a specific order.
# Think of a list like:
# A shopping list (milk, eggs, bread)
# A to-do list (tasks in order)
# A playlist (songs in sequence)

# Creating lists
# Emtpy list
my_list = []

# List with items
fruits = ["apple", "banana", "orange"]
numbers = [1, 2, 3, 4, 5]
mixed = ["hello", 2, True, 3.14]

# Accesing items
# Lists are mutable, you can change items

fruits = ["apple", "banana", "orange"]
# Change an item
fruits[0] = "mango"
print(fruits)  # ["mango", "banana", "orange"]

# Add item
fruits.append("grape")  # Add to end
fruits.insert(1, "kiwi")  # Insert in a position

# Remove items
fruits.remove("banana")
last = fruits.pop()
del fruits[0]

# list methods
numbers = [3, 1, 4, 1, 5, 9]

# Information
print(len(numbers))  # 6 (length)
print(numbers.count(1))  # 2 (count occurences)
print(numbers.index(4))  # 2 (find position)

# Sorting
numbers.sort()  # sort in place
print(numbers)  # [1, 1, 3, 4, 5, 9]

# Copy
new_list = numbers.copy()  # Create a copy
print(new_list)

# Checking lists
fruits = ["apple", "banana", "orange"]

# Check if item exists
if "apple" in fruits:
    print("Found an apple!")

# Check if list is empty
if fruits:
    print("List has items")
else:
    print("List is empty")

# Modify whiel looping
numbers = [1, 2, 3, 4]
numbers = [num for num in numbers if num != 2]
print(numbers)

# Copy a list the right way
# WRONG WAY
list1 = [1, 2, 3]
list2 = list1
list2.append(4)
print(list1)

# CORRECT WAY
list1 = [1, 2, 3]
list2 = list1.copy()
list2.append(4)
print(list1)  # [1, 2, 3] - unchanged
