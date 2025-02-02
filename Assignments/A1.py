import math

'''

To make the output cleaner and easier to read, i implemented a divider using the below 'divider', 
as a way to divide the code sections in the terminal to make it easier to visualize what part of 
code is what.

'''

divider = '-=+------------------------------------+=-'

# These following booleans determines if the code will continue based on the user input in the menu.

selection_input = False # If the required input in the menu is satisified, will exit the menu and follow the code.

escape_input = False # The escape boolean works such that, if "esc" is inputted, it will shut down the program.

planet_status = False # Will determine if a planet is registered or not. Selecting 'b' beforehand will print an error message.

# These values will continue or break the loop depending on user input. Used in "Part 2".

planet_radius = -1.0
planet_velocity = -1.0
planet_temperature = -1.0

# The following is for the equations used in "Part 3"



'''

Part #1 Below is the menu setup in a loop, with a set variable (selection_input), that if set to 
"True" will break the loop and continue the code.

'''

while not selection_input: # Will keep asking until the condition is satisfied, 'esc', 'a', or 'b'.
    print(f'{divider}\nHello, Welcome to Planet Manager!\nPlease select one of the following options: ')
    selection = input('a) Register Planet \nb) Planet Info\nesc) Close Program\n[Your Selection]: ')
    selection = selection.lower()

    if selection == 'esc':     # To escape the loop and "shutdown" the program.
        selection_input = True # Setting this function to True will break the loop and continue the program.
        print(f'{divider}\nThe program has been successfully shut down.\n{divider}')

    elif selection == 'a':
        print(f'{divider}\nYou have chosen \'Register Planet!\'')
        selection_input = True

    elif selection == 'b' and planet_status == False: # Refer to boolean variables at the start.
        print(f'{divider}\nYou have not yet registered a planet, please do so first.')

    elif selection == 'b' and planet_status == True:
        print(f'{divider}\nYou have chosen \'Planet Info!\n{divider}')
        selection_input = True

    else: 
        print(f'{divider}\nPlease enter a valid input of \'a\', \'b\', or \'esc\'')

    # Part 2: Registering planet and outputing new values based on userinput

    if selection_input == True and selection == 'a':
        print(f'{divider}\nPlease answer appropriately to the following:\n ')
        planet_name = input('The name of the planet: ')

        while planet_radius < 0 or planet_velocity < 0 or planet_temperature < 0: # If either is negative, will make an error message to retry.

            planet_radius = float(input('The radius of the planet?: '))
            planet_velocity = float(input('What is the tangential velocity of the planet?: '))
            planet_temperature = float(input('What is the temperature of the planet?: '))

            if planet_radius > 0 and planet_velocity > 0 and planet_temperature > 0:
                planet_status = True # Confirm that the planet exists.
                selection_input = False # This at the end of this if statement will output all the code above it and return to the original while loop (menu)
            else:
                print(f'{divider}\n Please enter positive values.\n{divider}') 

# Part 3: If all the conditions are satisified, it will print calculated values of the equations regarding the planet.

    elif selection_input == True and selection == 'b' and planet_status == True: 
        print(f'Here is the following information about the planet:\n[{planet_name}]')
        print(f'Radius: {planet_radius} m\nVelocity: {planet_velocity} m/s\nTemperature: {planet_temperature}')

        selection_input = False
        