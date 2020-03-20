
class Board(object):
    def __init__(self, x, y, mark):
        """instantiate board"""
        self._x = x
        self._y = y
        self.mark = mark
        self.pieces = []

        y_map = []

        for j in range(y):
            x_map = []
            for i in range(x):
                x_map.append(self.mark)
            y_map.append(x_map)

        self.board = y_map

    def pnt(self):
        for row in self.board:
            for square in row:

                print(square, end=' ')
            print()
        print('')

    def _insert(self, x, y, mark):
        if self._check_empty(x, y):

            self.board[y][x] = mark
        else:
            self.board[y][x-1] = mark

    def _check_empty(self, x, y):
        if self.board[y][x] == self.mark:
            return True
        else:
            return False
        
    def _erase(self, x, y):
        self.board[y][x] = self.mark

    def add_piece(self, piece):
        self._insert(piece._x, piece._y, piece.mark)
        self.pieces.append(piece)



if __name__ == "__main__":
    new_one = Board(10, 10, '.')
    new_one.pnt()

    new_one.insert(1, 2, "P")
    new_one.insert(4, 4, 'X')
    new_one.pnt()

    new_one.erase(4, 4)
    new_one.pnt()