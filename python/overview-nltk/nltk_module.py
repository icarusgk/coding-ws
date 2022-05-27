import nltk

# Tokenization
# The main task is to split a given sequence of characters into units, called tokens.
# Tokens are usually represented by words, numbers, or punctuation marks.
# Sometimes, they can be represented by sentences or morphemes (word parts).

# * Tokenization in NLTK

from nltk.tokenize import word_tokenize, sent_tokenize, TreebankWordTokenizer, WordPunctTokenizer, \
    regexp_tokenize

text = "I have got a cat. My cat's name is C-3PO. He's golden."


# the function splits the string into words and punctuation marks.
print(word_tokenize(text))
# ['I', 'have', 'got', 'a', 'cat', '.', 'My', 'cat', "'s", 'name', 'is', 'C-3PO', '.'
# , 'He', "'s", 'golden', '.']

# All the punctuation marks including dashes and apostrophes are recognized as separate tokens.
wpt = WordPunctTokenizer()
print(wpt.tokenize(text))
# ['I', 'have', 'got', 'a', 'cat', '.', 'My', 'cat', "'", 's', 'name', 'is', 'C', '-',
# '3PO', '.', 'He', "'", 's', 'golden', '.']


# The TreebankWordTokenizer() minds fulls stops
tbw = TreebankWordTokenizer()
print(tbw.tokenize(text))
# ['I', 'have', 'got', 'a', 'cat.', 'My', 'cat', "'s", 'name', 'is', 'C-3PO.',
# 'He', "'s", 'golden', '.'

# regexp_tokenize() function makes use of regular expressions and accepts two arguments,
# a string and a pattern for tokens.

# 1
print(regexp_tokenize(text, "[A-z]+"))
# ['I', 'have', 'got', 'a', 'cat', 'My', 'cat', 's', 'name', 'is', 'C', 'PO', 'He', 's', 'golden']

# 2
print(regexp_tokenize(text, "[0-9A-z]+"))
# ['I', 'have', 'got', 'a', 'cat', 'My', 'cat', 's', 'name', 'is', 'C', '3PO', 'He', 's', 'golden']

# 3
print(regexp_tokenize(text, "[0-9A-z']+"))
# ['I', 'have', 'got', 'a', 'cat', 'My', "cat's", 'name', 'is', 'C', '3PO', "He's", 'golden']

# 4
print(regexp_tokenize(text, "[0-9A-z'\-]+"))
# ['I', 'have', 'got', 'a', 'cat', 'My', "cat's", 'name', 'is', 'C-3PO', "He's", 'golden']


# sent_tokenize() splits the given strings into sentences
print(sent_tokenize(text))
# ['I have got a cat.', "My cat's name is C-3PO.", "He's golden."]


# However, a dot can be used to mark abbreviations or contractions
text_2 = "Mrs. Beam lives in the U.S.A., it is her motherland. She lost about 9 kilos (20 lbs.) " \
         "last year."
print(sent_tokenize(text_2))
# ['Mrs. Beam lives in the U.S.A., it is her motherland.',
# 'She lost about 9 kilos (20 lbs.)', 'last year.']

# after tokenizing the text_2 above, .) was recognized as the end of the sentence.

# there are lots of periods and no spaces, so two sentences were recognized as one.
text_3 = "The plot of the film is cool!!!!!!! but the characters leave much to be desired...." \
         "i don't like them."
print(sent_tokenize(text_3))
# ['The plot of the film is cool!!!!!!!',
# "but the characters leave much to be desired....i don't like them."]