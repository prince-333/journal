"""
Prompt: The cost of train tickets deponds on the distance of the trip, and on wehter a passenger
is a frequent passenger.

For Frequent Customers: 
- If the trip is under 500 km, the cost is $50
- If the trip is 500 km or more, the cost is $100

For everyone else:
- If the trip is under 300 km, the cost is $75
- If the trip is 300 km or more, but less than 500 km, the cost is $150
- If the trip is 500 km or more, the cost is $200

Task: Write a program that prints the cost of a ticket, given the customer type and distance.

"""

Frequent = input('Are you a frequent customer?: (Y/N) ')
Distance = int(input('What is the distance you are travelling?: (Integer) '))
price = -1

if Frequent == 'Y':
    if Distance >= 500:
        price = 100
    else:
        price = 50
else:
    if Distance >= 500:
        price = 200
    elif Distance >= 300:
        price = 150
    else:
        price = 75
print(f'According to the {Distance} km you are travelling and your frequency status\nyour total ticket price is ${price}')