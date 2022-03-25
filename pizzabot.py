input_houses = ["5x5", "(0, 0)", "(1, 3)", "(4, 4)", "(4, 2)", "(4, 2)", "(0, 1)", "(3, 2)", "(2, 3)", "(4, 1)"]
# Here is where our inputted houses will go

targetHouseNum = 1  # This variable will keep track of which house we are going to

# Sets the starting co-ords for our bot
Bot_x = 0
Bot_y = 0

CommandString = ""

for i in range(len(input_houses) - 1):
    # Start of Loop

    targetHouse = input_houses[targetHouseNum]
    # Takes the co-ordinates of the house we are going to and puts it into an isolated string for analysis

    char_to_replace = \
        {
            '(': '',
            ')': '',
            ' ': ''
        }
    targetHouse = targetHouse.translate(str.maketrans(char_to_replace))
    # Replaces the brackets and spaces in out string to make an easier value to manipulate, i.e (2, 4) -> 2,4

    target_x = int(targetHouse[0])
    target_y = int(targetHouse[2])

    if Bot_x == target_x and Bot_y == target_y:
        CommandString += 'D'  # Inserts the Delivery command into our string if we are at out target destination
    else:
        # Checks to see if our Bot's x location is more or less than the target
        # so we can determine whether to go East or West
        if Bot_x < target_x:
            for a in range(target_x - Bot_x):
                CommandString += 'E'
        else:
            for a in range(Bot_x - target_x):
                CommandString += 'W'

        # Checks to see if our Bot's y location is more or less than the target
        # so we can determine whether to go North or South
        if Bot_y < target_y:
            for b in range(target_y - Bot_y):
                CommandString += 'N'
        else:
            for a in range(Bot_y - target_y):
                CommandString += 'S'

        # Updates location of Bot for the next iteration
        Bot_x = target_x
        Bot_y = target_y

        CommandString += 'D'    # inserts delivery command to String once we have arrived at target location

    # End of Loop
    targetHouseNum += 1

print(CommandString)
# Printing the end String of our direction commands

print(CommandString == 'DENNNDEEENDSSDDWWWWSDEEENDWNDEESSD')
# Checks to see if our end string is equal to the manually solved chain of directions
