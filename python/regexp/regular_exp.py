import re

# * match()
regexp = 'burrito'
string = 'boorrito'

result = re.match(regexp, string)
print(result)  # None


result = re.match('hedge', 'hedgehog')
print(result is None)  # False

result = re.match('hog', 'hedgehog')  # no match
# because the beginning of the string doesn't match the template 'hog'

empty_result = re.match('', 'not an empty string')  # match
# because an empty template doesn't need anything to match the string

# Regular Expressions are case sensitive
sensitive_result = re.match('HURRAY', 'hurray')  # no match


# * The dot character
# It is one of the most important special symbols allowing to do this
# It matches any single character. (Digit, letter, space, and so on) except for the \n

# This regexp will correspond to the substring 'python'
# followed by a space and any character
regexp = 'python .'

# all examples match the regexp
re.match(regexp, 'python 3')
re.match(regexp, 'python 2')
re.match(regexp, 'python !')

# The dot doesn't match \n
newline = re.match(regexp, 'python \n')

# `?` doesn't match the space
question = re.match(regexp, 'python?!')


# * The question mark
# It is a quantifier that means "the previous character can be absent"
# Basically it signals that the character before it <char>? can occur once or zero times

regexp = 'regexp?'
word1 = re.match(regexp, 'regex')   # match
word2 = re.match(regexp, '')  # match


# You can combine it with the dot character

regexp = '.? points? to gryffindor'

# `.? points?` matches `1 point`
re.match(regexp, '1 point to gryffindor')

# `.? points?` matches `0 points`
re.match(regexp, '0 points to gryffindor')

# no match, since `.? points?` doesn't match `-5 points`
re.match(regexp, '-5 points to gryffindor')

# `.? points?` matches ` points`
re.match(regexp, ' points to gryffindor')
