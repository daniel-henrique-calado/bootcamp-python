"""
Calculate the total price of list based on below data:
["apple", "banana", "cherry"]
{"apple": 0.45, "banana": 0.30, "cherry": 0.65}
"""

fruits:list = ["apple", "banana", "cherry"]
price_fruits = {"apple": 0.45, "banana": 0.30, "cherry": 0.65}
total: float = sum(price_fruits[fruit] for fruit in fruits)

# for fruit in fruits:
#     total += price_fruits[fruit]
print(f"Total list costs: $ {total:.2f}")