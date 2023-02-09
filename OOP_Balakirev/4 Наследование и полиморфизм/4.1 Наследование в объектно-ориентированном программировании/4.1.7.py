class Singleton:
    instance = None

    def __new__(cls, *args, **kwargs):
        if cls.instance is None:
            cls.instance = super().__new__(cls)
        return cls.instance

    def __del__(self):
        Singleton.instance = None

    def __init__(self, name):
        self.name = name


class Game(Singleton):

    def __init__(self, name):
        if 'name' not in self.__dict__:
            self.name = name


a = Game('First')
b = Game('Second')
print(a.name, b.name)
