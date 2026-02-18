"""Loops
Repeat code multiple times

​
What are loops?
Loops let you repeat code without writing it multiple times. Instead of copying and pasting, you tell Python to repeat the code for you.
"""

# Without loops:
print("Hello!")
print("Hello!")
print("Hello!")
print("Hello!")
print("Hello!")

# With loops
for i in range(5):
    print("Hello!")

# For loops, the for loop is the most common loop in python
# Print numbers 0 thorough 4
for i in range(5):
    print(i)

# Output:
# 0
# 1
# 2
# 3
# 4

"""Python starts counting at 0, not 1.
This is called “zero-indexing”. So range(5) gives you 0, 1, 2, 3, 4 (five numbers total)."""

# Count from different starting points
# Count from 1 to 5
for i in range(1, 6):
    print(i)
# Output: 1, 2, 3, 4, 5

# Count by 2s
for i in range(0, 10, 2):
    print(i)
# Output: 0, 2, 4, 6, 8

# Loop through text, you can loop through each character
name = "Python"
for letter in name:
    print(letter)

# Loop thorugh a list (preview)
colors = ["red", "blue", "yellow", "green"]
for color in colors:
    print(f"I like {color}")

# While loops, it continues to loop as long as a condition is true
count = 0
while count < 5:
    print(f"Count is {count}")
    count = count + 1  # Increase after each count by 1

# Output:
# Count is 0
# Count is 1
# Count is 2
# Count is 3
# Count is 4

"""ALWAYS MAKE SURE YOUR WHILE LOOP WILL STOP, OTHERWISE WILL RUN FOREVER"""
