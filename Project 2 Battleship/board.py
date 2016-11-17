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

# --------------------------------------

# -- SETOUT PLAYER BOARD --

    # Player input for ship position
    def ship_position(self):
        self.ship_input = (
        (input("Where would you like to place the {}? The {} takes up {} spaces: ".format(
            self.ship[0],
            self.ship[0],
            self.ship[1])
            )).strip()).lower()
        self.ship_loc = list(self.ship_input)
        if len(self.ship_loc) == 2:
            self.ship_x_pos = ord(self.ship_loc[1]) - 97
            self.ship_y_pos = int(self.ship_input[0]) - 1
        elif len(self.ship_loc) == 3:
            self.ship_x_pos = ord(self.ship_loc[2]) - 97
            self.ship_y_pos = int(self.ship_input[0] + self.ship_input[1]) - 1
        else:
            self.ship_position()


    # Player input ship alignment
    def ship_alignment(self):
        self.alignment = (input("Press [h] to place it horizontal, or [v] to place it vertical: ")).lower()
        if self.alignment == 'h':
            # Check and see if the ship will fit on the board horizontally
            for pos in range(int(self.ship[1])):
                # If the ship fits add the markers to the board
                if (self.ship_x_pos + int(self.ship[1])) > BOARD_SIZE:
                    print(
                    "The {} takes up {} spaces. There are only {} spaces available to the right of position {}"
                        .format( self.ship[0], self.ship[1], (BOARD_SIZE - self.ship_x_pos), self.ship_input))
                    print("Please try again")
                    self.ship_position()
                else:
                    self.board[self.ship_y_pos][self.ship_x_pos + pos] = HORIZONTAL_SHIP
            self.print_board()

        elif self.alignment == 'v':
            # Check and see if the ship will fit on the board vertically
            for pos in range(int(self.ship[1])):
                # If the ship fits add the markers to the board
                if (self.ship_y_pos - int(self.ship[1])) < BOARD_SIZE:
                    self.board[self.ship_y_pos + pos][self.ship_x_pos] = VERTICAL_SHIP
                    self.display_board()
                # If the ship does not fit on the board ask the player to try again.
                else:
                    print("The {} takes up {} spaces. There are only {} spaces available from position {}"
                        .format( self.ship[0], self.ship[1], (BOARD_SIZE - self.ship_y_pos), self.alignment))
                    print("Please try again")
                    self.ship_position()
        else:
            self.ship_alignment()


    def place_ship(self):
        self.display_board()
        print("\n")
        print("Place your ship by first selecting a Row and then a Column, for example 3C or 7F.")
        print("\n")
        for self.ship in SHIP_INFO:
            self.ship_position()
            self.ship_alignment()





player1_board = Board()
player1_board.place_ship()


# print('-' * 20)
#
# player2_board = Board()
# player2_board.place_ship()
