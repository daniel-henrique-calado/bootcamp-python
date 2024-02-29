"""
Extract the keys and values from dictionary and store it two separate lists.
"""
dictionary: dict = {"a": 1, "b": 2, "c": 3}
keys: list = list(dictionary.keys())
values: list = list(dictionary.values())

print(f"Keys: {keys}")
print(f"Values: {dictionary.values()}")
