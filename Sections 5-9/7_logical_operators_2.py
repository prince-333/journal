# Logical operators = evaluate multiple conditions (or, and, not)
#                     or = at least one condition must be true
#                     and = both conditions must be True
#                     not = inverts the condition (Not false, not True)

temp = 28
is_sunny = False

if temp >= 28 and is_sunny:
    print('It is HOT outside!')
    print('It is Sunny as well')
elif temp <= 0 and is_sunny:
    print('It is cold outside')
    print('It is not sunny')
elif temp > 28 and temp > 0 and is_sunny:
    print('It is warm outside')
    print('It is sunny outside')
elif temp >= 28 and not is_sunny:
    print('It is HOT outside!')
    print('It is cloudy as well')
elif temp <= 0 and not is_sunny:
    print('It is cold outside')
    print('It is cloudy')
elif temp > 28 and temp > 0 and not is_sunny:
    print('It is warm outside')
    print('It is cloudy')

    #When using "not", it sets the boolean to the opposite it is set to, e.g, True, would turn it into False.