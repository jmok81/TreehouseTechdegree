import os


SHIP_INFO = [
    ("Aircraft Carrier", 5),
    ("Battleship", 4),
    ("Submarine", 3),
    ("Cruiser", 3),
    ("Patrol Boat", 2)
]

BOARD_SIZE = 10

VERTICAL_SHIP = '|'
HORIZONTAL_SHIP = '-'
EMPTY = 'O'
MISS = '.'
HIT = '*'
SUNK = '#'


def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def print_board_heading():
    print("   " + " ".join([chr(c) for c in range(ord('A'), ord('A') + BOARD_SIZE)]))


def print_board(board):
    print_board_heading()

    row_num = 1
    for row in board:
        print(str(row_num).rjust(2) + " " + (" ".join(row)))
        row_num += 1


# Prompt the players for their names.
# Refer to players using their names whenever possible.
def player_names():
    player_one = (input("Please enter Player One's name: ")).strip()
    print("Welcome {}".format(player_one))
    player_two = (input("Please enter Player Two's name: ")).strip()
    print("Welcome {}".format(player_two))


# Display an empty board.
# Clear the screen and display an empty board on the screen.
# Use the EMPTY marker for all locations on the board.
# The board displays column headers as letters in the alphabet and displays
# numeric row numbers along the left side of the board.

def make_board():
    board = []
    for row in range(BOARD_SIZE):
        board.append([])
        for column in range(BOARD_SIZE):
            board[row].append(EMPTY)
    return board

board = make_board()


def display_board():
    clear_screen()
    print_board(board)


# Prompt user to place a ship.
# Under the board, prompt the user to enter one ship at a time.
# For each ship, ask if they want the ship to be oriented horizontally
# or vertically then ask which location on the board the first ships
# should be placed at: Below is an example prompt. You can use a different prompt.
#Place the location of the aircraft carrier (5 spaces): a2 Is it horizontal? (Y)/N: n


def ship_location():
    print("\n")
    player_board = board
    for ship in SHIP_INFO:
        ship_input = ((input("Place the location of the {} ({} spaces): ".format(ship[0], ship[1]))).strip()).lower()
        ship_loc = list(ship_input)
        ship_x_pos = ord(ship_loc[1]) - 97
        ship_y_pos = int(ship_input[0]) - 1
        ship_dir = (input("[h] to place it horizontal, or [v] to place it vertical: ")).lower()

        if ship_dir == 'h':
            for pos in range(int(ship[1])):
                player_board[ship_y_pos][ship_x_pos + pos] = HORIZONTAL_SHIP
            print_board(player_board)


            #player_board[ship_y_pos][ship_x_pos] = HORIZONTAL_SHIP
            #player_board[ship_y_pos][ship_x_pos + 1] = HORIZONTAL_SHIP
        # display_board(player_board)




    #new_board = board
    #if p1_pboat_dir == 'h':
        #new_board[y_pos][x_pos] = HORIZONTAL_SHIP
        #new_board[y_pos][x_pos + 1] = HORIZONTAL_SHIP
    #print_board(new_board)






#for x in SHIP_INFO:
    #if "Aircraft Carrier" in x:
        #print(x)

#player_names()
#display_board()
ship_location()





# Validate user input.
# If, at any time, the player enters input that can’t be parsed then continue
# prompting until valid input has been entered. Tell the user why their input
# was invalid before prompting again.
# Be as accepting as possible of input. For example, spaces before or after
# the player’s input is allowed. Both lower and uppercase characters are also allowed.
# In order to reduce confusion, you may want to clear the screen and display the
# screen again before each attempt.











# Validate ship placement.
# Verify that the ships fit on the board and that they don’t overlap with any
#  existing ships. If a ship violates either of these rules, inform the player
#  about the problem and prompt for a new location.






# Update the board.
# After the user places a ship, clear the screen and print the board to the
# screen with all of the ships that the player has placed up until that point
# displayed on the board using the appropriate symbols.










# Prompt second player to place their ships
# After the first player has placed all their ships, clear the screen and prompt
#  the second player, by name, to begin placing their ships.






# Allow players to take turns.
# Clear the screen after each player has finished taking their turn.
# Prompt the next player, by name, that it is their turn. Prompt them
# to press enter to continue. This gives the previous player a chance to
# hand the computer to the next player so they don’t see each other’s boards










# Display boards to the screen.
#Clear the screen and print a board that shows where the current player has
# guessed so far. Use the appropriate markers to display which locations hit
# a ship, which locations are misses, and which locations are a sunken ship.
# On the same screen but on a separate printed board, print a board that displays
#  where their opponent has guessed up until then. Use the appropriate markers to
# display which locations hit a ship, which locations are misses, and which
# locations are a sunken ship. This board also displays the full locations of
# the current player’s ships using the appropriate markers.







# Prompt player for guess.
# Prompt the player, by name, to guess where their opponent’s ships are
# by entering a location. For example:
# Bob, enter a location: f7





# Validate guess.
# If the player enters a location that they’ve already guessed, then prompt
# the user for a new location after telling them why their previous guess
# was unacceptable.











# Display guess results.
# Clear the screen, and print a message stating that the player missed, hit,
# or sunk a ship. Prompt the next player, by name, that it is their turn and
# to press enter to continue.













# Declare a winner.
# Continue the game until one of the players has sunk all of their opponent’s ships.
# Congratulate the winner with a final message. For an exceeds, display both the
# player’s boards on the screen.




















