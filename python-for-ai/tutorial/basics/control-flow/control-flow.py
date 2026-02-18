"""Control flow
Make your programs smart with decisions

​
Making programs think
So far, your programs run top to bottom, executing every line. But real programs need to make decisions - “if this, then that”.
Control flow is what makes programs intelligent!
"""

"""
Real-world examples
Decision-making is everywhere:
ATM: IF password correct, THEN allow access
Apps: IF user clicks button, THEN perform action
Weather app: IF temperature < 0, THEN show snow icon
Games: IF health = 0, THEN game over
​
Prerequisites
Before starting this section, make sure you understand:
Variables and data types
Operators (especially comparison operators)
Boolean values (True/False)"""

"""If statements
Make decisions in your code

​
What are if statements?
If statements let your program make decisions. They check if something is true or false, then act accordingly.
Real-life logic:
IF it’s raining THEN take umbrella
IF battery < 20% THEN charge phone
IF password correct THEN allow access"""

# Basic if statement
age = 18
if age >= 18:
    print("You can vote!")
    print("You are not an adult!")

# if-else statement
temperature = 28
if temperature > 30:
    print("It's hot!")
else:
    print("Temperature is ok.")

# if-elif-else statement
score = 75

if score >= 90:
    print("A - Excellent")
elif score >= 80:
    print("B - Good job!")
elif score >= 70:
    print("C - Keep it up!")
else:
    print("F - Need improvement")

"""Why elif instead of multiple if statements? With elif, Python stops checking once it finds a true condition.
This is more efficient and prevents multiple blocks from running. 
The order matters - always put more specific conditions first!"""

# Multiple condtions
# combine conditions with and, or, not:

age = 25
has_license = True

# Both must be True
if age >= 18 and has_license:
    print("You can legally drive.")

# At least one must be True
day = "Saturday"
holiday = "Independance Day"
weekend = day == "Saturday" or day == "Sunday"
if weekend or holiday:
    print("No work today!")

# Reverse the condition
if not holiday:
    print("We work today!")

# Nested if statements
# Putt if statements inside of other if statements
has_ticket = True
age = 15

if has_ticket:
    if age >= 18:
        print("Enjoy the movie!")
    else:
        print("Need adult supervision.")
else:
    print("Buy a ticket first.")
