import re

# * search()
# checks for matches throughout the string

string = "roads? where we're going we don't need roads."

result_1 = re.search(r'roads\?', string)  # match
print(result_1)
result_2 = re.search(r'roads\.', string)  # match
print(result_2)
result_3 = re.search(r'Roads', string)  # no match
print(result_3)
result_4 = re.search(r'here', string)  # match
print(result_4)

# Both search() and match() return only the first pattern occurrence in the string
result = re.search('roads', string)
print(result)  # <re.Match object; span=(0, 5), match='roads'>


# * findall()
# This function returns a list with string that match the pattern
string = "A million dollars isn’t cool. You know what’s cool? A billion dollars."

result_1 = re.findall('[mb]illion', string)  # ['million', 'billion']
result_2 = re.findall('thousand', string)  # []

# Note that the findall() function returns a list of tuples when a pattern
# contains one or more groups.
string = '3 apples, 2 bananas, 5 pears, 10 strawberries'

ungrouped_results = re.findall(r'\d+ \w+', string)  # without grouping
grouped_results = re.findall(r'(\d+) (\w+)', string)  # with grouping
print(grouped_results)

# finditer() does the same, but it returns an iterator of regexp match objects

# * split()
# splits a string by occurrences of pattern and returns a list of strings
string = '111412222234333345555544'

results_1 = re.split('4', string)
print(results_1)  # ['111', '1222223', '3333', '55555', '', '']

# This function can take an additional maxsplit argument.
# It specifies the number of splits.
results_2 = re.split('4', string, maxsplit=3)  # ['111', '1222223', '3333', '5555544']
print(results_2)

# If you want to store the matching substrings removed, you can use capturing groups
string = "Roads? Where we're going we don't need roads."

split_result_1 = re.split(r'\W+', string)
# ['Roads', 'Where', 'we', 're', 'going', 'we', 'don', 't', 'need', 'roads', '']

split_result_2 = re.split(r'(\W+)', string)
# ['Roads', '? ', 'Where', ' ', 'we', "'", 're', ' ', 'going', ' ', 'we', ' ', ...]


# Searching and replacing
# * sub()
# It takes three arguments:
# a regular expression pattern, a replacement string, and an initial string

# It replaces all pattern occurrences with the specified replacement.
string = 'blue jeans, white shirt, yellow socks'
pattern = r'(blue|white|yellow)'
replacement = 'black'

r_result_1 = re.sub(pattern, replacement, string)  # 'black jeans, black shirt, black socks'
r_result_2 = re.sub(pattern, replacement, string, count=2)  # 'black jeans, black shirt, yellow socks'



# Precompiling patterns
# * compile()
# It allows you to compile a pattern and reuse it later in the code.
# Takes a pattern and returns a special Pattern object

string = "roads? where we're going we don't need roads."

# define a pattern in a string format
string_pattern = 'roads'

# pass the pattern to the re.compile() method
my_pattern = re.compile(string_pattern)

# use the returned Pattern object to match a pattern
compiled_result_1 = my_pattern.match(string)  # <re.Match object; span=(0, 5), match='roads'>
compiled_result_2 = my_pattern.findall(string)  # ['roads', 'roads']
compiled_result_3 = my_pattern.split(string)  # ['', "? where we're going we don't need ", '.']
compiled_result_4 = my_pattern.sub('cars', string)  # 'cars? where we're going we don't need cars.'

