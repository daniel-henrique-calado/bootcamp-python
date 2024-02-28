"""
Count the number of occurrences of each character in a string using dictionary
"""

phrase:str = input("Enter a phrase or any word: ")

counters:dict = {}

for char in phrase:
    if char in counters:
        counters[char] += 1
    else:
        counters[char] = 1

print(counters)