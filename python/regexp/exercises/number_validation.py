import re

s1 = "+1-234-567-89-00"
s2 = "+1-234-567-89-00"
s3 = "+1 234 567 89 00"
s4 = "+12345678900"
s5 = "some string"
template = r"^\+(\d)[- ]?(\d{3})[- ]?(.*)"

result = re.match(template, s5)

if result:
    a, b, c, = result.group(1), result.group(2), result.group(3)
    print(f"Full number: {s1}")
    print(f"Country code: {result.group(1)}")
    print(f"Area code: {result.group(2)}")
    print(f"Number: {result.group(3)}")
else:
    print("no match")