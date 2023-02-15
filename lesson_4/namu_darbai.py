# 1 START -> Create a program which would take 5 separate sentences containing 5 words.
#       sentence reversed in input

inpt_one = input("Please write first sentence with 5 words:").split() # (str)
inpt_two = input("Please write second sentence with 5 words:").split()
inpt_three = input("Please write third sentence with 5 words:").split()
inpt_four = input("Please write fourth sentence with 5 words:").split()
inpt_five = input("Please write fifth sentence with 5 words:").split()

print("Input ->")
print('\n', inpt_one, '\n', inpt_two, '\n', inpt_three, '\n', inpt_four, '\n', inpt_five)

# -< END 1

# 2 START -> Make those sentences in separate lists and sort them out (reverse=False)

list_n_separated = [inpt_one, inpt_two, inpt_three, inpt_four, inpt_five] # list of all inputs (str)

list_one = []
list_two = []
list_three = []
list_four = []
list_five = []

for item in list_n_separated[0]:    # loop kad gražiau atrodytų sąrašas, kad būtų 5 elementai sąraše (str)
    list_one.append(item)

for item in list_n_separated[1]:
    list_two.append(item)

for item in list_n_separated[2]:
    list_three.append(item)

for item in list_n_separated[3]:
    list_four.append(item)

for item in list_n_separated[4]:
    list_five.append(item)

list_one.reverse()
list_two.reverse()
list_three.reverse()
list_four.reverse()
list_five.reverse()

print('\n', "Reversed lists -> ")
print('\n', list_one, '\n', list_two, '\n', list_three, '\n', list_four, '\n', list_five)
# -< END 2

# 3 START -> Create 5 five new lists what would contain first, second  indexed elements from those lists. (first list containing
# all first elements of those five, second list second elements and so on).
#       lists of first, second and etc item of lists

list_one_new = [list_one[0], list_two[0], list_three[0], list_four[0], list_five[0]]    # (str)
list_two_new = [list_one[1], list_two[1], list_three[1], list_four[1], list_five[1]]
list_three_new = [list_one[2], list_two[2], list_three[2], list_four[2], list_five[2]]
list_four_new = [list_one[3], list_two[3], list_three[3], list_four[3], list_five[3]]
list_five_new = [list_one[4], list_two[4], list_three[4], list_four[4], list_five[4]]

print('\n', "Lists have firsts, seconds and etc elements -> ")
print('\n', list_one_new, '\n', list_two_new, '\n', list_three_new, '\n', list_four_new, '\n', list_five_new)

# -< END 3

# 4  START  -> print the length of all list items and print the longest lenght list and shortest.

list_sum = list_one_new, list_two_new, list_three_new, list_four_new, list_five_new # again to one list (str)

list_max_min = []   # lists lenght in integers in list (int)

for item_x in list_sum:
    a = 0
    for item_y in item_x:
        a = len(item_y) + a
    list_max_min.append(a)
    
#list_max = list_max_min.index(max(list_max_min))    # find place of longest list in list_max_min list (int)
#list_min = list_max_min.index(min(list_max_min))    # find place of shortest list in list_max_min list (int)

print('\n', "Sum of all lengt of lists: ", sum(list_max_min)) # Lenght of all items in lists
print('\n', "Max lenght list: ", * list_sum[list_max_min.index(max(list_max_min))])
print(" Min lenght list: ", * list_sum[list_max_min.index(min(list_max_min))])

# -< END 4