"""
Verify if a word is a palindrome.
"""

try:
    word = input("Digite uma palavra: ")
    print(f"A palavra '{word}' digitada é palíndromo? {word.strip() == word.strip()[::-1]}")
except:
    print("Dado inesperado. O valor informado deve ser uma string.")

