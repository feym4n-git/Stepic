class PrimaryKeyError(Exception):

    def __init__(self, id=None, pk=None):
        if id is None and pk is None:
            self.ms = 'Первичный ключ должен быть целым неотрицательным числом'
            print(self.ms)
            return
        if type(id) is not int or type(pk) is not int:
            if id is None:
                self.ms = f'Значение первичного ключа pk = {pk} недопустимо'
                print(self.ms)
            else:
                self.ms = f'Значение первичного ключа id = {id} недопустимо'
                print(self.ms)

    def __str__(self):
        return self.ms

try:
    e1 = PrimaryKeyError(id = -10.5)
except Exception as e:
    print(e)
