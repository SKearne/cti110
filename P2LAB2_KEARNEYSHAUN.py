print("Shaun Kearney")
print("June 20, 2025")
print("P2LAB2")
print("tests student's knowledge of how to write code that uses a dictionary to store user input and displays output to the user")
print("\n")
# Create the dictionary
car_mpg = {
    "Camaro": 18.21,
    "Prius": 52.36,
    "Model S": 110,
    "Silverado": 26
}

# Create a variable to hold the keys and print it
keys = car_mpg.keys()
print(keys)
print("\n")
# Enter a vehicle
vehicle_choice = input("Enter a vehicle to see it's mpg: ")
print("\n")
# Display the MPG for the chosen vehicle
if vehicle_choice in car_mpg:
    mpg = car_mpg[vehicle_choice]
    print(f"The {vehicle_choice} gets {mpg} mpg")
    print("\n")
    # Input miles to drive
    try:
        miles_to_drive = float(input(f"How many miles will you drive the {vehicle_choice} "))
        print("\n")
        # Calculate gallons needed
        gallons_needed = miles_to_drive / mpg

        # Display gallons needed, rounded to two decimal places
        print(f"{gallons_needed:.2f} gallon(s) of gas are needed to drive the {vehicle_choice} {miles_to_drive} miles.")
        print("\n")
    except ValueError:
        print("Invalid input for miles. Please enter a valid number.")

else:
    print("Invalid vehicle choice. Please enter a vehicle from the list.")
