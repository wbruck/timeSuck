from Board import Board
from Piece import Piece

if __name__ == "__main__":
    new = Board(10, 10, '.')

    new.pnt()

    pawn = Piece()
    pawn.set_location(2, 2)
    pawn.set_mark('X')

    new.add_piece(pawn)
