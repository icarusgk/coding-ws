# groups = ['1A', '1B', '1C', '2A', '2B', '2C', '3A', '3B', '3C']

# n_groups = int(input())

# rooms = dict.fromkeys(groups)

# for i in range(n_groups):
#   rooms[groups[i]] = int(input())

# print(rooms)

# import math

# angle = int(input())

# angle_in_radians = math.radians(angle)

# result = round((1 / math.tan(angle_in_radians)), 10)
# print(result)


passwords = ['0vbno0re', 'ad12', 'fgghut', '4qp', 'qwerty']

sorted_passwords = sorted(passwords, key=len)
for password in sorted_passwords:
  print(password, len(password))