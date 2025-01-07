# Exercise 2 Shopping Cart Program

item = input("What would you like to buy?: ")
price = float(input("How much is it?: "))
quantity = int(input("How much do you want?: "))
total = price * quantity 
print(f"The total cost is ${total} for an amount of {quantity} {item}. ")