class Tuple(tuple):

    def __add__(self, other):
        return Tuple(tuple(self) + tuple(other))

