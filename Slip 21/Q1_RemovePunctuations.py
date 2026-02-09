# Q1_RemovePunctuations.py
# Program to remove punctuations from a given string

punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

text = input("Enter a string: ")

cleaned = ""

for ch in text:
    if ch not in punctuations:
        cleaned += ch

print("\nString after removing punctuations:")
print(cleaned)


# ---------------- SAMPLE OUTPUT (NOT printed automatically) ----------------
SAMPLE_OUTPUT = """
Enter a string: Hello!!! How are you??

String after removing punctuations:
Hello How are you
"""
# ---------------------------------------------------------------------------
