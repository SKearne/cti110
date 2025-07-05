# Shaun Kearney
# July 5, 2025
# P4HW1
# Ask user to enter the number of scores they want to enter

num_scores = int(input("How many scores do you want to enter? "))
print("\n")
# Initialize an empty list to store scores

scores = []

# Loop to collect scores

for i in range(1, num_scores + 1):

    # Loop until a valid score is entered

     while True:

        try:

            score = float(input(f"Enter score #{i}: "))

            if 0 <= score <= 100:

                scores.append(score)

                break
                
            else:  
                print("\n")
                print("INVALID Score entered!!!!")
                print("Score should be between 0 and 100")
            
                
        except ValueError:
            print("Invalid input!")
            print("Please enter a number.")

# Calculate the lowest score

lowest_score = min(scores)

# Remove the lowest score from the list

scores.remove(lowest_score)

# Calculate the average of the modified list

average_score = sum(scores) / len(scores)

# Determine the letter grade for the calculated average

if 90 <= average_score <= 100:

    grade = 'A'

elif 80 <= average_score < 90:

    grade = 'B'

elif 70 <= average_score < 80:

    grade = 'C'

elif 60 <= average_score < 70:

    grade = 'D'

else:

    grade = 'F'

# Display the results

print("\n--------------Results-----------")

print(f"Lowest Score  : {lowest_score}")

print("Modified List :", scores)

print(f"Scores Average: {average_score:.2f}")

print(f"Grade         : {grade}")
