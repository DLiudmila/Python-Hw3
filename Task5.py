# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример: для k = 8 список будет выглядеть так: 
# [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

print('Введите число: ')
num = int(input())
one = 0
two = 1
sum = 0
list = [None] * (2*num + 1)

for i in range(1, num):
    sum = one - two
    list[num-1 - i] = sum
    one = two
    two = sum
    
list[num - 1] = 1
list[num] = 0
list[num + 1] = 1

one = 0
two = 1
sum = 0
for i in range(1, num):
    sum = one + two
    list[num+1 + i]  = sum
    one = two
    two = sum
    
print(list)