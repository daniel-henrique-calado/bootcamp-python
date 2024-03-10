"""
Receives a user name, his salary and a bonification value percent.
Uses the following expression to calculate his salary bonus.
salary_bonus: 1000 + salary * bonus_percent
"""
CONSTANT = 1000

try:
    user_name = input("Enter your name: ")

    if user_name.isspace() or len(user_name) == 0:
        raise ValueError("The name can not be blank.")

    if any(char.isdigit() or not char.isalpha() for char in user_name):
        raise ValueError("The name must not contain numbers or "
                         "special characters.")

except ValueError as e:
    print(e)

try:
    salary = float(input("Enter your monthly salary: R$ "))

    if salary < 0:
        raise ValueError("The salary cannot be less than zero.")
except ValueError:
    print("The invalid value provided for the salary. Try again.")

try:
    bonus_percent = float(input("Enter your percentage bonus: "))

    if bonus_percent < 0:
        raise ValueError("The bonus cannot be less than zero.")
except ValueError:
    print("Invalid value provided for the bonus. Please try again.")

salary_bonus = CONSTANT + salary * bonus_percent
print(f"Hi {user_name}, your bonus was {salary_bonus:.2f}")


# Expected bugs on this script
# 1. Invalid name: numbers or special caracteres inputed by user.
# 2. Negative salary: it's impossible.
# 3. Invalid salary/bonus: a text or any different caracter informed by user.
# 4. Negative bonus: on this case, it's not expected to reduce user's salary.
