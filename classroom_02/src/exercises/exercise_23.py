"""
Simple calculator: enter two float/int values and asks for a operator (+,-,*,/).
Print out the results or a error message. 
"""

try:
    num_01 = float(input("Informe um número: "))
    num_02 = float(input("Informe outro número: "))

    operator = input("Informe a operação que deseja executar (+,-,*,/): ")

    if operator == "+":
        print(f"A soma entre {num_01} e {num_02} é: {num_01 + num_02}")
    elif operator == "-":
        print(f"A diferença entre {num_01} e {num_02} é: {num_01 - num_02}")
    elif operator == "*":
        print(f"O produto entre {num_01} e {num_02} é: {num_01 * num_02}")
    elif operator == "/":
        print(f"A divisão entre {num_01} e {num_02} é: {num_01 / num_02}")
    else:
        raise("Operador inválido. Tente novamente.")
except ValueError:
    print("Dado inválido. Os dados devem ser do tipo float/int.")
except ZeroDivisionError:
    print("O divisor deve ser diferente de zero.")