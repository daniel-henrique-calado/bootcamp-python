"""
Asks for list of int numbers, separated by comma and check if all numbers of the list are integers.
"""

try:
    list_str = input("Digite uma lista de números inteiros separados por vírgula (,): ").split(',')
    list_int = []
    for num in list_str:
        list_int.append(int(num.strip()))
    print(f"Toda a lista informada é composta por números inteiros: {list_int}.")
except ValueError:
    print("Foram informados dados que não são inteiros.")