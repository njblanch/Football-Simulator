# Skyler Heininger
# CS 021
# This will basically

# When this function is called, it creates a new user by taking inputs
# and validating that the username or such is not taken
def make_user(inpfile):
    # Open the file that has the save states
    infile = open(inpfile, "r")

    # Get dictionary of all names as keys and all resulting data for each user
    # Uses a for loop and splitting by "\n" to get all the values and store into dictionary.
    text = infile.read()
    infile.close()
    users = text.split("\n")
    user_dictionary = {}
    usernames = set()
    for items in users:
        data = items.split(":")
        username = data[0]
        usernames.add(username)
        del data[0]
        user_dictionary[username] = data

    # Get a username from the user. If the username is already in the dictionary.
    username = input("What do you want your username to be? ")
    while username in usernames:
        if username != "":
            print("This username is already taken.")
            username = input("What do you want your username to be? ")
        else:
            username = input("Enter an actual username: ")

    # Use a loop to validate the password of the user is good.
    # The while loop has "" as a sort of sentinel,
    # returned when the user decides to choose a new password
    password = check_password()
    while password == "":
        password = check_password()
    return username, password


# Validates the inputted password
def check_password():
    password = input("Input password: ")
    # Checks to make sure that the user has both uppercase and lowercase letters in password
    while password == password.lower():
        password = input("Put in an input that has at least one uppercase letter.\n")
    # Have user input their password again to validate it. Uses while loop to validate that
    # it is not same password and exits loop if there is a new password wanted.
    password1 = input("Put in password again to validate it: ")
    while password1 != password:
        password1 = input("Please put in the same password as you entered before\n"
                          "(press enter to make a new password): ")
        if password1 == "":
            return ""
    return password

