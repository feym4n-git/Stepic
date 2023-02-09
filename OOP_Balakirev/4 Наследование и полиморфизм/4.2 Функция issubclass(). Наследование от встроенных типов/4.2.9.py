class IteratorAttrs:

    def __iter__(self):
        a = (i for i in self.__dict__.items())
        return a

    def __next__(self):
        return next(self.__dict__)


class SmartPhone(IteratorAttrs):

    def __init__(self,model, size, memory):
        self.model = model
        self.size = size
        self.memory = memory


phone = SmartPhone(model = 'iPhone', size = 10,  memory = 8)

for attr, value in phone:
    print(attr, value)