# Skyler Heininger, Nathan Blanchard
# CS 021
# This main function takes in all the information from other
# files of the football game and puts them together

# Import statements
import league_play
import play_game
import help
import validate_password
import make_user


def main():
    # Constants for file saving
    INFILE_SAVES = "savestates.txt"
    INFILE_TEAMS = "teamstats.txt"

    # Index lists for different things in the dictionary for user stats
    IDX_USER = 0
    IDX_PASS = 1
    IDX_TEAM = 2
    IDX_BRACKET = 3
    IDX_WINS = 4

    # First displays the option for help
    help_need = input(f"""Type "HELP" for help (anything else to play)\n""")
    if help_need == "HELP":
        help.help()

    # Before moving forward, get info on all the teams
    infile = open(INFILE_TEAMS, "r")
    teams = infile.readline().rstrip("\n").split(",")
    infile.close()

    played_before = input("Have you played before(Y / N): ")
    print()
    # basically gets the data of the given save state. The while loop has to do
    # with user verification
    if played_before.upper() == "Y":
        bracket = []
        data = validate_password.main(INFILE_SAVES)
        while data == "":
            data = validate_password.main(INFILE_SAVES)

        # Make a list for the bracket
        teamname = data[IDX_TEAM]
        bracket_initial = league_play.bracket(teamname, teams)
        data.append(bracket_initial)
        bracket_initial = data[IDX_BRACKET].lstrip("[").rstrip("]").split(",")
        LENGTH = len(bracket_initial)
        # For loop to make the bracket from the previously made data
        for index in range(LENGTH):
            team = bracket_initial[index].strip().strip("'")
            bracket.append(team)

    else:
        # make a username and password for the user by calling make_user
        username, password = make_user.make_user(INFILE_SAVES)
        print()
        # basically start to go through building a data save for the user:
        data = [username, password]
        teamname = ""
        # Also display list of teams for user to choose from
        while teamname not in teams:
            print("Here are your choices for teams")
            for item in teams:
                print(item)
            teamname = input("What team do you want to play as?\n")
        # Further data making for the user. This will effectively be
        # used for saving user data at the end of the game
        data.append(teamname)
        bracket = league_play.bracket(teamname, teams)
        data.append(bracket)
        data.append(0)
        bracket = data[IDX_BRACKET]



    # Check to make sure that this save has not already played all games.
    # If user has played the three games, then will exit the program. This
    # will also write out the saved data again
    if str(bracket) == "['']":
        print("This save already has finished the game.")
        outfile = open(INFILE_SAVES, "a")
        bracket_string = str(data[IDX_BRACKET]).lstrip("[").rstrip("]")
        data_str = str(f"{data[IDX_USER]}:{data[IDX_PASS]}:{data[IDX_TEAM]}:"
                       f"{bracket_string}:{data[IDX_WINS]}\n")
        outfile.write(data_str)
        return


    # Makes a loop for playing a game for each team in the bracket
    NEXT_TEAM_IDX = 1
    # Bracket copy for use later
    bracket1 = [] + bracket
    number_games = 0
    for compteam in bracket1:
        outcome, win_loss = play_game.game(teamname, compteam.strip("'"))
        wins = int(data[IDX_WINS])
        wins += win_loss
        data[IDX_WINS] = wins
        # remove the team from the bracket only if the user finishes the game

        data[IDX_BRACKET] = bracket
        if outcome:
            del bracket[0]
        if number_games < len(bracket1) - 1:
            next_game = ""
            while next_game.lower() != "n" and next_game.lower() != "y":
                next_game = input(f"Do you want to play the next game against {bracket1[NEXT_TEAM_IDX]} (Y/N)?\n"
                                  f"If not, the current standings will be saved.\n")
                if next_game.lower() == "n":
                    next_game = input(f"Are you sure? (Y/N)\n")
                    if next_game.lower() == "y":
                        # Write the saved data to the output file
                        outfile = open(INFILE_SAVES, "a")
                        bracket_string = str(data[IDX_BRACKET]).lstrip("[").rstrip("]")
                        data_str = str(f"{data[IDX_USER]}:{data[IDX_PASS]}:{data[IDX_TEAM]}:"
                                       f"{bracket_string}:{data[IDX_WINS]}\n")
                        outfile.write(data_str)
                        return
        else:
            print("That is all the games played in the bracket!")
        NEXT_TEAM_IDX += 1
        number_games += 1


    # Write the saved data to the output file
    outfile = open(INFILE_SAVES, "a")
    bracket_string = str(data[IDX_BRACKET]).lstrip("[").rstrip("]")
    data_str = str(f"{data[IDX_USER]}:{data[IDX_PASS]}:{data[IDX_TEAM]}:"
                   f"{bracket_string}:{data[IDX_WINS]}\n")
    outfile.write(data_str)

    # Prints a final statement to show user how many games of bracket they won
    if data[IDX_WINS] == 3:
        print("Congrats! You won all the games!")
    elif data[IDX_WINS] == 2:
        print("Good job! You won two of the games.")
    elif data[IDX_WINS] == 1:
        print(f"Nice Job. You won one of the games.")
    elif data[IDX_WINS] == 0:
        print(f"It's ok. You'll win one next time.")


main()



