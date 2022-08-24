# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, 
# второй и предпоследний и т.д. Пример:  [2, 3, 4, 5, 6] => [12, 15, 16];  [2, 3, 5, 6] => [12, 15]

col = list(range(5,18,2))
print(col)
size = len(col)
i = 0
if(size%2 == 0):
    while (i <= size-1):
        col[i] = col[i] * col[size-1]
        i+=1
        size-=1
        col.pop()
else:
    while (i <= size-1):
        col[i] = col[i] * col[size-1]
        i+=1
        size-=1
        if i < size:
            col.pop()

print(col)
    

