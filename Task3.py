# Задайте список из вещественных чисел. 
# Напишите программу, которая найдёт разницу между максимальным 
# и минимальным значением дробной части элементов.
# Пример: [1.1, 1.2, 3.1, 5, 10.01]  =>  0.19

import random

print('Ведите число элементов: ')
N = int(input())
numbers = []
for i in range(N):
    numbers.append(round(random.uniform(1, 12), 2))
print(numbers)

min = 1.0
max = 0.0
for element in numbers:
    num2 = element - int(element)
    if num2 < min:
        if num2 != 0:
            min = num2
    if num2 > max:
        max = num2


print('min =', round(min, 2))
print('max =', round(max, 2))
print('difference', round(max-min, 2))
