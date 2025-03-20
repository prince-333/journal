# Function - a block of reusable code
#            place () after the function name to invoke it.

def happybirtday(name, age):
    print(f'Happy Birthday To {name}')
    print(f'You are {age}!')
    print('Happy Birthday To You')
    print()

happybirtday('Moe', 23)
happybirtday('Joe', 22)
happybirtday('Roe', 21)

print('----------------------------')

# Example 2
def displace_invoice(username, amount, due):
    print(f'Hello {username}')
    print(f'Your bill of {amount:.2f} is due on {due}')

displace_invoice('Joe', 25.098, 'April 20')

print('----------------------------')

# Example 3
def add(x, y):
    z = x + y
    return z
def subtract(x, y):
    z = x - y
    return z
def multiply(x, y):
    z = x * y
    return z
def divide(x,y):
    z = x / y
    return z

print(add(6,7))
print(subtract(9, 6))
print(multiply(5, 5))
print(divide(15, 5))
print('----------------------------')

# Exercise
def create_name(first, last):
    first = first.capitalize()
    last = last.capitalize()
    return first + ' ' + last

full_name = create_name('stephen', 'curry')
print(full_name)





