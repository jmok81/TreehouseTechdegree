from battleship import Battleship


class Player:

    def player_names(self):
        player_one = (input("Please enter Player One's name: ")).strip()
        print("Welcome {}".format(player_one))

        player_two = (input("Please enter Player Two's name: ")).strip()
        print("Welcome {}".format(player_two))








# Prompt the players for their names.
# Refer to players using their names whenever possible.
# def player_names():
#     player_one = (input("Please enter Player One's name: ")).strip()
#     print("Welcome {}".format(player_one))
#     player_two = (input("Please enter Player Two's name: ")).strip()
#     print("Welcome {}".format(player_two))



# Prompt user to place a ship.
# Under the board, prompt the user to enter one ship at a time.
# For each ship, ask if they want the ship to be oriented horizontally
# or vertically then ask which location on the board the first ships
# should be placed at: Below is an example prompt. You can use a different prompt.
#Place the location of the aircraft carrier (5 spaces): a2 Is it horizontal? (Y)/N: n
#
# class ship_locations:
#
#     def ship_location(self):
#         print("\n")
#         self.player_board = board
#
#         for ship in SHIP_INFO:
#             ship_count = 0
#             while ship_count < len(SHIP_INFO):
#                 ship_input = ((input("Place the location of the {} ({} spaces): ".format(ship[0], ship[1]))).strip()).lower()
#                 ship_loc = list(ship_input)
#                 if len(ship_loc) == 2:
#                     ship_x_pos = ord(ship_loc[1]) - 97
#                     ship_y_pos = int(ship_input[0]) - 1
#                 else:
#                     ship_x_pos = ord(ship_loc[2]) - 97
#                     ship_y_pos = int(ship_input[0]+ ship_input[1] ) - 1
#
#                 ship_dir = (input("[h] to place it horizontal, or [v] to place it vertical: ")).lower()
#                 # if they want to place the ship horizontally.
#                 if ship_dir == 'h':
#                     #Check and see if the ship will fit on the board
#                     for pos in range(int(ship[1])):
#                         # If the ship fits add the markers to the board
#                         if (ship_x_pos + int(ship[1])) < BOARD_SIZE:
#                            self.player_board[ship_y_pos][ship_x_pos + pos] = HORIZONTAL_SHIP
#                             ship_count += 1
#                         # If the ship does not fit on the board ask the player to try again.
#                         else:
#                             print("The {} takes up {} spaces. There are only {} spaces available from position {}".format(ship[0], ship[1], (BOARD_SIZE - ship_x_pos), ship_input))
#                             print("Please try again")
#                             break
#
# ship_locations()