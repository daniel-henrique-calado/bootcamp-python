"""
Extract and print out a day, month and year from date on the following format "DD/MM/YYYY".
"""

date = input("Informe uma data no seguinte formato (DD/MM/AAAA): ")
print(f"Dia: {date.split('/')[0]}")
print(f"Mês: {date.split('/')[1]}")
print(f"Ano: {date.split('/')[2]}")