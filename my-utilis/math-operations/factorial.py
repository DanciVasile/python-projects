def factorial():
    # Start an infinite loop to repeatedly ask for input until valid
    while True:
        user_input = input("Type a positive whole number:")  # Ask the user for input
        try:
            num = int(user_input)  # Try to convert input to an integer
            if num < 0:             # Check if the number is negative
                print("Number must be positive. Try again.")  # Warn the user
                continue            # Go back to the start of the loop to ask again
            break  # If input is valid (non-negative integer), exit the loop
        except ValueError:        # If input cannot be converted to int (e.g., letters)
            print("That's not a valid number. Try again.")  # Warn the user

    # Calculate factorial using a loop
    factorial_num = 1           # Start with 1 because factorial multiplies numbers
    for i in range(1, num + 1): # Loop from 1 up to the number
        factorial_num *= i      # Multiply factorial_num by each i

    # Print the result
    print(f"The factorial of {num} is: {factorial_num}")  # Show factorial to the user

# Call the function to run it
factorial()
