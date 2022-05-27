import re

# * Sets

# sets provide us with the opportunity to be more specific in our regexp templates
# and narrow down the scope of our search

# Each set in the regular expression takes the place of exactly one character
# in the string, but it defines a whole number of characters that can match it.

template = '[bd]a[td]'

re.match(template, 'bat')  # match
re.match(template, 'dad')  # match
re.match(template, 'cat')  # no match: 'c' is not in the first set
re.match(template, 'dot')  # no match: 'o' instead of 'a'

# One is for python the other for regex
# re.match('[', '[')  # sre_constants.error: unexpected end of regular expression


# * Escaping in sets

# Sets in regular expressions have a sort of superpower: they automatically "neutralize"
# the metacharacters listed inside the square brackets, turning them into regular characters.

template = 'Hodor[?.]'
re.match(template, 'Hodor?')  # match
re.match(template, 'Hodor.')  # match
re.match(template, 'Hodor!')  # no match

# The only metacharacters that do not fall under this rule and keep their special status are,
# predictably, the right square bracket ] and the backslash \

template = r'=[\]]'
re.match(template, '=]')  # match

template = r'=[)]]'
re.match(template, '=]')  # no match
re.match(template, '=)]')  # match (the only string this template can match)

# You need to escape the backslash
template = r'¯[\\]_'
re.match(template, r'¯\_(ツ)_/¯')  # match
# remember that re.match checks whether regexp matches the beginning of the string, not the whole string


# Here the backslash is not escaped and serves as a part of the escape sequence:
template = r'¯[\t]_'
re.match(template, '¯\_(ツ)_/¯')  # no match
re.match(template, '¯\t_')  # match


# There are character that acquire especial meaning specifically when they're used inside sets

re.match('ja[a-z].', 'jazz')  # match
re.match('[A-Z]ill', 'kill')  # no match: [A-Z] matches only uppercase letters
re.match('[A-Z]ill', 'Bill')  # match


# [0-9] does it for the digits.
re.match('[0-9]', '7')   # match
re.match('[1-9]', '07')  # no match

# Several ranges can be easily put in one set. They do not have to follow each other in any way:
re.match('love [a-zA-Z]', 'love U')  # match: [a-zA-Z] matches both uppercase and lowercase
re.match('love [a-z!A-Z]', 'love !')  # match: [a-zA-Z!] matches letters and !

# To use the dash - as a regular character in a set, you should "strip" it of the
# left or right character defining the range, so just put the dash in the first or last
# position in the set, [-abc] or [abc-]:

re.match('[-1-9]1', '-1')  # match
re.match('[1-9-]1', '-1')  # match


# * The hat aka the caret ^
# It excludes the characters that you don't want in the text

re.match('[^A-Z]ond', 'Bond')  # no match
re.match('Bon[^A-Z]', 'Bond')  # match


# The hat placed anywhere else in the set, except for the first position, will lose
# its special meaning and become a regular character:

re.match('[A-Z^]ames', 'James')  # match
re.match('[A-Z^]ames', '^ames')  # match










