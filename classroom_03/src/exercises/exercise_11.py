"""
Read data until the keyword 'quit' be informed.
"""

data = []
user_data = ""

while user_data != "quit":
    user_data = input("Type anything or 'quit' to exit: ")
    
    if user_data.lower() != "quit":
        data.append(user_data)

print(data)