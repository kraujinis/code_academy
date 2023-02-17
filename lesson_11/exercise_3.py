
from typing import List

# list_1 = ["at", "be", "th", "au"]
# list_2 = ["beautiful", "the", "hat"]    # True

# list_1 = ["ay", "be", "ta", "cu"]
# list_2 = ["maybe", "beta", "abet", "course"]    # False

list_1 = ["th", "fo", "ma", "or"]
list_2 = ["the", "many", "for", "forest"]   # True

# list_1 = ["oo", "mi", "ki", "la"]
# list_2 = ["milk", "chocolate", "cooks", "cooks"]    # False


def bigram(list1: List[str], list2: List[str]) -> bool:

    list_double = []
    filtered = []

    for i in range(len(list2)):
        for j in range(len(list2[i]) - 1):
            a = list2[i][j]
            b = list2[i][j + 1]
            c = a + b
            list_double.append(c)

    for i in list1:
        if i in list_double:
            filtered.append(i)
    if len(list1) == len(filtered):
        return True
    else:
        return False


print(bigram(list_1, list_2))
