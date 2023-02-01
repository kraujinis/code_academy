my_list = [1, 2, 5, 6, 8, 5, 5]

#my_list[1] += 50 # prie 1 elemento pridedame 50
new_list = []

for i in my_list:
    i += 50
    new_list.append(i)


print(my_list)
print(new_list)