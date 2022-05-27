import re

# * Escaping through backslashes
# The backslash is a so-called escape-character
# it helps symbols to "escape their work duties

re.match("\?", "?")  # match, '?' is the matching string
re.match("\\?", "?")  # match, '?' is the matching string
re.match("\\.", ".")  # match, '.' is the matching string
# re.match("?", "?")  # SyntaxError
# SyntaxError is caused by a "dangling metacharacter" in the regexp,
# an unescaped question mark not preceded by any character


question = "who let the dogs out?!"
re.match("who let the dogs out?!", question)  # no match
re.match("who let the dogs out\?!", question)  # match
re.match("woof\.", "woof!")  # no match
re.match("woof\.", "woof.")  # match


re.match("\\\\", "\\")  # match
# Python requires backslash to be escaped in the string as well
# so the string consists of one literal backslash and one escape symbol
# re.match("\\", "\\")  # SyntaxError


re.match("\t", "\t")  # match
re.match("\\t", "\t")  # match


# * The r prefix
# The r prefix is a raw string notation prefix:
# it tells Python to cancel the usage of escape sequences in this string and treat
# all backslashes in their literal meaning.

# For example, the string r'\t' will be treated by Python as a combination of a backslash
# and a letter t, not as tabulation.
# \\t printed is \t

re.match(r"\\", "\\")  # match: regexp consists of a regexp escape and a backslash
# \ is used to escape the second \
re.match(r"\\.", ".")  # no match: no backslash in the string

# (doubt) \ is used to escape the second \ but the '?' is unescaped therefore it performs its function
# of checking whether the \ string is there
re.match(r"\\?", "?")  # match is an empty string: the question mark in regexp is unescaped

re.match(r"\?", "?")  # match, as in the example above, \ is the regexp escape character
re.match(r"\t", "\t")  # match, \t is the regexp escape sequence


# * re.escape

# re.escape function can help you escape all special characters in your string automatically

template = 'hyperskill.org'
escaped_template = re.escape(template)

print(escaped_template)  # 'hyperskill\.org'

print(re.escape('whitespace is here'))  # The output is 'whitespace\ is\ here'

