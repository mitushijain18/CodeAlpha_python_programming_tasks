import random

def hangman():
    # 1. Predefined list of 5 words
    words = ['python', 'coding', 'intern', 'development', 'software']
    word = random.choice(words)
    guessed_letters = []
    attempts = 6  

    print("Welcome to Hangman!")

    while attempts > 0:
        display_word = "".join([letter if letter in guessed_letters else "_" for letter in word])
        print(f"\nWord: {display_word}")
        print(f"Attempts left: {attempts}")
        if "_" not in display_word:
            print("Congratulations! You guessed the word!")
            break

        guess = input("Guess a letter: ").lower()
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single valid letter.")
            continue
        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.append(guess)
        if guess in word:
            print(f"Good job! '{guess}' is in the word.")
        else:
            attempts -= 1
            print(f"Sorry, '{guess}' is not in the word.")

    if attempts == 0:
        print(f"\nGame Over! The word was: {word}")

if __name__ == "__main__":
    hangman()