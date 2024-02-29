"""
Given a list of dictionaries with people's data, sort it using the person's name.
"""

persons:list = [
    {"name": "Alice", "age": 30},
    {"name": "Bob", "age": 25},
    {"name": "Carol", "age": 20}
]

persons.sort(key=lambda persons: persons["name"])
print(persons)