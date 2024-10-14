# 26
'''
Класс Point.
Задаются декартовы координаты  x, y.

Методы:
- вывод координат точки на экран
- расстояние от начала координат до точки
- переместить точку на плоскости на вектор (a,b)

Свойства:
- умножение координаты точки на скаляр
'''

from math import *


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

    def distance_from_0(self):
        return sqrt(self.x ** 2 + self.y ** 2)

    def move(self, x_b, y_b):
        return Point(self.x + x_b, self.y + y_b)

    @property
    def mul_coord(self):
        pass

    @mul_coord.setter
    def mul_coord(self, k):
        self.x *= k
        self.y *= k


a = Point(1, 3)

print(f"Текущие координаты т-ки: {a.__str__()}")

a.mul_coord = 2
print(f"Умножим координаты т-ки на 2: {a.__str__()}")

a = a.move(3, 4)
print(f"Переместим т-ку на вектор (3, 4): {a.__str__()}")

s = a.distance_from_0()
print("Расстояние от (0, 0) до т-ки: %.2f" % s)

a.mul_coord = 2
print(f"Умножим координаты т-ки на 2: {a.__str__()}")