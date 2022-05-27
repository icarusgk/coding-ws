import re

# Ignoring case
# * re.IGNORECASE / re.I

lower = 'you shall not pass\!'
upper = 'YOU SHALL NOT PASS\!'
string = 'You Shall Not Pass!'
result_lower = re.match(lower, string, flags=re.IGNORECASE)  # match
result_upper = re.match(upper, string, flags=re.IGNORECASE)  # match

# Changing metacharacter behavior
# * re.DOTALL / re.S
# It matches the special . character with any character, including the newline \n character
pattern = 'precious .'
result_1 = re.search(pattern, 'my precious \n')  # no match
result_2 = re.search(pattern, 'my precious \n', flags=re.DOTALL)  # match

# * re.MULTILINE / re.M
# This flag matches the ^ and the $ character
string = '''A million dollars isn’t cool.\nYou know what’s cool?\nA billion dollars.'''

result_1 = re.findall('^(A|You)', string)  # ['A']
result_2 = re.findall('^(A|You)', string, flags=re.MULTILINE)  # ['A', 'You', 'A']

result_3 = re.findall('(cool.)$', string)  # []
result_4 = re.findall('(cool.)$', string, flags=re.MULTILINE)  # ['cool.', 'cool?']


# Making patterns more readable
# * re.VERBOSE
# doesn't change the way your pattern behaves
# but makes the pattern compilation more comprehensible instead

pattern = re.compile(r"""
                      ^([a-z0-9_\.-]+)               # username
                       @                             # @ sign
                      ([0-9a-z\.-]+)                 # host name
                       \.                            # a dot .
                      ([a-z]{2,6})$                  # top level domain     
                      """, flags=re.VERBOSE)

results = pattern.match('username@abc.com')  # match


# Matching ASCII only
# By default \w, \W, \b, \B, \d, \D, \s and \S match the entire UNICODE.
# To make a pattern match only ASCII characters, you can use re.ASCII or re.A

result_1 = re.findall('\w', 'ä, Ä, ö. Ö, ü, Ü, ß.')  # ['ä', 'Ä', 'ö', 'Ö', 'ü', 'Ü', 'ß']
result_2 = re.findall('\w', 'ä, Ä, ö. Ö, ü, Ü, ß.', flags=re.ASCII)  # []

# When using several flags at the same time use the | operator
string = "A million dollars isn’t cool.\nYou know what’s cool?\nA billion dollars."

result = re.findall('^(a|you)', string, flags=re.IGNORECASE|re.MULTILINE)
print(result)