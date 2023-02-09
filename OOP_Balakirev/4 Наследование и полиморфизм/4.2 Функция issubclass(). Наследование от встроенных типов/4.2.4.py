class Thing:

    def __init__(self, name, price, weight):
        self.name = name
        self.price = price
        self.weight = weight


class DictShop(dict):

    def __init__(self, dct={}):
        if not isinstance(dct, dict):
            raise TypeError('аргумент должен быть словарем')
        if not all(isinstance(k, Thing) for k in dct.keys()):
            raise TypeError('ключами могут быть только объекты класса Thing')
        super().__init__(dct)

    def __setitem__(self, key, value):
        if not isinstance(key, Thing):
            raise TypeError('ключами могут быть только объекты класса Thing')
        super().__setitem__(key, value)
