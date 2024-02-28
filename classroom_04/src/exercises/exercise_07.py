"""
Given a list of ages, filter only those that are greater or equal then 18.
"""
ages:list = [20, 13, 19, 28, 12]
ages_filtered:list = [age for age in ages if age >= 18]
print(ages_filtered)