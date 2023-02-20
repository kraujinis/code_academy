# Create at least 5 different functions and try 
# to handle at least 5 built-in Python Exceptions.

from typing import Optional, Union

# 1 ----------------------------------------------------------------


def print_sum(number_one: Union[int, float], number_two: Union[int, float]) -> Optional[Union[int, float]]:

    try:
        return number_one + number_two

    except Exception as e:
        print(f"Error: print_sum() {e}")


print(print_sum(number_one=1.2, number_two=12))

# 2 ----------------------------------------------------------------


def print_division(number_one: Union[int, float], number_two: Union[int, float]) -> Optional[Union[int, float]]:

    try:
        return number_one / number_two

    except ZeroDivisionError as e:
        print(f"Error: print_division() dont delete by zero! {e}")

    except Exception as e:
        print(f"Error: print_division() dont use strings! {e}")


print(print_division(number_one=1.2, number_two=5))

# 3 ----------------------------------------------------------------


def print_name_and_surname(name: str, surname: str) -> Union[str, None]:

    try:
        print("Joined Name and Surname : ", name + surname)

    except TypeError as e:
        print(f"Error: print_name_and_surname() {e}")


print_name_and_surname(name="John", surname="Connor")

# 4 ----------------------------------------------------------------


def print_increament(number_one: Union[int, float], number_two: Union[int, float]) -> Optional[Union[int, float]]:
    try:
        return number_one * number_two

    except IndexError as e:
        print(f"Error: print_sum() {e}")
        

print_increament(number_one=1.2, number_two=12, number_three=5)
