# Task: Test if all numbers are even from 1 to N (user input)

stop_num = int(input('Please enter a starting number (Integer): '))
cur_num = 1
while cur_num <= stop_num:
    print(f'{cur_num} is an even number: {cur_num % 2 == 0}')
    cur_num += 1 



