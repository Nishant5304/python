
principle = 0
time = 0
rate = 0

while principle <= 0:
    principle = float(input("Enter the principle: "))
    if principle <= 0:
        print("principle can't be 0 or a negative number")

print(f'The principle is {principle}')

while rate <= 0:
    rate = float(input("Enter the rate: "))
    if rate <= 0:
        print("rate can't be 0 or a negative number")

print(f'The rate is {rate}')

while time <= 0:
    time = float(input("Enter the time: "))
    if time <= 0:
        print("time can't be 0 or a negative number")

print(f'The time is {time}')

ci = principle * pow((1 + rate/100), time)

print(f"The compound interest is {ci:.2f}")