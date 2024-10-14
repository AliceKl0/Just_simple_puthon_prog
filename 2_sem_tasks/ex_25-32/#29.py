# 29
'''
а) Ф-цией map утроить все числа из заданного списка
б) Сгенерировать список целых чисел, отобрать нечётные и упорядочить их по убыванию.
   С помощью reduce найти их произведение.
'''

# а)
from random import *

l = [randint(-0, 10) for _ in range(randint(3, 6))]
l_1 = list(map(lambda x: x * 3, l))

print(f"Исходный список чисел: {l}")
print(f"Результат (утроили каждый элемент): {l_1}\n")

# б)
from functools import reduce

s = [randint(-0, 10) for _ in range(randint(3, 6))]

print(f"Исходный список чисел: {s}")

s = sorted(list(filter(lambda x: x % 2 != 0, s)), key=lambda x: x, reverse=True)

print(f"Результат: {s}")

a = reduce(lambda x, y: x * y, s)

print(f"Произведение полученного списка чисел: {a}")