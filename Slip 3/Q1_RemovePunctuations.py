# Q1_RemovePunctuations.py
# Program to remove punctuations from the given string

def remove_punctuations(text):
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    result = ""

    for ch in text:
        if ch not in punctuations:
            result += ch
    return result


# -------- USER INPUT --------
user_input = input("Enter a string: ")

clean_text = remove_punctuations(user_input)
print("\nString without punctuations:")
print(clean_text)


"""
Enter a string: Hello!!! How are you??? I'm fine.
"""
