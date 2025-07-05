# Shaun Kearney
# July 5, 20255
# P4LAB2

def main():
    """
    This function prompts the user for an integer, displays its
    multiplication table (1-12) if it's non-negative, and allows
    the user to repeat the process.
    """
    repeat = "yes"  # Initialize the repeat variable

    # A while loop keeps the program running as long as the user wants to repeat
    while repeat.lower() == "yes":
        while True:  # A while loop is used for input validation
            try:
                num = int(input("Enter an integer: "))  # Get integer input from user
                break  # Exit the input loop if a valid integer is entered
            except ValueError:
                print("Invalid input! Please enter a valid integer.")  # Handle non-integer input

        if num < 0:  # Check if the number is negative
            print("This program does not handle negative numbers")
        else:
            print(f"Multiplication table for {num}:")
            # A for loop displays the multiplication table from 1 to 12
            for i in range(1, 13):
                result = num * i
                # Print each line of the multiplication table
                print(f"{num} * {i} = {result}")
            print("\n")
        # Ask the user if they wish to run the program again
        repeat = input("Would you like to run the program again? (yes/no): ")
        print("Exiting program...")  # Message to indicate the program has ended
# Call the main function to start the program
if __name__ == "__main__":
    main()
