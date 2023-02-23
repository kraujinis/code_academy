list_names = ["Giedrius", "Antanas", "Darius", "Marius", "Bob", "Johannes"]

names = []

for name in list_names:
    if len(name) >= 5:
        names.append(name)

print(f'Names_list_one : {names}')

names_list = [name for name in list_names if len(name) >= 5]

print(f'Names_list_two : {names_list}')
