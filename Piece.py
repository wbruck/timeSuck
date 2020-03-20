
class Piece(object):
    def __init__(self):
        self._x = 0
        self._y = 0
        self.hp = 0
        self.defense = 0
        self.mark = '+'

    def set_mark(self, mark):
        self.mark = mark

    def set_location(self, x, y):
        self._x = x
        self._y = y

    def set_hp(self, change):
        self.hp += change

    def set_def(self, defense):
        self.defense = defense

    def get_location(self):
        return (self._x, self._y)

    def get_location_mark(self):
        return (self._x, self._y, self.mark)

    def set_key(self, key):
        self.key = key

    def set_direction(self, direction):
        # direction is using clock face
        # 0 up
        # 3 right
        # 6 down
        # 9 left
        # TODO - change these to a single binary not an int
        self.direction = direction

    def current_direction(self):
        return self.current_direction

    def move(self, x, y):
        # check board
        # where are the other peices

        # where is teh edge

        # check move
        # Do move
        pass

    def __repr__(self):
        return "{}, {}, {}, {}".format(self.mark, self._x,
                                       self._y, self.direction)

    def __str__(self):
        return "{} at {}, {}, wants: {}".format(self.mark, self._x,
                                                self._y, self.direction)


if __name__ == "__main__":
    from Board import Board
    tank = Piece()
    tank.set_location(3, 3)
    tank.set_mark("x")

    new = Board(5, 5, '.')
    new._insert(*tank.get_location_mark())

    new

    new.pnt()
