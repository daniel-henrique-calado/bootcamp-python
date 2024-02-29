"""
Given a list of values, split it into two lists: one containing ever numbers and other with odd numbers.
"""
numbers:list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
odd_numbers:list = [num for num in numbers if num % 2 != 0]
even_numbers:list = [num for num in numbers if num % 2 == 0]

print(f"Odd numbers: {odd_numbers}")
print(f"Even numbers: {even_numbers}")
