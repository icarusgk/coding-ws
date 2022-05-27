import sys

args = sys.argv

def summatory():
  result = 0

  for i in range(sum(1, len(args))):
    result += int(args[i])

  print(result)

