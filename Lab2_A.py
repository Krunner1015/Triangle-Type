SL1 = float(input("Side length 1: ")) #user inputs the length of side one of the triangle
SL2 = float(input("Side length 2: ")) #user inputs the length of side two of the triangle
SL3 = float(input("Side length 3: ")) #user inputs the length of side three of the triangle

if (SL1 == SL2) and (SL1 == SL3): #checks if the lengths of all three sides are the same
    print("This is an equilateral triangle!") #displays the message that the triangle is an equilateral to the user
elif (SL1 == SL2) or (SL1 == SL3) or (SL2 == SL3): #checks if just two of the side lengths are the same
    print("This is an isosceles triangle!") #displays the message that the triangle is an isosceles to the user
else: #if none of the sides of equal
    print("This is a scalene triangle!") #displays the message that the triangle is scalene to the user