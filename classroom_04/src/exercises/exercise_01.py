"""
Create a list with range from 1 to 10 and print the square of each number.
"""
POW:int = 2

numbers:list = range(1, 11)

for num in numbers:
    print(num ** POW)