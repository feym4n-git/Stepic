class Vector:

    def __init__(self, *args):
        self.coord = args

    def __len__(self):
        return len(self.coord)

    def get_coords(self):
        return tuple(self.coord)

    def __add__(self, other):
        if len(self.coord) != len(other.coord):
            raise TypeError('размерности векторов не совпадают')
        return Vector(*((i + j) for i, j in zip(self.coord, other.coord)))

    def __sub__(self, other):
        if len(self.coord) != len(other.coord):
            raise TypeError('размерности векторов не совпадают')
        return Vector(*((i - j) for i, j in zip(self.coord, other.coord)))


class VectorInt(Vector):

    def __init__(self, *args):
        if all(isinstance(i, int) for i in args):
            self.coord = args
            return
        raise ValueError('координаты должны быть целыми числами')

    def __add__(self, other):
        if len(self.coord) != len(other.coord):
            raise TypeError('размерности векторов не совпадают')
        if all(isinstance(i, int) for i in other.coord):
            return VectorInt(*((i + j) for i, j in zip(self.coord, other.coord)))
        return Vector(*((i + j) for i, j in zip(self.coord, other.coord)))

    def __sub__(self, other):
        if len(self.coord) != len(other.coord):
            raise TypeError('размерности векторов не совпадают')
        if all(isinstance(i, int) for i in other.coord):
            return VectorInt(*((i + j) for i, j in zip(self.coord, other.coord)))
        return Vector(*((i + j) for i, j in zip(self.coord, other.coord)))


v1 = Vector(1, 2, 3)
v2 = Vector(3, 4, 5)
print((v1 + v2).get_coords())
assert (v1 + v2).get_coords() == (
    4, 6, 8), "операция сложения дала неверные значения (или некорректно работает метод get_coords)"
assert (v1 - v2).get_coords() == (
    -2, -2, -2), "операция вычитания дала неверные значения (или некорректно работает метод get_coords)"

v = VectorInt(1, 2, 3, 4)
assert isinstance(v, Vector), "класс VectorInt должен наследоваться от класса Vector"

try:
    v = VectorInt(1, 2, 3.4, 4)
except ValueError:
    assert True
else:
    assert False, "не сгенерировалось исключение ValueError для команды v = VectorInt(1, 2, 3.4, 4)"

v1 = VectorInt(1, 2, 3, 4)
v2 = VectorInt(4, 2, 3, 4)
v3 = Vector(1.0, 2, 3, 4)

v = v1 + v2
assert type(
    v) == VectorInt, "при сложении вектором с целочисленными координатами должен формироваться объект класса VectorInt"
v = v1 + v3
assert type(v) == Vector, "при сложении вектором с вещественными координатами должен формироваться объект класса Vector"
