# Create a list of letters and generate 5 diferent words for 5 different lists.
# (A word must the size between 5 and letters)
# Then count how many each letters are in those words.
# Return answer as a dictionary. {'letter': count}
# And all words sorted in one list.
import random

letter_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
                 'l', 'm', 'n', 'o', 'p', 'q', 'r']

letter_list_1 = []
letter_list_2 = []

for _ in range(0, 10):
    for _ in range(0, 5):
        a = random.choice(letter_list)
        letter_list_1.append(a)
print(letter_list_1)      
print(letter_list_2)



