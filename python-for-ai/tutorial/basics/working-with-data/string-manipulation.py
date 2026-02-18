# STRING OPERATIONS

# CONCATENATION
first_name = "Jane"
last_name = "Doe"

# Using +
full_name = first_name + " " + last_name

# Using f-strings (modern Python way!)
greeting = f"Hello, {first_name}!"  # Hello, Jane!

# Multiple variables
age = 25
intro = f"I'm {first_name} and I'm {age} years old."
print(intro)  # I'm Jane and I'm 25 years old.

# REPETITION
star = "*"
stars = star * 10  # Output: "**********"
separator = "-" * 20  # Output: "--------------------"
print(stars)
print(separator)

# STRING METHODS

# Changing case
text = "python programming"
print(text.lower())
print(text.upper())
print(text.title())

# Cleaning strings
messy = "   Hello, World!   "
print(messy.strip())  # Removes leading/trailing whitespace

price = "$19.99"
print(price.strip("$"))  # Output: "19.99"
print(price)

# Finding and replacing
message = "I love Python programming with Python"

# Check if something exists
print("Python" in message)  # Output: True
print(message.startswith("I"))  # Output: True
print(message.endswith("Python"))  # Output: True

# Find position
print(message.find("Python"))  # Output: 7 (first occurrence)
print(message.count("Python"))  # Output: 2 (occurrences)

# Replace
new_message = message.replace("Python", "JavaScript")
print(new_message)  # Output: "I love JavaScript programming with JavaScript"

# COMMON MISTAKES
# Forget the f in f-strings
# Wrong
name = "Alice"
message = "Hello {name}"  # Prints: Hello {name}
print(message)

# Right
message = f"Hello {name}"  # Prints: Hello Alice
print(message)

# Wrong quotes in strings
# text = 'It's Python'  # SyntaxError: invalid syntax

# Right - escape or use different quotes
text = "It's Python"  # Double quotes outside
text = "It's Python"  # Excape the apostrophe
print(text)
