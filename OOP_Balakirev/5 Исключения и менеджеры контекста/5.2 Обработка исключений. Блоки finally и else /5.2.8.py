class Rect:

    def __init__(self, x, y, width, height):
        self._x = self.check(x, 0)
        self._y = self.check(y, 0)
        self._width = self.check(width, 1)
        self._height = self.check(height, 1)

    def __repr__(self):
        return f'({self._x}, {self._y}, {self._width}, {self._height})'

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    @property
    def width(self):
        return self._width

    @property
    def height(self):
        return self._height

    @staticmethod
    def check(value, param):
        types = (float, int)
        if param == 0:
            if type(value) not in types:
                raise ValueError('некорректные координаты и параметры прямоугольника')
        if param == 1:
            if type(value) not in types or value <= 0:
                raise ValueError('некорректные координаты и параметры прямоугольника')
        return value

    def is_collision(self, rect):

        x = []
        if self.x <= rect.x:
            if self.x + self.width >= rect.x:
                x.append(1)
        else:
            if rect.x + rect.width >= self.x:
                x.append(1)
        if self.y <= rect.y:
            if self.y + self.height >= rect.y:
                x.append(1)
        else:
            if rect.y + rect.height >= self.y:
                x.append(1)
        if x == [1, 1]:
            raise TypeError('прямоугольники пересекаются')


lst_rect = [Rect(0, 0, 5, 3), Rect(6, 0, 3, 5), Rect(3, 2, 4, 4), Rect(0, 8, 8, 1)]
lst_not_collision = []
for i in lst_rect:
    x = 0
    for j in lst_rect:
        try:
            if i!= j:
                i.is_collision(j)
                x += 1
        except:
            continue
    if x == 3:
        lst_not_collision.append(i)
print(lst_not_collision)

r = Rect(1, 2, 10, 20)
print(r)
assert r._x == 1 and r._y == 2 and r._width == 10 and r._height == 20, "неверные значения атрибутов объекта класса Rect"

r2 = Rect(1.0, 2, 10.5, 20)

try:
    r2 = Rect(0, 2, 0, 20)
except ValueError:
    assert True
else:
    assert False, "не сгенерировалось исключение ValueError при создании объекта Rect(0, 2, 0, 20)"


assert len(lst_rect) == 4, "список lst_rect содержит не 4 элемента"
assert len(lst_not_collision) == 1, "неверное число элементов в списке lst_not_collision"

def not_collision(rect):
    for x in lst_rect:
        try:
            if x != rect:
                rect.is_collision(x)
        except TypeError:
            return False
    return True

f = list(filter(not_collision, lst_rect))
assert lst_not_collision == f, "неверно выделены не пересекающиеся прямоугольники, возможно, некорректно работает метод is_collision"

r = Rect(3, 2, 2, 5)
rr = Rect(1, 4, 6, 2)

try:
    r.is_collision(rr)
except TypeError:
    assert True
else:
    assert False, "не сгенерировалось исключение TypeError при вызове метода is_collision() для прямоугольников Rect(3, 2, 2, 5) и Rect(1, 4, 6, 2)"