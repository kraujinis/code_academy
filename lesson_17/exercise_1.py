
# Create a Calculator class with main functionality:
# add, divide, multiply, subtract , etc..
# Initiate class and show up some calculations.

class Calculator():
    def __init__(self, number_one: float, number_two: float):
        self.number_one: float = number_one
        self.number_two: float = number_two

    def add(self) -> float:
        return round((self.number_one + self.number_two), 2)

    def div(self):
        return round((self.number_one / self.number_two), 2)

    def multiply(self) -> float:
        return round((self.number_one * self.number_two), 2)

    def subtract(self) -> float:
        return round((self.number_one - self.number_two), 2)


x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

calc = Calculator(x, y)


print(calc.add())
print(calc.div())
print(calc.multiply())
print(calc.subtract())


print(calc.add() + calc.div())
