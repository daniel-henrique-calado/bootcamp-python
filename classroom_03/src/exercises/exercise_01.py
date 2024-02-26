"""
Data Quality - verify if the price and quantity of a product are been correctn recorded. 
If both are positive return "Valid data.", otherwise "Invalid data.
"""

try:
    quantity = int(input("How many products do you want to record? "))
    price = float(input("How much for one unit of this product? $ "))

    if quantity < 0 or price < 0:
        raise ValueError("Invalid data.")
    
    print("Valid data.")
except ValueError as e:
    print(e)