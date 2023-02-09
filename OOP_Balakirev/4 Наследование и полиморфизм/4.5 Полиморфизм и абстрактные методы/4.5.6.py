from abc import ABC, abstractmethod

class Model(ABC):

    @abstractmethod
    def get_pk(self):
        pass

    def get_info(self):
        return 'Базовый класс Model'

class ModelForm(Model):

    __id = 0

    def __init__(self,login, password):
        self._login = login
        self._password = password
        self._id = ModelForm.__id + 1
        ModelForm.__id += 1

    def get_pk(self):
        return self._id




