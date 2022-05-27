def take(a, b, c):
  room_1 = (a // 2) + (a % 2)
  room_2 = (b // 2) + (b % 2)
  room_3 = (c // 2) + (c % 2)

  return room_1 + room_2 + room_3  


print(take(20, 21, 22))
print(take(16, 18, 20))
# take(17, 22, 23)
