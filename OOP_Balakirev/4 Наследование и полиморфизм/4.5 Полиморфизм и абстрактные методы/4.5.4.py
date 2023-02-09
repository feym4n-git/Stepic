class ShopInterface:

    _id = 0

    def get_id(self):
        raise NotImplementedError('в классе не переопределен метод get_id')


class ShopItem(ShopInterface):

    def __init__(self,name, weight, price):
        self._name = name
        self._weight = weight
        self._price = price
        self._id = ShopItem._id + 1
        ShopItem._id += 1

    def get_id(self):
        return self._id

