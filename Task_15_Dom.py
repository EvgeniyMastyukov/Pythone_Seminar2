# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример: # - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

num = int(input('Введите число N:'))
col = list(range(1, num+1))
print(col)
f = 1
count = 1
for i in range(num):
    col[i] = f * count
    count += 1
    f = col[i]    
print(col)    
    