# Skyler Heininger, Nathan Blanchard
# CS 021
# This program displays various help data from a text file,
# will take in user input and display wanted data

# help function that will display help options for the user
# takes input to select options
def help():
    # Print help options
    print("What do you need help with?")
    # Run the help displaying function
    count, help_dict = help_text()
    # Get user input(set variable to start while loop)
    print("If you would like to see these options at any time, type \"HELP\"")
    choice = input()
    while choice != "":
        # Uses while loop to validate the choice. Goes to count + 1
        # to ensure that it is in the given range of the help file
        try:
            if choice == "HELP":
                count, help_dict = help_text()
            elif int(choice) in range(1, count + 1):
                print(help_dict[int(choice)])
                print("Do you need more help? press enter when done\n")
            else:
                print("Enter a valid choice")
        except:
            print("Enter a valid choice")
        finally:
            choice = input()
    return

# Pulls all of the help information from the help text file and stores in dictionary
def help_text():
    # Set dictionary to read to for later use
    help_dict = {}
    # Open the help file containing the information(This is a given download)
    help_file = open("footballhelp.txt", "r")
    read_help = help_file.readlines()
    # Set constants and counters
    count = 0
    HELP_INDEX = 0
    TEXT_INDEX = 1

    # For loop to make a dictionary of the help text
    for lines in read_help:
        count += 1
        line = lines.split(":")
        print(str(count) + ": " + line[HELP_INDEX].strip())
        help_dict[int(count)] = line[TEXT_INDEX].strip()
    help_file.close()
    return count, help_dict


