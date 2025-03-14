import random

options = ('rock', 'paper', 'scissors')

player = None
computer = random.choice(options)
is_running = True
count = 0

while is_running:

    while player not in options:

        player = input('Enter a choice (rock, paper, or scissors): ')

        print(f'Player: {player}\nComputer: {computer}')

        if player == computer:
            print('It is a tie!')
            player = ''
            count += 1

        elif player == 'rock' and computer == 'scissors':

            print(f'You win! after {count} tries')
            is_running = False
            count += 1

        elif player == 'paper' and computer == 'rock':

            print(f'You win! after {count} tries')
            is_running = False
            count += 1

        elif player == 'scissors' and computer == 'paper':

            print(f'You win! after {count} tries')
            is_running = False
            count += 1
            
        else:
            print('You lose.')
            player = ''
            count += 1