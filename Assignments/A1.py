import math

'''

- To make the output cleaner and easier to read, I implemented a divider using the below 'divider', 
as a way to divide the code sections in the terminal to make it easier to visualize what part of 
code is what.
- [] indicates the line of code, e.g., [18] indicates line 18.

'''

divider = '-=+------------------------------------+=-'

# These following booleans determines if the code will continue based on the user input in the menu.

selection_input = False # If the required input in the menu is satisified, will exit the menu and 
#                         follow the code. If set set to False, will return to main menu.

planet_status = False # Will determine if a planet is registered or not. Selecting 'b' beforehand 
#                       results into a error message, saying to input a planet first.

# The following is for part 4, a string to store the planet data(s) [108] - [115]

planet_data = ''


'''

Part 1, below is the menu setup in a loop, with a set variable (selection_input), that if set to 
"True" will break the loop and continue the code. If set to "False", will return to this main menu.

'''

print(f'{divider}\nHello, Welcome to Planet Manager!')

while not selection_input: # Will keep asking until the condition is satisfied, 'esc', 'a', or 'b'.
    selection = input('Please select one of the following options:\na) Register Planet\
    \nb) Planet Info\nesc) Close Program\n[Your Selection]: ').lower()

    if selection == 'esc':     # To escape the loop and "shutdown" the program.
        selection_input = True # If set to true, it will break out of the loop/continue the program.
        print(f'{divider}\nThe program has been successfully shut down.\n{divider}')

    elif selection == 'a': 
        print(f'{divider}\nYou have chosen \'Register Planet!\'')
        selection_input = True

    elif selection == 'b' and not planet_status: # Refer to boolean variables at the start.
        print(f'{divider}\nYou have not yet registered a planet, please do so first.\n{divider}')

    elif selection == 'b' and planet_status == True:
        print(f'{divider}\nYou have chosen \'Planet Info!\'\n{divider}')
        selection_input = True

    else: 
        print(f'{divider}\nPlease enter a valid input of \'a\', \'b\', or \'esc\'\n{divider}') 
            # If no valid input, prints out error code.

    # Part 2, 4: Registering planet to planet_data and outputing new values based on user input. 

    if selection_input == True and selection == 'a':
        print(f'{divider}\nPlease answer appropriately to the following:\n ')
        planet_name = input('The name of the planet: ').strip()
        # The code below allows another input of another planet if inputted before.
        planet_radius = -1.0
        planet_velocity = -1.0
        planet_temperature = -1.0

        '''

        Below is a loop where it asks for user input regarding information about the planet and will
        return with an error message if the value is less than 0, and asks them to try again with
        a positive value.

        '''
        
        # If any input is negative, will make an error message to retry.
        while planet_radius < 0 or planet_velocity < 0 or planet_temperature < 0: 
                
            planet_radius = float(input('The radius of the planet?: '))
            if planet_radius < 0 :
                print(f'{divider}\nPlease enter a positive value.\n{divider}')
            else:
                while planet_velocity < 0:
                    planet_velocity = float(input('The tangential velocity of the planet?: '))
                    if planet_velocity < 0:
                        print(f'{divider}\nPlease enter a positive value.\n{divider}')
                    else:
                        while planet_temperature < 0:
                            planet_temperature = float(input('The temperature of the planet?: '))
                            if planet_temperature <0:
                                print(f'{divider}\nPlease enter a positive value.\n{divider}')
                            else:
                                print(f'{divider}')

        # Code below will add the inputted values towards a new string that will add to another,  
        # if it is the initial planet, only such information will be printed, refer to [114-115].    
        new_planet = f'{planet_name},{planet_radius},{planet_velocity},{planet_temperature}'

        # Adding if statement to determine if ";" should be added in "planet_data" which seperates 
        # the planets, and their seperate information. Above comments explains the else statement.
        if planet_data:
            planet_data += ';' + new_planet
        else:
            planet_data = new_planet

        # Positive number constraint satisfied below

        if planet_radius > 0 and planet_velocity > 0 and planet_temperature > 0:
            planet_status = True # Confirms that the planet exists.
            selection_input = False # Output all the code above it and returns to the menu.

        # Part 3, and 4.
        
    elif selection_input == True and selection == 'b' and planet_status == True: 
        start_index = 0  

# Below code will process planet_data from the start, looking for ";" to seperate the planets 
# and their information.       

        while start_index < len(planet_data):
            end_index = planet_data.find(';', start_index)
            if end_index == -1: # If no ";", it indicates it is the last planet.
                end_index = len(planet_data)

            # Planet Name Index, # the code below extracts the seperated planet
            
            planet_input = planet_data[start_index:end_index]
            # Finds the first "," seperator, which indicates the first planet name. [142]
            name_index_end = planet_input.find(',')
            if name_index_end == -1:
                selection_input = False  # If no ',' indicates single planet, and returns to menu.
            else: # If more than 2 planets, it will continue the loop.
                planet_name = planet_input[:name_index_end] 
                name_index = planet_input[:name_index_end] 
                # Takes the string input until the first ",". [146] and [147]

            # Planet Radius Index

            # Skips the first "," because name_index_end finds the first ",". [155]
            # Takes the string input after the second "," before the third "," [156] and [157]

            radius_index_start = name_index_end + 1 
            radius_index_end = planet_input.find(',', radius_index_start) 
            radius_index = float(planet_input[radius_index_start:radius_index_end]) 

            # Planet Velocity Index - Pattern from above essentially just continues down the code.
            veloicty_index_start = radius_index_end + 1 
            velocity_index_end = planet_input.find(',', veloicty_index_start)
            velocity_index = float(planet_input[veloicty_index_start:velocity_index_end])

            #Temperature Index
            temp_start = velocity_index_end + 1
            temp_index = float(planet_input[temp_start:])

            # Calculating the inputted values from the indexes to planet attributes.

            planet_circumference = (2 * math.pi * radius_index)
            planet_core_temp = ((temp_index - 32) * (5/9) + 273.15)
            planet_rotational_period = ((2 * math.pi * radius_index) / velocity_index)  

            # Printing the input of the planet with their unique indexes assocoiated with them.

            # All the indexing above ensures every planet is unique if met with different inputs.

            print(f'[{planet_name}]\nPlanet Information:\nRadius: {radius_index:.2f} km')
            print(f'Velocity: {velocity_index:.2f} km/s\nTemperature: {temp_index:.2f}°F')
            print(f'Calculating new attributes...\nCircumference: {planet_circumference:.2f} km')
            print(f'Core Temperature: {planet_core_temp:.2f} K')
            print(f'Rotational Period: {planet_rotational_period:.2f} hours')
            print(divider)

            start_index = end_index + 1  # Loop continues until final planet index is printed. 

        selection_input = False # Return to menu after displaying inputted planet(s). [46]
