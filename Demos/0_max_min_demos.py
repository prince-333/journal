"""

Write a program that gets random numbers between 0 and 1000 from a user.

- Loop until "quit" is entered.

- Keep track of the minimum and maximum numbers, and print when loop ends.

"""

maximum = -1 #the first number will be larger and overwrite this
minimum = 1001 #the first number will be smaller and overwrite this

text = input("Enter a positive integer between 0 and 1000, or 'quit' to quit.")

while text != "quit":
    if text.isnumeric() and int(text) >= 0 and int(text) <= 1000:
        number = int(text)
        print(number)
        if number > maximum: #new number is larger than previous max
            maximum = number
        if number < minimum: #new number is smaller than previous min
            minimum = number
    text = input("Enter another number: ")

print("The minimum was {} and the maximum was {}".format(minimum,maximum))