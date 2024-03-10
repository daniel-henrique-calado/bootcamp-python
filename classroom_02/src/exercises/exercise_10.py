"""
Calculate a circle area using radio informed by user.
"""
from math import pi

EXPONENT = 2

radius = float(input("Enter the circle's radius: "))
area = pi * radius ** EXPONENT

print(f"The area of the circle of radius {radius} is: {area:.2f}")
