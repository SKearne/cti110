print("Shaun Kearney")
print("June 18, 2025")
print("P2LAB1")
print("how to write code that performs mathematical calculations")
print("\n")
# diameter = 2 * radius
# circumference = 2 * math.pi * radius
# area = math.pi * radius**2
import math
def calculate(radius):
    diameter = 2 * radius   #calculating diameter of circle by multipying radius with 2
    area = math.pi * radius ** 2  #calculating area of circle by multipying pi value with r^2
    circumference = 2 * math.pi * radius  #calculating circumference of circle by multipying radius with 2 and pi value
    print("\n")

    print("The diameter of the circle is: {:.1f}".format(diameter))  #displaying diameter of circle
    print("\n")
    
    print("The circumference of the circle is: {:.2f}".format(circumference))   #displaying circumference of circle
    print("\n")
     
    print("The area of the circle is: {:.3f}".format(area)) #displaying area of circle
    print("\n")
    
radius=float(input("What is the radius of the circle? ")) #taking radius from user
calculate(radius)  #calling calculate function by passing radius as parameter

