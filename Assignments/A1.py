import math

'''

 To make the output cleaner and easier to read, i implemented a divider using the below format to
 divide code sections in the terminal to make it easier to visualize what part of code is what.

'''

divider = '-=+------------------------------------+=-'

# These boolean determines if the code will continue based on the user input in the menu.
# The escape boolean works such that, if "esc" is inputted, it will shut down the program.

selection_input = False

escape_input = False

'''

Part #1 Below is the menu setup in a loop, with a set variable (selection_input), that if set to 
"True" will break the loop and continue the code.

'''

while not selection_input: # Will keep asking until the condition is satisfied, 'esc', 'a', or 'b'.
    print(f'{divider}\nHello, Welcome to Planet Manager!\nPlease select one of the following options: ')
    selection = input('a) Register Planet \nb) Planet Info\nesc) Close Program\n[Your Selection]: ')
    selection = selection.lower()

    if selection == 'esc':     # To escape the loop and "shutdown" the program. Refer to next #.
        selection_input = True
        escape_input = True

    elif selection == 'a':
        print(f'{divider}\nYou have chosen \'Register Planet!\'\n{divider}')
        selection_input = True

    elif selection == 'b':
        print(f'{divider}\nYou have chosen \'Planet Info!\n{divider}')
        selection_input = True

    elif escape_input == True and selection_input == True:   # If 'esc' is typed, program will stop.
        print(f'{divider}\nThe program has been successfully shut down.\n{divider}')

    else: 
        print(f'{divider}\nPlease enter a valid input of \'a\', \'b\', or \'esc\'\n{divider}')

    # Part 2
    if selection_input == True and selection == 'a':
        print('Please answer appropriately to the following: ')

        planet_name = input('The name of the planet: ')
        planet_radius = input('The radius of the planet: ')
        selection_input = False # This at the end will output all the code above it and return to the original loop


    elif selection_input == True and selection == 'b':
        print(f'Here is the following information about the planet:\n[{planet_name}]')
        
