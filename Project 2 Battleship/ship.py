from board import *

SHIP_INFO = [
    ("Aircraft Carrier", 5),
    ("Battleship", 4),
    ("Submarine", 3),
    ("Cruiser", 3),
    ("Patrol Boat", 2)
]


class Ship():

    def place_ship(self):

        self.player_board = self.board

        for ship in SHIP_INFO:
            self.ship_count = 0
            while self.ship_count < len(SHIP_INFO):
                self.ship_input = (
                (input("Place the location of the {} ({} spaces): ".format(ship[0], ship[1]))).strip()).lower()
                self.ship_location()
                self.ship_alignment()
                if self.alignment == 'h':
                    # Check and see if the ship will fit on the board
                    for pos in range(int(ship[1])):
                        # If the ship fits add the markers to the board
                        if (self.ship_x_pos + int(ship[1])) < BOARD_SIZE:
                            self.player_board[self.ship_y_pos][self.ship_x_pos + self.pos] = HORIZONTAL_SHIP
                            self.ship_count += 1
                        # If the ship does not fit on the board ask the player to try again.
                        else:
                            print(
                                "The {} takes up {} spaces. There are only {} spaces available from position {}".format(
                                    ship[0],
                                    ship[1], (
                                        BOARD_SIZE - self.ship_x_pos),
                                    self.alignment))
                            print("Please try again")
                            self.place_ship()


    def ship_location(self):
                self.ship_loc = list(self.ship_input)
                if len(self.ship_loc) == 2:
                    self.ship_x_pos = ord(self.ship_loc[1]) - 97
                    self.ship_y_pos = int(self.ship_input[0]) - 1
                else:
                    self.ship_x_pos = ord(self.ship_loc[2]) - 97
                    self.ship_y_pos = int(self.ship_input[0] + self.ship_input[1]) - 1


    def ship_alignment(self):
        self.alignment = (input("[h] to place it horizontal, or [v] to place it vertical: ")).lower()


    def vertical_alignment(self):
        # if they want to place the ship horizontally.
        if self.alignment == 'h':
            # Check and see if the ship will fit on the board
            for pos in range(int(ship[1])):
                # If the ship fits add the markers to the board
                if (self.ship_x_pos + int(ship[1])) < Board.BOARD_SIZE:
                    self.player_board[self.ship_y_pos][self.ship_x_pos + pos] = HORIZONTAL_SHIP
                    self.ship_count += 1
                # If the ship does not fit on the board ask the player to try again.
                else:
                    print("The {} takes up {} spaces. There are only {} spaces available from position {}".format(ship[0],
                                                                                                                  ship[1], (
                                                                                                                  Board.BOARD_SIZE - self.ship_x_pos),
                                                                                                                  self.alignment))
                    print("Please try again")

                    break

test = Ship()
test.place_ship()