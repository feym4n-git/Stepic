def decorator(func, param):
    def wrapper(self, *args, **kwargs):
        if func not in param:
            param.append(func.__name__)
        res = func(self, *args, **kwargs)
        return res

    return wrapper


def class_log(param):
    def integer_params(cls: classmethod):
        methods = {k: v for k, v in cls.__dict__.items() if callable(v)}
        print(methods)
        for k, v in methods.items():
            setattr(cls, k, decorator(v, param))
        return cls
    return integer_params


vector_log = []  # наименование (vector_log) в программе не менять!


@class_log(vector_log)
class Vector:
    def __init__(self, *args):
        self.__coords = list(args)

    def __getitem__(self, item):
        return self.__coords[item]

    def __setitem__(self, key, value):
        self.__coords[key] = value


v = Vector(1, 2, 3)
v[0] = 10

print(vector_log)