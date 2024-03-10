"""
Evaluate two boolean values given by user, using a OR operator.
"""

expression_01 = bool(int(input("Enter a boolean (0 or 1): ")))
expression_02 = bool(int(input("Enter other boolean (0 or 1): ")))

print(f"OR operation between informed booleans: "
      f"{expression_01 or expression_02}")

print(f"Type: {type(expression_01)}, Value: {expression_01}")
print(f"Type: {type(expression_02)}, Value: {expression_02}")
