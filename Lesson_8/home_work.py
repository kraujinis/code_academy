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

for _ in range(0, 5):   # create first loop of 5 for make 5 words in list
    letter_random = random.sample(letter_list, random.randint(5, 15))   # take random 5 letters from list
    letter_list_1.append(''.join(letter_random))   # join and append letters to list

    if len(letter_list_1) >= 5:   # checking if list lenght is 5
        for _ in range(0, 5):
            letter_random = random.sample(letter_list, random.randint(5, 15))
            letter_list_2.append(''.join(letter_random))

        if len(letter_list_2) >= 5:
            for _ in range(0, 5):
                letter_random = random.sample(letter_list, random.randint(5, 15))
                letter_list_3.append(''.join(letter_random))

            if len(letter_list_3) >= 5:
                for _ in range(0, 5):
                    letter_random = random.sample(letter_list, random.randint(5, 15))
                    letter_list_4.append(''.join(letter_random))

                if len(letter_list_4) >= 5:
                    for _ in range(0, 5):
                        letter_random = random.sample(letter_list, random.randint(5, 15))
                        letter_list_5.append(''.join(letter_random))

# START 2 --> then count how many each letters are in those words.
# Return answer as a dictionary. {'letter': count}

list_all_words_joined = [ 
                        ''.join(letter_list_1) + ''.join(letter_list_2)
                        + ''.join(letter_list_3) + ''.join(letter_list_4)
                        + ''.join(letter_list_5)
                        ]

# print(" List all words joined: ", list_all_words_joined)

for letter in list_all_words_joined:    # take from list all unique letters
    unique_letter_set = set(letter)

# print("Unique letter set: ", unique_letter_set)

# extract unique letters and count them
for letter_x in unique_letter_set:
    unique_letter_dictionary[letter_x] = list_all_words_joined[0].count(letter_x)   # create dictionary 

print("Counted letter dictionary: ", unique_letter_dictionary)
print("Sum of all letters in lists: ", sum(unique_letter_dictionary.values()))

# --> END 2