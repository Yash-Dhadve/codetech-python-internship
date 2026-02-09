# Q1_HangmanGame.py
# Simple Hangman game in Python

# The hidden word for the game
secret_word = "PYTHON".lower()

# Convert to list of underscores
display = ["_"] * len(secret_word)

# Set to store already guessed letters
guessed = set()

# Maximum wrong tries allowed
max_attempts = 6
wrong_attempts = 0

print("HANGMAN GAME\n")
print("Guess the word (one letter at a time):")
print(" ".join(display))

while wrong_attempts < max_attempts and "_" in display:
    guess = input("\nEnter a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Invalid input! Enter a single alphabet.")
        continue

    if guess in guessed:
        print("You already guessed this letter.")
        continue

    guessed.add(guess)

    if guess in secret_word:
        print("Correct guess!")

        # Reveal all positions of the guessed letter
        for i, ch in enumerate(secret_word):
            if ch == guess:
                display[i] = guess
    else:
        wrong_attempts += 1
        print("Wrong guess! Attempts left:", max_attempts - wrong_attempts)

    print(" ".join(display))

# ---- Final Result ----
if "_" not in display:
    print("\nCongratulations! You guessed the word:", secret_word.upper())
else:
    print("\nGame Over! You failed to guess the word.")
    print("The correct word was:", secret_word.upper())

