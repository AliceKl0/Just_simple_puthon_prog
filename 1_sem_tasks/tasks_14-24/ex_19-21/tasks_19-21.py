# 19
'''
Дано целое число  K  ( 0<K<10 ) и текстовый файл, содержащий более  K  строк.
Создать новый текстовый файл, содержащий  K  последних строк исходного файла.
'''

file_1 = open('file_1.txt', 'r')
s_1 = file_1.readlines()

k = int(input("Введите целое число 0 < K < 10: "))

s_1 = s_1[len(s_1) - k::]
file_2 = open('file_2.txt', 'w')

for row in s_1:
    file_2.write(row)


# 20
'''
Дан файл  f , компоненты которого являются действительными числами. Найти произведение компонент файла.
'''

# Думаю, возможны два основных случая. Первый: каждое число на новой строке
from math import prod

file_3 = open('file_3.txt', 'r')
s_1 = file_3.readlines()
s_1 = [float(i) for i in s_1]

a = prod(s_1)

print("Произведение: %.2f" % a)

# Второй: в строку через пробел
file_4 = open('file_4.txt', 'r')
s_1 = file_4.read()
s_1 = s_1.split()
s_1  = [float(i) for i in s_1]

a = prod(s_1)

print("Произведение: %.2f" % a)


# 21
'''
В первом файле хранится  k  матриц размерности  m×n , во втором —  l  матриц размерности  m×n . 
Те матрицы из первого файла, у которых  a00=0 , перенести в конец второго файла. Вывести на экран содержимое обоих файлов.
'''

# Матрицы в файлы можно записать посредством randint
'''
from random import *

k = randint(2, 5)
l = randint(1, 4)
m = randint(2, 5)
n =  randint(2, 5)

file_5 = open('file_5.txt', 'a+')

for count in range(k):
    file_5.write('\n')
    for row in range(m):
        file_5.write('\n' + ' '.join([str(randint(0,23)) for i in range(n)]))

file_6 = open('file_6.txt', 'a+')

for count in range(l):
    file_6.write('\n')
    for row in range(m):
        file_6.write('\n' + ' '.join([str(randint(0,23)) for i in range(n)]))
'''

file_5 = open('file_5.txt', 'r')
s_1 = [list(map(int, line.split())) for line in file_5]
s_matrix = []
matrix_1 = []

for row in s_1:
    if row == []:
        s_matrix.append(matrix_1)
        matrix_1 = []
    else:
        matrix_1.append(row)

with open('file_6.txt', 'a') as file_6:
    for matrixx in s_matrix:
        if matrixx[0][0] == 0:
            file_6.write('\n')

            for row in matrixx:
                row = [str(i) for i in row]
                file_6.write('\n' + ' '.join(row))

file_6.close()

file_6 = open('file_6.txt', 'r')
s_2 = [list(map(int, line.split())) for line in file_6]

print("\nИсходный файл:" + '\n')
for row in s_1:
    print(' '.join([str(i) for i in row]))

print("\nРезультат в другом файле:" + '\n')
for row in s_2:
    print(' '.join([str(i) for i in row]))