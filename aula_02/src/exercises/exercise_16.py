"""
Evaluate two boolean values given by user, using a AND operator.
"""

expression_01 = bool(int(input("Informe um booleano (0 ou 1): ")))
expression_02 = bool(int(input("Informe outro booleano (0 ou 1): ")))

print(f"A operação AND para os dois booleanos é: {expression_01 and expression_02}")

print(f"Tipo: {type(expression_01)}, Valor: {expression_01}")
print(f"Tipo: {type(expression_02)}, Valor: {expression_02}")