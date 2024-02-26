"""
Process items in a list until it finds a specific value that indicates the stop
"""

itens = [1, 2, 3, "stop", 4, 5]
iterator = 0

while itens[iterator] != "stop":
    print(f"Processing item: {itens[iterator]}")
    iterator += 1

print("Finished processing.")