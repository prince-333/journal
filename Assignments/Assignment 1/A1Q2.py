'''

Purpose: Create a simple Python program to test if a certain number of numbers are a palindrome

'''

count = int(input('Please enter a positive integer: '))  # How much times the loop will repeat.

# Code referenced from class demo, lines 14-22.

while count > 0: 
    Number = int(input('Please enter a number to test: ')) # Number being tested.
    Number_input = Number # Stores the original input of the number being tested.
    reversed_num = 0
    while Number > 0:
        last_digit = Number % 10
        Number //= 10

        reversed_num = (reversed_num * 10) + last_digit


        if Number_input == reversed_num: # Checks if it is a palindrome or not.
            final_check = 'True'
        else:
            final_check = 'False'

    print (f'Is {Number_input} a palindrome? {final_check}')
    count -= 1 # If N > 1, the next user input will be evaluated, if it is 0, it ends the program.

print('Task completed!\nProgram has been terminated.') # End.