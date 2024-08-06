bigram
import nltk
from nltk.tokenize import word_tokenize
from nltk import bigrams
from nltk.probability import FreqDist
import string

# Download necessary NLTK data
nltk.download('punkt')

# Sample text corpus
text = """Natural language processing (NLP) is a field of artificial intelligence (AI) that focuses on the interaction between computers and humans through natural language. The ultimate goal of NLP is to enable computers to understand, interpret, and generate human language in a way that is both meaningful and useful."""

# Tokenize the text into words
words = word_tokenize(text)

# Remove punctuation and convert to lower case
words = [word.lower() for word in words if word.isalnum()]

# Compute bigrams
bi_grams = list(bigrams(words))
bi_gram_freq = FreqDist(bi_grams)

# Display the bigrams and their frequencies
print("Bigrams and their frequencies:")
for bigram, freq in bi_gram_freq.items():
    print(f"{bigram}: {freq}")

trigram
import nltk
from nltk.tokenize import word_tokenize
from nltk import trigrams
from nltk.probability import FreqDist
import string

# Download necessary NLTK data
nltk.download('punkt')

# Sample text corpus
text = """Natural language processing (NLP) is a field of artificial intelligence (AI) that focuses on the interaction between computers and humans through natural language. The ultimate goal of NLP is to enable computers to understand, interpret, and generate human language in a way that is both meaningful and useful."""

# Tokenize the text into words
words = word_tokenize(text)

# Remove punctuation and convert to lower case
words = [word.lower() for word in words if word.isalnum()]

# Compute trigrams
tri_grams = list(trigrams(words))
tri_gram_freq = FreqDist(tri_grams)

# Display the trigrams and their frequencies
print("Trigrams and their frequencies:")
for trigram, freq in tri_gram_freq.items():
    print(f"{trigram}: {freq}")

BigramProbabilities
import nltk
from nltk.tokenize import word_tokenize
from nltk import bigrams
from nltk.probability import FreqDist

# Download necessary NLTK data
nltk.download('punkt')

# Sample text corpus
text = """Natural language processing (NLP) is a field of artificial intelligence (AI) that focuses on the interaction between computers and humans through natural language. The ultimate goal of NLP is to enable computers to understand, interpret, and generate human language in a way that is both meaningful and useful."""

# Tokenize the text into words
words = word_tokenize(text)

# Remove punctuation and convert to lower case
words = [word.lower() for word in words if word.isalnum()]

# Compute unigrams and bigrams
unigram_freq = FreqDist(words)
bigram_freq = FreqDist(bigrams(words))

# Compute bigram probabilities
bigram_probabilities = {}
for bigram in bigram_freq:
    first_word = bigram[0]
    bigram_prob = bigram_freq[bigram] / unigram_freq[first_word]
    bigram_probabilities[bigram] = bigram_prob

# Display the bigrams and their probabilities
print("Bigram Probabilities:")
for bigram, prob in bigram_probabilities.items():
    print(f"{bigram}: {prob:.4f}")
output
Bigram Probabilities:
('natural', 'language'): 1.0000
('language', 'processing'): 0.3333
('processing', 'nlp'): 1.0000
('nlp', 'is'): 1.0000
('is', 'a'): 0.5000
('a', 'field'): 0.5000
('field', 'of'): 1.0000
('of', 'artificial'): 0.3333
('artificial', 'intelligence'): 1.0000
('intelligence', 'ai'): 1.0000
('ai', 'that'): 1.0000
('that', 'focuses'): 0.5000
('focuses', 'on'): 1.0000
('on', 'the'): 1.0000
('the', 'interaction'): 0.2500
('interaction', 'between'): 1.0000
('between', 'computers'): 1.0000
('computers', 'and'): 0.6667
('and', 'humans'): 0.2500
('humans', 'through'): 1.0000
('through', 'natural'): 1.0000
('language', 'the'): 0.3333
('the', 'ultimate'): 0.2500
('ultimate', 'goal'): 1.0000
('goal', 'of'): 1.0000
('nlp', 'is'): 1.0000
('is', 'to'): 0.5000
('to', 'enable'): 1.0000
('enable', 'computers'): 1.0000
('computers', 'to'): 0.3333
('to', 'understand'): 0.3333
('understand', 'interpret'): 1.0000
('interpret', 'and'): 1.0000
('and', 'generate'): 0.2500
('generate', 'human'): 1.0000
('human', 'language'): 1.0000
('language', 'in'): 0.3333
('in', 'a'): 1.0000
('a', 'way'): 0.5000
('way', 'that'): 1.0000
('that', 'is'): 0.5000
('is', 'both'): 0.5000
('both', 'meaningful'): 1.0000
('meaningful', 'and'): 1.0000
('and', 'useful'): 0.2500
Nextword
import nltk
from nltk.tokenize import word_tokenize
from nltk import bigrams
from nltk.probability import FreqDist
import string

# Download necessary NLTK data
nltk.download('punkt')

# Sample text corpus
text = """Natural language processing (NLP) is a field of artificial intelligence (AI) that focuses on the interaction between computers and humans through natural language. The ultimate goal of NLP is to enable computers to understand, interpret, and generate human language in a way that is both meaningful and useful."""

# Tokenize the text into words
words = word_tokenize(text)

# Remove punctuation and convert to lower case
words = [word.lower() for word in words if word.isalnum()]

# Compute bigrams and their frequencies
bigram_freq = FreqDist(bigrams(words))
unigram_freq = FreqDist(words)

def predict_next_word(prev_word):
    """Predict the next word given the previous word using bigram probabilities."""
    next_words = [(bigram[1], freq) for bigram, freq in bigram_freq.items() if bigram[0] == prev_word]
    if not next_words:
        return "No prediction available."
   
    # Sort next words by frequency in descending order
    next_words_sorted = sorted(next_words, key=lambda x: x[1], reverse=True)
   
    # Return the most probable next word
    return next_words_sorted[0][0]

# Example usage
prev_word = "language"
next_word = predict_next_word(prev_word)

print(f"The most likely next word after '{prev_word}' is '{next_word}'.")
output
The most likely next word after 'language' is 'processing'.
unigram
import nltk
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist
import string

# Download necessary NLTK data
nltk.download('punkt')

# Sample text corpus
text = """Natural language processing (NLP) is a field of artificial intelligence (AI) that focuses on the interaction between computers and humans through natural language. The ultimate goal of NLP is to enable computers to understand, interpret, and generate human language in a way that is both meaningful and useful."""

# Tokenize the text into words
words = word_tokenize(text)

# Remove punctuation and convert to lower case
words = [word.lower() for word in words if word.isalnum()]

# Compute unigrams
unigrams = FreqDist(words)

# Display the unigrams and their frequencies
print("Unigrams and their frequencies:")
for unigram, freq in unigrams.items():
    print(f"{unigram}: {freq}")
