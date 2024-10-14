# 31
'''
а) Функция-генератор: последовательность Фибоначчи до заданного числа.
б) Функция-генератор: создает все возможные варианты расположения фотографий на стене.
в) Выражение-генератор: сумму квадратов всех чисел от 1 до 10.
г) Выражение-генератор: список всех чисел, являющихся квадратами других чисел из заданного диапазона.
'''

# а)


def fib(n):
    current, nextt = 0, 1

    while current <= n:
        yield current
        current, nextt = nextt, current + nextt


n = 30

# l = fib(n)
# print(next(l))
# ...

print(f"Последовательность Фибоначчи до {n}: ")

for numb in fib(n):
    print(numb)


# б) Будем считать, что количество фотографий не превышает количества свободных "ячеек" на стене
import itertools


def photo_pos(photos, wall_size):
    comb_list = list(itertools.permutations(photos, wall_size))

    for comb in comb_list:
        yield comb


photos = ['photo_1', 'photo_2', 'photo_3']
wall_size = 3

# positions = photo_pos(photos, wall_size)
# print(next(positions))
# ...

print("\nВарианты расположения фотограий на стене:")
for wall in photo_pos(photos, wall_size):
    print(wall)

# в)

summ = sum(x ** 2 for x in range(1, 11))

print(f"\nСумма квадратов чисел от 1 до 10: {summ}")


# г)
start_num = 4
end_num = 150

# l = (x ** 2 for x in range(start_num, end_num + 1) if x ** 2 in range(start_num, end_num + 1))
l = (x ** 2 for x in range(start_num, end_num + 1) if start_num <= x ** 2 <= end_num)

print(f"\nСписок чисел, соответствующих условию: {list(l)}")