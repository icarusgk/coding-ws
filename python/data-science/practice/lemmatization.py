from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()

dataset = ['mice', 'children']

dataset = list(map(lemmatizer.lemmatize, dataset))

print(dataset)