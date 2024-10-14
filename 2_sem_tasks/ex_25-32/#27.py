# 27
'''
Класс Figure.
Дочерние классы: Rectangle, Circle, Triangle

Методы:
- вычисление площади
- вычисление периметра
- вывод информации о фигуре на экран (только у Figure)
'''

from math import *


class Figure:
    def __init__(self, name):
        self.name = name

    def p(self):
        pass

    def s(self):
        pass

    def info(self):
        return f"Название фигуры: {self.name} \nПлощадь: {self.s()} \nПериметр: {self.p()}"


class Rectangle(Figure):
    def __init__(self, name, side_1, side_2):
        super().__init__(name)
        self.side_1 = side_1
        self.side_2 = side_2

    def p(self):
        # super().p()
        return (self.side_1 + self.side_2) * 2

    def s(self):
        # super().s()
        return self.side_1 * self.side_2


class Circle(Figure):
    def __init__(self, name, R):
        super().__init__(name)
        self.R = R

    def p(self):
        # super().p()
        return 2 * pi * self.R

    def s(self):
        # super().s()
        return pi * self.R ** 2


class Triangle(Figure):
    def __init__(self, name, side_1, side_2, side_3):
        super().__init__(name)
        self.side_1 = side_1
        self.side_2 = side_2
        self.side_3 = side_3

    def _is_valid_triangle(self):
        return self.side_1 + self.side_2 > self.side_3 and self.side_1 + self.side_3 > self.side_2 \
               and self.side_2 + self.side_3 > self.side_1

    def p(self):
        # super().p()
        return self.side_1 + self.side_2 + self.side_3 if self._is_valid_triangle() else 0

    def s(self):
        # super().s()
        p = self.p() / 2
        return sqrt(p * (p - self.side_1) * (p - self.side_2) * (p - self.side_3)) if self._is_valid_triangle() \
            else 0


r_c_t = [Rectangle('Прямоугольник', 2, 3), Circle('Круг', 5), Triangle('Треугольник', 2, 3, 4)]

for figure in r_c_t:
    print(figure.info() + '\n')