#22
'''
а) Напишите программу, которая проверяет введенный пользователем email на соответствие стандарту.
б) Дан текстовый файл. Найдите все email-адреса в этом файле и выведите их на экран.
'''

from re import *

# а)
n = input("Введите предполагаемый email: ")

expr = search(r'[a-zA-Z0-9!#$%&;+=?_{ }½~]+@[a-zA-Z0-9]+[.]([a-zA-Z]{2,})', n)

if expr:
    print("Да, это email!")
else:
    print("Данная строка не представляет собой email.")

# б)

file_e = open('file_email.txt', 'r')
s_e = file_e.readlines()

for em in s_e:
    print(em)

print("\nРезультат:" + '\n')

for em in s_e:
    expr = search(r'[a-zA-Z0-9!#$%&;+=?_{ }½~]+@[a-zA-Z0-9]+[.]([a-zA-Z]{2,})', em)

    if expr:
        print(em)

# 23

# а)
'''
Пользователь вводит число. Если число отрицательное, выводится сообщение «Число должно быть положительным». 
Если число равно нулю, выводится сообщение «Число не может быть нулевым». 
В остальных случаях выводится сообщение «Число введено корректно». 
Используйте исключения ValueError и ZeroDivisionError.
'''

n = float(input("Введите число: "))

if n < 0:
    raise ValueError("Число должно быть положительным")
elif n == 0:
    raise ZeroDivisionError("Число не может быть нулевым")
else:
    print("Число введено корректно")

# б)
'''
Пользователь вводит свой возраст. Если возраст меньше 18 лет, выбрасывается исключение «Несовершеннолетний пользователь». 
Если возраст больше 100 лет, выбрасывается исключение «Неверный возраст». 
В остальных случаях выводится сообщение «Возраст введен корректно».
'''

class UnderAgeError(Exception):
    pass

class OverHundredError(Exception):
    pass

age = int(input("Введите свой возраст: "))

if age < 18:
        raise UnderAgeError("Несовершеннолетний пользователь")
elif age > 100:
        raise OverHundredError("Неверный возраст")
else:
        print("Возраст введен корректно")

# в)
'''
Пользователь вводит число. Если число отрицательное, используя инструкцию assert, 
проверить условие и вывести сообщение «Число должно быть положительным». 
В остальных случаях выводится сообщение «Число введено корректно».
'''

n = float(input("Введите число: "))

assert n >= 0, "Число должно быть положительным"

print("Число введено корректно")

# 24

# а)
'''
Counter: Подсчитать количество повторений каждого элемента в списке и вывести на экран.
'''

from random import *
from collections import *

s = [randint(-100, 100) for i in range(randint(50, 100))]

print(f"Исходный список: {s}" + '\n')

num_counter = Counter(s)

for i in num_counter:
    print(f"Количество чисел {i} = {num_counter[i]}")

# б)
'''
defaultdictr: Написать функцию, которая принимает на вход список слов и возвращает словарь, 
в котором каждое слово является ключом, а значение — количество раз, которое это слово встречается в списке.
'''

from collections import *

s = ['один', 'два', 'три', 'четыре', 'два', 'пять', 'четыре', 'шесть']

def defaultdictr(s):
    str_count  = Counter(s)

    return str_count

print(dict(defaultdictr(s)))

# в)
'''
enum: Создать перечисление для дней недели и написать функцию, 
которая принимает на вход день недели и выводит его название на русском языке.
'''

import enum

class Week_days(enum.Enum):

    Monday = 'Понедельник'
    Tuesday = 'Вторник'
    Wednesday = 'Среда'
    Thursday = 'Четверг'
    Friday = 'Пятница'
    Saturday = 'Суббота'
    Sunday = 'Воскресенье'

n = input("Введите день недели на английском языке: ")

for i in Week_days:
    if i.name == n:
        print(f"День недели на русском языке: {i.value}")

        break

# г)
'''
frozenset: Напишите программу, которая принимает на вход два множества и выводит их пересечение в виде frozenset.
'''

a = frozenset('12345678')
b = frozenset('02369')

print(f"Множество a: {a}" + f"\nМножество b: {b}")

c = a & b # a.intersection(b)

print(f"\nПересечение множеств a и b: {c}")

# д)
'''
namedtuple: Написать функцию, которая принимает список кортежей (имя, фамилия, возраст) 
и возвращает список объектов класса namedtuple с соответствующими полями.
'''

from collections import *

list_tuple = [('Василий', 'Васильев', 23), ('Егор', 'Егоров', 21), ('Анна', 'Аннушкина', 20), ('Пётр', 'Петров', 25)]
information = namedtuple('information', 'name surname age')
data_base = []

for index in range(len(list_tuple)):
    data_base.append(information(name=list_tuple[index][0], surname=list_tuple[index][1], age=list_tuple[index][2]))

print(f"Список: {data_base}")

# е)
'''
OrderedDict: Создать упорядоченный словарь, 
содержащий информацию о количестве продаж каждого товара в интернет-магазине за последний месяц.
'''

from collections import *
from random import *

products_count_sale = OrderedDict()

for index in range(randint(10, 30) + 1):
    products_count_sale[f"товар_{index}"] = randint(10, 100)

print(f"Упорядоченный словарь: \n{products_count_sale}")