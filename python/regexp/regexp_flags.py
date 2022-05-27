import re
# when the match is successful and an example of your template is present 
# in the string, match() returns a so-called Match object containing the 
# data about the matching substring
template = "match"
match_result = re.match(template, "match")
print(match_result)
# the output is "<_sre.SRE_Match object; span=(0, 5), match='match'>"

# What makes Match objects useful is that they contain important 
# information on the results of the matching operation.

# By calling the group() method with no arguments, you can extract the 
# substring that matches your template:

template = r"b.d"
match_1 = re.match(template, 'bad').group()   
match_2 = re.match(template, "bed").group()  

print(match_1)  # the result is a string "bad"
print(match_2)  # the result is a string "bed"


# * Extracting match indexes
# The start method

# The match function always searches for matches starting at the beginning of the string.
start = re.match(template, "bad").start()
print(start)  # the result is int 0

# The end method can facilitate slicing
template = "100%?"
string = "100% reason to remember the name"
end = re.match(template, string).end()
print(string[end:])
# the output is " reason to remember the name"


# The span method returs a tuple with start and end
span = re.match(template, "100%").span()  # the result is tuple (0, 4)

# Regexp are case sensitive
lower = r'where are the money, Lebowski\?'
upper = r'WHERE ARE THE MONEY, Lebowski\?'
# These are different templates

# To make regex case-insensitve, use the optional flags argument
# ? re.IGNORECASE
lower = r'where is the money, Lebowski\?'
upper = r'WHERE IS THE MONEY, Lebowski\?'
string = 'Where Is the money, lebowski?'
result_lower = re.match(lower, string, flags=re.IGNORECASE)  # match
result_upper = re.match(upper, string, flags=re.IGNORECASE)  # match


# ? re.DOTALL
# it matches a dot character with literally every character, including \n
dot_template = 'new line .'
no_flag = re.match(dot_template, 'new line \n')  # None
with_flag = re.match(dot_template, 'new line \n', flags=re.DOTALL) 
# match

# To enable several flags at once, pass their sum as the flags value.
result = re.match('FLAG ME.', 'flag me\n', flags=re.IGNORECASE + re.DOTALL)  # match