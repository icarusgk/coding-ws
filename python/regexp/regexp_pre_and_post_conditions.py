import re

# Lookaround assertions
# You can use them to make your patterns match specific string that
# follow or precede another pattern.

# Lookaround assertions are enclosed in parentheses; they do not return the matched pattern
# That's why they are called 'zero-width' assertions.


# * Positive lookaheads
# This is the first type of assertion
# Their syntax is (?=pattern)

# They match the pattern to the right sie of the target match.

pattern = r'JetBrains (?=Academy)'
string_1 = 'JetBrains Academy'
string_2 = 'JetBrains Company'

# i.e. JetBrains (?=Academy) will match JetBrains only if Academy follows it.

result_1 = re.match(pattern, string_1)  # match
result_2 = re.match(pattern, string_2)  # no match
result_3 = re.match(pattern, 'JetBrains')  # no match

# * Negative lookaheads
# Their syntax is (?!pattern)

# They match if a pattern defined in parentheses doesn't follow a string
pattern = r'JetBrains (?!Academy)'
string_1 = 'JetBrains Academy'
string_2 = 'JetBrains Company'

result_1 = re.match(pattern, string_1)  # no match
result_2 = re.match(pattern, string_2)  # match


# They have to be a fixed size, and it's better to use a search() instead of match()



# * Positive lookbehinds
# Their syntax is (?<=pattern)

# They match a string if the specified phrase precedes it.

pattern = '(?<=JetBrains )Academy'
string = 'JetBrains Academy'

result = re.search(pattern, string)
print(result.group())  # Academy


# * Negative lookbehinds
# Their syntax is (?<!pattern)

# They match a string if the current position in the string is not preceded by the match
pattern = r'(?<!JetBrains )Academy'
string_1 = 'JetBrains Academy'
string_2 = 'Hyperskill Academy'

re.search(pattern, string_1)  # None
re.search(pattern, string_2)  # Academy