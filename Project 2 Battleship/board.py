from battleship import *


BOARD_SIZE = 10
VERTICAL_SHIP = '|'
HORIZONTAL_SHIP = '-'
EMPTY = 'O'
MISS = '.'
HIT = '*'
SUNK = '#'


SHIP_INFO = [
    ("Aircraft Carrier", 5),
    ("Battleship", 4),
    ("Submarine", 3),
    ("Cruiser", 3),
    ("Patrol Boat", 2)
]


class Board:

    def __init__(self):
        self.board = []

# -- DISPLAY THE EMPTY START BOARD --

    def print_board_heading(self):
        print("   " + " ".join([chr(c) for c in range(ord('A'), ord('A') + BOARD_SIZE)]))

    def make_board(self):
        for row in range(BOARD_SIZE):
            self.board.append([])
            for column in range(BOARD_SIZE):
                self.board[row].append(EMPTY)

    def print_board(self):
        row_num = 1
        for row in self.board:
            print(str(row_num).rjust(2) + " " + (" ".join(row)))
            row_num += 1

    def display_board(self):
        self.print_board_heading()
        self.make_board()
        self.print_board()

#
# player1_board = Board()
# player1_board.place_ship()


# print('-' * 20)
#
# player2_board = Board()
# player2_board.place_ship()
