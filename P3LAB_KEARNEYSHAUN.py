# Shaun Kearney
# June 28, 2025
# This program calculates the most efficient number of dollars, quarters, dimes, nickels, and pennies for a given amount of money.

# Prompt the user for a monetary value
def main():
    amount = float(input("Enter the amount of money as a float: $"))

   # Convert the amount to pennies to work with integers
    total_pennies = int(amount * 100)

    # Calculate the number of dollars, quarters, dimes, nickels, and pennies
    dollars = total_pennies // 100  
    remaining_pennies = total_pennies % 100 

    quarters = remaining_pennies // 25  
    remaining_pennies %= 25  

    dimes = remaining_pennies // 10  
    remaining_pennies %= 10  

    nickels = remaining_pennies // 5  
    pennies = remaining_pennies % 5  
    
    # Display the results
    if(pennies == 0):
        print("No Change")

    if(dollars == 1):
        print(dollars, "Dollar")
    elif(dollars > 0):
        print(dollars, "Dollars")

    if(quarters == 1):
        print(quarters, "Quarter")
    elif(quarters > 0):
        print(quarters, "Quarters")

    if(dimes == 1):
        print(dimes, "Dime")
    elif(dimes > 0):
        print(dimes, "Dimes")

    if(nickels == 1):
        print(nickels, "Nickel")
    elif(nickels > 0):
        print(nickels, "Nickels")

    if(pennies == 1):
        print(pennies, "Penny")
    elif(pennies > 0):
        print(pennies, "Pennies")

if __name__ == "__main__":
    main()
