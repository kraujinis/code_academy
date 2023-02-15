# Create a list of letters and generate 5 diferent words for 5 different lists.
# (A word must the size between 5 and letters)
# Then count how many each letters are in those words.
# Return answer as a dictionary. {'letter': count}
# And all words sorted in one list.

import random

# START 1 --> create 5 lists with diferent lenght of 5 words

letter_list = [
                'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',
                'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
                's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
                ]

letter_list_1 = []
letter_list_2 = []
letter_list_3 = []
letter_list_4 = []
letter_list_5 = []
unique_letter_dictionary = {}

'''
Create 5 lists with diferent lenght of 5 words
    1) Loop for of 5, create 5 lists
        2) Take a random letter ramdomly from 5-15 letter from {letter_list} and join to word
        
        3) If the length of lists items is 5 make list and go to create next
'''

for _ in range(0, 5):
    letter_list_1.append(''.join(random.sample(letter_list, random.randint(5, 15))))

    if len(letter_list_1) >= 5:
        for _ in range(0, 5):
            letter_list_2.append(''.join(random.sample(letter_list, random.randint(5, 15))))

        if len(letter_list_2) >= 5:
            for _ in range(0, 5):
                letter_list_3.append(''.join(random.sample(letter_list, random.randint(5, 15))))

            if len(letter_list_3) >= 5:
                for _ in range(0, 5):
                    letter_list_4.append(''.join(random.sample(letter_list, random.randint(5, 15))))

                if len(letter_list_4) >= 5:
                    for _ in range(0, 5):
                        letter_list_5.append(''.join(random.sample(letter_list, random.randint(5, 15))))

# START 2 --> then count how many each letters are in those words.
# Return answer as a dictionary. {'letter': count}

all_words_list_joined = ''.join(letter_list_1) + ''.join(letter_list_2) + ''.join(letter_list_3) + ''.join(letter_list_4) + ''.join(letter_list_5)

all_words_list = letter_list_1 + letter_list_2 + letter_list_3 + letter_list_4 + letter_list_5

# print(" List all words joined: ", all_words_list_joined)

unique_letter_set = ''.join(set(all_words_list_joined))

# print("Unique letter set: ", unique_letter_set)

"""
Create a dictionary:
    1) Take one letter {letter_x} from joined {unique_letter_set}
    2) Count how many times that letter appears in {all_words_list_joined}
"""
for letter_x in unique_letter_set:
    unique_letter_dictionary[letter_x] = all_words_list_joined.count(letter_x)

print("Counted letter dictionary: ", unique_letter_dictionary)
print("Sum of all letter in lists: ", sum(unique_letter_dictionary.values()))
print("All words from lists to one list: ", all_words_list)

# --> END 2