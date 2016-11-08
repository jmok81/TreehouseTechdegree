import sys
import os

from player import Player

class Battleship:

    def __init__(self):
        self.title_screen()
        self.clear_screen()
        self.name = Player()
        self.name.player_names()



    def title_screen(self):
        print("     _           _   _   _           _     _         ")
        print("    | |         | | | | | |         | |   (_)        ")
        print("    | |__   __ _| |_| |_| | ___  ___| |__  _ _ __    ")
        print("    | '_ \ / _` | __| __| |/ _ \/ __| '_ \| | '_ \   ")
        print("    | |_) | (_| | |_| |_| |  __/\__ \ | | | | |_) |  ")
        print("    |_.__/ \__,_|\__|\__|_|\___||___/_| |_|_| .__/   ")
        print("                                            | |      ")
        print("                                            |_|      ")

        self.start_game = input("    To begin press Enter, or to Quit press Q".lower() )
        if self.start_game == 'q':
            sys.exit()
        else:
            pass

    def clear_screen(self):
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')


    #def test(self):
        #self.test1 = Board()
        #self.test1.title_screen()



testing = Battleship()
testing()