# input () = A function that prompts the user to enter data
#            Returns the entered data as a string.

name = input("What is your name?: ")
age = input("How old are you?: ")

age = int(age)
age = age + 1

print(f"Hello {name}!")
print(f"HAPPY BIRTDAY!")
print (f"You are {age}!")

#For line 7 and 8, this can be condensed by writing it as 
# age = int(input("How old are you?: "))