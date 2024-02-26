"""
Extract all even numbers from a list.
"""

num_list = range(10)

even_list = [num for num in num_list if num % 2 == 0]

print(even_list)