import math

math.sqrt(16)

from math import sqrt, pi

import random

# Use module functions
number = random.randint(1, 10)
choice = random.choice(["Apple", "Orange", "Coconut"])

# Date and time
import datetime

today = datetime.date.today()
print(today)

# Operating system
import os

current_dir = os.getcwd()
print(current_dir)

# JSON data
import json

data = {"name": "Alice", "age": 30}
json_string = json.dumps(data)
print(json_string)

# Import methods
# Different ways to import

# Import the entire module
import math

result = math.sqrt(16)

# Import specific fucntions
from math import sqrt, pi

result = sqrt(16)
radius = 10
circle_area = pi * radius**2

# Import with alias
import pandas as pd

df = pd.DataFrame(data)

# Import everything (avoid this!)
from math import *

"""Avoid 'from module import *' as it can cause naming conflicts and makes the
code harder to understand"""

# Install packages
# External packages need installation:
"""pip install requests"""

# Install specific versions
"""pip install requests==2.28.0"""

# Install multiple packages
"""pip install pandas numpy matplotlib"""

"""Always ensure your virtual environment is activated before installing!
This is the #1 source of import errors.
If you get “ModuleNotFoundError” after installing, you probably installed to the wrong environment.
Learn more about virtual environments."""

# ⚠️ Sharing your project
# When you share your Python project, others need to know which packages to install.
# The standard way is using a requirements.txt file:
# List all your project's packages:
"""pip freeze > requirements.txt"""
# This creates a file like:
"""
certifi==2024.2.2
charset-normalizer==3.3.2
idna==3.6
requests==2.31.0
urllib3==2.2.0
"""

# Installing from requirements.txt:
# When someone gets your package they run:
"""pip install -r requirements.txt"""

# This installs all the packages at once!

# Using external packages
# After installation, import and use:

# Web requests
import requests

response = requests.get("https://api.example.com/data")
data = response.json()

# Data analysis
import pandas as pd

# Create a simple DataFrame
data = {
    "name": ["Alice", "Bob", "Charlie"],
    "age": [22, 43, 12],
    "city": ["Dallas", "NYC", "Chicago"],
}
df = pd.DataFrame(data)
print(df)
