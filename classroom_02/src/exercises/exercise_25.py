"""
Asks for list of int numbers, separated by comma and check if
all numbers of the list are integers.
"""

try:
    list_str = input("Enter a list of comma-separated integers (,): ")
    list_int = []
    for num in list_str.split(','):
        list_int.append(int(num.strip()))
    print(f"The whole list is made up of integers: {list_int}.")
except ValueError:
    print("Non-integer data has been entered.")
