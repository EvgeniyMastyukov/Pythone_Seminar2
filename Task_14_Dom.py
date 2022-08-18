# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример: # - 6782 -> 23
          # - 0,56 -> 11

num = float(input('Введите число: '))
num1 = str(num)
length = len(num1)
print(length)
num = num * 10**(length)
print(num)
sum = 0
while (num != 0):
    sum += num%10  #4, 3, 2,  1
    num //= 10    #123, 12, 1, 0 
   
print(sum)