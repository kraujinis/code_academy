import logging


def add_new_numbers(number_one: int, number_two: int) -> int:
    logging.debug(f"Adding {number_one} and {number_two}")
    return number_one + number_two


add_new_numbers(1, 2)

# testas