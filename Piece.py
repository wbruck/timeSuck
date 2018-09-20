
class Piece(object):
    def __init__(self):
        self._x = 0
        self._y = 0
        self.hp = 0
        self.defense = 0


    def set_location(self, x, y):
        self._x = x
        self._y = y

    def set_hp(self, change):
        self.hp += change

    def set_def(self, defense):
        self.defense = defense

