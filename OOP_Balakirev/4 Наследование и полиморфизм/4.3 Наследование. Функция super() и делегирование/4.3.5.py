class SellItem:

    def __init__(self, name, price):
        self.name = name
        self.price = price


class House(SellItem):

    def __init__(self, name, price, material, square):
        SellItem.__init__(self, name, price)
        self.material = material
        self.square = square


class Flat(SellItem):

    def __init__(self, name, price, size, rooms):
        SellItem.__init__(self, name, price)
        self.size = size
        self.rooms = rooms


class Land(SellItem):

    def __init__(self, name, price, square):
        SellItem.__init__(self, name, price)
        self.square = square


class Agency:

    def __init__(self, name):
        self.name = name
        self.sell_items = []

    def add_object(self, item):
        self.sell_items.append(item)

    def remove_object(self, item):
        self.sell_items.remove(item)

    def get_objects(self):
        return self.sell_items
    
