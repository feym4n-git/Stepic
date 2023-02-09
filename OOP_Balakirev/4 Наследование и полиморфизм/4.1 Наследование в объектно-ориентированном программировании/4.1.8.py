class Validator:

    def _is_valid(self, data):
        return True

    def __call__(self, *args, **kwargs):
        return self._is_valid(*args, **kwargs)


class IntegerValidator(Validator):

    def __init__(self, mn, mx):
        self.min = mn
        self.max = mx

    def _is_valid(self, data):
        if isinstance(data, int) and self.min <= data <= self.max:
            return True
        raise ValueError('данные не прошли валидацию')


class FloatValidator(Validator):

    def __init__(self, mn, mx):
        self.min = mn
        self.max = mx

    def _is_valid(self, data):
        if isinstance(data, float) and self.min <= data <= self.max:
            return True
        raise ValueError('данные не прошли валидацию')


integer_validator = IntegerValidator(-10, 10)
float_validator = FloatValidator(-1, 1)
res1 = integer_validator(10)  # исключение не генерируется (проверка проходит)
res2 = float_validator(10)