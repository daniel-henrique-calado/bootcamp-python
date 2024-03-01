"""
Create a function to sum a list of numbers.
"""

def sum_numbers_list(numbers:list) -> float:
    
    new_list_numbers = numbers[:]

    try:
        if not isinstance(new_list_numbers, list):
            raise TypeError(f'The function "{sum_numbers_list.__name__}" expect a list as input type.')
        
        if any(False if type(num) not in ("float", "int") else True for num in new_list_numbers):
            raise TypeError("The values of informed list must be type equals to float/int.")
        
        sum_numbers = 0
        for num in new_list_numbers:
            sum_numbers += num
        
        return sum_numbers
    except TypeError as e:
        print(e)

if __name__ == "__main__":
    numbers = list(range(1, 10))
    print(sum_numbers_list(numbers=numbers))
