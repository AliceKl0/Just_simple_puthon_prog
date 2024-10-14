# 30
'''
а) Декоратор, который будет выводить время выполнения функции и сохранять его в файл.
б) Декоратор, который будет принимать аргументы и передавать их в функцию
   в качестве позиционных параметров с заданными значениями по умолчанию.
'''

# а)
from time import *


def measure_time(func):
    def wrapper():
        start_time = time()
        func()
        end_time = time()

        dif_time = end_time - start_time

        with open('time.txt', 'a') as time_file:
            time_file.write(f"Время выполнения ф-ции: {dif_time}\n")

    return wrapper


@measure_time
def func():
    for _ in range(200):
        print('Error')


func()


# б) Ф-ция получает значения по умолчанию (1 и 2). Выводится последовательность переданных аргументов.


def dec_with_arg(arg_1, arg_2):
    def dec(func):
        def wrapper(*args, **kwargs):
            result = func(arg_1, arg_2, *args, **kwargs)
            return result
        return wrapper
    return dec


@dec_with_arg(1, 2)
def func(a, b, *c):
    print(a, b, *c)


print("\nРезультат:")

func(3, 4, 5)