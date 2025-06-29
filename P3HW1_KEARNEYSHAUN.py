# Shaun Kearney
# June 28, 2025
# P3HW1
# This program takes a number grade , determines average and displays letter grade for average.

#Enter float input formula for modules 1 - 6
m1=float(input("Enter grade for module 1 :"))
m2=float(input("Enter grade for module 2 :"))
m3=float(input("Enter grade for module 3 :"))
m4=float(input("Enter grade for module 4 :"))
m5=float(input("Enter grade for module 5 :"))
m6=float(input("Enter grade for module 6 :"))
#grades empty list
grades=[ ]
#appending one by one grades into list with name grades
grades.append(m1)
grades.append(m2)
grades.append(m3)
grades.append(m4)
grades.append(m5)
grades.append(m6)
#Enter the formula grades for input
lg=min(grades)
hg=max(grades)
sg=sum(grades)
avg=sg/6
print("\n")

print("--------------------------Results------------------------------")
print("Lowest Grade  :   ",lg)
print("Highest Grade :   ",hg)
print("Sum of Grades :   ",sg)
print("Average       :    %.2f"%avg)

print("----------------------------------------------------------------")

if avg >= 90 and avg <= 100:
    print("Your Grade is: A")
elif avg >= 80 and avg < 89:
    print("Your Grade is: B")
elif avg >= 70 and avg < 79:
    print("Your Grade is: C")
elif avg >= 60 and avg < 69:
    print("Your Grade is: D")
else:
    print("Your grade is: F")






