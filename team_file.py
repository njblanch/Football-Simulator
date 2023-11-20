# Skyler Heininger
# CS 021
# This program takes an input file of team statistics and converts
# all of the information into useable for the rest of the program.
# The output will include two lists, one of offensive stats and one of defensive stats

def take_stats(teamname, index):
    INFILE = "teamstats.txt"
    infile = open(INFILE, "r")
    # get the team names, making sure that the user given
    # name is actually in the file
    read = infile.readline().rstrip("\n").split(",")
    index = read.index(teamname)

    # empty lists for offensive and defensive stats.
    # Iterates over the four lines containing each kind of stats
    LINES = 4
    offensive_stats = []
    defensive_stats = []
    # All values appended to lists are done so as floats for future use in math
    for i in range(LINES):
        read = infile.readline().rstrip("\n").split(",")
        offensive_stats.append(float(read[index]))
    for i in range(LINES):
        read = infile.readline().rstrip("\n").split(",")
        defensive_stats.append(float(read[index]))
    infile.close()
    return offensive_stats, defensive_stats


