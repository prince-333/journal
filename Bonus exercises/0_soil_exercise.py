import math    

max_soil_capacity = 8
truck_minimum_capacity = 4

soil_purchased = int(input('Enter the amount of soil you would like to purchase: '))

# Print error message, indicating a negative integer, and ask for a positive integer.

while soil_purchased < 0:
    soil_purchased = int(input('Please enter a positive value: '))


# Calculate price of soil depending on the constraints provided.

if soil_purchased >= 50:
    price_soil = 10
elif soil_purchased > 20 and soil_purchased < 49:
        price_soil = 20
else: price_soil = 30

# Number of Trips portion

trips = soil_purchased / 8
trips = math.ceil(trips)    # Rounds up 

# Delivery cost of Trips

if trips >= 10:
    delivery_cost = 100
else: delivery_cost = 80

# Tax
tax = 0.12

# Printing everything now

total_cost = tax * (soil_purchased * price_soil) + (trips * delivery_cost)

print(f'The cost of buying and transporting {soil_purchased} cubic metres in {trips} loads is ${total_cost}')

# Just need to work on section 8, everyhting in the code works except section 8.