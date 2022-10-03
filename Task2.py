# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример: [2, 3, 4, 5, 6]  =>  [12, 15, 16];  [2, 3, 5, 6]  =>  [12, 15]

from random import randint

print('Ведите число элементов: ')
N = int(input())
numbers = []
for i in range(N):
    numbers.append(randint(1, N))
print(numbers)

x = 0
y = N - 1
new = []
while x <= y:
    res = numbers[x] * numbers[y]
    x += 1
    y -= 1
    new.append(res)
print(new)
 