# Weight converter

weight = float(input("Enter your weight: "))
unit = input("Kilograms or Pounds (K or L): ")

if unit == "K":
    weight = round(weight * 2.205, 1)
    unit = "Lbs."
    print("Your weight is {} {}".format(weight, unit))
elif unit == "L":
    weight = round(weight / 2.205, 1)
    unit = "Kgs."
    print("Your weight is {} {}".format(weight, unit))
else:
    print("{} is neither (K or L)".format(unit)) 