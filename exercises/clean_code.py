# Task Nr.1: Fix these coding examples according to
# the standards we learnt during this lecture:

# 1 ------
class Person:
    def __init__(self, name: str, surname: str) -> None:
        self.name = name
        self.surname = surname

    def say_hello(self) -> None:
        print(f"Hello, {self.name} {self.surname}")


person = Person("first", "person")
person.say_hello()

# 2 -------
def greeting_person(name: str) -> None:
    """Function greets a person
    given full name as a string"""

    print(f"Hello {name.split()[0]} {name.split()[1]}, how are you today?")


greeting_person(name="Jonas Bakas")

# 3 --------
def greet_user(age):
    eligieble_to_enter = age >= 21

    if eligieble_to_enter is True:
        print("Welcome")
    if eligieble_to_enter is False:
        print("Access denied")


greet_user(22)

# Task Nr.2: Magic Number problem. A number is said to be a magic number,
# if the sum of its digits are calculated till a single digit recursively
# by adding the sum of the digits after every addition. If the single digit
# comes out to be 1,then the number is a magic number.


def recursion(number: int) -> int:
    while number > 9:
        number_sum = sum(int(digit) for digit in str(number))
        number = number_sum
    return number == 1


print(recursion(10112))


def is_magic_number(number: int) -> bool:
    number = str(number)
    if len(number) == 1:
        if number == "1":
            return True
        else:
            return False
    else:
        number = sum([int(n) for n in number])
        return is_magic_number(number)


print(is_magic_number(50113))
