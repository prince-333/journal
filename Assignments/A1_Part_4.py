# Part 4 section

import math

'''

To make the output cleaner and easier to read, I implemented a divider using the below 'divider', 
as a way to divide the code sections in the terminal to make it easier to visualize what part of 
code is what.

'''

divider = '-=+------------------------------------+=-'

# These following booleans determines if the code will continue based on the user input in the menu.

selection_input = False # If the required input in the menu is satisified, will exit the menu and follow the code.

escape_input = False # The escape boolean works such that, if "esc" is inputted, it will shut down the program.

planet_status = False # Will determine if a planet is registered or not. Selecting 'b' beforehand will print an error message.

# The following is for part 4, a string to store the planet data(s)

planet_data = ''


'''

Part #1 Below is the menu setup in a loop, with a set variable (selection_input), that if set to 
"True" will break the loop and continue the code.

'''

print(f'{divider}\nHello, Welcome to Planet Manager!')

while not selection_input: # Will keep asking until the condition is satisfied, 'esc', 'a', or 'b'.
    selection = input('Please select one of the following options:\na) Register Planet \nb) Planet Info\nesc) Close Program\n[Your Selection]: ').lower()

    if selection == 'esc':     # To escape the loop and "shutdown" the program.
        selection_input = True # Setting this function to True will break the loop and continue the program.
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
        print(f'{divider}\nPlease enter a valid input of \'a\', \'b\', or \'esc\'')

    # Part 2: Registering planet and outputing new values based on userinput

    if selection_input == True and selection == 'a':
        print(f'{divider}\nPlease answer appropriately to the following:\n ')
        planet_name = input('The name of the planet: ').strip()
        # The code below allows another input of another planet if inputted before.
        planet_radius = -1.0
        planet_velocity = -1.0
        planet_temperature = -1.0

        while planet_radius < 0 or planet_velocity < 0 or planet_temperature < 0: # If either is negative, will make an error message to retry.

            planet_radius = float(input('The radius of the planet?: '))
            planet_velocity = float(input('What is the tangential velocity of the planet?: '))
            planet_temperature = float(input('What is the temperature of the planet?: '))
            print(divider)

        # Code below will add the inputted values towards a new string that will add to another, if it is the initial planet, only such information will be printed.
        new_planet = f'{planet_name},{planet_radius},{planet_velocity},{planet_temperature}'

        # Adding if statement to determine if ";" should be added in "planet_data" which seperates the planets, and their seperate information. If it's the first planet, it only only add such and no ";" input.
        if planet_data:
            planet_data += ';' + new_planet
        else:
            planet_data = new_planet
        
        if planet_radius > 0 and planet_velocity > 0 and planet_temperature > 0:
            planet_status = True # Confirm that the planet exists.
            selection_input = False # This at the end of this if statement will output all the code above it and return to the original while loop (menu)
        else:
            print(f'{divider}\n Please enter positive values.\n{divider}') 

# Part 3: If all the conditions are satisified, it will print calculated values of the equations regarding the planet.

    elif selection_input == True and selection == 'b' and planet_status == True: 
        start_index = 0  # This will begin processing planet_data, looking for ";" to seperate the planets and their information.
        
        while start_index < len(planet_data):
            end_index = planet_data.find(';', start_index)
            if end_index == -1: # If no ";", it indicates it is the last planet.
                end_index = len(planet_data)

            # Planet Name Index
            planet_input = planet_data[start_index:end_index] # Now the code extracts the seperated planet
            name_index_end = planet_input.find(',') # Finds the first "," seperator, which indicates the first planet name.
            if name_index_end == -1:
                selection_input = False  # Return to menu if it is only a single planet.
            else:
                planet_name = planet_input[:name_index_end] # If more than 2 planets will continue the loop.
            name_index = planet_input[:name_index_end] # Takes the string input until the first ",".

            # Planet Radius Index
            radius_index_start = name_index_end + 1 # Skips the first "," because name_index_end finds the first ",".
            radius_index_end = planet_input.find(',', radius_index_start) # Will find the next "," after the first ",".
            radius_index = float(planet_input[radius_index_start:radius_index_end]) # Takes the string input after the second "," before the third ","

            # Planet Velocity Index
            veloicty_index_start = radius_index_end + 1
            velocity_index_end = planet_input.find(',', veloicty_index_start)
            velocity_index = float(planet_input[veloicty_index_start:velocity_index_end])

            #Temperature Index
            temp_start = velocity_index_end + 1
            temp_index = float(planet_input[temp_start:])

            # Calculating the inputted values of the user about the planet to planet attributes.
            planet_circumference = (2 * math.pi * planet_radius)
            planet_core_temp = ((planet_temperature - 32) * (5/9) + 273.15)
            planet_rotational_period = ((2 * math.pi * planet_radius) / planet_velocity)  

            # Printing the input of the planet.

            print(f'[{planet_name}]\nPlanet Information:\nRadius: {planet_radius:.2f} km')
            print(f'Velocity: {planet_velocity:.2f} km/h\nTemperature: {planet_temperature:.2f}°F\n')
            print(f'Calculating new attributes...\nCircumference: {planet_circumference:.2f} km')
            print(f'Core Temperature: {planet_core_temp:.2f}°F\nRotational Period: {planet_rotational_period:.2f} hours')
            print(divider)

            start_index = end_index + 1

        selection_input = False
         

        