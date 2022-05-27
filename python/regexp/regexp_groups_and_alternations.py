import re

# When we want to specify the number of times that a string of different characters should
# occur in the string  we should resort to parenthesis characters ()

# The parenthesis in regular expressions can group desired parts of the template into single
# units and process them together.

# * Groups
template = r"(h[ao]){2}"  # matches a string consisting of two "ha" or "ho"
re.match(template, "haha")  # a match
re.match(template, "hoha")  # a match
re.match(template, "haa")  # no match
re.match(template, "hho")  # no match

# You can apply any quantifier you want, but the syntax remains.
# For example, you can mark an optional substring with a question mark quantifier ?.
# It will make the group match one or no occurrences of the group in the string:

template = r"ha(\?!)?"  # we expect "?!" to occur together and in this exact order
re.match(template, "ha?!")  # a match
re.match(template, "ha")  # a match
# in case "?" or "!" occur separately, the group won't match them
re.match(template, "ha?")  # matches only "ha", but not "?", since there's no "!" succeeding "?"
re.match(template, "ha!")  # matches only "ha", but not "!", since there's no "?" preceding "!"


# * Nested groups
# You can put a group inside a group to specify smaller substring repetitions inside
# larger substrings.

template = r"(([A-Z]\d){2}\.)+"
re.match(template, "A0C3.B8K5.")  # a match
re.match(template, "A0C3.")  # a match
re.match(template, "A0.C3B8K5")  # no match, as a dot separates two letter-digit combinations
re.match(template, "A0.C3.B8K5")  # no match, as "A0.C3." is separated by a dot
# and "B8K5" aren't followed by a dot

# Groups are also a tool that gives your template a structure when you need it.


# * Method groups()

template = r"([Pp]ython) (\d)\.([0-9]+)"
match = re.match(template, "Python 3.10")
print(match.groups())  # The output is ('Python', '3', '10')

# If a group is optional None will appear in the tuple
template = r"([Pp]ython)( \d)?"
match = re.match(template, "Python")
print(match.groups())  # The output is ('Python', None)



# * Method group()
# This method accepts an integer designating the number of the group that you want to extract:
template = r"Python (\d)"
match_1 = re.match(template, "Python 2")
print(match_1.group(1))  # The output is "2"
match_2 = re.match(template, "Python 3")
print(match_2.group(1))  # The output is "3"


# * Group enumeration
# The groups are enumerated in linear order, from left to right.
# To be precise, the group numbers coincide with the numbers of their opening parentheses
# in the template. The group with the first parenthesis gets the first number.

template = r"(a)(b)(c)"
match = re.match(template, "abc")
match.group(1)  # "a"
match.group(2)  # "b"
match.group(3)  # "c"


# This is also true for nested groups
template = r"((\w+) group) ((\w+) group)"
match = re.match(template, "first group second group")
match.group(1)  # "first group"
match.group(2)  # "first"
match.group(3)  # "second group"
match.group(4)  # "second"


template = r"(Python (\d) ){2,}"
results = re.match(template, "Python 2 Python 3 ")  # The output is "3"
print(results.groups())


# Alternations
# | is the or operator in regexps.
# By separating alternative substrings with vertical bars, you are matching any of these
# substrings with the template.

template = r"python|java|kotlin"
re.match(template, "python")  # a match
re.match(template, "java")  # a match
re.match(template, "kotlin")  # a match
re.match(template, "c++")  # no match
re.match(template, "k")  # no match
re.match(template, "jav")  # no match


# Groups and alternations
# To mark the borders of the OR operator, we need to use groups.
# Put the parentheses around the entire OR expression, as in (course|lesson):

template = r"(python|kotlin) (course|lesson)"
re.match(template, "kotlin")  # no match
re.match(template, "lesson")  # no match
re.match(template, "python lesson")  # match
re.match(template, "kotlin course")  # match


















