
class Board(object):
    def __init__(self, x, y, mark):
        """instantiate board"""
        self._x = x
        self._y = y
        self.mark = mark
        # assign key in add_piece
        self.next_key = 0

        self.pieces = {}

        y_map = []

        for j in range(y):
            x_map = []
            for i in range(x):
                x_map.append(self.mark)
            y_map.append(x_map)

        self.board = y_map

    def _get_key(self):
        self.next_key += 1
        return self.next_key

    def draw(self):
        for row in self.board:
            for square in row:

                print(square, end=' ')
            print()
        print('')

    def _insert(self, x, y, new_mark):
        if self._check_empty(x, y):
            self.board[y][x] = new_mark
        else:
            self.board[y][x-1] = new_mark

    def _update(self, x, y, new_mark):
        # insert new mark
        self._insert(x, y, new_mark)

    def _check_empty(self, x, y):
        if self.board[y][x] == self.mark:
            return True
        else:
            return False

    def _erase(self, x, y):
        self.board[y][x] = self.mark

    def add_piece(self, piece):
        self._insert(piece._x, piece._y, piece.mark)

        new_key = self._get_key()
        self.pieces[new_key] = piece

        return new_key

    def update_piece(self, piece_key):
        pass

    def move_piece(self, piece_key):
        cur_piece = self.pieces[piece_key]
        print(cur_piece)

        # do math to derive square from direction
        if cur_piece.direction == 3:
            old_x, old_y = cur_piece.get_location()
            x = old_x + 1
            y = old_y

        print(x, y)

        # check if square is free
        if self._check_empty(x, y):
            cur_piece.set_location(x, y)
            # clear square
            self.board[old_y][old_x] = self.mark
            self._update(x, y, cur_piece.mark)
        else:
            print("not empty")

        # move
        return True


if __name__ == "__main__":
    new_one = Board(10, 10, '.')
    new_one.pnt()

    new_one._insert(1, 2, "P")
    new_one._insert(4, 4, 'X')
    new_one.pnt()

    new_one._erase(4, 4)
    new_one.pnt()
