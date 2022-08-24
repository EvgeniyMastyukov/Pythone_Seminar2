# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, 
# стоящих на нечётной позиции. Пример:  [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

# col = list(range(5,10))
# print(col)
# sum = 0
# for i in range(len(col)):
#     if i%2 != 0:
#         sum += col[i]

# print(sum)

users_arr = list(range(5,10))
print(users_arr)
sum_result = 0
for num in users_arr[1::2]:
    sum_result += num
print(sum_result)
print(
f"Результат без использования генератора списка: {sum_result}\n"
f"Результат с использованием генератора списка: {sum(users_arr[1::2])}"
)
