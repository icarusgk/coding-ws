from itertools import chain, product, combinations
import string

correct = 'a7aB1'
first_letter = correct[0]

def generate():
  index = 1
  pass_characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
  while True:
    yield from product(pass_characters, repeat=index)
    index += 1


for i in generate():
  correct_password = first_letter + ''.join(i)

  if correct_password == correct:
    print('the correct password:', correct_password)
    break
