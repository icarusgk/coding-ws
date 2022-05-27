# Intro to text representations

Texts in natural language mainly consist of alphabetical characters, words,
and bigger linguistic units.

In order for computers to operate on such data, they apply various mathematical operations
to compare numbers and find patterns in numeric input
So, in other words they convert linguistic data, into a numeric format
The most convenient way is to provide a vector for each unit of a text

## Vector
It is an ordered sequence of numbers. In NLP, we can use them to describe any element
be it a single word or an entire text. What a vector encodes, depends solely on our objective and
the approach we choose.
That is what text representations deals with - how to convert a text into a vector.
There are several ways to do it.

## Bag of words model
This is the easiest one to implement
Here we consider each word independently, without taking into account the surrounding
context. We describe a text as a sequence of all words it contains, but we do not keep their
original order.

The resulting vector encodes the text and stores information about occurrences of words in it.
The model is frequently used in document classification and information retrieval.

**TF-IDF can help us normalize our bag-of-words**
It helps us increase proportionality and emphasize those words that actually contain useful info
TF-IDF is short for term frequency-inverse document frequency.

Here we mark counts not only in a specific document but also in an entire text collection.
To get TF-IDF, you need to calculate two metrics:
- Term frequency
- Inverse document frequency

IDF measures the rarity of a word across an entire set of documents. The more common a word,
the closer its weight to 0.

The TF-IDF is the product of these two metrics
According to this representation, if a word is frequent in one document and not in others,
it is valuable for this specific text.

If the word occurs in most documents, it is regarded as meaningless and
gets a very low weight due to IDF.

In the end, we also get a vector representation, but this time the score for each word
is calculated by means of TF-IDF.


## Word embeddings
Usually we want our representation to keep the most of linguistic information from the data
such as semantic properties or word order. 

This is where word embedding comes.
Embeddings that words provide are also vectors, but they represent a **word** rather than the whole text. 
And the way its weights are calculated is not as obvious as in the previous approaches. 

Here we have lower-dimensional and denser vectors compared to the ones before, that means that they are shorter and have less zero values in them. Which makes them easy to process.

Moreover, word embeddings allow us to capture semantic and syntactic relations.
For example, the words 'lamp' and 'lantern' will have very similar vectors, while 'lantern' and 'can'
will have different representations

We cannot simply score the values manually, as we have done it with the bag-of-words and TF-IDF. 
Instead, the weights should be obtained during training on very large text collections.

There are two types of word embeddings

- Context independent
Where a model provides a single embedding, analyzing all usages of the word and generalizing them as one meaning in a vector.

- Contextual
Where a model provides different word embeddings based on the context of a word. The most common are ELMo and BERT

Embeddings are usually given for a single word. In case you need to get one vector for a text, you can take the average, the sum, or the product of all word vectors in it.

