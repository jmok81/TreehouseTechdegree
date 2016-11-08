import os

BOARD_SIZE = 10

VERTICAL_SHIP = '|'
HORIZONTAL_SHIP = '-'
EMPTY = 'O'
MISS = '.'
HIT = '*'
SUNK = '#'


board = []

class Board():

    def print_board_heading(self):
        print("   " + " ".join([chr(c) for c in range(ord('A'), ord('A') + BOARD_SIZE)]))


    def make_board(self):
        for row in range(BOARD_SIZE):
            board.append([])
            for column in range(BOARD_SIZE):
                board[row].append(EMPTY)
        return board


    def print_board(self):
        self.print_board_heading()
        self.make_board()

        row_num = 1
        for row in board:
            print(str(row_num).rjust(2) + " " + (" ".join(row)))
            row_num += 1


    def display_board(self):
        self.clear_screen()
        self.print_board()



