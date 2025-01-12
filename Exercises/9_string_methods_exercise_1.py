# Validate user input exercise
# 1. username is no more than 12 characters
# 2. username must not contain spaces
# 3. username must not contain digits

username = input('Please enter your username: ')

length = len(username) 
characters = username.isalpha()
spaces = username.find(' ')

if length > 12 and characters == False and spaces >  0:
    print('You have exceeded the character count.')
    print('Only characters are allowed.')
    print('Make sure to not includes spaces.')
elif length > 12 and characters == True and spaces < 0:
    print('You have exceeded the character count.')
elif length > 12 and characters == False and spaces < 0:
    print('You have exceeded the character count')
    print('Only characters are allowed')
elif characters == False or spaces > 0:
    print('Only characters are allowed.')
    print('Make sure to not includes spaces.')

if length <= 12 and characters == True and spaces < 0:
    print('Your username of {} has been successfully made.'.format(username))
else:
    print('Please try again.')

age = int(input('Now please enter your age: '))
age_verificaiton = 'Adult' if age >= 18 else 'Minor'

if age_verificaiton == 'Adult':
    print('You may now enter the site.')
elif age_verificaiton == 'Minor':
    print('You must be 18+ to access this website.')
