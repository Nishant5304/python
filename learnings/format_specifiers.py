
price1 = 3.14159
price2 = -98798.65
price3 = 12321.34

## decimals

print(f"price 1 is ${price1:.2f}")
print(f"price 2 is ${price2:.2f}")
print(f"price 3 is ${price3:.2f}")

## total space

print(f"price 1 is ${price1:10}")
print(f"price 2 is ${price2:10}")
print(f"price 3 is ${price3:10}")

## left align

print(f"price 1 is ${price1:<10}")
print(f"price 2 is ${price2:<10}")
print(f"price 3 is ${price3:<10}")

## right align

print(f"price 1 is ${price1:>10}")
print(f"price 2 is ${price2:>10}")
print(f"price 3 is ${price3:>10}")

## center align

print(f"price 1 is ${price1:^10}")
print(f"price 2 is ${price2:^10}")
print(f"price 3 is ${price3:^10}")

## sign prefix (+-=)

print(f"price 1 is ${price1:+}")
print(f"price 2 is ${price2:+}")
print(f"price 3 is ${price3:+}")


print(f"price 1 is ${price1:=}")
print(f"price 2 is ${price2:=}")
print(f"price 3 is ${price3:=}")

# space prefix

print(f"price 1 is ${price1: }")
print(f"price 2 is ${price2: }")
print(f"price 3 is ${price3: }")

## thousand seperator

print(f"price 1 is ${price1:,}")
print(f"price 2 is ${price2:,}")
print(f"price 3 is ${price3:,}")



