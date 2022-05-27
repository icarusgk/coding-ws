x = int(input())
y = int(input())

if 1 < x < 8:
  if 1 < y < 8:
    print("8")
  if y == 1 or y == 8:
    print("5")
elif (x == 1 or x == 8) and (y > 1 and y < 8):
  print("5")
else:
  print("3")