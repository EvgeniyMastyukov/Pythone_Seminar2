# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным
#  и минимальным значением дробной части элементов. Пример:  [1.1, 1.2, 3.1, 5, 10.01] => 0.19

numbers = ['1.1', '1.2', '3.1', '5.1', '10.01']
print(numbers)
num = []                        # Иницировали новый список num
for i in numbers:
    num.append(i.split('.'))    # добавили в список num элементы - списки 
print(num)    
for el in range(len(numbers)):  
    num[el] = num[el].pop()   # удалили целую часть 
    num[el] = '0.' + num[el]   # добавили '0.' к целой части.
    num[el] = float(num[el])   # элементы списка перевели во float
result = max(num) - min(num)
print(num) 
print(result)



# Второй вариант с использованием модуля math и Функции modf() => вывод: кортеж (дробная часть, целая)
   
# import math
# my_list = [1.1, 1.2, 3.1, 5.2, 10.01]
# new_list = []
# for i in my_list:
#     new_list.append(round(math.modf(i)[0], 2))
# y = max(new_list)
# o = min(new_list)
# print(o)
# print(y - o)

# print(new_list)
