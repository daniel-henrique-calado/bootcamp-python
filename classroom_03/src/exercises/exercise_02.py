"""
Classify a sensor temperature based on the following rules:
- LOW < 18°C;
- NORMAL >= 18° and <= 26°C
- HIGH > 26°C
"""

LOW_TEMPERATURE = 18
HIGH_TEMPERATURE = 26

try:
    temperature = float(input("Sensor temperature: "))

    if temperature < LOW_TEMPERATURE:
        print("Low.")
    elif LOW_TEMPERATURE <= temperature <= HIGH_TEMPERATURE:
        print("Normal.")
    else:
        print("High.")
except ValueError as e:
    print("Invalid data.")