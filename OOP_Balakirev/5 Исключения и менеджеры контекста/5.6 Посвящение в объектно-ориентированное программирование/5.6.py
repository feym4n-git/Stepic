from random import randint, choice


class Ship:

    def __init__(self,
                 length,
                 tp=1,
                 x=None,
                 y=None
                 ):
        self._length = length
        self._tp = tp
        self._x = x
        self._y = y
        self._is_move = True
        self._cells = [1] * length
        self.all_coordinates = []

    def set_start_coords(self, x, y):
        self._x = x
        self._y = y
        self.all_coords()

    def all_coords(self):
        self.all_coordinates = []
        if self.tp == 1:
            for r in range(self.length):
                self.all_coordinates.append((self._x + r, self._y))
        if self.tp == 2:
            for r in range(self.length):
                self.all_coordinates.append((self._x, self._y + r))

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    @property
    def length(self):
        return self._length

    @property
    def tp(self):
        return self._tp

    @property
    def cells(self):
        return self._cells

    def get_start_coords(self):
        return self._x, self._y

    def move(self, go):
        """
        Перемещение корабля в направлении его ориентации на go клеток
        (go = 1 - движение в одну сторону на клетку; go = -1 - движение в другую сторону на одну клетку);
        движение возможно только если флаг _is_move = True;
        """
        if not self._is_move:
            return
        old_coords = self.get_start_coords()
        if self.tp == 1:
            if go == 1:
                self._x += 1
            elif go == -1:
                self._x -= 1
        if self.tp == 2:
            if go == 1:
                self._y += 1
            elif go == -1:
                self._y -= 1
        self.all_coords()

    def is_collide(self, ship) -> bool:
        """
        Проверка столкновения.
        """
        self.all_coords()
        ship.all_coords()
        self_ship = set(self.all_coordinates)
        for i in range(len(self.all_coordinates)):
            f_c, s_c = self.all_coordinates[i]
            self_ship.add((f_c - 1, s_c - 1))
            self_ship.add((f_c - 1, s_c))
            self_ship.add((f_c - 1, s_c + 1))
            self_ship.add((f_c, s_c - 1))
            self_ship.add((f_c, s_c + 1))
            self_ship.add((f_c + 1, s_c - 1))
            self_ship.add((f_c + 1, s_c))
            self_ship.add((f_c + 1, s_c + 1))
        second_ship = set(ship.all_coordinates)
        cross = self_ship.intersection(second_ship)
        if cross:
            return True
        return False

    def is_out_pole(self, size=10):
        """
        Проверка на выход из игрового поля.
        """
        self.all_coords()
        for i in range(len(self.all_coordinates)):
            f_c, s_c = self.all_coordinates[i]
            if f_c < 0 or f_c > size - 1 or s_c < 0 or s_c > size - 1:
                return True
        return False

    def __getitem__(self, item):
        return self._cells[item]

    def __setitem__(self, key, value):
        self._cells[key] = value


class GamePole:

    def __init__(self, size=10):
        self._size = size
        self._ships = []
        self.pole = []

    def game_pole(self):
        self.pole = [[0] * self._size for _ in range(self._size)]
        return self.pole

    def init(self):
        """
        Начальная инициализация поля.
        :return: None
        """

        free_coords = []
        for i in range(self._size):
            for j in range(self._size):
                free_coords.append((i, j))
        self._ships = [
            Ship(4, tp=randint(1, 2)),
            Ship(3, tp=randint(1, 2)),
            Ship(3, tp=randint(1, 2)),
            Ship(2, tp=randint(1, 2)),
            Ship(2, tp=randint(1, 2)),
            Ship(2, tp=randint(1, 2)),
            Ship(1, tp=randint(1, 2)),
            Ship(1, tp=randint(1, 2)),
            Ship(1, tp=randint(1, 2)),
            Ship(1, tp=randint(1, 2)),
        ]
        self.game_pole()
        for i in range(len(self._ships)):
            # print('Расставляем корабль: ', i)
            while True:
                rand_coords = (choice(free_coords))
                self._ships[i].set_start_coords(*rand_coords)
                # print(f'Для корабля {i} установили стартовые координаты {rand_coords}')
                # print(f'Координаты получились: {self._ships[i].all_coordinates}')
                if self._ships[i].is_out_pole(size=self._size):
                    # print(f'Корабль {i} выходит за пределы игрового поля')
                    continue

                for j in range(len(self._ships)):
                    if self._ships[j] != self._ships[i] and self._ships[j].get_start_coords() != (None, None):
                        if self._ships[i].is_collide(self._ships[j]):
                            break
                else:
                    for x in range(len(self._ships[i].all_coordinates)):
                        a = self._ships[i].all_coordinates[x][0]
                        b = self._ships[i].all_coordinates[x][1]
                        self.pole[a][b] = 1
                        free_coords.remove((a, b))
                    # self.show()
                    # print('Получилось так')
                    break

    def collide(self, ship) -> bool:
        for j in range(len(self._ships)):
            if self._ships[j] != ship and self._ships[j].get_start_coords() != (None, None):
                if ship.is_collide(self._ships[j]):
                    return True
        return False

    def get_ships(self):
        return self._ships

    def show(self):
        self.game_pole()
        for i in range(len(self._ships)):
            ship = self._ships[i]
            for j in range(len(ship.all_coordinates)):
                a, b = ship.all_coordinates[j]
                self.pole[a][b] = ship.cells[j]

        for i in range(len(self.pole)):
            print(*self.pole[i])

    def get_pole(self):
        return tuple(tuple(i) for i in self.pole)

    def move_ships(self):
        for i in range(len(self._ships)):
            dir = [1, -1]
            old_coords = self._ships[i].get_start_coords()
            where = choice(dir)
            dir.remove(where)
            self._ships[i].move(where)
            if self._ships[i].is_out_pole(size=self._size) or self.collide(self._ships[i]):
                self._ships[i].set_start_coords(*old_coords)
                where = choice(dir)
                dir.remove(where)
                self._ships[i].move(where)
                if self._ships[i].is_out_pole(size=self._size) or self.collide(self._ships[i]):
                    self._ships[i].set_start_coords(*old_coords)
                    continue
                else:
                    continue
            else:
                continue




# test_pole = GamePole(size=10)
# test_pole.init()
# # for i in test_pole.pole:
# #     print(i)
# # a = test_pole.get_pole()
# # print(a)
# test_pole.show()
# test_pole.move_ships()
# print('Передвинули')
# test_pole.show()

ship = Ship(2)
ship = Ship(2, 1)
ship = Ship(3, 2, 0, 0)

assert ship._length == 3 and ship._tp == 2 and ship._x == 0 and ship._y == 0, "неверные значения атрибутов объекта класса Ship"
assert ship._cells == [1, 1, 1], "неверный список _cells"
assert ship._is_move, "неверное значение атрибута _is_move"

ship.set_start_coords(1, 2)
assert ship._x == 1 and ship._y == 2, "неверно отработал метод set_start_coords()"
assert ship.get_start_coords() == (1, 2), "неверно отработал метод get_start_coords()"

ship.move(1)
s1 = Ship(4, 1, 0, 0)
s2 = Ship(3, 2, 0, 0)
s3 = Ship(3, 2, 0, 2)

assert s1.is_collide(s2), "неверно работает метод is_collide() для кораблей Ship(4, 1, 0, 0) и Ship(3, 2, 0, 0)"
assert s1.is_collide(
    s3) == False, "неверно работает метод is_collide() для кораблей Ship(4, 1, 0, 0) и Ship(3, 2, 0, 2)"

s2 = Ship(3, 2, 1, 1)
assert s1.is_collide(s2), "неверно работает метод is_collide() для кораблей Ship(4, 1, 0, 0) и Ship(3, 2, 1, 1)"

s2 = Ship(3, 1, 8, 1)
assert s2.is_out_pole(10), "неверно работает метод is_out_pole() для корабля Ship(3, 1, 8, 1)"

s2 = Ship(3, 2, 1, 5)
assert s2.is_out_pole(10) == False, "неверно работает метод is_out_pole(10) для корабля Ship(3, 2, 1, 5)"

s2[0] = 2
assert s2[0] == 2, "неверно работает обращение ship[indx]"

p = GamePole(10)
p.init()
for nn in range(5):
    for s in p._ships:
        assert s.is_out_pole(10) == False, "корабли выходят за пределы игрового поля"

        for ship in p.get_ships():
            if s != ship:
                assert s.is_collide(ship) == False, "корабли на игровом поле соприкасаются"
    p.move_ships()

gp = p.get_pole()
assert type(gp) == tuple and type(gp[0]) == tuple, "метод get_pole должен возвращать двумерный кортеж"
assert len(gp) == 10 and len(gp[0]) == 10, "неверные размеры игрового поля, которое вернул метод get_pole"

pole_size_8 = GamePole(8)
pole_size_8.init()
