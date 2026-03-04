# Python code​​​​​​‌‌‌‌​​‌​‌‌‌​​​​​​​‌​​‌‌‌‌ below
hexNumbers = {
    "0": 0,
    "1": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "A": 10,
    "B": 11,
    "C": 12,
    "D": 13,
    "E": 14,
    "F": 15,
}


# Converts a string hexadecimal number(max 3 characters) into an integer decimal
# If hexNum is not a valid hexadecimal number, returns None
def hexToDec(hexNum):
    if not isinstance(hexNum, str) or len(hexNum) == 0 or len(hexNum) > 3:
        return None

    total = 0

    for char in hexNum:
        if char not in hexNumbers:
            return None
        total = total * 16 + hexNumbers[char]

    return total


hexToDec("FCF")
