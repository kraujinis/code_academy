# Create a list of letters and generate 5 diferent words for 5 different lists.
# (A word must the size between 5 and letters)
# Then count how many each letters are in those words.
# Return answer as a dictionary. {'letter': count}
# And all words sorted in one list.

import random

# START 1 --> create 5 lists with diferent lenght of 5 words

letter_list = [
                'a', 'b', 'c', 'd', 'e', 'f',
                'g', 'h', 'i', 'j', 'k', 'l',
                'm', 'n', 'o', 'p', 'q', 'r'
                ]


letter_list_1 = []
letter_list_2 = []
letter_list_3 = []
letter_list_4 = []
letter_list_5 = []
unique_letter = []

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
# print(letter_list_1)
# print(letter_list_2)
# print(letter_list_3)
# print(letter_list_4)
# print(letter_list_5)
# --> END 1

# START 2 --> then count how many each letters are in those words.
# Return answer as a dictionary. {'letter': count}

list_all_words = [''.join(letter_list_1)] + [''.join(letter_list_2)] + [''.join(letter_list_3)] + [''.join(letter_list_4)] + [''.join(letter_list_5)]

print(list_all_words)

for word in list_all_words:
    unique_word = set(word)
    unique_letter.append(list(unique_word))
    

print(set(list_all_words))
print("unique  ", unique_letter)
i: int = 0
for letter in unique_letter:
    print("len", len(unique_letter))
    print("for ", letter)
    for word, x in unique_letter:
    
        print()
        print(f"letter{str(i)}: {x} = ", word.count(x))
        
        
    # for word in list_all_words:
    #     i += 1
    #     print(f"letter{str(i)}: {x} = ", word.count(x))
        

# --> END 2