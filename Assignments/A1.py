import math

print('Hello, Welcome to Planet Manager!\nPlease selection one of the following options: ')

# This variable below determines if the code will continue based on the user input in the menu.

selection_input = False

'''

Below is the menu setup in a loop, with a set variable (selection_input), that if set to "True" will 
break the loop and continue the code.

'''

while not selection_input:
    selection = input('a) Register Planet \nb) Planet Info\nYour Selection: ')

    if selection == 'a':
        print('You have chosen \'Register Planet!\'')
        selection_input = True
    elif selection == 'b':
        print('You have chosen \'Planet Info!\'')
        selection_input = True
    else: print('Please enter a valid input of \'a\' or \'b\' ')

if selection_input:
    print('nice')