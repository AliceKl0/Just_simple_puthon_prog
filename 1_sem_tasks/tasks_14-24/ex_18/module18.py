def mid_line(x1, y1, x2, y2):
    return ((x1 + x2)/2, (y1 + y2)/2)

def triangle(a, b, c):
    s = []

    s.append(a)
    s.append(b)
    s.append(c)

    maxs = max(s)
    s.remove(maxs)

    if maxs < sum(s):
        return 'Треугольник с заданными сторонами существует', True
    else:
        return 'Треугольник с заданными сторонами НЕ существует', False

def S(a, b, c):
    p = (a + b + c)/2
    return (p * (p - a) * (p - b) * (p - c)) ** 0.5 if triangle(a, b, c)[1] else "Треугольник с заданными сторонами НЕ существует"