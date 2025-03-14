# dictionary = a collection of {key:value} pairs ordered and changeable. No duplicates
#

capitals = {"USA": "Washing D.C",
            "India": "New Delhi",
            "China": "Beijing",
            "Russia": "Moscow",
            'Japan': 'Tokyo'
            }

# Get value associated with the key
print(capitals.get('India'))

'''

if capitals.get('Japan'):
    print('That capital exists')
else:
    print(f'That capital doesn\'t exist')

'''

# Updates key and/or value(s)
capitals.update({"Germany": "Berlin"})
capitals.update({"USA": "Detroit"})

# capitals.pop('China')  # Removes key AND value
# capitals.popitem()     # Removes latest key AND value PAIR
# capitals.clear()       # Clears dictionary
# keys = capitals.keys()   # Shows ALL keys


# for key in capitals.keys():
    # print(key)

# Prints all values
# for value in capitals.values():
#    print(value)

# items = capitals.items()  prints tuple asscoiated with the dictionary

for key, value in capitals.items():
    print(f'{key}: {value}')
