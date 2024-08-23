import random

def display_board(word, guessed_letters):
    display = ''.join([letter if letter in guessed_letters else '_' for letter in word])
    return ' '.join(display)

def hangman():
    words = ['python', 'hangman', 'challenge', 'programming', 'developer']
    word = random.choice(words).lower()
    guessed_letters = set()
    attempts = 6
    guessed_word = False
    
    print("Welcome to Hangman!")
    print(display_board(word, guessed_letters))

    while attempts > 0 and not guessed_word:
        guess = input("Guess a letter: ").lower()
        
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single alphabetical character.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.add(guess)

        if guess in word:
            print("Good guess!")
        else:
            attempts -= 1
            print(f"Incorrect! You have {attempts} {'attempts' if attempts > 1 else 'attempt'} left.")
        
        print(display_board(word, guessed_letters))

        if '_' not in display_board(word, guessed_letters):
            guessed_word = True
            print("Congratulations! You guessed the word!")

    if not guessed_word:
        print(f"Game over! The word was '{word}'.")

if __name__ == "__main__":
    hangman()

