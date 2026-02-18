"""What are if statements?
If statements let your program make decisions. They check if something is true or false, then act accordingly.
Real-life logic:
IF it’s raining THEN take umbrella
IF battery < 20% THEN charge phone
IF password correct THEN allow access"""

# Basic
age = 18

if age >= 20:
    print("You can vote!")
    print("you are an Adult")
else:
    print("You are not an adult yet!")

# If-else chains
score = 56
if score >= 90:
    print("A - Excellent!")
elif score >= 80:
    print("B - Good job!")
elif score >= 70:
    print("C - Keep it up!")
else:
    print("F - Need improvement")
