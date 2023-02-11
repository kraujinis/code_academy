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
letter_list_3 = []
letter_list_4 = []
letter_list_5 = []

for _ in range(0, 5):
    for _ in range(0, 5):
        a = random.sample(letter_list, 5)
    b = ''.join(a)
    letter_list_1.append(b)
    if len(letter_list_1) >= 5:
        for _ in range(0, 5):
            for _ in range(0, 5):
                a = random.sample(letter_list, 5)
            b = ''.join(a)
            letter_list_2.append(b)
        print(len(letter_list_2))

        if len(letter_list_2) >= 5:
            for _ in range(0, 5):
                for _ in range(0, 5):
                    a = random.sample(letter_list, 5)
                b = ''.join(a)
                letter_list_3.append(b)
            print(len(letter_list_3))

            if len(letter_list_3) >= 5:
                for _ in range(0, 5):
                    for _ in range(0, 5):
                        a = random.sample(letter_list, 5)
                    b = ''.join(a)
                    letter_list_4.append(b)
                print(len(letter_list_3))

                if len(letter_list_4) >= 5:
                    for _ in range(0, 5):
                        for _ in range(0, 5):
                            a = random.sample(letter_list, 5)
                        b = ''.join(a)
                        letter_list_5.append(b)
                    print(len(letter_list_3))



print(letter_list_1)      
print(letter_list_2)
print(letter_list_3)
print(letter_list_4)
print(letter_list_5)


