'''#14 Ф-ция, вычисляющая ср. арифм. и ср. геом.
       2-х положит. чисел'''

x = float(input("Введите положительное число: "))
y = float(input("Введите положительное число: "))

def Mean(x, y):
        AMean = (x + y) / 2
        GMean = x * y

        return AMean, GMean

ar, gr = Mean(x, y)

print("Ср. арифм. = %.2f" % ar, '\nСр. геом. = %.2f' % gr)


'''#15 Удалить элемент из матрицы по номеру'''

from random import *

m = int(input("Введите целое значение M: "))
n = int(input("Введите целое значение N: "))
k = int(input("Введите целое значение K: "))
l = int(input("Введите целое значение L: "))
s = [[randint(-1000,1000) for i in range (n)] for j in range (m)]

print (s)

def RemoveRowCol(m, n, k, l, s):

    if k <= m and l <= n:
        s[k-1].pop(l-1)

    return s

print (RemoveRowCol(m, n, k, l, s))


'''#16
a) На вход ФИО (отчество необязательно). Вывод: Ф + И + О
б) Список чисел + возможность преобразования
в) Сумма неопределённого количества аргументов
г) Два словаря, возвращаем словарь с совпадающими ключами'''

#а)

a = input("Введите имя: ")
b = input("Введите фамилию: ")
c = input("Введите отчество: ")

def FIO(a, b, c):

    if c != '':
        return b + ' ' + a + ' ' + c
    else:
        return b + ' ' + a

print(FIO(a, b, c))

#б)

print ("Список возможных команд: +1, *2")

def spisok():
    s = []
    move = ['+1', '*2']
    a = input("Введите значение элемента: ")

    while a != '':
        s.append(float(a))
        a = input("Введите значение элемента: ")

    s_1 = s.copy()
    b = input("Введите команду из списка: ")

    if b in move:
        if b == '+1':
            s = [i+1 for i in s]
        elif b == '*2':
            s = [i*2 for i in s]

    return s_1, s

st, end = spisok()

print (st, '\n', end)

#в)

def summa():
    s = 0
    a = input("Введите значение a: ")

    while a != '':
        s += float(a)
        a = input("Введите значение a: ")

    return s

print(summa())

#г)

alph1 = {'Вася': 10, 'Лена': 12, }
alph2 = {'Игорь': 14, 'Марина': 7, 'Вася': 15}

def alph(alph1, alph2):
    alph3 = {k: [alph1.get(k, 0), alph2.get(k, 0)] for k in set(alph1) | set(alph2) if
             k in set(alph1) and k in set(alph2)}

    return alph3

print (alph(alph1, alph2))


'''#17 Fact и Fact2'''

def Fact(n):
    return 1 if n <= 1 else n * Fact(n - 1)

def Fact2(n):
    return 1 if n <= 1 else n * Fact2(n - 2)

n = int(input("Введите целое положительное число: "))

print('n! = ', Fact(n), '\nn!! = ', Fact2(n))