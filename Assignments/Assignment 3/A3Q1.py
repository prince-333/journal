"""

Purpose: To simulate a game that involves the guessing of a seed to escape a magical room. The Goal
is to calculate basic statistics involving the simulation.

"""

import random

# idk fix tmrw lol
Minimum_Value = 1

def game_info():
    selection_input = False # Change to True to finish lol.
    game_stats = [0,0,0,0]  # 0 - Players, 1 - Trials, 2 - Doors, 3 - Door to Freedom Converts to tuple when returning

    while selection_input is False:
        while game_stats[0] < Minimum_Value:        # How many players
            player_num = input('How many players are playing this game?: ')
            
            if player_num.isdigit():
                game_stats[0] = int(player_num)

                if game_stats[0] <  Minimum_Value:
                    print('Please enter a positive integer.')
            else:
                print('Please enter a positive integer.')

        while game_stats[1] < Minimum_Value:               # Number of Trials
            trial_num = input('How many trials of this game do you wish to run?: ')

            if trial_num.isdigit():
                game_stats[1] = int(trial_num)

                if game_stats[1] < Minimum_Value:
                    print('Please enter a positive integer.')
            else:
                print('Please enter a positive integer.')

        while game_stats[2] < Minimum_Value:               # Number of Doors
            door_num = input('Number of Doors: ')

            if door_num.isdigit():
                game_stats[2] = int(door_num)

                if game_stats[2] < Minimum_Value:
                    print('Please enter a positive integer.')
            else:
                print('Please enter a positive integer.')

        while game_stats[3] < Minimum_Value or game_stats[3] > game_stats[2]:            # Door to Freedom

            door_to_freedom = input('Which door takes them to freedom: ')

            if door_to_freedom.isdigit():
                game_stats[3] = int(door_to_freedom)
                if game_stats[3] > game_stats[2]:
                    print(f'Please enter a positive integer in the range [1,{game_stats[2]}].')
                else:
                    selection_input = True
            else:
                print(f'Please enter a positive integer in the range [1,{game_stats[2]}].')
    return tuple(game_stats)

def get_player_seeds(num_players):
    player_seeds = []

    for player in range(1, num_players + 1):
        selection_input = False

        while not selection_input:
            player_seed_input = input(f'Player {player}\'s seed guess: ')

            if player_seed_input.isdigit():
                player_seed_input = int(player_seed_input)
                player_seeds.append(player_seed_input)
                selection_input = True

            else: print(f'Input is not valid, please enter a positive integer.')
    return player_seeds

def get_door_walk_durations(num_doors):
    door_walk_durations = []

    for door_index in range(1, num_doors + 1):
        duration = (door_index % 5) + 1
        door_walk_durations.append(duration)
    return door_walk_durations


def main():
    game_results = game_info()
    num_players, num_trails, num_doors, freedom_door = game_results

    seeds = get_player_seeds(num_players)

    door_durations = get_door_walk_durations(num_doors)

    print(game_results)
    print(f'Door duation test: {door_durations}, seeds test: {seeds}')

if __name__ == "__main__":
    main()


# Finish parts D-H later (literally due tdy XDDDDDD)


    