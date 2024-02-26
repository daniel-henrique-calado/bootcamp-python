"""
Given a list of dictionaries containing student data, filter the dictionary with missing data.
users = [
    {"name": "Alice", "email": "alice@example.com"},
    {"name": "Bob", "email": ""},
    {"name": "Carol", "email": "carol@example.com"}
]
"""

users = [
    {"name": "Alice", "email": "alice@example.com"},
    {"name": "Bob", "email": ""},
    {"name": "", "email": "carol@example.com"}
]

valid_users = [user for user in users if user["email"] and user["name"]]

print(valid_users)