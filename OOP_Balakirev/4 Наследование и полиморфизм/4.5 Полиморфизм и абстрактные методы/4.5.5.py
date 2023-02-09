class Validator:

    def _is_valid(self,value):
        raise NotImplementedError('в классе не переопределен метод _is_valid')

class FloatValidator(Validator):

    def __init__(self,min_value,max_value):
        self.min_value = min_value
        self.max_value = max_value

    def _is_valid(self,value):
        if not isinstance(value,float) or value < self.min_value or value > self.max_value:
            return False
        return True

    def __call__(self, value):
        return self._is_valid(value)