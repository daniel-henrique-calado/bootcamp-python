"""
Validate inputed data following the rules below: 
Age - between 18 and 65 years.
email = "user@example.com"
"""

try:
    age = int(input("How old are you? "))

    if not 18 < age < 65:
        raise ValueError("Invalid data. Age must be between 18 and 65 years.")

    email = input("What's your email address? ")

    if "@" not in email or "." not in email:
        raise ValueError("Invalid email.")

    print("Data processed successfully.")
except ValueError as e:
    print(e)