class Furniture:

    def __init__(self, name, weight):
        self._name = self.__verify_name(name)
        self._weight = self.__verify_weight(weight)

    def __verify_name(self, name):
        if not isinstance(name, str):
            raise TypeError('название должно быть строкой')
        if len(name) == 0:
            raise ValueError("Name cannot be empty")
        return name

    def __verify_weight(self, weight):
        if not type(weight) in (int,float):
            raise TypeError('вес должен быть числом')
        if weight < 0:
            raise TypeError('вес должен быть положительным числом')
        return weight

    @property
    def name(self):
        return self._name

    @property
    def weight(self):
        return self._weight

    @weight.setter
    def weight(self, value):
        self._weight = self.__verify_weight(value)

    @name.setter
    def name(self, value):
        self._name = self.__verify_name(value)

    def get_attrs(self):
        return tuple(i for i in self.__dict__.values())

class Closet(Furniture):
    def __init__(self, name, weight,tp, doors):
        super().__init__(name, weight)
        self._tp = tp
        self._doors = doors

class Chair(Furniture):
    def __init__(self, name, weight, height):
        super().__init__(name, weight)
        self._height = height

class Table(Furniture):
    def __init__(self, name, weight, height, square):
        super().__init__(name, weight)
        self._height = height
        self._square = square


cl = Closet('шкаф-купе', 342.56, True, 3)
chair = Chair('стул', 14, 55.6)
tb = Table('стол', 34.5, 75, 10)
print(tb.get_attrs())

try:
    Furniture('name', '10')
except:
    print('ок')