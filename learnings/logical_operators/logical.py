
temp = 28
is_sunny = True

if temp >=28 and is_sunny:
    print("It is hot outside")
elif temp <=0 and is_sunny:
    print('it is cold outside')
elif 28 > temp > 0 and is_sunny:
    print('it is warm outside')
elif temp >= 28 and not is_sunny:
    print('it is cloudy')
else:
    print('invalid input')