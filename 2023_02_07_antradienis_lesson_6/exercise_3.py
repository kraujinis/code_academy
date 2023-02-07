# allow user to enter two numbers, print out which one 
# is higher than the other, or are they equal?

numbers = input("Please enter two integer numbers: ").split()

number_1 = int(numbers[0])
number_2 = int(numbers[1])

if number_1 > number_2:
    print(f"number 1: {number_1} > number 2: {number_2}")
elif number_1 < number_2:
    print(f"number 1: {number_1} < number 2: {number_2}")
else:
    print(f"number 1: {number_1} == number 2:{number_2}")
