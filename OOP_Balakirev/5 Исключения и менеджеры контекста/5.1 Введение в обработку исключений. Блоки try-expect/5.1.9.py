# здесь объявляйте класс Triangle
class Triangle:

    def __init__(self, a, b, c):
        t = (int, float)
        if type(a) not in t or type(b) not in t or type(c) not in t:
            raise TypeError('стороны треугольника должны быть положительными числами')
        if a <= 0 or b <= 0 or c <= 0:
            raise TypeError('стороны треугольника должны быть положительными числами')
        if a + b < c or a + c < b or b + c < a:
            raise ValueError('из указанных длин сторон нельзя составить треугольник')

        self._a = a
        self._b = b
        self._c = c


input_data = [(1.0, 4.54, 3), ('abc', 1, 2, 3), (-3, 3, 5.2), (4.2, 5.7, 8.7), (True, 3, 5),
              (7, 4, 6)]  # эту строчку не менять (переменную input_data также не менять)

# здесь формируйте список lst_tr
lst_tr = []

for i in input_data:
    try:
        lst_tr.append(Triangle(*i))
    except:
        continue

print(lst_tr)
