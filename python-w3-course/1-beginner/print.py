print("Hello World!")

# Must use double quotes inside print function
print("I am learning Python")

# By default, the print function ends with a new line character
# if you want to print multiple words on the same line, you can use the end parameter
print("Hello", end="")

print(3 + 4)
print(10 - 5)

print("I am ", 29, " years old")

# 1. The separator:
# Sometimes, the default space isn't what you want, maybe you want a list separated by dashed,
# or you want to print on the same line. This is where parameters come in handy.
print("Python", "is", "awesome", sep="-")
print("192", "168", "1", "1", sep=".")

# 2. The ender:
# By default, every print() command hits "Enter" at the end(it moves to a new line).
# You can stop this behaviour with "end" parameter.
print("Hello", end=" ")
print("Loading", end="...")
print("Done!")

# 3 f-strings:
# Think of it like Fill-in-the-blank template.
# Put a little f before the quotes.
# Put your variables inside curly braces {}.

name = "Mike"
age = 34

print(f"My name is {name} and I am {age} years old.")
