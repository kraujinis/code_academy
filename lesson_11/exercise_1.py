from typing import List

item_list_1 = [1, 8, 5, 0, -1, 7]
item_list_2 = [0, -7, -4, 1, 2, -6]


def add_puzle(item1: List[int], item2: List[int]) -> bool:
    c = []
    for x, y in zip(item1, item2):
        c.append(x + y)
    if len(set(c)) == 1:
        return True
    else:
        return False


print(add_puzle(item_list_1, item_list_2))