"""
Create a function to revert a string.
"""

def revert_string(string: str) -> str:
    try:
        if not isinstance(string, str):
            raise TypeError("The input must have a type string.")
        
        if len(string) == 0:
            raise ValueError("The input can not be blank.")
        
        return string[::-1]
    except TypeError as te:
        print(te)
        raise
    except ValueError as ve:
        print(ve)
        raise

if __name__ == "__main__":
    print(revert_string("Chidori"))
    print(revert_string(''))
    print(revert_string(1))