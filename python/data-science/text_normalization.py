# The main idea is to reduce different forms of one word to a single form.
# With this algorithm all forms like "plays", "playing", or "played" will be changed to "play".

# There are two approaches to text normalization: stemming and lemmatization.


# Stemming
# Stem is the most important part of the word, and other word parts (called affixes)
# are added to it.

# i.e. For instance, if we take the stem play and add the affix -ed to it, we get the past form
# of the verb play

# In this process we remove all affixes to get a stem
# Note that the result may not represent a real word, and it is okay!
# For example, for the word "ladies", we may have "ladi".

# For the english language we use the
# Porter stemmer and the Lancaster stemmer found in the nltk.stem module

# * The Porter Steamer
# Is the earliest and the most popular algorithm for this task.

from nltk.stem import PorterStemmer, SnowballStemmer, LancasterStemmer
from nltk.stem import WordNetLemmatizer

porter = PorterStemmer()
porter.stem('played')  # play
porter.stem('playing')  # play

# * The Snowball Stemmer
# can be seen as an improvement over the original Porter stemmer as it gives slightly
# better results

# It also supports 13 non-English languages such as
# Spanish, French, Russian, German, Swedish, and others.



snowball = SnowballStemmer('english')
snowball.stem('playing')  # play
snowball.stem('played')  # play

# It works better than Porter
snowball.stem('generously')   # generous
porter.stem('generously')     # gener

snowball.stem('dangerously')  # danger
porter.stem('dangerously')    # danger


# * The Lancaster Stemmer
# the Lancaster stemmer works faster.
# if you are working with huge text data and need to process it in a short time,
# use Lancaster Stemmer.

lancaster = LancasterStemmer()
lancaster.stem('played')       # play
lancaster.stem('playing')      # play
lancaster.stem('generously')  # gen
lancaster.stem('dangerously')  # dang



# * Lemmatization
# They analyze the word, its context, its part of speech, and then give the answer.
# The result is always a real word in its dictionary form called a lemma.
#  In general, lemmatizers rely on dictionaries (or corpora) when looking for lemmas.

lemmatizer = WordNetLemmatizer()
lemmatizer.lemmatize('playing')  # playing

# As you can see, the word remained unchanged after lemmatization
# As far as we know, lemmatizers need to know the context or the part of speech of the word.
# The default part of speech here is a noun and, as a noun, the word 'playing' is its own lemma.

# Part of speech	Tag
# Noun	            n
# Verb	            v
# Adjective	        a

# pos - part-of-speech
lemmatizer.lemmatize('playing', pos='v')  # play
lemmatizer.lemmatize('plays')             # play


# Stemming vs Lemmatizers
# stemming
snowball.stem('worst')                   # worst
snowball.stem('bought')                  # bought
snowball.stem('mice')                    # mice

# lemmatization
lemmatizer.lemmatize('worst', pos='a')   # bad
lemmatizer.lemmatize('bought', pos='v')  # buy
lemmatizer.lemmatize('mice')             # mouse


# But If you need to normalize text faster, stemming is the right choice.


