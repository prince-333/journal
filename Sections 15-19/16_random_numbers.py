import random

low = 1
high = 100
options = ('Rock', 'Paper', 'Scissors')
cards = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

# number = random.randint(low, high)  Random number between 1-100
# number = random.random()  Random float number where number < 1.0

option = random.choice(options)
random.shuffle(cards)

print(cards)