# Напишите программу, которая будет преобразовывать десятичное число в двоичное. Пример: 
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

num_dec = int(input('Enter positive number: '))
base_num = int(input('Enter base of number: '))
d10 = 1        # определяем разряд числа(единицы, сотни, тысячи)
result = 0
while num_dec > 0:
    result += num_dec % base_num * d10
    num_dec //= base_num
    d10 *= 10
print(result) 


