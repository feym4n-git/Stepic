class Star:

    __slots__ = ('_name','_massa','_temp')

    def __init__(self,name,massa,temp):
        self._name = name
        self._massa = massa
        self._temp = temp

class WhiteDwarf(Star):

    __slots__ = ('_radius','_type_star')

    def __init__(self,name,massa,temp,radius,type_star):
        Star.__init__(self,name,massa,temp)
        self._radius = radius
        self._type_star = type_star


class YellowDwarf(Star):
    __slots__ = ('_radius', '_type_star')

    def __init__(self, name, massa, temp, radius, type_star):
        Star.__init__(self, name, massa, temp)
        self._radius = radius
        self._type_star = type_star


class RedGiant(Star):
    __slots__ = ('_radius', '_type_star')

    def __init__(self, name, massa, temp, radius, type_star):
        Star.__init__(self, name, massa, temp)
        self._radius = radius
        self._type_star = type_star

class Pulsar(Star):
    __slots__ = ('_radius', '_type_star')

    def __init__(self, name, massa, temp, radius, type_star):
        Star.__init__(self, name, massa, temp)
        self._radius = radius
        self._type_star = type_star

stars = [RedGiant('Альдебаран', 5, 3600, 'красный гигант', 45),
         WhiteDwarf('Сириус А', 2.1, 9250, 'белый карлик', 2),
         WhiteDwarf('Сириус B', 1, 8200, 'белый карлик', 0.01),
         YellowDwarf('Солнце', 1, 6000, 'желтый карлик', 1)]

white_dwarfs = [i._type_star for i in stars if i._radius == 'белый карлик']

print(white_dwarfs)