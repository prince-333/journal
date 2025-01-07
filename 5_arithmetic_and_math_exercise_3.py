# Finding the hypotenuse of a triangle

import math

a = float(input("Enter side A: "))
b = float(input("Enter side B: "))

c = math.sqrt(pow(a, 2) + pow(b, 2))

print(f"The hypotenuse of this triangle with the values of a = {a} cm and b = {b} cm is {c} cm.")