class PointTrack:

    def __init__(self, x, y):
        self._x = self.check_coords(x)
        self._y = self.check_coords(y)

    @staticmethod
    def check_coords(value):
        if type(value) not in (int, float):
            raise TypeError('координаты должны быть числами')

    def __str__(self):
        return f'PointTrack: {self._x}, {self._y}'


class Track:

    def __init__(self, *args):
        self.__points = []
        if len(args) == 2:
            self.__points.insert(0, PointTrack(args[0], args[1]))
        for i in args:
            self.__points.append(i)

    @property
    def points(self):
        return tuple(self.__points)

    def add_back(self, pt):
        self.__points.append(pt)

    def add_front(self, pt):
        self.__points.insert(0, pt)

    def pop_back(self):
        return self.__points.pop()

    def pop_front(self):
        return self.__points.pop(0)


