"""
Receives a user name, his salary and a bonification value percent.
Uses the following expression to calculate his salary bonus.
salary_bonus: 1000 + salary * bonus_percent
"""
CONSTANT = 1000

user_name = input("Digite seu nome: ")
salary = float(input("Informe seu salário mensal : R$ "))
bonus_percent = float(input("Informe seu bônus percentual: "))

salary_bonus = CONSTANT + salary * bonus_percent

print(f"Olá {user_name}, seu bônus foi de {salary_bonus}")

# Expected bugs on this script
# 1. Invalid name: numbers or special caracteres inputed by user.
# 2. Negative salary: it's impossible.
# 3. Invalid salary/bonus: a text or any different caracter informed by user.
# 4. Negative bonus: on this case, it's not expected to reduce user's salary.

