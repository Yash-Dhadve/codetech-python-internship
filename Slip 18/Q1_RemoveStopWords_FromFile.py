# Q1_RemoveStopWords_FromFile.py
# Program to remove stopwords from a text file using NLTK

# Install NLTK:
# pip install nltk

import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Download required NLTK data (only once)
# nltk.download('punkt')
# nltk.download('stopwords')

# -------- READ FILE --------
filename = input("Enter filename: ")

try:
    with open(filename, "r") as f:
        text = f.read()
except FileNotFoundError:
    print("File not found!")
    exit()

# -------- REMOVE STOPWORDS --------
stop_words = set(stopwords.words("english"))
words = word_tokenize(text)

filtered_words = [w for w in words if w.lower() not in stop_words]

clean_text = " ".join(filtered_words)

print("\nText after removing stop words:")
print(clean_text)

# ---------------- SAMPLE OUTPUT (not printed automatically) ----------------
SAMPLE_OUTPUT = """
Enter filename: sample.txt

Text after removing stop words:
quick brown fox jumps lazy dog
"""
# ---------------------------------------------------------------------------
