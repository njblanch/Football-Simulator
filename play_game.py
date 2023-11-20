# Skyler Heininger and Nathan Blanchard
# CS 021
# This function will play out an entire game with a user
import team_file
import random
import calculate_play
import yards
import time


def game(user_team, computer_team):
    # Print an opening statement for the game
    print(f"You are playing the {computer_team}")

    # get stats for user team and computer team
    infile = open("teamstats.txt", "r")
    read = infile.readline().rstrip("\n").split(",")
    infile.close()
    # Gets the team stats from the team stats file, for both user and computer
    user_index = read.index(user_team)
    computer_index = read.index(computer_team)
    user_offense, user_defense = team_file.take_stats(user_team, user_index)
    computer_offense, computer_defense = team_file.take_stats(computer_team, computer_index)

    # Changes the offensive stats to acknowledge the defensive stats
    for i in range(0, len(user_offense)):
        user_offense[i] -= computer_defense[i]

    for i in range(0, len(computer_offense)):
        computer_offense[i] -= user_defense[i]


    # Go through a coin toss, using input validation and error handling
    print("A coin toss will decide who starts with the ball")
    coin = random.randint(0, 1)
    user_coin = -1
    while user_coin == -1 and user_coin != "heads" and user_coin != "tails":
        try:
            user_coin = input("Take a guess for which side (Heads/Tails) ").lower()
        except ValueError:
            print("Enter a valid input")
            user_coin = -1

    # The illusion of choice :)
    if coin == 0:
        turn1 = "user"
    else:
        turn1 = "computer"

    # if statement to determine who is driving/defending first. Call function for plays
    # Set variables for yards to be added to by called function each time
    user_score = 0
    computer_score = 0

    # Overarching while loop to keep playing until a team has gotten 21 points
    while user_score < 21 and computer_score < 21:
        # If statement uses the coin flip to determine if the user is going first
        if turn1 == "user":
            # Reset constants since will be used multiple times in the while loop
            yard_down = 10
            yard = 0
            down = 1
            print("It is now the user's turn.\n")
            # While loop to keep playing through the user's four downs
            while down <= 4 and yard < 100:
                print(f"It is down {down}.")
                # This will get the play type and the yards gained.
                # These will be used in the following statements.
                play_type = calculate_play.user_play()
                yard_gained = yards.calculate_yards(play_type, user_offense)
                yard += yard_gained
                td_yard = 100 - yard
                # If statement will make sure that yard never goes negative
                # (can't go negative in yards on the field)
                if yard < 0:
                    td_yard = 100
                    yard = 0
                    yard_gained = 0
                # Nested if/elif/else statements to determine outputs to the user.
                # Each one will give the outcome of a play.
                if yard_down < 100:
                    if yard >= 100:
                        print(f"You gained {100 - yard + yard_gained} yards and got a touchdown!\n"
                              f"The score is now...\n"
                              f"User: {user_score + 7}\n"
                              f"Computer: {computer_score}\n")
                    elif yard >= yard_down:
                        yard_down = yard + 10
                        down = 0
                        if yard_down < 100:
                            print(f"You passed the first down line!\n"
                                f"You gained {yard_gained} yard(s).\n"
                                f"You are {yard_down - yard} yard(s) from the first down line.\n"
                                f"You are {td_yard} yard(s) away from the touchdown line.\n")
                        else:
                            print(f"You passed the first down line!\n"
                                f"You gained {yard_gained} yard(s).\n"
                                f"You are {td_yard} yard(s) away from the touchdown line.\n")
                    else:
                        if yard_gained > 0:
                            print(f"You gained {yard_gained} yard(s).\n"
                                  f"You are {yard_down - yard} yards from the first down line.\n"
                                  f"You are {td_yard} yard(s) away from the touchdown line.\n")
                        elif yard_gained < 0:
                            print(f"You lost {-yard_gained} yard(s).\n"
                                  f"You are {yard_down - yard} yard(s) from the first down line.\n"
                                  f"You are {td_yard} yard(s) away from the touchdown line.\n")
                        else:
                            print(f"You gained no yards\n"
                                  f"You are still {yard_down - yard} yard(s) from the first down line.\n"
                                  f"You are still {td_yard} yard(s) away from the touchdown line.\n")
                else:
                    if yard >= 100:
                        print(f"You gained {100 - yard + yard_gained} yard(s) and got a touchdown!\n"
                              f"The score is now...\n"
                              f"User: {user_score + 7}\n"
                              f"Computer: {computer_score}\n")
                    elif yard >= yard_down:
                        yard_down = yard + 10
                        down = 1
                        print(f"You passed the first down line!\n"
                              f"You gained {yard_gained} yard(s).\n"
                              f"You are {td_yard} yard(s) away from the touchdown line.\n")
                    else:
                        if yard_gained > 0:
                            print(f"You gained {yard_gained} yard(s).\n"
                                  f"You are {td_yard} yard(s) away from the touchdown line.\n")
                        elif yard_gained < 0:
                            print(f"You lost {-yard_gained} yard(s).\n"
                                  f"You are {td_yard} yard(s) away from the touchdown line.\n")
                        else:
                            print(f"You gained no yards\n"
                                  f"You are still {td_yard} yard(s) away from the touchdown line.\n")

                # Add one to down for the while loop
                down += 1
                # Sleep so that user has time to read the given code
                time.sleep(2)
            # If statement to add to user's score if the user makes a touchdown
            if yard >= 100:
                user_score += 7
        # Reset play variables and make turn1 "user" so that the user will have alternating
        # turns with the computer from now on.
        turn1 = "user"
        yard_down = 10
        yard = 0
        down = 1

        # If statement to make sure that the user did not get a touchdown in their last play
        if user_score < 21 and computer_score < 21:
            print("It is now the computer's turn.\n")
            while down <= 4 and yard < 100:
                # Time to make computer output readable to the user
                time.sleep(4)
                print(f"It is down {down}.")
                play_type = calculate_play.computer_play(yard, yard_down, down)
                # Make a dictionary for plays, use it to display the output (faster than if statements)
                comp_dict = {0: "Computer ran the ball.", 1: "Computer threw a short pass.",
                             2: "Computer threw a medium pass.", 3: "Computer threw a Hail Mary."}
                print(comp_dict[play_type])
                yard_gained = yards.calculate_yards(play_type, computer_offense)
                yard += yard_gained
                td_yard = 100 - yard
                # Make sure yard doesn't go negative
                if yard < 0:
                    td_yard = 100
                    yard = 0
                    yard_gained = 0
                # Set down lower once the computer gets a first down
                if yard >= yard_down:
                    yard_down = yard + 10
                    down = 0
                    print(f"The computer got a first down.")
                # Nested if/elif/else statements to display proper output to the user.
                if yard_down < 100:
                    if yard >= 100:
                        print(f"The computer gained {100 - yard + yard_gained} yards and got a touchdown!\n"
                              f"The score is now...\n"
                              f"User: {user_score}\n"
                              f"Computer: {computer_score + 7}\n")
                    elif yard_gained > 0:
                        down += 1
                        print(f"The computer gained {yard_gained} yard(s).\n"
                              f"The computer is {yard_down - yard} yard(s) from the first down line.\n"
                              f"The computer is {td_yard} yard(s) from a touchdown.\n")
                    elif yard_gained < 0:
                        down += 1
                        print(f"The computer lost {-yard_gained} yard(s).\n"
                              f"The computer is {yard_down - yard} yard(s) from the first down line.\n"
                              f"The computer is {td_yard} yard(s) from a touchdown.\n")
                    else:
                        down += 1
                        print(f"The computer gained no yards.\n"
                              f"The computer is still {yard_down - yard} yard(s) from the first down line.\n"
                              f"The computer is still {td_yard} yard(s) from a touchdown.\n")

                else:
                    if yard >= 100:
                        print(f"The computer gained {100 - yard + yard_gained} yard(s) and got a touchdown!\n"
                              f"The score is now...\n"
                              f"User: {user_score}\n"
                              f"Computer: {computer_score + 7}\n")
                    elif yard_gained > 0:
                        down += 1
                        print(f"The computer gained {yard_gained} yard(s).\n"
                              f"The computer is {td_yard} yard(s) from a touchdown.\n")
                    elif yard_gained < 0:
                        down += 1
                        print(f"The computer lost {-yard_gained} yard(s).\n"
                              f"The computer is {td_yard} yard(s) from a touchdown.\n")
                    else:
                        down += 1
                        print(f"The computer gained no yards.\n"
                              f"The computer is still {td_yard} yard(s) from a touchdown.\n")

        # If statement to add to the computer's score
        if yard >= 100:
            computer_score += 7

    # Determines the result of the game, and returns a given value to be stored
    # win_loss and outcome are used in main with data storing
    if user_score >= 21:
        print(f"The user won against {computer_team}.\n"
              f"The score was {user_score} to {computer_score}.")
        outcome = True
        win_loss = 1
    else:
        print(f"{computer_team} won against the user.\n"
              f"The score was {computer_score} to {user_score}")
        outcome = True
        win_loss = 0

    return outcome, win_loss
