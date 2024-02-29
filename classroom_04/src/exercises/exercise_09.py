"""
Calculate the mean of a list of numbers.
"""

numbers: list = [10, 20, 30, 40, 50]
mean: float = sum(numbers)/len(numbers)
print(f"The mean of the following numbers {numbers} is: {mean:.2f}")