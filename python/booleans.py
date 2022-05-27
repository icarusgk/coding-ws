def xor(a, b):
  # If both values are equal (truthy or falsy)
  if bool(a) == bool(b):
    return False
  return a or b


def compare(numerator, denominator):
    return bool(denominator) and numerator / denominator == 0.5

real_password = 'hiii'
def wrong_password(password):
              # False           # True            # True
              # False      or   # True
    return (password == "" or (not password and real_password))

print(wrong_password(False))


