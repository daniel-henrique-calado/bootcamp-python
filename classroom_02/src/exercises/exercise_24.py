"""
Inform with given number is positive, negative or zero. Check if is odd or even.
"""

try:
    num = int(input("Digite um número: "))

    if num > 0:
        print(f"O número {num} é positivo.")
    elif num < 0:
        print(f"O número {num} é negativo.")
    else:
        print(f"O número {num} é zero.")

    if num % 2 == 0:
        print(f"O número {num} é par.")
    else: 
        print(f"O número {num} é ímpar.")

except ValueError as e:
    print("O dado deve ser do tipo int.")