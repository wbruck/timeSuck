
class Piece(object):
    def __init__(self):
        self._x = 0
        self._y = 0
        self.hp = 0
        self.defense = 0
        self.mark = ''

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

if __name__ == "__main__":
    from Board import Board
    tank = Piece()
    tank.set_location(3, 3)
    tank.set_mark("x")

    new = Board(5, 5)
    new.insert(*tank.get_location_mark())
    new.pnt()
