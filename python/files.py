file = open('animals.txt', 'r')
# read
# print(file.read())
# The output:
# Dog
# Cat
# Rabbit
# Sea turtle
# Penguin

# readline()
# print 3 bytes
# print(file.readline(3))
# print(file.readline(3))
# print(file.readline(3))
# print(file.readline(3))
# print(file.readline(3))
# print(file.readline(3))
# The output:
# Dog
# 
# 
# Cat
# 
# 
# Rab
# bit


# readlines()
# allows us to read the whole file as a list of lines
# print(file.readlines())
# Output
# ['Dog\n', 'Cat\n', 'Rabbit\n', 'Sea turtle\n', 'Penguin']

for line in file:
  print(line.strip())

# The output:
# Dog
# 
# Cat
# 
# Rabbit
# 
# Sea turtle
# 
# Penguin



file.close()


