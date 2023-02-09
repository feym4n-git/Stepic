from abc import ABC, abstractmethod


class StackInterface(ABC):

    @abstractmethod
    def push_back(self, item):
        pass

    @abstractmethod
    def pop_back(self):
        pass


class Stack(StackInterface):

    def __init__(self):
        self._top = None

    def push_back(self, item):
        tp = self._top
        if tp is None:
            self._top = item
            return
        while tp._next is not None:
            tp = tp._next
        tp._next = item

    def pop_back(self):
        tp = self._top
        if self._top is None:
            return None
        if tp._next is None:
            ret_bj = self._top
            self._top = None
            return ret_bj
        while tp._next._next is not None:
            tp = tp._next
        ret_bj = tp._next
        tp._next = None
        return ret_bj



class StackObj:

    def __init__(self, data):
        self._data = data
        self._next = None


assert issubclass(Stack, StackInterface), "класс Stack должен наследоваться от класса StackInterface"

try:
    a = StackInterface()
    a.pop_back()
except TypeError:
    assert True
else:
    assert False, "не сгенерировалось исключение TypeError при вызове абстрактного метода класса StackInterface"


st = Stack()
assert st._top is None, "атрибут _top для пустого стека должен быть равен None"

obj_top = StackObj("obj")
st.push_back(obj_top)

assert st._top == obj_top, "неверное значение атрибута _top"

obj = StackObj("obj")
st.push_back(obj)

n = 0
h = st._top
while h:
    assert h._data == "obj", "неверные данные в объектах стека"
    h = h._next
    n += 1

assert n == 2, "неверное число объектов в стеке (или структура стека нарушена)"

del_obj = st.pop_back()
assert del_obj == obj, "метод pop_back возвратил неверный объект"

del_obj = st.pop_back()
print(del_obj)
print(obj_top._data)
assert del_obj == obj_top, "метод pop_back возвратил неверный объект"

assert st._top is None, "неверное значение атрибута _top"