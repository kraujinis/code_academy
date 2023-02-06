# Write python program that asks user to enter name, surname, age. Put these values into a dictionary and print dictionary

name = input("Pease input you name: ")
surname = input("Please input you surname: ")
age = int(input("Please input you age: "))

my_dict_keys = ['name', 'surname', 'age']
my_dict_values = [name, surname, age]

my_dict = dict(zip(my_dict_keys, my_dict_values))
print(my_dict)