# Написать программу, которая принимает на вход число N и выдает последовательность из N членов.
# Пример, Для N = 5: 1, -3, 9, -27, 81

num = int(input('Введите число N членов последовательности: '))
# col = range(1, num)
# print(col)
# order = list(range(num))
# print(order)
# order[0] = 1
# for i in col:
#     order[i] = order[i-1] * 3
#     print(order[i])

# for i in range(num):
#    if i %2 != 0:
#       order[i] = order[i] * -1

# print(order)

for i in range(num):
   if i%2 == 0:
      print(3 ** i, end="  ")
   else:
      print(-3 ** i, end="  ")   