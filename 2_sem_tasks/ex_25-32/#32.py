# 32
'''
Используем array и numpy.
а) Дан массив размера  N. Найти количество участков, на которых его элементы возрастают.
б) Дана квадратная матрица  A порядка  M.
   Найти сумму элементов каждой её диагонали, параллельной главной.
'''

# а)
from numpy import *


def count_increasing(arr):
    arr_dif = diff(arr)  # Вычисляем разности между соседними элементами
    arr_dif = where(arr_dif > 0, 1, 0)
    id_0 = where(arr_dif == 0)[0]
    list_dif = split(arr_dif[arr_dif], id_0)
    # list_dif = split(arr_dif[arr_dif != 0], id_0 - arange(len(id_0)))
    count = len([arr for arr in list_dif if 1 in arr])
    # list_dif = [el for el in ''.join(list(map(str, arr_dif))).split('0') if el != '']
    return count


l = array([2, 1, 2, 3, 2, 5, 4, 6, 7, 8, 1])

print(f"Исходный массив: {l}")
print(f"Кол-во участков, элементы которых расположены в порядке возрастания: {count_increasing(array(l))}")


# б)
from random import *


def summ_diag(A):
    M = len(A)
    sum_l = []

    for i in range(-M + 1, M):
        sum_l.append(sum(A.diagonal(offset=i)))

    return sum_l


M = randint(3, 6)
A = array([[randint(1, 10) for el in range(M)] for row in range(M)])

print(f"\nМатрица: \n{A}")
print(f"Список сумм диагоналей, //-ных главной: {summ_diag(A)}")