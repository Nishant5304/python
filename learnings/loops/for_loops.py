

for i in range(1, 11):
  print(i)
print("Happy New Year")

for i in reversed(range(1, 11)):
  print(i)
print("Happy New Year")


for i in range(1, 21):
  if i == 13:
    continue
  else:
    print(i)
print("mewo")

for i in range(1, 21):
  if i == 13:
    break
  else:
    print(i)
print("mewo")
