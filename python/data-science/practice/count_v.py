from sklearn.feature_extraction.text import CountVectorizer

# list of text documents
dataset = ["So no one told you life was gonna be this way",
           "Your job's a joke, you're broke",
           "Your love life's DOA",
           "It's like you're always stuck in second gear",
           "When it hasn't been your day, your week, your month",
           "Or even your year, but",
           "I'll be there for you"]

# create the transform
vectorizer = CountVectorizer()

# tokenize and build vocab
vectorizer.fit(dataset)

# summarize
# print(vectorizer.vocabulary_)

vocab = vectorizer.vocabulary_
print(vocab)

# encode document
vector = vectorizer.transform(dataset)
print(vector)
print(vector.toarray()[4][37])
