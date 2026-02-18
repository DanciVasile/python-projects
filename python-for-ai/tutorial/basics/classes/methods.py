# Add functionality to classes with methods
# Methods are functions defined inside a class. They can operate on the data (attributes) of the class and perform
# Attributes: storing data, they are variables that belong to an object,
# There are two types of methods:


# Instance attributes: (unique to each object/instance):
class APIClient:
    def __init__(self, api_key, base_url):
        self.api_key = api_key  # Each client has its own API key
        self.base_url = base_url  # Each client has its own base URL
        self.request_count = 0  # Track requests per client


# Creating instances with named arguments
client1 = APIClient(api_key="key1", base_url="https://api1.com")
client2 = APIClient(api_key="key2", base_url="https://api2.com")


# Class attributes: shared across all instances of the class
class APIClient:
    version = "1.0"  # Same for all the clients
    max_retries = 3  # Same for all the clients

    def __init__(self, api_key):
        self.api_key = api_key  # Unique to each client


# METHODS: Adding behaviour to our classes
# Methods are functions that belong to a class. They always have self as the first parameter
# but you don;t pass it when calling:


class DataValidator:
    def __init__(self):
        self.errors = []

    def validate_email(self, email):
        if "@" not in email:
            self.errors.append(f"Invalid email: {email}")
            return False
        return True

    def validate_age(self, age):
        if age < 0 or age > 150:
            self.errors.append(f"Invalid age: {age}")
            return False
        return True

    def get_errors(self):
        return self.errors


# Use the validator
validator = DataValidator()

# Notice: we don't pass self, just the email
validator.validate_email(email="bad-email")
validator.validate_age(age=200)

# Or using positional arguments
validator.validate_email("another-bad-email")
validator.validate_age(150)

print(validator.get_errors())
# ['Invalid email: bad-email', 'Invalid age: 200', 'Invalid email: another-bad-email']

"""When you call a method like validator.validate_email("test@example.com"),
Python automatically passes the validator object as self.
You only provide the other arguments."""
