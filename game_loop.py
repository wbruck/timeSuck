from Board import Board
from Piece import Piece

if __name__ == "__main__":

    # create board
    new_b = Board(10, 10, '.')

    new_b.draw()

    # create pieces
    pawn = Piece()
    pawn.set_location(2, 2)
    pawn.set_mark('X')
    pawn.set_direction(3)

    bishop = Piece()
    bishop.set_location(4, 4)
    bishop.set_mark('B')
    bishop.set_direction(9)

    key = new_b.add_piece(pawn)
    pawn.set_key(key)

    key2 = new_b.add_piece(bishop)
    bishop.set_key(key2)

    # print loop
    print(pawn)
    print(bishop)

    new_b.draw()

    move_key = pawn.key
    new_b.move_piece(move_key)

    new_b.draw()
