"""
Verify if a word is a palindrome.
"""

try:
    word = input("Enter a word: ")
    if any(char for char in word if char.isdigit()):
        raise ValueError("Number is not allowed.")

    if len(word) <= 1:
        raise ValueError("The word length must be greater then 1.")

    print(f"The word '{word}' is palindrome? "
          f"{word.strip() == word.strip()[::-1]}")
except ValueError as ve:
    print(ve)
