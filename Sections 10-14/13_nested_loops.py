'''

Nested loop = A loop within another loop (outer, inner)
#             Outer loop:
#               Inner Loop:

'''

rows = int(input('Enter the # of rows: '))
columns = int(input('Enter the number of columns: '))
symbol = input('Enter a symbol to use: ')

for x in range(rows):
    for y in range(columns):
        print(symbol, end='')
    print()