from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer

# list of text documents
text = [
    'The quick brown fox jumped over the lazy dog.',
    'The dog.',
    'The fox'
    ]

dataset = [
           "So no one told you life was gonna be this way",
           "Your job's a joke, you're broke",
           "Your love life's DOA",
           "It's like you're always stuck in second gear",
           "When it hasn't been your day, your week, your month",
           "Or even your year, but",
           "I'll be there for you"]

# create the transform
vectorizer = TfidfVectorizer()

# tokenize and build vocab with '.fit()'
# .fit() learns vocabulary from training set
# vectorizer.fit(dataset)

# .transform() (s) documents to document-term matrix
# uses the vocab and document frequencies learned by .fit()

# .fit_transform() learns vocabulary and idf, returns document-term matrix

x = vectorizer.fit_transform(dataset)
print(f'the shape is: {x.shape}')
print(f"\nThe fit_transform is: \n{x}")

# summarize
print('\nThe vocab is: ')
terms_mapping = vectorizer.vocabulary_  # A mapping of terms to feature indices
# print(terms_mapping)

terms = vectorizer.get_feature_names_out()
print(terms)


print('\nprinting matrix...')

matrix = x.toarray()
print(matrix)


for i, arr in enumerate(matrix):
    print(f'\nPrinting {i + 1} array\n')

    for j, score in enumerate(arr):
        if score > 0:
            print(score, terms[j])


