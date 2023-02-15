import numbers

# digits = list(map(float, input().split()))


class TupleLimit(tuple):

    def __new__(cls, lst, max_size):
        return super(TupleLimit, cls).__new__(cls, tuple(lst))

    def __init__(self, lst, max_size):
        # super().__init__(tuple(lst))
        self.lst = tuple(lst)
        self.max_size = max_size
        if len(self) > self.max_size:
            raise ValueError('число элементов коллекции превышает заданный предел')

    def __str__(self):
        return ' '.join(map(str, self))

    def __repr__(self):
        return ' '.join(map(str, self))

lst = list(map(float, '5 6 7 8 3 4'.split()))
a = TupleLimit(lst, max_size=7)
print(a)