print("Shaun Kearney")
print("June 21, 2025")
print("P2HW1")
print("\n")
#Display "This program calculates and displays travel expenses" for the title of program
print("This program calculates and displays travel expenses")
print("\n")
#Get user input
budget = float(input("Enter Budget: "))
print("\n")
destination = input("Enter your travel destination: ")
print("\n")
gas_expenses = float(input("How much do you think you will spend on gas? "))
print("\n")
accommodation_expenses = float(input("Approximately, how much will you need for accomodation/hotel? "))
print("\n")
food_expenses = float(input("Last, how much do you need for food? "))
print("\n")
# Calculate total travel expenses
total_travel_expenses = gas_expenses + accommodation_expenses + food_expenses

# Calculate remaining balance
remaining_balance = budget - total_travel_expenses
print("------------Travel Expenses------------")
# Display travel expenses in a nicely aligned format
print(f"Location:\t", destination)
print("Initial Budget:\t", "${:.2f}".format(budget))
print("Fuel:\t\t", "${:.2f}".format(gas_expenses))
print("Accommodation:\t", "${:.2f}".format(accommodation_expenses))
print("Food:\t\t", "${:.2f}".format(food_expenses))
print("---------------------------------------")
print("\n")
print("Remaining Balance:", "${:.2f}".format(remaining_balance))
