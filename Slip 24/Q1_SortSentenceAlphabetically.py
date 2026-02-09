# Q1_SortSentenceAlphabetically.py
# Program to sort words in a sentence in alphabetical order

sentence = input("Enter a sentence: ")

# Split sentence into words
words = sentence.split()

# Sort alphabetically (case-insensitive)
words_sorted = sorted(words, key=str.lower)

print("\nSentence after sorting words alphabetically:")
print(" ".join(words_sorted))


# ------------- SAMPLE OUTPUT (NOT printed automatically) -------------
SAMPLE_OUTPUT = """
Enter a sentence: Python is a powerful and easy language

Sentence after sorting words alphabetically:
a and easy is language powerful Python
"""
# --------------------------------------------------------------------
