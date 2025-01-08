# Python Calculator

operator = input("Enter an operator (+ - * /): ")
num1 = float(input("Enter the first number you would like to use: "))
num2 = float(input("Enter the second number you would like to use: "))

if operator == "+":
    result = num1 + num2
    print(round(result, 3))
elif operator == "-":
    result = num1 - num2
    print(round(result, 3))
elif operator == "*":
    result = num1 * num2
    print(round(result, 3))
elif operator == "/":
    result = num1 / num2
    print(round(result, 3))
else:
    print("{} is not a valid operator".format(operator))
