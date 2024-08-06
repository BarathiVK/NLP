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
