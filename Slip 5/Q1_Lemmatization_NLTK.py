# Q1_Lemmatization_NLTK.py
# Program to perform Lemmatization using NLTK

import nltk
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet


nltk.download('wordnet')
nltk.download('omw-1.4')
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger_eng')   # IMPORTANT for Python 3.13


# Helper: convert POS tag from NLTK to wordnet format
def get_wordnet_pos(tag):
    if tag.startswith('J'):
        return wordnet.ADJ
    elif tag.startswith('V'):
        return wordnet.VERB
    elif tag.startswith('N'):
        return wordnet.NOUN
    elif tag.startswith('R'):
        return wordnet.ADV
    else:
        return wordnet.NOUN   # default


# Main lemmatization function
def lemmatize_sentence(sentence):
    lemmatizer = WordNetLemmatizer()
    words = nltk.word_tokenize(sentence)
    pos_tags = nltk.pos_tag(words)

    lemmatized_words = []

    for word, tag in pos_tags:
        wn_pos = get_wordnet_pos(tag)
        lemma = lemmatizer.lemmatize(word, wn_pos)
        lemmatized_words.append(lemma)

    return " ".join(lemmatized_words)


# -------- USER INPUT --------
text = input("Enter a sentence: ")

result = lemmatize_sentence(text)
print("\nAfter Lemmatization:")
print(result)


# If NLTK is not installed, install using:
# pip install nltk

"""
Enter a sentence: The children were playing in the parks
"""

