# TF-IDF
# Term Frequency-Inverse Document Frequency

# It denotes a way to statistically reflect how important a word is for a document in a collection
# Basically, it is a metric to evaluate a word's importance

# or to construct word representation vectors


# It consists of two parts
# - term frequency
# tf(w,d) = number of times w appears in d / the total number of words in d

# - inverse document frequency
# illustrates how often a word occurs across the whole collection
# idf(w,D) = log((total number of documents in D) + 1 /            + 1
#            (the number of documents in D that include w) + 1

# The final TF-IDF score is calculated in the usual way:
# tfidf(w) = tf(w,d) x idf(w, D)

# The most convenient way of getting a TF-IDF matrix is with the class TfidfVectorizer class
from sklearn.feature_extraction.text import TfidfVectorizer

# Each string in our dataset represents a separate document
# We have seven documents in total
# They form a document collection
dataset = ["So no one told you life was gonna be this way",
           "Your job's a joke, you're broke",
           "Your love life's DOA",
           "It's like you're always stuck in second gear",
           "When it hasn't been your day, your week, your month",
           "Or even your year, but",
           "I'll be there for you"]


vectorizer = TfidfVectorizer(input='content', use_idf=True, lowercase=True, analyzer='word',
                             ngram_range=(1, 2), stop_words=None, vocabulary=None, min_df=0.01,
                             max_df=0.60)


tfidf_matrix = vectorizer.fit_transform(dataset)
print('Matrix dimension:', tfidf_matrix.shape)  # Matrix dimension: (7, 38)
# 7 rows in the matrix correspond to the number of documents in our dataset.
# the number of columns (38) reflects the number of different terms (the vocabulary size)
print(tfidf_matrix)

# (0, 32)   0.32013213618851233
# (0, 29)   0.32013213618851233
# (0, 1)    0.26573716575927475
# ...
# (3, 0)    0.35903541343111484
# (3, 17)   0.35903541343111484
# ...
# (6, 1)    0.4115330003294659
# (6, 36)   0.3054049222662203

# Use indexation to access the term weights of a particular document
print(tfidf_matrix[6])
# (0, 8)    0.4957715949559137
# (0, 28)   0.4957715949559137
# (0, 18)   0.4957715949559137
# (0, 1)    0.4115330003294659
# (0, 36)   0.3054049222662203

# To see the vocabulary, use the get_feature_names()
terms = vectorizer.get_feature_names_out()
print(terms)  # ['always', 'be', 'been', 'broke', ...]...
print(terms[8])  # for

# Specifying vocabulary parameters

# If we provide a list of stopwords, these words will be excluded from the
# vocabulary and, subsequently, from the matrix:
stopwords = ['so', 'or', 'be']

vectorizer = TfidfVectorizer(stop_words=stopwords)
tfidf_matrix = vectorizer.fit_transform(dataset)
terms = vectorizer.get_feature_names_out()
print(terms)  # compare the list with the one above: words 'so', 'or', and 'be' are not in the vocabulary

# ['always', 'been', 'broke', 'but', 'day', 'doa', 'even', 'for', 'gear', 'gonna', 'hasn',
# 'in', 'it', 'job', 'joke', 'life', 'like', 'll', 'love', 'month', 'no', 'one', 're', 'second',
# 'stuck', 'there', 'this', 'told', 'was', 'way', 'week', 'when', 'year', 'you', 'your']

# n case you only want to know the importance of particular words, mention them in the vocabulary
# parameter; the final matrix will only contain their scores:

my_vocab = ['it', 'your']
vectorizer = TfidfVectorizer(vocabulary=my_vocab)

tfidf_matrix = vectorizer.fit_transform(dataset)
terms = vectorizer.get_feature_names_out()

print(terms)  # ['it', 'your']

print(tfidf_matrix)

# (1, 1)    1.0
# (2, 1)    1.0
# (3, 0)    1.0
# (4, 1)    0.9122058069917823
# (4, 0)    0.40973230979564096
# (5, 1)    1.0
