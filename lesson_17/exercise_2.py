# Create the instance attributes fullname and email in the Employee class.
# Given a person's first and last names:
# Form the fullname by simply joining the first and last name together, separated by a space.
# Form the email by joining the first and last name together with a . in between, and follow 
# it with @company.com at the end. Make sure the entire email is in lowercase.

class Employee:

    def __init__(self, name: str, surname: str):
        self.name: str = name
        self.surname: str = surname

    def fullname(self) -> str:
        return f"{self.name} {self.surname}"

    def mail(self) -> str:
        make_mail = f'{self.name}.{self.surname}@company.com'
        return make_mail.lower()


employee = Employee("John", "Doe")

print(employee.fullname())
print(employee.mail())