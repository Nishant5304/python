
# weight convertor

weight = float(input("Enter your weight: "))

unit = input("Enter the unit(K or L): ")

if weight == 'K':
    w = weight * 2.205
    print("Your weight in kilos is {w} kilos")
elif weight == 'L':
    w = weight / 2.205
    print("Your weight in pounds is {w} lbs")
else:
    print('invalid input')
