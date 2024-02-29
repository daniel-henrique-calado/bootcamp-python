"""
Unify two dictionaries.
"""

dict_1: dict = {"a": 1, "b": 2}
dict_2: dict = {"c": 3, "d": 4}

new_dict: dict = dict_1 | dict_2

print(new_dict)