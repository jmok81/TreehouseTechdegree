import sys
import os


def title_screen():
    print("     _           _   _   _           _     _         ")
    print("    | |         | | | | | |         | |   (_)        ")
    print("    | |__   __ _| |_| |_| | ___  ___| |__  _ _ __    ")
    print("    | '_ \ / _` | __| __| |/ _ \/ __| '_ \| | '_ \   ")
    print("    | |_) | (_| | |_| |_| |  __/\__ \ | | | | |_) |  ")
    print("    |_.__/ \__,_|\__|\__|_|\___||___/_| |_|_| .__/   ")
    print("                                            | |      ")
    print("                                            |_|      ")
    print("\n")

    start_game = input(" To commence your Battle press Enter, or to Quit press Q \n > ").lower()
    if start_game == 'q':
       sys.exit()
    else:
       pass

def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def player_names():
    player_one = (input("Please enter Player One's name: ")).strip()
    print("Welcome {}".format(player_one))
    input("Press Enter to continue...")
    clear_screen()
    player_two = (input("Please enter Player Two's name: ")).strip()
    print("Welcome {}".format(player_two))

    #def test(self):
        #self.test1 = Board()
        #self.test1.title_screen()


def game():
    clear_screen()
    title_screen()
    clear_screen()
    player_names()



