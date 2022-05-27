import re

# * Shorthands for sets

# * \w stands for [a-zA-Z0-9_]
# * \d matches a digit and is equivalent to [0-9]
# * \s matches the white space characters equivalent to [ \t\n\r\f\v]

re.match('\w\scamels?', '1 camel')  # match
re.match('\w\scamels?', 'a\tcamel')  # match
re.match('\d\scamels?', '8\ncamels')  # match


# Negated shorthands are the total opposites
# \W matches everything except for alphanumeric characters, [^a-zA-Z0-9_]
# \D matches any non-digit character, [^0-9]
# \S matches any non-whitespace character and is equivalent to [^ \t\n\r\f\v]

re.match('\D\S\W', 'A1-')  # match
re.match('\D\S\W', '1 A')  # no match


# If you need to escape a shorthand, just escape its backslash
re.match(r'\\w', r'\w')  # match
re.match(r'\\w', r'\k')  # no match, because \\w isn't a shorthand here


# Another great feature of shorthands is that they maintain their metacharacter abilities
# when they are put in sets.

re.match('no[!\w]', 'no!')  # match
re.match('no[!\w]', 'noo')  # match


re.match('[\D\S]', '0')   # match, 0 is not a whitespace character
re.match('[\D\S]', '\n')  # match, \n is not a digit
re.match('[\D\S]', 'a')   # match, 'a' is not a digit and not a whitespace character


# Instead of [\D\S], use [^\d\s]. This set matches everything that does not fall into
# the categories of whitespaces and digits at the same time.
re.match('[^\d\s]', '0')   # no match, 0 is a digit
re.match('[^\d\s]', '\t')  # no match, \t is a whitespace character
re.match('[^\d\s]', 'a')   # match, 'a' is not a digit and not a whitespace


# You can add some characters banned by the negated shorthand to the set
re.match('[\Wa-c]', 'a')  # match, 'a' is in the set
re.match('[\Wa-c]', 'z')  # no match: 'z' is alphanumeric and is not in the a-c range
re.match('[\Wa-c]', '?')  # match, ? is not alphanumeric


# * Boundary shorthands
# they match an empty string between a character matching \w and a character matching \W
# they do not match any characters.
# You can use it to make sure that your regular expression will match only a separate word,
# not a part of a bigger word

re.match(r'\b', 'Hello?')  # match (an empty string between the absence of a character and a letter)
re.match(r'\b', '')  # no match (no alphanumeric character)
re.match(r'Hail\b', 'Hail Mary!')  # match

re.match(r'Hail\b Caesar', 'Hail Caesar')  # match (but \b is useless here)


# \B matches the absence of the word boundary, that is, an empty string between two
# alphanumeric characters \w

re.match(r'Hail\b', 'Hailey')  # no match
re.match(r'Hail\B', 'Hailey')  # match


# \A matches only an empty string at the start of the string
# This way, you can make sure that the substring matching your regular expression will be
# located at the very beginning of the string.


# \Z matches an empty string at the end of the string
re.match('Hail\Z', 'Hail!')  # no match
re.match('Hail\Z', 'Hail')   # match

# you need to space \b correctly with r''
re.match('Hail\b', 'Hail Mary!')   # no match, \b is a Python escape character
re.match(r'Hail\b', 'Hail Mary!')  # match, \b is a regexp shorthand

# The hat character ^ is identical to \A. The dollar sign $ is equivalent to \Z.
re.match("^Bring cash", "^Bring cash$")  # no match: ^ in regexp means "the start of the string"
re.match("^Bring cash", "Bring cash$")   # match
re.match("\ABring cash", "Bring cash$")  # match: \A is identical to ^
re.match("Bring cash", "Bring cash$")    # match: match() matches the start of the string by default


