# Nathan Blanchard
# CS 021
# Calculates yards gained/lost based on play type, offensive stats, and defensive stats.

import random


def calculate_yards(play, offense):
    # Constants that are used
    PERCENT_CONVERSION = 100
    MAX_NUM = 100
    RUN = 0
    RUN_SHORT_NUM = 86
    RUN_SHORT_YD = 5
    RUN_LONG_NUM = 98
    RUN_LONG_YD = 25
    RUN_LOSS_CHANCE = 15
    RUN_LOSS_MIN = 1
    RUN_LOSS_MAX = 3
    SHORT = 1
    SHORT_SHORT_NUM = 84
    SHORT_SHORT_YD = 7
    SHORT_LONG_NUM = 96
    SHORT_LONG_YD = 25
    SHORT_LOSS_CHANCE = 18
    SHORT_LOSS_MIN = 2
    SHORT_LOSS_MAX = 4
    MED = 2
    MED_SHORT_NUM = 84
    MED_SHORT_YD_MIN = 3
    MED_SHORT_YD = 15
    MED_LONG_NUM = 96
    MED_LONG_YD = 35
    MED_LOSS_CHANCE = 20
    MED_LOSS_MIN = 3
    MED_LOSS_MAX = 6
    HM = 3
    HM_NUM = 86
    HM_YD = 40
    HM_LOSS_CHANCE = 30
    HM_LOSS_MIN = 4
    HM_LOSS_MAX = 7
    TD = 100

    # Yard calculation for a run. Basically just a lot of If statements.
    if play == RUN:
        chance = random.randint(0, MAX_NUM) / PERCENT_CONVERSION
        # Successful play
        if chance < offense[RUN]:
            rand_num = random.randint(0, MAX_NUM)
            if 0 <= rand_num < RUN_SHORT_NUM:
                return random.randint(1, RUN_SHORT_YD)
            elif RUN_SHORT_NUM <= rand_num < RUN_LONG_NUM:
                return random.randint(RUN_SHORT_YD + 1, RUN_LONG_YD)
            else:
                return TD
        # Unsuccessful play
        else:
            rand_num = random.randint(0, MAX_NUM)
            if rand_num <= RUN_LOSS_CHANCE:
                return -random.randint(RUN_LOSS_MIN, RUN_LOSS_MAX)
            else:
                return 0
    # Yard calculation for a short pass
    elif play == SHORT:
        chance = random.randint(0, MAX_NUM) / PERCENT_CONVERSION
        # Successful play
        if chance < offense[SHORT]:
            rand_num = random.randint(0, MAX_NUM)
            if 0 <= rand_num < SHORT_SHORT_NUM:
                return random.randint(1, SHORT_SHORT_YD)
            elif SHORT_SHORT_NUM <= rand_num < SHORT_LONG_NUM:
                return random.randint(SHORT_SHORT_YD + 1, SHORT_LONG_YD)
            else:
                return TD
        # Unsuccessful play
        else:
            rand_num = random.randint(0, MAX_NUM)
            if rand_num <= SHORT_LOSS_CHANCE:
                return -random.randint(SHORT_LOSS_MIN, SHORT_LOSS_MAX)
            else:
                return 0
    # Yard calculation for a medium pass
    elif play == MED:
        chance = random.randint(0, MAX_NUM) / PERCENT_CONVERSION
        # Successful play
        if chance < offense[MED]:
            rand_num = random.randint(0, MAX_NUM)
            if 0 <= rand_num < MED_SHORT_NUM:
                return random.randint(MED_SHORT_YD_MIN, MED_SHORT_YD)
            elif MED_SHORT_NUM <= rand_num < MED_LONG_NUM:
                return random.randint(MED_SHORT_YD + 1, MED_LONG_YD)
            else:
                return TD
        # Unsuccessful play
        else:
            rand_num = random.randint(0, MAX_NUM)
            if rand_num <= MED_LOSS_CHANCE:
                return -random.randint(MED_LOSS_MIN, MED_LOSS_MAX)
            else:
                return 0
    # Yard calculation for a hail mary
    else:
        chance = random.randint(0, MAX_NUM) / PERCENT_CONVERSION
        # Successful play
        if chance < offense[HM]:
            rand_num = random.randint(0, MAX_NUM)
            if rand_num < HM_NUM:
                return HM_YD + rand_num // 7
            else:
                return TD
        # Unsuccessful play
        else:
            rand_num = random.randint(0, MAX_NUM)
            if rand_num <= HM_LOSS_CHANCE:
                return -random.randint(HM_LOSS_MIN, HM_LOSS_MAX)
            else:
                return 0
