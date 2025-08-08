import random

# Predefined list of 5 words
word_list = ["apple", "table", "grape", "chair", "plant"]

# Randomly select a word
secret_word = random.choice(word_list)
guessed_letters = []
max_attempts = 6
wrong_attempts = 0

# Display current progress
def display_word():
    display = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "
    return display.strip()

print("🎯 Welcome to Hangman!")
print("Guess the word, one letter at a time.")

# Game loop
while wrong_attempts < max_attempts:
    print("\nWord:", display_word())
    guess = input("Enter a letter: ").lower()

    if not guess.isalpha() or len(guess) != 1:
        print("❌ Please enter a single valid alphabet letter.")
        continue

    if guess in guessed_letters:
        print("⚠ You've already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in secret_word:
        print("✅ Good guess!")
        if all(letter in guessed_letters for letter in secret_word):
            print("🎉 Congratulations! You guessed the word:", secret_word)
            break
    else:
        wrong_attempts += 1
        print(f"❌ Wrong guess! Attempts left: {max_attempts - wrong_attempts}")

else:
    print("💀 Game Over! The word was:", secret_word)
