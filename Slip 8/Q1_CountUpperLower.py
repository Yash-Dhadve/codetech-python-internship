# Q1_CountUpperLower.py
# Program to count uppercase and lowercase letters in a string

text = input("Enter a string: ")

upper_count = 0
lower_count = 0

for ch in text:
    if ch.isupper():
        upper_count += 1
    elif ch.islower():
        lower_count += 1

print("\nNumber of uppercase letters:", upper_count)
print("Number of lowercase letters:", lower_count)



"""
Enter a string: Hello World 123

Number of uppercase letters: 2
Number of lowercase letters: 8
"""
