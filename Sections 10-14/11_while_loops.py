'''

While loop - Execute some code WHILE some condition reminas true.

'''

name = input('Enter you name: ')

while name == '':
    print('You did not enter your name.')
    name = input('Enter you name: ')
else:
    print(f'Hello {name}.')


# --------------------------------------------------------------

age = int(input('Please enter your age: '))

while age < 0:
    print(f'Age cannot be negative.')
    age = int(input('Please enter your age: '))
else:
    print('You are {age} years old')

# --------------------------------------------------------------

food = input('Enter a food (q to quit): ')

while not food == 'q':
    print(f'You like {food}')
    food = input('Enter a food (q to quit): ')
else: 
    print('bye')

# --------------------------------------------------------------

num = int(input('Enter  a number between 1 - 10: '))

while num < 1 or num > 10:
    num = int(input('Please try again: '))
else:
    print(f'{num} is between 1 - 10. Good job!')
