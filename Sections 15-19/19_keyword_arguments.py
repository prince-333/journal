# Keyword Arguments - An argument preceded by an identifier
#                     Helps with readability
#                     order of arguments does not matter
#                     1. Positional 2. Default 3. Keyword 4. Arbitrary
 
def hello(greeting, title, first, last):
    print(f'{greeting} {title} {first} {last}')

# Positional, matters where it is placed
hello('Hello', 'Mr.', 'Spongebob', 'Squarepants') 

# 2, can choose which one is for what variable.
hello(last='Squarepants', first='Spongebob.', title='Mr.', greeting='Hello') 
# Make sure any positional arguments are first before using keyword arguments.

# Example 3
for x in range(1,11):
    print(x, end=' ')
print('\n--------------------------')

print('1', '2', '3', '4', '5', sep='-')

print('\n--------------------------')

# Exercise

def get_phone(country, area, first, last):
    return (f'{country}-{area}-{first}-{last}')

phone_num = get_phone(country='1',area='123',first='456',last='7890')
print(phone_num)

