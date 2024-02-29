"""
Update a price of a product, in a list of dictionaries representing a product.
"""
USER_ATTEMPTS = 1
USER_ATTEMPTS_LIMIT = 5

products:list = [
    {"id": 1, "name": "Teclado", "price": 100},
    {"id": 2, "name": "Mouse", "price": 80},
    {"id": 3, "name": "Monitor", "price": 300}
]

while USER_ATTEMPTS <= USER_ATTEMPTS_LIMIT:
    try:
        product_informed:str = input("What product will be the price changed? ")

        if len(product_informed) == 0:
            raise ValueError(f"The product name can not be blank. Try again.\nAttempt {USER_ATTEMPTS} of {USER_ATTEMPTS_LIMIT}.")
                
        if any(not char.isalpha() for char in product_informed):
            raise ValueError(f"The product name can not contain numbers or special characteres. Try again.\nAttempt {USER_ATTEMPTS} of {USER_ATTEMPTS_LIMIT}.")
        
        if not any(True if product_informed == product["name"] else False for product in products):
            raise ValueError(f"The informed product does not exists on the system. Try again.\nAttempt {USER_ATTEMPTS} of {USER_ATTEMPTS_LIMIT}.")
        
        USER_ATTEMPTS = 1
        break
    except ValueError as e:
        USER_ATTEMPTS += 1
        print(e)
    
while USER_ATTEMPTS <= USER_ATTEMPTS_LIMIT:
    try:
        new_price: float = float(input(f"What is the new value for product: {product_informed}? "))

        if new_price < 0:
            raise ValueError("The value can not be less then zero. Try again \nAttempt {USER_ATTEMPTS} of {USER_ATTEMPTS_LIMIT}.")
        
        break
    except ValueError as e:
        USER_ATTEMPTS += 1
        print(e)


for product in products:
    if product["name"] == product_informed:
        product["price"] = new_price

print(f"Price update successfully: \n {products}")