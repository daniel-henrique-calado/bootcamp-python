"""
Create a function to receive a dictionary and return a list of keys in sorted order.
"""

def extract_keys(dictionary: dict) -> list:
    return sorted(list(dictionary.keys()))

if __name__ == "__main__":
    dictionary: dict = {"a": 3, "c": 10, "g": 19, "d": 1}
    print(f"Sorted keys list: {extract_keys(dictionary=dictionary)}")
