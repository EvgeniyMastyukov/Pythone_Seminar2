# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов. 
# Пример: для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] 
# [Негафибоначчи]
num = int(input('Enter number Negafibonacci: '))
numbers = []           #инициализация первого списка
numbers.append(0)
numbers.append(1)
for i in range(2,num +1):
    numbers.append((numbers[i-1] + numbers[i-2]))

numbers_neg = []                  #инициализация второго списка с отрицательными элементами
numbers_neg.append(1)
numbers_neg.append(1)
for i in range(2,num):
    numbers_neg.append((numbers_neg[i-1] + numbers_neg[i-2]))
for i in range(len(numbers_neg)):  #Меняем знак у элемента с нечетным индексом               
    numbers_neg[i] = ((-1)**i) * numbers_neg[i]
    
numbers_neg.reverse()               # Разворот второго списка
res = numbers_neg + numbers         # Слияние двух списков в один
print(numbers)
print(numbers_neg)
print ('negafibonacci = ', res)




