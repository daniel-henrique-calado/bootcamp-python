"""
Sales calculator by category.

sales = [
    {"category": "eletronics", "value": 1200},
    {"category": "books", "value": 200},
    {"category": "eletronics", "value": 800}
]
"""

sales = [
    {"category": "eletronics", "value": 1200},
    {"category": "books", "value": 200},
    {"category": "eletronics", "value": 800}
]

consolidate_sale = {}

for sale in sales:
    if sale["category"] in consolidate_sale:
        consolidate_sale[sale["category"]] += sale["value"]
    else:
        consolidate_sale[sale["category"]] = sale["value"]

print(consolidate_sale)



