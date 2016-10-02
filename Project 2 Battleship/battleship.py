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
    print("\033c", end="")


def print_board_heading():
    print("   " + " ".join([chr(c) for c in range(ord('A'), ord('A') + BOARD_SIZE)]))


def print_board(board):
    print_board_heading()

    row_num = 1
    for row in board:
        print(str(row_num).rjust(2) + " " + (" ".join(row)))
        row_num += 1



# Prompt the players for their names.
#  Refer to players using their names whenever possible.







# Display an empty board.
# Clear the screen and display an empty board on the screen.
# Use the EMPTY marker for all locations on the board.
# The board displays column headers as letters in the alphabet and displays
# numeric row numbers along the left side of the board.






# Prompt user to place a ship.
# Under the board, prompt the user to enter one ship at a time.
# For each ship, ask if they want the ship to be oriented horizontally
# or vertically then ask which location on the board the first ships
# should be placed at: Below is an example prompt. You can use a different prompt.
#Place the location of the aircraft carrier (5 spaces): a2 Is it horizontal? (Y)/N: n







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








