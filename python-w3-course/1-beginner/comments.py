# Comments are lines in your code that the program skips when running the code.
# The are used for documentation and explaining what the code does.


# HOW TO COMMENT THE RIGHT WAY
# 1. Use comments to explain why something is done, not what is done.
# 2. Use comments to explain complex code, not simple code.
# 3. Use comments to explain the purpose of a function, not how it works.
# 4. Use comments to explain the expected input and output of a function.
# 5. Use comments to explain the overall structure of your code, not every single line.
# 6. Use comments to explain the reasoning behind a decision, not the decision itself.
# 7. Use comments to explain the context of a piece of code, not the code itself.
# 8. Use comments to explain the assumptions made in your code, not the code itself.
# 9. Use comments to explain the limitations of your code, not the code itself.
# 10. Use comments to explain the potential pitfalls of your code, not the code itself.

# When to use single line comments:
# Document assumptions, TODOs, use as section dividers:

# ================= Data loading =================

# ================= Data cleaning =================

# ================= Data analysis =================

# When to use multi-line comments:
# Document complex code
"""This is a multi-line comment."""
# ⚠️ Important Truth:
# Python doesen't have actually multi-line comments, they are just multi-line strings
# that Python ignores because they are not assigned to a variable.

# 1. Use them for: File Headers
"""
File: data_processor.py
Author: Marian Danci
Created: 2026-02-16
Description: Processes customer data from CSV files and generates reports.

Dependencies:
- pandas >= 2.0.0
- numpy >= 1.24.0

Usage:
    python data_processor.py --input customers.csv --output report.pdf
"""

# 2. Complex algorithms explanations
"""
This function implements the Quicksort algorithm.

How it works:
1. Pick a pivot element from the array
2. Partition: reorder array so elements < pivot come before, > pivot come after
3. Recursively sort the sub-arrays

Time Complexity: O(n log n) average, O(n²) worst case
Space Complexity: O(log n)

Why chosen: Better average performance than bubble sort for large datasets.
"""

# 3. Temporarily Disable Large Code Blocks:
"""
# Old implementation - keeping for reference
def old_calculate_tax(income):
    if income < 10000:
        return income * 0.1
    elif income < 50000:
        return income * 0.2
    else:
        return income * 0.3
"""

# 4. Long Explanations:
"""
IMPORTANT: This function makes an assumption that might not be obvious.

The input data is expected to be in UTC timezone. If you pass local time,
the calculations will be incorrect. Always convert to UTC first using:

    from datetime import timezone
    utc_time = local_time.astimezone(timezone.utc)

This design decision was made because:
- API returns UTC timestamps
- Avoids daylight saving time issues
- Simplifies timezone math across different regions
"""


# ---------------------------------------------------------------------------------------------|
# | Aspect     | Comments                          | Docstrings                                |
# ---------------------------------------------------------------------------------------------|
# | Purpose    | Explain HOW/WHY code works        | Describe WHAT function/class does         |
# | Location   | Anywhere in code                  | First line of function/class/module       |
# | Accessible | No – just for reading code        | Yes – accessible via help() and __doc__   |
# | For        | Developers reading the code       | Users of your function/class              |
# | Syntax     | # or """ anywhere                 | """ as first statement                    |
# ---------------------------------------------------------------------------------------------|


# What is docstring?
# A docstring is a special type of comment that is used to describe what a function, class,
# or module does. It is written as a string literal that is the first statement in the function,
# class, or module.


def greet(name):
    """
    This is a DOCSTRING.
    It describes what the function does.
    """
    return f"Hello, {name}!"


# Docstrings are accessible via the __doc__ attribute of the function, classm or module.
print(greet.__doc__)

# Comments are not accesible this way.

# **Notice:**

# - ✅ Docstrings explain WHAT each part does
# - ✅ Comments explain WHY for non-obvious decisions
# - ✅ Function names are self-documenting
# - ✅ Constants replace magic numbers
# - ✅ Type hints show expected types
# - ❌ No comments explaining obvious code

# ---

# ## 🎯 Comment Quality Checklist

# Before writing a comment, ask:

# 1. ☑️ **Can I use a better variable/function name instead?**
# 2. ☑️ **Can I extract this to a function with a descriptive name?**
# 3. ☑️ **Does this explain WHY, not WHAT?**
# 4. ☑️ **Will this be helpful 6 months from now?**
# 5. ☑️ **Would a beginner understand the code without this comment?**

# If you answer "no" to all, then write the comment!


# 💡 Pro Tip: The best comment is no comment - because the code explains itself!
# Aim for code so clear that comments are only needed for complex business logic and "why" decisions.
