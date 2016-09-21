"""
Treehouse Techdegree - Python Web Development
Build a Soccer League

INSTRUCTIONS
PART 1:
We have provided information for the 18 players in the attached file. Read the data from the file and store it in an appropriate data type so that it can be used in Part 2.

PART 2:
Create logic that can iterate through all 18 players and assign them to teams such that each team has the same number of players.
The number of experienced players on each team should be the same. Store each team’s players in its own new collection variable for use in Part 3.
Please note: your logic should work correctly regardless of the initial ordering of the players.

PART 3:
Create logic that iterates through all three teams of players and generates a personalized letter to the guardians,
letting them know which team the child has been placed on and when they should attend their first team team practice.
As long as you provide the necessary information (player name, guardians’ names, practice date/time), feel free to have fun with the content of the letter.

The team practice dates/times are as follows: Dragons - March 17, 1pm, Sharks - March 17, 3pm, Raptors - March 18, 1pm
"""

import csv

# PART 1: Read soccer_players.csv, convert player data to a dictionary and return a list of the player dictionaries
def read_data ():
    with open('soccer_players.csv', newline='' ) as csvfile:
        soccerreader = csv.DictReader(csvfile, delimiter=',')
        players_info = list(soccerreader)
    return players_info


# PART 2: Seperate the players into 2 groups: Experienced Players (exp_players) and Non-experienced Players (non_players)
players_info = read_data()
def experience(players_info):
    exp_players = []
    non_players = []
    for player in players_info:
        if player['Soccer Experience'] == 'YES':
            exp_players.append(player)
        else:
            non_players.append(player)
    return exp_players, non_players

# PART 2: Assign players to teams. The same number of Experienced Players are on each team

exp_players, non_players = experience(players_info)
def assign(exp_players, non_players):
    dragons= []
    sharks = []
    raptors = []
    teams = (dragons, sharks, raptors)
    # Loop through each team assigning an Experienced Player(exp_players) and Non-experienced Player(non_players)
    while True:
        try:
            for team in teams:
                team.append(exp_players.pop())
                team.append(non_players.pop())
        except IndexError:
            break

    return dragons, sharks, raptors, teams


# PART 3: Add additional information to player dictionaries for use in Team Letters
dragons, sharks, raptors, teams = assign(exp_players, non_players)
def add_info(dragons, sharks, raptors):
    for player in dragons:
         player.update({'Team':'Dragons', 'Practice':'March 17 at 1pm'})

    for player in sharks:
         player.update({'Team':'Sharks', 'Practice':'March 17 at 3pm'})

    for player in raptors:
         player.update({'Team':'Raptors', 'Practice':'March 18 at 1pm'})

# PART 3: Template for personalised letters to each player
def template():
    letter_info = """
                        Soccer League - Team {Team}

        Dear {Guardian Name(s)},


        I would like to welcome you and {Name} to the new season.
        This year {Name} will be playing for the {Team}
        The first practice for the season will be on {Practice}

        We are all looking forward to a great year!

        Regards

        Coach
        """

    return letter_info

# PART 3: Iterate through all three teams of players and generates a personalised letter
letter_info = template()
def letter(teams, letter_info):
    for team in teams:
        for player in team:
            letter = open("{}.txt".format(("_".join(player['Name'].split()))).lower(), 'w')
            letter.write(letter_info.format(**player))


# Run through the different functions
def main():
    read_data()
    experience(players_info)
    assign(exp_players, non_players)
    add_info(dragons, sharks, raptors)
    template()
    letter(teams, letter_info)

#  Ensure your script doesn't execute when imported
if __name__ == "__main__":
    main()