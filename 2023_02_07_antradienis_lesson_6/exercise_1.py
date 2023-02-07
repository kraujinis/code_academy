# Let user enter name, surname and age. Print if user is allowed to enter an online casino or not.
#  21 is the age cap.

name = input("Please enter you name: ")
age = int(input("Please enter you age: "))

if age >= 21:
    print(f"{name} you age is greather then 21 and you can get in!")
else:
    print(f"{name} you age less then 21 and not alowed to get in ")