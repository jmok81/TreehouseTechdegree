from board import Board, SHIP_INFO, BOARD_SIZE, HORIZONTAL_SHIP


from battleship import *



class Ship:

# -- SETOUT PLAYER BOARD --

    # Player input for ship position
    def ship_position(self):
        self.ship_input = (
        (input("Where would you like to place the {}? The {} takes up {} spaces: ".format(
            self.ship[0],
            self.ship[0],
            self.ship[1]
            ))).strip()).lower()
        self.ship_location = list(self.ship_input)
        if len(self.ship_location) == 2:
            self.ship_x_pos = ord(self.ship_location[1]) - 97
            self.ship_y_pos = int(self.ship_input[0]) - 1
        elif len(self.ship_location) == 3:
            self.ship_x_pos = ord(self.ship_location[2]) - 97
            self.ship_y_pos = int(self.ship_input[0] + self.ship_input[1]) - 1
        else:
            self.ship_position()
        self.player_input_check()


    # Check and see if the position is on the board
    def player_input_check(self):
        if chr(self.ship_x_pos + 97) not in ("abcdefghij") or (self.ship_y_pos + 1) > 10:
            print("Try Again")
            self.ship_position()
        else:
            pass

    # Check and see if the ship hits an existing ship
    def hits_existing_ship(self):
        self.ship_setout = []
        for self.pos in range(int(self.ship[1])):
            self.ship_setout.append(self.board.board[self.ship_y_pos][self.ship_x_pos + self.pos])
        print(self.ship_setout)

        if HORIZONTAL_SHIP in self.ship_setout:
            print ("There is an existing ship in the way. Try again")
            self.ship_position()
            self.ship_alignment()
        else:
            for self.pos in range(int(self.ship[1])):
                self.board.board[self.ship_y_pos][self.ship_x_pos + self.pos] = HORIZONTAL_SHIP

    # Player input ship alignment
    def ship_alignment(self):

        self.alignment = (input("Press [h] to place it horizontal, or [v] to place it vertical: ")).lower()
        if self.alignment == 'h':
            # Check and see if the ship will fit on the board horizontally
            if (self.ship_x_pos + int(self.ship[1])) < BOARD_SIZE:
                # Check and see if the ship hits an existing ship
                self.hits_existing_ship()
            else:
                print(
                    "The {} takes up {} spaces. There are only {} spaces available to the right of position {}"
                    .format(self.ship[0], self.ship[1], (BOARD_SIZE - self.ship_x_pos), self.ship_input))
                print("Please try again")
                self.ship_position()
            self.board.print_board_heading()
            self.board.print_board()
        elif self.alignment == 'v':
            # Check and see if the ship will fit on the board vertically
            for self.pos in range(int(self.ship[1])):
                # If the ship fits add the markers to the board
                if (self.ship_y_pos - int(self.ship[1])) < BOARD_SIZE:
                    self.hits_existing_ship()
                    #self.board[self.ship_y_pos - self.pos][self.ship_x_pos] = VERTICAL_SHIP
                else:
                    print(
                        "The {} takes up {} spaces. There are only {} spaces available above the position of {}"
                        .format(self.ship[0], self.ship[1], (BOARD_SIZE - self.ship_y_pos), self.ship_input))
                    print("Please try again")
                    self.ship_position()
            self.board.print_board_heading()
            self.board.print_board()
        else:
            self.ship_alignment()
#
#
    def place_ship(self):
        self.board = Board()
        self.board.display_board()
        print("\n")
        print("Place your ship by first selecting a Row and then a Column, for example 3C or 7F.")
        print("\n")
        for self.ship in SHIP_INFO:
            self.ship_position()
            self.ship_alignment()



test = Ship()
test.place_ship()
