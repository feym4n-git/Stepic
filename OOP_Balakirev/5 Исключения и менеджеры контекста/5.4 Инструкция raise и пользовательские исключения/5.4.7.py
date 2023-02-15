# raise CellIntegerException('значение выходит за допустимый диапазон')  # для объектов класса CellInteger
# raise CellFloatException('значение выходит за допустимый диапазон')    # для объектов класса CellFloat
# raise CellStringException('длина строки выходит за допустимый диапазон')  # для объектов класса CellString

class CellException(Exception):
    pass


class CellIntegerException(CellException):
    pass


class CellFloatException(CellException):
    pass


class CellStringException(CellException):
    pass


class Cell:

    def __init__(self, min_value, max_value):
        self._min_value = min_value
        self._max_value = max_value
        self._value = None
        self._exception = Exception

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        if value < self._min_value or value > self._max_value:
            raise self._exception('значение выходит за допустимый диапазон')
        self._value = value


class CellInteger(Cell):

    def __init__(self, min_value, max_value):
        super().__init__(min_value, max_value)
        self._exception = CellIntegerException


class CellFloat(Cell):

    def __init__(self, min_value, max_value):
        super().__init__(min_value, max_value)
        self._exception = CellFloatException


class CellString(Cell):

    def __init__(self, min_length, max_length):
        self._min_length = min_length
        self._max_length = max_length
        self._value = None
        self._exception = CellStringException

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        if len(value) < self._min_length or len(value) > self._max_length:
            raise self._exception('длина строки выходит за допустимый диапазон')
        self._value = value


class TupleData:

    def __init__(self, *args):
        for i in args:
            if not isinstance(i, Cell):
                raise TypeError('Некорректный аргумент')
        self._cells = list(args)

    def __getitem__(self, index):
        return self._cells[index].value

    def __setitem__(self, index, value):
        self._cells[index].value = value

    def __len__(self):
        return len(self._cells)

    def __iter__(self):
        return iter(i.value for i in self._cells)


t = TupleData(CellInteger(-10, 10), CellInteger(0, 2), CellString(5, 10))

d = (1, 0, 'sergey')
t[0] = d[0]
t[1] = d[1]
t[2] = d[2]
for i, x in enumerate(t):
    assert x == d[i], "объект класса TupleData хранит неверную информацию"

assert len(t) == 3, "неверное число элементов в объекте класса TupleData"

cell = CellFloat(-5, 5)
try:
    cell.value = -6.0
except CellFloatException:
    assert True
else:
    assert False, "не сгенерировалось исключение CellFloatException"

cell = CellInteger(-1, 7)
try:
    cell.value = 8
except CellIntegerException:
    assert True
else:
    assert False, "не сгенерировалось исключение CellIntegerException"

cell = CellString(5, 7)
try:
    cell.value = "hello world"
except CellStringException:
    assert True
else:
    assert False, "не сгенерировалось исключение CellStringException"

assert issubclass(CellIntegerException, CellException) and issubclass(CellFloatException, CellException) and issubclass(
    CellStringException,
    CellException), "классы CellIntegerException, CellFloatException, CellStringException должны наследоваться от класса CellException"
