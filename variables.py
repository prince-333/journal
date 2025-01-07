#Variable = A container for a value (string, integer, float, boolean).
#           A variable behaves as if it was the value it contains.
# Strings (Series of text)

first_name = "Prince"
food = "pizza"
email = "testemail@gmail.com"

print(first_name)
#This ^ can be condensed to such by using an f-string, this is commonly used to display variables in an expression directly into strings. 
print(f"Hello {first_name}")
print(f"It seems you have been enjoying {food} as of recently")
print(f"So we decided to email you a copy of our offer, and the email to look for is {email}")

# Integers (Whole number)
age = 18
quantity = 3
num_of_students = 30
print(f"You are {age} years old and seems like you bought {quantity} boxes of pizza when you really needed {num_of_students}")

# Float (Contain a decimal portion)
price = 10.99
gpa = 3.2
distance = 5.5
print(f"The price is ${price}")
print(f"your gpa is {gpa}")
print(f"you ran {distance} km")

# Boolean (Either True or False)
is_student = True

if is_student:
    print("You are a student")
else:
    print("You are not a student")