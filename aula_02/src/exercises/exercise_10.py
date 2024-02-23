"""
Calculate a circle area using radio informed by user.
"""
from math import pi

EXPONENT = 2

radius = float(input("Informe o raio do círculo: "))
area = pi * radius ** EXPONENT

print(f"A área do círculo de raio {radius} é: {area:.2f}")