"""
Receives a user name, his salary and a bonification value percent.
Uses the following expression to calculate his salary bonus.
salary_bonus: 1000 + salary * bonus_percent
"""
CONSTANT = 1000

user_name = input("Enter your name: ")
salary = float(input("Enter your monthly salary: R$ "))
bonus_percent = float(input("Enter your percentage bonus: "))

salary_bonus = CONSTANT + salary * bonus_percent

print(f"Hi {user_name}, your bonus was R$ {salary_bonus}")

# Expected bugs on this script
# 1. Invalid name: numbers or special caracteres inputed by user.
# 2. Negative salary: it's impossible.
# 3. Invalid salary/bonus: a text or any different caracter informed by user.
# 4. Negative bonus: on this case, it's not expected to reduce user's salary.

