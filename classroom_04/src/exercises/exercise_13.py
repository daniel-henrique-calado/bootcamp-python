"""
Given a product stock dictionary, filter out those with a quantity greater than 0.
"""

stock:dict = {"Keyboard": 10, "Mouse": 0, "Monitor": 3, "CPU": 0}
filtered_stock:dict = {key: value for key, value in stock.items() if value > 0}
print(f"Stock validated:\n {filtered_stock}")

