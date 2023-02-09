class ListInteger(list):

    def __init__(self, *args):
        if not all(isinstance(x, int) for x in args[0]):
            raise TypeError('можно передавать только целочисленные значения')
        list.__init__(self, *args)

    def __setitem__(self, index, value):
        if not isinstance(value, int):
            raise TypeError('можно передавать только целочисленные значения')
        list.__setitem__(self, index, value)

    def append(self, value):
        if not isinstance(value, int):
            raise TypeError('можно передавать только целочисленные значения')
        list.append(self, value)


s = ListInteger((1, 2, 3))
s[1] = 10
s.append(11)
print(s)
s[0] = 10.5 # TypeError