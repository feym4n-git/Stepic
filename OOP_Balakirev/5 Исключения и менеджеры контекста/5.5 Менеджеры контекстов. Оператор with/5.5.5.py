from copy import deepcopy


class Box:

    def __init__(self, name, max_weight):
        self._name = name
        self._max_weight = max_weight
        self._cur_weight = 0
        self._things = []

    def add_thing(self, obj):
        if self._cur_weight + obj[1] > self._max_weight:
            # print('превышен суммарны,й вес вещей')
            raise ValueError('превышен суммарный вес вещей')
        self._things.append(obj)
        self._cur_weight += obj[1]


class BoxDefender:

    def __init__(self, box):
        self._box = deepcopy(box)
        self._orig = box

    def __enter__(self):
        return self._box

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None:
            # print('сохранено')
            # print(self._box._things)
            # print(self._orig._things)
            self._orig._things[:] = self._box._things
            # print(self._orig._things, 'список нужный')
        return False


b = Box('name', 2000)
assert b._name == 'name' and b._max_weight == 2000, "неверные значения атрибутов объекта класса Box"

b.add_thing(("1", 100))
b.add_thing(("2", 200))

try:
    with BoxDefender(b) as bb:
        bb.add_thing(("3", 1000))
        bb.add_thing(("4", 1900))
except ValueError:
    assert len(b._things) == 2

else:
    assert False, "не сгенерировалось исключение ValueError"
# print(b._things)
try:
    with BoxDefender(b) as bb:
        bb.add_thing(("3", 100))
except ValueError:
    assert False, "возникло исключение ValueError, хотя, его не должно было быть"
else:
    print(b._things,'список конечный')
    assert len(b._things) == 3, "неверное число элементов в списке _things"
