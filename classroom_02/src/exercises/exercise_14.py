"""
Extract and print out a day, month and year from
date on the following format "DD/MM/YYYY".
"""

date = input("Enter a date using the following format (DD/MM/AAAA): ")
print(f"Day: {date.split('/')[0]}")
print(f"Month: {date.split('/')[1]}")
print(f"Year: {date.split('/')[2]}")
