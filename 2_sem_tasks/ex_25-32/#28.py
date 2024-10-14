# 28
'''
lambda-функции

а) x + 15 и x * y
б) min и max значение в списке кортежей
в) извлечь из списка строк те, длина которых соотвествует изначально заданной
'''

# а)
add_fifteen = lambda x: x + 15

a = 10
print(f"Ф-ция add_fifteen, применяем к a = 10: {add_fifteen(a)}")


mul_y = lambda x, y: x * y

x = 2
y = 3
print(f"Ф-ция mul_y, применяем к x = 2 и y = 3: {mul_y(x, y)}\n")

# б)
from random import *

l = [tuple(randint(-10, 10) for i in range(randint(2, 5))) for tup in range(randint(2, 4))]

maxx = lambda x: max(tuple(max(tup) for tup in x))
minn = lambda x: min(tuple(min(tup) for tup in x))

print(f"Исходный список кортежей: {l}")
print(f"Max элемент: {maxx(l)}")
print(f"Min элемент: {minn(l)}\n")

# в)
from string import *

len_str = randint(3, 5)

all_symbols = ascii_uppercase + digits
l_str = [''.join(choice(all_symbols) for _ in range(randint(1, 6))) for _ in range(randint(5, 10))]

l_str_len = lambda x, y: [s for s in y if len(s) == x]

print(f"Выбранная длина строки: {len_str}")
print(f"Исходный список строк: {l_str}")
print(f"Результат: {l_str_len(len_str, l_str)}")

# Другой вариант с filter
l_str_1 = list(filter(lambda x: len(x) == len_str, l_str))

print(f"Результат_1: {l_str_1}")