import re
# Quantifiers always follow some other character (or a group of characters)

# * The plus quantifier
# The plus + quantifier basically means "the preceding character should appear one or more times"

template = "wo+w!"  # matches "wow!" with one or more 'o'
re.match(template, "wow!")            # match: one 'o' character encountered
re.match(template, "wooooooooooow!")  # match: many (11) 'o' characters encountered
re.match(template, "ww!")             # no match: no 'o' character encountered

template = ".+Jack Sparrow"  # matches the string "Jack Sparrow" with some preceding characters
re.match(template, "Captain Jack Sparrow")  # match: there are some characters before "Jack"
re.match(template, "Jack Sparrow")          # no match: the string starts with "Jack"

template = "Louis [IXV]+"
re.match(template, "Louis III")  # match
re.match(template, "Louis XVI")  # match
re.match(template, "Louis ")     # no match


# * The asterisk quantifier

# The asterisk * quantifier does almost the same thing, but the scope is a bit wider;
# it also matches the absence of the previous character.

template = "go*d"
re.match(template, "good")  # match: double 'o' occured
re.match(template, "god")   # match: one 'o' occured
re.match(template, "gd")    # match: no 'o' occured, but the rest of the string matches the template
re.match(template, "gud")   # no match: 'u' is not in the template

# You can pair the asterisk with other metacharacters in the same way as the plus quantifier.
# For example, the combination of the dot character and the asterisk quantifier, .*, matches
# any string of any length, including an empty string.

template = ".*no.*"  # matches 'no' with any or no preceding/following sequences of characters
re.match(template, "no")                             # match: 'no' is the whole string
re.match(template, "no rest for the wicked")         # match: 'no' at the start of the string
re.match(template, "I'm no superman")                # match: 'no' inside the string
re.match(template, "— Luke, I'm your father. — no")  # match: 'no' at the end of the string

# * A fixed number of repetitions
# In case we want to match a fixed number of occurrences of a certain character,
# we can use curly brackets with a number inside them, just like that: {n}
# This quantifier matches exactly n consecutive occurrences of the preceding character.

template = "\w{5}"  # matches a sequence of exactly 5 alphanumeric characters
re.match(template, "doggy")  # match: 5 letters sequence
re.match(template, "dog")    # no match: there are only 3 alphanumeric characters
re.match(template, "a dog")  # no match: space doesn't match \w

#  * A range of repetitions
# {n,m}. The quantifier matches at least n and no more than m instances of the previous

template = "\d{5,10}"  # matches any sequence of digits with length from 5 to 10
re.match(template, "12345")       # match: 5 digits
re.match(template, "1234567890")  # match: 10 digits
re.match(template, "12345678")    # match: 8 digits
re.match(template, "1234")        # no match: only 4 digits

# {n,} matches n and more occurrences of the character
# while {,m} matches no more than m (including zero occurrences)
template = "i'm just a po{2,}r boy"  # there should be at least 2 'o' in the string
re.match(template, "i'm just a poor boy")         # match: 2 'o'
re.match(template, "i'm just a pooooooooor boy")  # match: 9 'o'
re.match(template, "i'm just a por boy")          # no match

template = "i need no sy{,3}mpathy"  # there should be no more than 3 'y'
re.match(template, "i need no sympathy")     # match: 1 'y'
re.match(template, "i need no syyympathy")   # match: 3 'y'
re.match(template, "i need no smpathy")      # match: zero occurrences match the quantifier too
re.match(template, "i need no syyyympathy")  # no match: 4 'y'


# Greedy quantifier
template = "<p>.*</p>"
re.match(template, "<p>paragraph</p><p>another paragraph</p>")
# the template matches the whole string "<p>paragraph</p><p>another paragraph</p>"


# The question mark has another function when used in quantifiers
# It switches the quantifier from the 'greedy' mode to 'lazy'

# Lazy quantifier
template = "<p>.*?</p>"
re.match(template, "<p>paragraph</p><p>another paragraph</p>")
# the template first matches the substring "<p>paragraph</p>"

# Note that lazy and greedy modes do not work with the quantifier {n}
