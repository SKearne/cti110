print("Shaun Kearney")
print("June 13, 2025")
print("P1HW2")
print("\n")
# Step 1: Display "This program calculates and displays travel expenses" for the title of program
print("This program calculates and displays travel expenses")
print("\n")

# Step 2: Display "Enter Budget:"
# Step 3: Input first set of numbers to produce value
print("Enter Budget: ", end ="")
Budget = int(input())
print("\n")

# Step 4: Display "Enter your travel destination:"
# Step 5: Input name of your destination country/state
destination = input("Enter your travel destination: ")
print("\n")

# Step 6: Display "How much do you think you will spend on gas?"
# Step 7: Input second set of numbers to produce value
print("How much do you think you will spend on gas? ", end ="")
gas = int(input())
print("\n")

# Step 8: Display "Approximattely, how much will you need for accomodation/hotel?"
# step 9: Input third set of numbers to produce value
print("Approximattely, how much will you need for accomodation/hotel? ", end ="")
accomodation = int(input())
print("\n")

# Step 10: Display "Last, how much do you need for food?"
# Step 11: Input fourth set of numbers to produce value
print("Last, how much do you need for food? ", end ="")
food = int(input())
print("\n")

# Step 12: Display "------------Travel Expenses------------"
# Step 13: Display "Location: ", linked with destination formula
# Step 14: Display "Initial Budget: ", linked with Budget formula
# Step 15: Space
print("------------Travel Expenses------------")
print("Location: ",destination)
print("Initial Budget: ",Budget)

print("\n")

# Step 16: Display "Fuel: ", linked with gas formula
# Step 17: Display "Accomodation: ", linked with accomodation formula
# Step 18: Display "Food", linked with food formula
# Step 19: Space
print("Fuel: ",gas)
print("Accomodation: ",accomodation)
print("Food: ",food)

print("\n")

# Step 20: Display "Remaining Balance". Initial Budget link minus Fuel link minus Accomodation link minus Food link to produce Balance value

print("Remaining Balance: ",Budget - gas - accomodation - food)
