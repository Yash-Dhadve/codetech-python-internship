# Q1_HangmanGame.py
# Hangman game with 5 AI-related words stored internally

import random

def hangman(word):
    word = word.lower()
    guessed = set()
    attempts = 6  # allowed wrong guesses

    print("Welcome to Hangman (AI Edition)!")
    display = ["_" for _ in word]

    while attempts > 0 and "_" in display:
        print("\nWord:", " ".join(display))
        print("Remaining attempts:", attempts)
        guess = input("Enter a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single alphabet.")
            continue

        if guess in guessed:
            print("You already guessed that letter.")
            continue

        guessed.add(guess)

        if guess in word:
            print("Correct guess!")
            for i in range(len(word)):
                if word[i] == guess:
                    display[i] = guess
        else:
            print("Wrong guess!")
            attempts -= 1

    # Final Result
    if "_" not in display:
        print("\nCongratulations! You guessed the word:", word)
    else:
        print("\nGame Over! The correct word was:", word)


# -------- WORD SELECTION --------
ai_words = ["neural", "learning", "robot", "vision", "dataset"]

secret_word = random.choice(ai_words)   # pick random AI-related word
hangman(secret_word)


"""
Welcome to Hangman (AI Edition)!

Word: _ _ _ _ _ _
Remaining attempts: 6
Enter a letter: e
Correct guess!

Word: _ e _ _ _ _
Remaining attempts: 6
Enter a letter: l
Correct guess!

Word: _ e _ r n _
Remaining attempts: 6
Enter a letter: a
Wrong guess!

...

Congratulations! You guessed the word: learning
"""