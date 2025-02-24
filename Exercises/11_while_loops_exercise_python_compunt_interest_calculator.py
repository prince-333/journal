'''

Python compound interest calculator

Formula - A = P(1 + r/n)^t

A = Final Amount

P = Initial Principal Balance

r = Interest Rate

t = Number of Time Periods Elapsed. 

'''

initial_principal_balance = 0
rate = 0
time_period = 0

while initial_principal_balance <= 0:
    initial_principal_balance = float(input('Enter the principle amount: '))
    if initial_principal_balance <= 0:
        print('Please enter a positive integer.')

while rate <= 0:
    rate = float(input('Enter the interest rate: '))
    if rate <= 0:
        print('Please enter a positive integer.')

while time_period <= 0:
    time_period = float(input('Enter the time period: '))
    if time_period <= 0:
        print('Please enter a positive integer.')

final_amount = initial_principal_balance * (1 + (rate / 100)) ** time_period

print(f'With your given values, the final amount is ${final_amount:.2f} after {time_period} years')


