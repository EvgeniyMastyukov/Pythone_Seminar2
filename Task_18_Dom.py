# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов
#  на указанных позициях. Позиции хранятся в файле file.txt в  одной строке одно число.

num = int(input('Введите число N:  '))
col = list(range(-num, num + 1))
print(col)
data = open('file.txt', 'w')
for i in range(num*2+1):
    data.writelines(f'{i}\n')
data.close()
data = open('file.txt', 'r')
for e in data:
   print(e)
data.close()    



