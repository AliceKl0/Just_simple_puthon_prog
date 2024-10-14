# 25
'''
Класс – комплексное число.
Методы – сумма, разность, произведение комплексных чисел.
'''


class ComplexNumber:
    """
    Класс комплексных чисел.
    Сложение, вычитание умножение.
    """
    def __init__(self, real, im):
        self.real = real
        self.im = im

    def summ(self, other):
        real_part = self.real + other.real
        im_part = self.im + other.im
        return ComplexNumber(real_part, im_part)

    def sub(self, other):
        real_part = self.real - other.real
        im_part = self.im - other.real
        return ComplexNumber(real_part, im_part)

    def mul(self, other):
        real_part = self.real * other.real - self.im * other.im
        im_part = self.real * other.im + self.im * other.real
        return ComplexNumber(real_part, im_part)


print(ComplexNumber.__doc__)

cn_1 = ComplexNumber(2, 3)
cn_2 = ComplexNumber(0, 1)

s = cn_1.summ(cn_2)
print(f"Сумма: {s.real} + {s.im}i")

d = cn_1.sub(cn_2)
print(f"Разность: {d.real} + {d.im}i")

m = cn_1.mul(cn_2)
print(f"Произведение: {m.real} + {m.im}i")