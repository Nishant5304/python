
# temperature convertor

unit = input("Is this temperature in Celsius or Farhenheit: ")

temperature = float(input("Enter the temperature: "))

if unit == 'Celsius':
    temp = round((temperature * 9) / 5 + 32, 2)
    print(f"The temperature in Farhenheit is {temp}°F")
if unit == 'Farhenheit':
    temp = round((temperature - 32) * 5 / 9, 2)
    print(f"The temperature in Celsius is {temp}°C")
else:
    print('invalid input')