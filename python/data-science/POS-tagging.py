# part-of-speech tagging is the process of classifying words into such lexical categories

# POS tagging is a step of text preprocessing, and its results may be used to improve performance
# of various NLP tasks
# Such as lemmatization (a procedure that reduced word forms to one root form),
# semantic analysis, machine translation, and many others

# * POS-tagging in NLTK

# POS-tags are assigned to words with the help of a POS-tagger.
# It works with a tokenized text only, so you need to split your text into tokens beforehand.

import nltk

text = ['there', 'is', 'a', 'dwarf', 'looking', 'out', 'of', 'the', 'window', '!']
print(nltk.pos_tag(text))

# convert the list into a list of tuples consisting of words and tags
# [('there', 'EX'), ('is', 'VBZ'), ('a', 'DT'), ('dwarf', 'NN'), ('looking', 'VBG'),
# ('out', 'IN'), ('of', 'IN'), ('the', 'DT'), ('window', 'NN'), ('!', '.')]


# * POS Tags
# A set of tags is called a tagset
# In general for English, NLTK uses Penn Treebank's POS tagset, one of the most popular
# The tagsets are called based on the text resources they are used at

# You can find more info about tags from the Penn Treebank that are used in NLTK by typing
nltk.help.upenn_tagset('VBG')
# VBG: verb, present participle or gerund
#     telegraphing stirring focusing angering judging stalling lactating
#     hankering alleging veering capping approaching traveling besieging
#     encrypting interrupting erasing wincing ...


# * POS disambiguation
# Sometimes, the same form of a word, i.e. 'play may be a noun or a verb, depending on the context
# This is called - ambiguity - meaning that the tag we should assign for the word is ambiguous

# The process of resolving the ambiguity, understanding which tag is correct is called
# disambiguation

sentence = ['My', 'peer', 'will', 'peer', 'through', 'the', 'window', 'hole', '.']
tagged_words = nltk.pos_tag(sentence)
print(tagged_words)
# [('My', 'PRP$'), ('peer', 'NN'), ('will', 'MD'), ('peer', 'VB'), ('through', 'IN'),
# ('the', 'DT'), ('window', 'NN'), ('hole', 'NN'), ('.', '.')]

# As you can see, 'peer' comes up first as a noun and then as a verb. Both these words are the same,
# but NLTK labels them differently. How does this happen?

# The NLTK tagger deals with ambiguity with the help of the context: trained on a huge tagged corpus
# if you put 'to' before 'peer', the tagger will label it as a verb.
# Similarly, if you put 'the' before a word, the tagger will label it as a noun.

words = ['run', 'ate', 'table']
pos_speech = [nltk.pos_tag([word]) for word in words]
nouns_list = [word[0][0] for word in pos_speech if word[0][1] == 'NN']


for word, token in nltk.pos_tag(words):
    if token == 'NN':
        print('word:', word)

print(nouns_list)
