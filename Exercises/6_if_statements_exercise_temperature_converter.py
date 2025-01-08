# Temperature converter

unit = input("Is this temperature in Celsius or Fahrenheit (C/F): ")
temp = float(input("What is the temperature?: "))

if unit == "C":
    temp = round((9 * temp) / 5 + 32, 2)
    unit = "°F"
    print("The temperature in Fahrenheit is {} {}".format(temp, unit))
elif unit == "F":
    temp = round((temp - 32) * 5 / 9, 1)
    unit = "°C"
    print("The temperature in Celsius is {} {}".format(temp, unit))
else:
    print("{} is neither Celsius (C) or Fahrenheit (F)".format(unit))