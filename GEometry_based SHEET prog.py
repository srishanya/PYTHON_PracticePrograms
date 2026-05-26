#GEOMETRY BASED PROGRAMS
#Q1: Check if a triangle is equilateral, isosceles or scalene
a = float(input("Enter the length of the first side of the triangle: "))
b = float(input("Enter the length of the second side of the triangle: "))
c = float(input("Enter the length of the third side of the triangle: "))
if a == b == c:
    print("The triangle is equilateral.")
elif a == b or b == c or a == c:
    print("The triangle is isosceles.")
else:  
    print("The triangle is scalene.")


#Q2: check for right angled triangle
a = float(input("Enter the length of the first side of the triangle: "))
b = float(input("Enter the length of the second side of the triangle: "))
c = float(input("Enter the length of the third side of the triangle: "))
sides = sorted([a, b, c])
if sides[0]**2 + sides[1]**2 == sides[2]**2:
    print("The triangle is a right-angled triangle.")
else:
    print("The triangle is not a right-angled triangle.")
    
