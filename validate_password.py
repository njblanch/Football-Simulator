# Skyler Heininger
# CS 021
# This program is essentially a function that checks a user's
# inputted password to validate that it is the user's save file

def main(file_name):
    # Open the file that has the save states
    infile = open(file_name, "r")

    # Get dictionary of all names as keys and all resulting data for each user
    text = infile.read()
    infile.close()
    users = text.split("\n")
    user_dictionary = {}
    for items in users:
        data = items.split(":")
        username_key = data[0]
        user_dictionary[username_key] = data


    # Get user input, double checking to make sure it's in the file,
    # also pop it out so that we can re-write it in later for saving
    stats = ""
    username = ""
    while stats == "":
        username = input("Please enter your username: ")
        while username == "":
            username = input("Please enter an actual username: ")
        stats = user_dictionary.pop(username, "")

    # Index lists for different things in the dictionary for user stats
    IDX_USER = 0
    IDX_PASS = 1
    IDX_TEAM = 2
    IDX_BRACKET = 3
    IDX_WINS = 4
    outfile = open(file_name, "w")
    user_dictionary = user_dictionary.items()
    # Uses for loop to iterate and add to the dictionary
    for user, data in user_dictionary:
        if user != "":
            data_str = str(f"{data[IDX_USER]}:{data[IDX_PASS]}:{data[IDX_TEAM]}:"
                           f"{data[IDX_BRACKET]}:{data[IDX_WINS]}\n")
            outfile.write(data_str)
    outfile.close()
    # Get the password from the list of stats for the user
    PASSWORD_INDEX = 1
    user_password = stats[PASSWORD_INDEX]

    password = str(input("Put in your password: "))
    tries = 0
    # Validate that the password is correct and within the
    # correct number of tries (3)
    while password != user_password and tries < 2:
        password = str(input(f"Incorrect password for {username}.\n"
                             f"Put in your password: "))
        tries += 1


    # Set constant for invalids
    INVALID = "Too many invalid passwords, savestate deleted."

    # logic to return different things based on outcomes of putting in password
    if tries == 2:
        print(INVALID)
        return ""
    elif password == user_password:
        return stats
    else:
        return ""


