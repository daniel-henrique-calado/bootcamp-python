"""
Implement a function that takes two arguments: a list of numbers and a number. 
The function should return all combinations of pairs in the list that add up to the given number.
"""

def combinate_numbers(numbers: list, reference: float) -> list:
    
    return [num + reference for num in numbers]

if __name__ == "__main__":
    numbers: list = list(range(1, 10))
    reference: int = 10

    print(combinate_numbers(numbers=numbers, reference=reference))

