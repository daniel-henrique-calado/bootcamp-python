"""
Remove the item 'C++' and insert 'Ruby' from the list below:
["Python", "Java", "C++", "JavaScript"]
"""

programming_languages:list = ["Python", "Java", "C++", "JavaScript"]

programming_languages.remove("C++")
programming_languages.append("Ruby")

print(programming_languages)

