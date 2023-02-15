class Validator:
    LST = ()

    def __init__(self, min_value, max_value):
        self.min_value = min_value
        self.max_value = max_value

    def __call__(self, value):
        if type(value) not in self.LST:
            raise ValueError('значение не прошло валидацию')
        if value < self.min_value or value > self.max_value:
            raise ValueError('значение не прошло валидацию')
        return value


class FloatValidator(Validator):
    LST = (float,)


class IntegerValidator(Validator):
    LST = (int,)


def is_valid(lst, validators):
    res = []
    for i in lst:
        for v in validators:
            try:
                res.append(v(i))
                break
            except:
                continue
    return res

fv = FloatValidator(0, 10.5)
iv = IntegerValidator(-10, 20)
lst_out = is_valid([1, 4.5, -10.5, 100, True, 'abc', (1, 2)], validators=[fv, iv])   # [1, 4.5]
print(lst_out)

