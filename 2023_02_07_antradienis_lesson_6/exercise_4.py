# Write a small calculator application, that allows user to enter 
# two numbers and a symbol, given and then do the operation and 
# print an answer.

numbers = input("Please enter first digit, and simbol, and second digit: ").split()

number_1 = int(numbers[0])
number_2 = int(numbers[2])
symbol = str(numbers[1])

symbol_list = ['+', '-', '*', '/']  # tikrinama ar yra tinkami simboliai

if symbol in symbol_list:
    if symbol == '/':
        answer = number_1 / number_2
    if symbol == '*':
        answer = number_1 * number_2
    if symbol == '-':
        answer= number_1 - number_2
    if symbol == '+':
        answer = number_1 + number_2


print(f"You entered {number_1} {symbol} {number_2}. Answer: {answer}")

