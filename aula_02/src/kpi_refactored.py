"""
Receives a user name, his salary and a bonification value percent.
Uses the following expression to calculate his salary bonus.
salary_bonus: 1000 + salary * bonus_percent
"""
CONSTANT = 1000

try:
    user_name = input("Digite seu nome: ")

    if user_name.isspace() or len(user_name) == 0:
        raise ValueError("O nome não ser vazio.")

    if any(char.isdigit() or not char.isalpha() for char in user_name):
        raise ValueError("O nome não deve conter números ou caracteres especiais.")

except ValueError as e:
    print(e)

try:
    salary = float(input("Informe seu salário mensal : R$ "))

    if salary < 0:
        raise ValueError("O salário ou bônus não podem ser menor que zero.")
except ValueError:
    print("O valor inválido fornecido para o salário. Tente novamente.")

try:
    bonus_percent = float(input("Informe seu bônus percentual: "))

    if bonus_percent < 0:
        raise ValueError("O  bônus não podem ser menor que zero.")
except ValueError:
    print("O valor inválido fornecido para o bônus. Tente novamente.")

salary_bonus = CONSTANT + salary * bonus_percent
print(f"Olá {user_name}, seu bônus foi de {salary_bonus:.2f}")


# Expected bugs on this script
# 1. Invalid name: numbers or special caracteres inputed by user.
# 2. Negative salary: it's impossible.
# 3. Invalid salary/bonus: a text or any different caracter informed by user.
# 4. Negative bonus: on this case, it's not expected to reduce user's salary.

