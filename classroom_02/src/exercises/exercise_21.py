"""
Convert a Celsius temperature to Fahrenheit and implement
try-except to validate the data.
"""

try:
    temperature_celsius = float(input("Enter a temperature in °C: "))
    temperature_fahrenheit = temperature_celsius * 1.8 + 32

    print(f"The temperature {temperature_celsius} °C is equals to "
          f"{temperature_fahrenheit} °F.")
except ValueError:
    print("Unexpected data. Entered value must be of type int or float.")
