"""
Receives a user name, his salary and a bonification value percent.
Uses the following expression to calculate his salary bonus.
salary_bonus: 1000 + salary * bonus_percent
"""

def get_user_name(user: dict) -> dict:
    try:
        user_name:str = input("Enter your name: ")
        
        if user_name.isspace() or len(user_name) == 0:
            ValueError("Name can not be blank.")

        if any(char.isdigit() or not char.isalpha() for char in user_name):
            ValueError("Name can not contain numbers or special characters.")
        
        user["name"] = user_name
        return user
    except ValueError as ve:
        print(ve)
        raise

def get_user_salary(user:dict) -> dict:
    try:
        salary:float = float(input("Enter your monthly salary: $ "))

        if salary < 0:
            raise ValueError("The salary cannot be lower than zero.")
        
        user["salary"] = salary
        return user
    except ValueError:
        print("The value provided is invalid for the salary. Try again.")

def get_user_bonus(user: dict) -> dict:
    try:
        bonus_percent:float = float(input("Enter your percentual bonus: "))

        if bonus_percent < 0:
            raise ValueError("The bonus cannot be lower than zero.")
        
        user["bonus"] = bonus_percent
        return user
    except ValueError:
        print("The value provided is invalid for the bonus. Try again.")

def calculate_user_salary_bonus(user:dict) -> dict:
    CONSTANT:int = 1000
    user["salary_bonus"] = user["salary"] * user["bonus"] + CONSTANT
    return user
    

if __name__ == "__main__":
    user:dict = {}
    user = get_user_name(user=user)
    user = get_user_salary(user=user)
    user = get_user_bonus(user=user)
    user =calculate_user_salary_bonus(user=user)

    print(f"User info:\n{user}")
    

