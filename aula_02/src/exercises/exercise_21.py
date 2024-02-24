"""
Convert a Celsius temperature to Fahrenheit and implement try-except to validate the data.
"""

try:
    temperature_celsius = float(input("Informe a temperatura em °C: "))
    temperature_fahrenheit = temperature_celsius * 1.8 + 32
    
    print(f"A temperatura {temperature_celsius} °C equivale a {temperature_fahrenheit} °F.")
except ValueError as e:
    print("Dado inesperado. Valor informado deve ser do tipo int ou float.")