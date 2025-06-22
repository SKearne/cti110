print("Shaun Kearney")
print("June 21, 2025")
print("P2HW2")
print("Assess student understanding of Lists")
print("\n")
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

print("-----------------------------Results---------------------------")
print("Lowest grade  :   ",lg)
print("Highest grade :   ",hg)
print("Sum of grades :   ",sg)
print("Average       :    %.2f"%avg)

print("----------------------------------------------------------------")
