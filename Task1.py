# Задайте список из нескольких чисел. Напишите программу, 
# которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример: [2, 3, 5, 9, 3]  ->  на нечётных позициях элементы 3 и 9, ответ: 12

from random import randint

print('Ведите число элементов: ')
N = int(input())
numbers = []
for i in range(N):
    numbers.append(randint(1, N))
print(numbers)
sum = 0
for i in range(len(numbers)):
    if i % 2 != 0:
        sum += numbers[i]
print(sum)        
