"""
Inform with given number is positive, negative or zero.
Check if is odd or even.
"""

try:
    num = int(input("Enter a number: "))

    if num > 0:
        print(f"The number {num} is positive.")
    elif num < 0:
        print(f"The number {num} is negative.")
    else:
        print(f"The number {num} is zero.")

    if num % 2 == 0:
        print(f"The number {num} is even.")
    else:
        print(f"The number {num} is odd.")

except ValueError:
    print("The data must be of type int.")
