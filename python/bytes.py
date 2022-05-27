# str object is a sequence of Unicode characters

# bytes data type makes string more suitable for processing by the computer

# * ord()
# accepts as an argument a string consisting of a single Unicode character
# and returns an integer equal to the code point assidned to this character
# in the Unicode

# * chr()
# allows you to convert an integer to the corresponding Unicode character

a_char = 'a'
a_code = ord(a_char)
print(a_code) # 97

a_char = chr(a_code)
print(a_char) # 'a'

a_character = 'a'
one_character = '1'
print(ord(a_character))             # 97
print(ord(one_character))           # 49
print(a_character > one_character)  # True


a_character = 'a'
print(ord(a_character))    # 97
b_character = 'b'
print(ord(b_character))    # 98
aa_line = a_character * 2  # 'aa'
ab_line = a_character + b_character  # 'ab'
print(aa_line < ab_line)   # True
# because the first characters of the strings are equal and the code point 
# of the second character of ab_line is bigger than that of aa_line


# * bytes
# ? Any bytes object is a sequence of integers representing single bytes
# Each of these integers has a value between 0 and 255 (including 0 and 255), 
# so there are 256 possible values. They are immutable

first_bytes = b'123'
print(first_bytes)       # b'123'
print(len(first_bytes))  # 3

print(first_bytes[0])  # 49
print(first_bytes[1])  # 50
print(first_bytes[2])  # 51