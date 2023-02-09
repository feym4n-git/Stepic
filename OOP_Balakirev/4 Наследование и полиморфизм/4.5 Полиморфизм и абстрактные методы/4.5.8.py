from abc import ABC, abstractmethod


class CountryInterface(ABC):

    @property
    @abstractmethod
    def name(self):
        pass

    @property
    @abstractmethod
    def population(self):
        pass

    @property
    @abstractmethod
    def square(self):
        pass

    @abstractmethod
    def get_info(self):
        return f'{self.name}: {self.square}, {self.population}'

    @population.setter
    def population(self, value):
        self.population = value

    @name.setter
    def name(self, value):
        self.name = value

    @square.setter
    def square(self, value):
        self.square = value


class Country(CountryInterface):

    def __init__(self, name_c, population_c, square_c):
        self._name = name_c
        self._population = population_c
        self._square = square_c

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def population(self):
        return self._population

    @population.setter
    def population(self, value):
        self._population = value

    @property
    def square(self):
        return self._square

    @square.setter
    def square(self, value):
        self._square = value

    def get_info(self):
        return f'{self._name}: {self._square}, {self._population}'
