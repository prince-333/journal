"""

- Write a program that asks the user to enter integers, and prints, "even" or, "odd"(or "error" if
something other than an integer is entered).

- Enter "quit" to exit.

"""

userInput = input("Enter a positive integer or quit: ")

while userInput != "quit":
    if not userInput.isnumeric(): #if not an integer
        print("error")
    elif int(userInput) % 2 == 0: #if a number is even, the remainder is 0 when dividing by 2
        print("even")
    else:
        print("odd")
    userInput = input("Enter another number or quit: ")

if userInput == 'quit':
    print('The program has successfully ended.')
