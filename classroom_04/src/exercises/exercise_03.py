"""
Create a dictionary to store the following informations about a book: title, author, publication year.  
Print all information.
"""

book:dict = {}

while True:
    try:
        title:str = input("Enter the title book: ")
        
        if title.strip() == "":
            raise ValueError("The book's name can not be blank.")
        
        book["title"] = title
        break

    except ValueError as e:
        print(e)

while True:
    try:
        author:str = input("Enter the author's name: ")
        
        if author.strip() is None:
            raise ValueError("The book's name can not be blank.")
        
        if  any(not char.isalpha() for char in author):
            raise ValueError("Author's name can not contain numbers or special characters.")
        
        book["author"] = author
        break

    except ValueError as e:
        print(e)

while True:
    try:
        pub_year:int = int(input("What was the publication year? "))
                
        book["year"] = pub_year
        break

    except ValueError as e:
        print("Publication year must be a integer value.")


print(book)