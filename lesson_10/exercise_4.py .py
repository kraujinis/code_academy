# Sukurkite funkciją, kuri grąžintų tik unikalius simbolius turinčias eilutes.
# TODO: pasibaigti

from typing import List

list =["Tomas", "Peter", "Jonas", "Peter", "Jonas", "Peter", "Jonas"]


def is_unique(list: List[str]) -> bool:
    return len(set(list)) == len(list)


print(is_unique(list))