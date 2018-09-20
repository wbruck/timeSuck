
class Board(object):
    def __init__(self, x, y):
        """instantiate board"""
        self._x = x
        self._y = y


        y_map = []


        for j in range(y):
            x_map = []
            for i in range(x):
                x_map.append(' ')
            y_map.append(x_map)

        self.board = y_map


    def pnt(self):
        for row in self.board:
            print(row)
        print()


    def insert(self, x, y, mark):
        self.board[y][x] = mark

    def erase(self, x, y):
        self.board[y][x] = ' '


if __name__ == "__main__":
    new_one = Board(10, 10)
    new_one.pnt()

    new_one.insert(1, 2, "p")
    new_one.insert(4, 4, 'x')
    new_one.pnt()

    new_one.erase(4, 4)
    new_one.pnt()