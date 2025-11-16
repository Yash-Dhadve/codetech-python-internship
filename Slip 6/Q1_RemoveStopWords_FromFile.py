# Q1_RemoveStopWords_FromFile.py
# Program to remove stop words from a text file using NLTK

# Install NLTK:
# pip install nltk

import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Download required NLTK data (run only once)
# nltk.download('punkt')
# nltk.download('stopwords')

# -------- READ FILE --------
filename = input("Enter filename: ")

try:
    with open(filename, "r") as file:
        text = file.read()
except FileNotFoundError:
    print("File not found!")
    exit()

# -------- REMOVE STOPWORDS --------
stop_words = set(stopwords.words("english"))
words = word_tokenize(text)

filtered_words = [w for w in words if w.lower() not in stop_words]

cleaned_text = " ".join(filtered_words)

print("\nText after removing stop words:")
print(cleaned_text)


"""
Enter filename: passage.txt

File Content:
The quick brown fox jumps over the lazy dog.
"""
