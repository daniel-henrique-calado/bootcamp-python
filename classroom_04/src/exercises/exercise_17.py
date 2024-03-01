"""
Create a function to check if a number is prime.
"""

def check_prime_number(number: int) -> bool:
    try:
        if not isinstance(number, int):
            raise TypeError("The input must be a int value.")
        
        if number < 0:
            raise ValueError("The number must be equal or greater than zero.")
        
        return number % 2 == 0
    except TypeError as e:
        print(e)
        raise
    except ValueError as e:
        print(e)
        raise

if __name__ == "__main__":

    print(check_prime_number(number=11))
    print(check_prime_number(number=4))
    print(check_prime_number(number="Olá"))
    print(check_prime_number(number=-8))