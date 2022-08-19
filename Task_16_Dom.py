#  Реализуйте алгоритм сортировки списка
# Первый вариант - Пузырьковый метод - через while, сравнение предыдущего со следующем элементом, больший отправляется правее, такие итерации до size>1 
# col = input('Введите элементы списка: ').split(",")
# print(col)
# print(type(col[0]))
# for i in range(len(col)):
#     col[i] = int(col[i])
# print(col)
# print(type(col[0]))

# size = len(col)
# while (size > 1):
#     i = 0
#     while (i < size-1):
#         if (col[i] > col[i + 1]):
#             temp = col[i]
#             col[i] = col[i+1]
#             col[i+1] = temp
#         i+=1
#     size -=1
# print(col)

# Второй метод -  Метод вставок.  min или max кладется в конец строки списка.
# col = [10, 8, 5, 0, -1, 3]
# print(col)
# def findImax(lis, length):
#     imax = 0
#     for i in range(length):
#         if lis[imax] < lis[i]:
#             imax = i
#     return imax

# size = len(col)
# while (size > 1):
#     imax = findImax(col, size)
#     temp = col[imax]
#     col[imax] = col[size-1]
#     col[size-1] = temp
#     size -= 1
# print(col)

# Третий метод - метод выбора min или max  через два цикла for (внешний и внутренний). min или max кладется в начало строки списка.
# col = [10, 8, 5, 0, -1, 3]
# print(col)
# for i in range(len(col) -1):
#     minIndex = i
#     for j in range(i+1,len(col)):
#         if col[j] < col[minIndex]:
#             minIndex = j
#     temp = col[minIndex]
#     col[minIndex] = col[i]
#     col[i] = temp
# print(col)

# Четвертый способ - пузырьковый метод через два цикла for
col = [10, 8, 5, 0, -1, 3]
print(col)
for i in range(len(col) - 1):
    for j in range(i+1, len(col)):
        if col[j] < col[i]:
            temp = col[j]
            col[j] = col[i]
            col[i] = temp
print(col)


