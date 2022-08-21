#  Задайте словарь из n элементов, где ключ = n, а значение = (1 + 1/n)^n и выведите на
#  экран. Пример: Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}
n = int(input('Введите n элеменетов словаря: '))
dictionary = {}
print(dictionary)

for i in range(1,n+1):
    dictionary[i] = round((1 + 1/n)**n,3)
    n += 1
print(dictionary)
