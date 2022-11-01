# WAPP which prompts the user to enter the radius of the circle.
# if the radius of the circe is greater than 0 then calculate
# and print the area, circumference of the circle

import math as M

r = float(input("Enter the radius = "))
area = M.pi * r * r
circumference = (M.pi * 2) * r

if (r > 0):
    print(f"The area is {area}")
    print(f"The circumference is {circumference}")
else:
    print("value is negative")