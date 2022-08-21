# Реализуйте алгоритм перемешивания списка.

import random
col = [1, 2, 3, 4, 5]
print(col)
# random.shuffle(col)             встроенная функция random.shuffle
# print(col) 

def shuffle_list(list):
    length = len(list)
    for i in range(0,length):
        random_index = random.randint(0,length-1)
        temp = list[i]
        list[i] = list[random_index]
        list[random_index] = temp
    return list

print(shuffle_list(col))







