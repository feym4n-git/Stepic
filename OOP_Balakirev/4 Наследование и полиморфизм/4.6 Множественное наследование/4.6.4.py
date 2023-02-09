class Digit:

    def __init__(self, value):
        self.check(value)
        self.value = self.check(value)

    @staticmethod
    def check(value):
        if not type(value) in (int, float):
            raise TypeError('значение не соответствует типу объекта')



class Integer(Digit):

    @staticmethod
    def check(value):
        if not type(value) in (int,):
            raise TypeError('значение не соответствует типу объекта')


class Float(Digit):

    @staticmethod
    def check(value):
        if not type(value) in (float,):
            raise TypeError('значение не соответствует типу объекта')


class Positive(Digit):

    @staticmethod
    def check(value):
        if not type(value) in (int, float) or value < 0:
            raise TypeError('значение не соответствует типу объекта')


class Negative(Digit):

    @staticmethod
    def check(value):
        if not type(value) in (int, float) or value > 0:
            raise TypeError('значение не соответствует типу объекта')


class PrimeNumber(Integer, Positive):

    @staticmethod
    def check(value):
        Integer.check(value)
        Positive.check(value)


class FloatPositive(Float, Positive):
    @staticmethod
    def check(value):
        Float.check(value)
        Positive.check(value)


digits = [PrimeNumber(3), PrimeNumber(1), PrimeNumber(4), FloatPositive(1.5), FloatPositive(9.2), FloatPositive(6.5),
          FloatPositive(3.5), FloatPositive(8.9)]

lst_positive = [i for i in digits if i.__class__ == Positive]
lst_float = [i for i in digits if i.__class__ == Float]
