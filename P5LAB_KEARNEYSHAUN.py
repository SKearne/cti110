# Shaun Kearney
# July 09, 2025
# P5LAB
# This program will simulate a customer using a self-checkout machine.


import random

def disperse_change(change_amount):
    """
    Calculates and displays the number of dollars, quarters, dimes, nickels,
    and pennies required to make up the change_amount.
    """
    dollars = int(change_amount // 1)
    change_amount -= dollars * 1
    
    quarters = int(change_amount // 0.25)
    change_amount -= quarters * 0.25
    
    dimes = int(change_amount // 0.10)
    change_amount -= dimes * 0.10
    
    nickels = int(change_amount // 0.05)
    change_amount -= nickels * 0.05
    
    pennies = round(change_amount / 0.01) # Rounding to handle potential float inaccuracies

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
 
def main():
    """
    Simulates a self-checkout transaction, generates a random bill,
    prompts for payment, and displays the change.
    """
    total_owed = round(random.uniform(0.01, 50.00), 2)  # Generate a random amount owed between $0.01 and $50.00.
    print(f"You owe: ${total_owed:.2f}")

    while True:
        try:
            amount_paid = float(input("How much cash will you put in the self-checkout?: $"))
            if amount_paid < total_owed:
                print("Error: Amount paid is less than the total owed. Please enter a higher amount.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a numerical value for the amount paid.")

    change_due = amount_paid - total_owed
    print(f"Change is: ${change_due:.2f}" "\n")

    disperse_change(change_due)

if __name__ == "__main__":
    main()
    
