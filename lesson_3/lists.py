my_list = [1, 2, 5, 6, 8, 5, 5]

#my_list[1] += 50 # prie 1 elemento pridedame 50
new_list = []

for i in my_list:
    i += 50 # prie my_list kiekvieno elemento pridedama 50
    new_list.append(i)  # i reikšmės įrašomos į naują sąrašą


print(my_list)  # senas sąrašas
print(new_list) # naujas sąrašas
