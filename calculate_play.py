# Skyler Heininger, Nathan Blanchard
# CS 021
# Contains functions for choosing plays
import random

# This function finds the likelihood of plays happening
# based on various factors such as team statistics
def user_play():
    # get user input for what play they want to make
    # Basically is just a while loop for returning the play to the index
    play = -1
    while play not in range(1, 5):
        try:
            play = int(input("What play do you want to make?\n"
                             "1) Run\n"
                             "2) Short Pass\n"
                             "3) Medium Pass\n"
                             "4) Hail Mary\n"))
        except ValueError:
            print("\nInvalid play type entered, please try again")
            play = -1
    # Returning play - 1 is so that it matches the indices of other lists in other functions
    return play - 1

# Chooses a play for the computer based on distance to first down and current down
def computer_play(yard, fd, down):
    # Creates constants
    FIRST_DOWN = 1
    SECOND_DOWN = 2
    THIRD_DOWN = 3
    FOURTH_DOWN = 4
    MAX_NUM = 100
    # Calculates the distance to the first down line
    distance = fd - yard
    # Creates a random number from 0 to 100, this is used later for play type probability
    rand_num = random.randint(0, MAX_NUM)
    # Chooses a play if it is first down
    if down == FIRST_DOWN:
        # standard first down
        if distance == 10:
            if rand_num <= 15:
                return 2
            elif rand_num <= 50:
                return 1
            else:
                return 0
        # near end zone
        else:
            if rand_num <= 10:
                return 2
            elif rand_num <= 65:
                return 1
            else:
                return 0
    # Chooses a play if it is second down
    elif down == SECOND_DOWN:
        # far
        if distance >= 10:
            if rand_num <= 35:
                return 2
            elif rand_num <= 80:
                return 1
            else:
                return 0
        # medium
        elif distance > 6:
            if rand_num <= 40:
                return 2
            elif rand_num <= 80:
                return 1
            else:
                return 0
        # close
        elif distance > 3:
            if rand_num <= 45:
                return 1
            elif rand_num <= 90:
                return 0
            else:
                return 2
        # very close
        else:
            if rand_num <= 80:
                return 0
            else:
                return 1
    # Chooses a play if it is third down
    elif down == THIRD_DOWN:
        # very far
        if distance > 15:
            if rand_num <= 70:
                return 2
            elif rand_num <= 85:
                return 1
            else:
                return 3
        # far
        elif distance >= 10:
            if rand_num <= 80:
                return 2
            elif rand_num <= 95:
                return 1
            else:
                return 0
        # medium
        elif distance > 6:
            if rand_num <= 60:
                return 2
            elif rand_num <= 95:
                return 1
            else:
                return 0
        # close
        elif distance > 3:
            if rand_num <= 45:
                return 1
            elif rand_num <= 85:
                return 0
            else:
                return 2
        # very close
        else:
            if rand_num <= 85:
                return 0
            else:
                return 1
    # Chooses a play if it is fourth down
    else:
        # very far
        if distance > 15:
            if rand_num <= 70:
                return 3
            else:
                return 2
        # far
        elif distance >= 10:
            if rand_num <= 30:
                return 3
            elif rand_num <= 95:
                return 2
            else:
                return 1
        # medium
        elif distance > 6:
            if rand_num <= 65:
                return 2
            else:
                return 1
        # close
        elif distance > 3:
            if rand_num <= 80:
                return 1
            else:
                return 2
        # very close
        else:
            if rand_num <= 90:
                return 0
            else:
                return 1