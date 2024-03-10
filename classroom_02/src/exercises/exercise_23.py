"""
Simple calculator: enter two float/int values and
asks for a operator (+,-,*,/). Print out the results or a error message.
"""

try:
    num_01 = float(input("Enter a number: "))
    num_02 = float(input("Enter other number: "))

    operator = input("Which operation do you want to execute (+,-,*,/): ")

    if operator == "+":
        print(f"The sum between {num_01} and {num_02} is: {num_01 + num_02}")
    elif operator == "-":
        print(f"The difference between {num_01} and {num_02} is: "
              f"{num_01 - num_02}")
    elif operator == "*":
        print(f"The product between {num_01} e {num_02} é: {num_01 * num_02}")
    elif operator == "/":
        print(f"The division between {num_01} e {num_02} é: {num_01 / num_02}")
    else:
        raise ("Invalid operator. Please try again.")
except ValueError:
    print("Invalid data. The data must be of type float/int.")
except ZeroDivisionError:
    print("The divisor must be different from zero.")
