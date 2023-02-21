# Create at least 5 different functions and try 
# to handle at least 5 built-in Python Exceptions.

from typing import List, Optional, Union

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
        print(f"Error: print_name_and_surname() please write strings not numbers !!! {e}")


print_name_and_surname(name="John", surname="Bond")

# 4 ----------------------------------------------------------------


def print_increament(number_one: List[int], list_index: int) -> None:
    try:
        list_arry = []
        for i in number_one:
            list_arry.append(i)
        print(f"List arry: {list_arry}")
        print(f"List index: {list_arry[list_index]}")

    except IndexError as e:
        print(f"Error: print_increament() wrong index number!!! {e}")


print_increament(number_one=[1, 2, 3, 4, 5], list_index=5)


# 5 ----------------------------------------------------------------

import random


def print_random_number(start_number: int, end_number: int) -> Optional[Union[int, float]]:

    try:
        return random.randint(start_number, end_number)

    except ValueError as e:
        print(f"Error: print_random_number() {e}")


print(print_random_number(start_number=1, end_number=10.5))
