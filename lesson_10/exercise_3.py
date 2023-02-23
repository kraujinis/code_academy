# Sukurkite mini python programą, kuri kaip įvestį paimtų du skaičius
# ir grąžintų jų sumą, atimtį, dalybą, daugybą.
from typing import Tuple

# numb_1, numb_2 =input("Enter two numbers: ").split()


def calculate(numb_1: int, numb_2: int) -> Tuple[int, int, int, float]:

    return numb_1 + numb_2, numb_1 - numb_2, numb_1 * numb_2, numb_1 / numb_2


print(calculate(10, 10))

sum, sub, div, mul = calculate(10, 10)  # išpakuojam kintamuosius iš funkcijos

print(sum)