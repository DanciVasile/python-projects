"""
Python Methods: Normal, Static, and Class Methods
"""

# -----------------------------
# STATIC METHODS
# -----------------------------
# A static method in a Python class is a function that lives inside a class,
# but does NOT use the class or the object.
# It’s just placed there because it logically belongs to that class.

# 🧠 Think of it like this:
# Imagine a class is a toolbox.
# Normal methods   → tools that need the toolbox
# Class methods    → tools that need the toolbox’s label
# Static methods   → tools that don’t need either — they’re just stored there


class MyClass:
    def __init__(self, x):
        self.x = x

    @staticmethod
    def static_method():
        return "I am a static method"


# -----------------------------
# STATIC METHOD EXAMPLE
# -----------------------------
class User:
    @staticmethod
    def is_valid_email(email):
        """Check if email contains '@' symbol"""
        return "@" in email


# Using static method (no object needed)
email1 = User.is_valid_email("text@email.com")
email2 = User.is_valid_email("textemail.com")
print(email1)  # True
print(email2)  # False


# -----------------------------
# NORMAL VS STATIC METHOD
# -----------------------------
# Normal method (needs object)
class Person:
    def greet(self):
        print("Hello!")


# Static method (no object needed)
class PersonHelper:
    @staticmethod
    def say_hi():
        print("Hi!")


p = Person()
p.greet()  # Hello!
PersonHelper.say_hi()  # Hi!


# -----------------------------
# CLASS METHODS
# -----------------------------
# A class method works with the class itself, not individual objects.
# It uses 'cls' (the class), not 'self'.


class UserCounter:
    count = 0

    @classmethod
    def add_user(cls):
        cls.count += 1


UserCounter.add_user()
print(UserCounter.count)  # 1


# -----------------------------
# WHEN TO USE EACH METHOD
# -----------------------------
# ✅ Normal method (self): when you need object-specific data
# Example: user’s name, age, settings.

# ✅ Class method (cls): when you need class-wide data shared by all objects
# Example: counters, factories, alternative constructors.

# ✅ Static method: when you need no class or object data but the function logically belongs to the class
# Example: validators, helpers, math functions

# -----------------------------
# SUMMARY TABLE
# -----------------------------
# | Method Type   | Uses    | When to Use      |
# | ------------- | ------- | ---------------- |
# | Normal        | self    | Per object       |
# | Class method  | cls     | Whole class      |
# | Static method | None    | Helper only      |
