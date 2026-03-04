# Python Exercise: Factorial Function
# Write a function called factorial that calculates the factorial of a given number.
# The factorial of a number n (written n!) is the product of all positive integers up to n.
# For example: 5! = 5*4*3*2*1 = 120, 0! = 1
# The function should only accept 0 or positive integers. If the input is invalid, return None.
# Do not use built-in factorial functions; implement the calculation yourself using loops.


def factorial():
    while True:
        user_input = input("Type a positive whole number:")
        try:
            num = int(user_input)
            if num < 0:
                print("Number must be positive. Try again.")
                continue
            break
        except ValueError:
            print("That's not a valid number. Try again.")

    factorial_num = 1
    for i in range(1, num + 1):
        factorial_num *= i

    print(f"The factorial of {num} is: {factorial_num}")


factorial()
