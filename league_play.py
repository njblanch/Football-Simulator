# Skyler Heininger
# Cs 021
# This function takes in a given team name, which was already verified,
# and makes a bracket. This is done simply using a randomizer.
import random


def bracket(teamname, team_list):
    # get a list of the team names
    index = team_list.index(teamname)
    team_list.remove(teamname)
    bracket_list = []
    # randomly gets the names of three teams (no repeats)
    for i in range(0, 3):
        compteam = random.choice(team_list)
        bracket_list.append(compteam)
        team_list.remove(compteam)
    return bracket_list



