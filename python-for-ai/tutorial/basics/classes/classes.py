class Dog:  # Note: class names use PascalCase
    pass


"""Adding an initializer
The __init__ method runs when you create a new object:"""


class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed


# Create dog objects - using positional arguments
dog1 = Dog("Budy", "Golden Retriever")
dog2 = Dog("Max", "Beagle")

# Or with named arguments (clearer)
dog3 = Dog(name="Charlie", breed="Malinois")

print(dog1.name)
print(dog2.breed)
print(dog3.name, dog3.breed)

"""Yes, __init__ looks weird with those double underscores!
This is called a “dunder” method (double underscore).
It’s just how Python works - you’ll need to type it exactly like this.
Don’t worry, after writing it a few times it becomes second nature.
Think of it as Python’s special way of saying “this is the setup method”."""


# Understanding self
# self refers to the current object. It’s how an object keeps track of its own data:
# When defining methods in a class, you always include self as the first parameter.
# But when calling the method, you don’t pass it - Python does that automatically!


class Dog:
    def __init__(self, hair_color):
        self.hair_color = hair_color


# Using positional arguments
dog1 = Dog("brown")

# Used named arguments (same results)
dog2 = Dog(hair_color="yellow")

# Each dog has its own hair color
print(dog1.hair_color)
print(dog2.hair_color)


# Real world examples: configuration
# Here is a practical class for AI engineering:
class APIConfig:
    def __init__(self, api_key, model="gpt-3.5-turbo", max_tokens=100):
        self.api_keys = api_key
        self.model = model
        self.max_tokens = max_tokens
        self.base_url = "https://api.openai.com/v1/"


# Create different configurations
# Using positional for required arg (arguments), named for optional
dev_config = APIConfig("sk-dev-key", max_tokens=50)

# Using all named arguments (clearest)
prod_config = APIConfig(api_key="sk-prod-key", model="gpt-4", max_tokens=1000)

# Access the configuration
print(dev_config.model)  # gpt-3.5-turbo
print(prod_config.model)  # gpt-4
print(prod_config.max_tokens)  # 1000

# CLASS VS INSTANCE
# # Class is the blueprint (like a recipe)
# Instance/Object: what you create from the class (like a cake from the recipe)

# APIConfig is the class
# config1 and config2 are the instances
config1 = APIConfig(api_key="key1", max_tokens=1000)
config2 = APIConfig(api_key="key2", max_tokens=500)

# Each instance has its own data
print(config1.max_tokens)  # 1000
print(config2.max_tokens)  # 500

# Changing one doesn't affect the other
config1.max_tokens = 1850
print(config1.max_tokens)  # 1850
print(config2.max_tokens)  # 500    (unchanged)

"""Always use clear, descriptive names for your classes. 
In Python, class names use PascalCase (like TextProcessor or DataLoader), 
while variable names use snake_case (like text_processor or data_loader)."""
