
def math_sum(num_one, num_two):
    sum = num_one + num_two
    return sum


def string_upper(str: str) -> str:
    return str.upper()


def volume_of_tank(height: int, length: int, witdh: int) -> int:
    volume = height * length * witdh
    if volume < 100:
        print(f"Volume of tank is {volume} its not full, add more")
    elif volume >= 100 and volume < 200:
        print(f"Volume of tank is {volume} almost full")
    else:
        print(f"Volume of tank is {volume} full")


def name_input():
    name = input(f"Enter your name: ")
    print(f"Your name is {name}")


def reverse_string(string: str) -> str:
    reversed_string = string[::-1]
    print(f"Reversed string is \"{reversed_string}\" original string was \"{string}\"")

reverse_string("hello")
