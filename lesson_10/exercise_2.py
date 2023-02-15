
from typing import List


user_string = input("Enter your string: ")

str_list = ["1", "2", "3", "4", "5", "6", "7"]


def add_str(my_list: List[str], my_string: str) -> List[str]:
    str_added = []
    for item in my_list:
        str_added.append(item + my_string)
    return str_added


a = add_str(str_list, user_string)
print(a)
