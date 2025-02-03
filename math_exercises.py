#circumference and area of a circle

import math
radius = float(input('Enter the radius of a circle(cm): '))

circumference = 2 * math.pi * radius

print(f"The circumference is {round(circumference, 3)} cm") #rounding upto 3 digits after point

area = math.pi * (radius ** 2)

print(f"The area is {round(area, 2)} cm² ") #SQUARE by alt + 0178 on windows

#finding hypotenuse

a = float(input("Enter Base: "))
b = float(input("Enter Altitude: "))

hypotenuse = math.sqrt(pow(a, 2) + pow(b, 2))

print(f"The Hypotenuse of the triangle is {hypotenuse} unit.")