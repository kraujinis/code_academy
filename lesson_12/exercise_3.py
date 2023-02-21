# Sukurkite mini "Python" programą, kuri įvestų du skaičius
# ir grąžintų jų sumą, atimtį, dalybą, daugybą. Tvarkykite visas
# galimas klaidas.


from typing import Union


def calculator(number_one: Union[int, float], number_two: Union[int, float]) -> str:

    try:
        sum = number_one + number_two
        substraction = number_one - number_two
        division = number_one / number_two
        multiplication = number_one * number_two
        return f"sum_s = {sum}, substraction = {substraction}, division = {division}, multiplication = {multiplication}"

    except (ZeroDivisionError, TypeError, Exception) as e:
        return f"Error: {e}"


print(calculator(10, 'a'))

