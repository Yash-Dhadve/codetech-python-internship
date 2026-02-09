# Q1_SortSentenceAlphabetically.py
# Program to sort words in a sentence alphabetically

import string

# -------- USER INPUT --------
sentence = input("Enter a sentence: ")

# Remove punctuation
clean_sentence = sentence.translate(str.maketrans("", "", string.punctuation))

# Split into words
words = clean_sentence.split()

# Sort words alphabetically
words.sort(key=str.lower)   # case-insensitive sort

# Print result
print("\nSorted sentence:")
for word in words:
    print(word)



"""
Enter a sentence: Hello this is a simple test sentence.
"""
