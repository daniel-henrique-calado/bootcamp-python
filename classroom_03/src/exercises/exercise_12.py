"""
Ask a user to input data in a specific interval until its reached.
"""

MIN_VALUE = 1
MAX_VALUE = 10

value = int(input("Type a number between 1 and 10: "))

while value < MIN_VALUE or value > MAX_VALUE :
    print("Invalid data.")
    value = int(input("Type a number between 1 and 10: ")) 

print("Valid data.")