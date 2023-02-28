from datetime import date


class Person:
    # Class atribute, can take any name
    description: str = "A simple normal human being"

    def __init__(self, name: str, surname: str):
        self.name: str = name
        self.surname: str = surname

    def greet(self):
        return f"Hello, my name is {self.name}"

    def calculate_days_left_till_black_friday(self):
        today = date.today()
        black_friday_date = date(2023, 11, 24)
        delta = black_friday_date - today
        return delta.days

    def get_eye_color(self, eye_color: str = "blue") -> str:
        return eye_color

    def __repr__(self) -> str:
        return f"Person: {self.name} {self.surname}"

    def __str__(self) -> str:
        return f"P: {self.name} {self.surname}"


person = Person("Giedrius", "Kuprys")
person2 = Person("Marius", "Karpis")

print(person.greet())
print(person2.greet())
print(person.description)
print(Person.description)
print(person.calculate_days_left_till_black_friday())
print(person.get_eye_color("brown"))
print(person.get_eye_color())
print(person)
