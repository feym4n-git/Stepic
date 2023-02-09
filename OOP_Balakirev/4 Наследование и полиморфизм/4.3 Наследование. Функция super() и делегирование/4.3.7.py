def integer_params_decorated(func):
    def wrapper(self,*args, **kwargs):
        if not all(type(arg) == int for arg in args):
            raise TypeError("аргументы должны быть целыми числами")
        if not all(type(arg) == int for arg in kwargs.values()):
            raise TypeError("аргументы должны быть целыми числами")
        res = func(self,*args, **kwargs)
        return res
    return wrapper


def integer_params(cls):
    methods = {k: v for k, v in cls.__dict__.items() if callable(v)}
    for k, v in methods.items():
        setattr(cls, k, integer_params_decorated(v))

    return cls


@integer_params
class Vector:
    def __init__(self, *args):
        self.__coords = list(args)

    def __getitem__(self, item):
        return self.__coords[item]

    def __setitem__(self, key, value):
        self.__coords[key] = value

    def set_coords(self, *coords, reverse=False):
        c = list(coords)
        self.__coords = c if not reverse else c[::-1]

