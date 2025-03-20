# Iterables - An object/collection that can return its element one at a time,
#             allowing it to be iterated over a loop

# List
numbers = [1,2,3,4,5]

for number in numbers[::-1]:
    print(number, end='-')

# Tuple
numbers = (1,2,3,4,5)

print(f'\n--------------------------------')

for number in numbers:
    print(number,end=' ')

print(f'\n--------------------------------')
# Set
fruits = {'apple', 'orange', 'banana', 'coconut'}

for fruit in fruits:
    print(fruit)

print(f'\n--------------------------------')

# String
name = 'Test lol'

for character in name:
    print(character,end=' ')

print(f'\n--------------------------------')

# Dictionar

my_dictionary = {'A': 1, 'B': 2, 'C': 3}

for key, value in my_dictionary.items():
    print(f'{key} = {value}')
    