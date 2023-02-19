#Create a dictionary with 5 kay:value pairs, Keys must be strings,
#  values must be numbers double digits(int)
# Use dictionary comprehension to create a new dictionary where keys are
#  the same keys as your currents ones just all cappital letters, 
# and values are in reverse order. (25 -> 52)

my_dictionary = {'Amba': 14, 'bamba': 24, 'curent': 35, 'dady': 45, 'Elvis': 58}

new_dictionary = {name.upper(): int(str(number)[::1]) for (name, number) in my_dictionary.items()}

print(new_dictionary)