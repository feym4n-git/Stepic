class Aircraft:

    def __init__(self, model, mass, speed, top):
        self._model = self.check_str(model)
        self._mass = self.check_int(mass)
        self._speed = self.check_int(speed)
        self._top = self.check_int(top)

    @staticmethod
    def check_int(value):
        if type(value) not in (int, float):
            raise TypeError('неверный тип аргумента')
        if value < 0:
            raise TypeError('неверный тип аргумента')
        return value

    @staticmethod
    def check_str(value):

        """
        Проверяет строку.

        :param value:
        :return:
        """

        if type(value) != str:
            raise TypeError('неверный тип аргумента')
        return value


class PassengerAircraft(Aircraft):

    def __init__(self, model, mass, speed, top, chairs):
        super().__init__(model, mass, speed, top)
        self._chairs = self.check_int_only(chairs)

    @staticmethod
    def check_int_only(value):
        if type(value) not in (int,):
            raise TypeError('неверный тип аргумента')
        if value < 0:
            raise TypeError('неверный тип аргумента')
        return value


class WarPlane(Aircraft):

    def __init__(self, model, mass, speed, top, weapons):
        super().__init__(model, mass, speed, top)
        self._weapons = self.check_dict(weapons)

    @staticmethod
    def check_dict(value):
        if type(value) != dict:
            raise TypeError('неверный тип аргумента')
        return value


planes = [PassengerAircraft('МС-21', 1250, 8000, 12000.5, 140),
          PassengerAircraft('SuperJet', 1145, 8640, 11034, 80),
          WarPlane('Миг-35', 7034, 25000, 2000, {"ракета": 4, "бомба": 10}),
          WarPlane('Су-35', 7034, 34000, 2400, {"ракета": 4, "бомба": 7})]
