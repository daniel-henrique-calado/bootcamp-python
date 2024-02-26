"""
Normalize a list to keep all data between 0 and 1. 
"""

list_to_check = [10, 20, 30, 40, 50]
min_value = min(list_to_check)
max_value = max(list_to_check)
new_list = [(x - min_value)/(max_value - min_value) for x in list_to_check]

print(new_list)

