""" Number Guess Game

Pick a random number between 1 and 100. If the random number is divisible by 7,
pick another number and continue picking new numbers until the random number is
not divisible by 7. ( hint: use a loop! )

Ask the user to guess the number. If the user's guess is higher than the random
number, tell the user the guess is too high. If the user's guess is lower than
the random number, tell the user the guess is too low. If the user guesses the
number, tell the user the guess is correct and stop the game. If the user does
not guess the number, allow the user to keep guessing until the user gets the
right answer.


Write the main part of your program as a loop. If the user guesses the number,
break out of the loop. If the user does not guess the number, continue the loop.

If the user guesses a number that is divisible by 7, tell the user "that is a
very bad number, starting over " and pick another number and continue picking
new numbers until the number is not divisible by 7.

Get a random number:
    n = random.randint(1, 100)

Use the ask_integer function to get the user's guess, like this:
    guess = ask_integer("Guess a number between 1 and 100: ")

NOTE! The prompts and output for your program will be in the teminal
at the bottom of the editor screen; this program does not use the GUI.

"""

import random

def ask_integer(prompt):
    """Function to ask the user for an integer"""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a valid number!")

def generate_random_number():
    """Generate a random number between 1 and 100 that is not divisible by 7"""
    while True:
        number = random.randint(1, 100)
        if number % 7 != 0:
            return number

def main():
    # Pick the random number
    random_number = generate_random_number()

    while True:
        # Get the user's guess
        guess = ask_integer("Guess a number between 1 and 100: ")

        # Check if the guess is divisible by 7
        if guess % 7 == 0:
            print("That is a very bad number, starting over.")
            random_number = generate_random_number()
            continue
        
        # Provide feedback based on the guess
        if guess < random_number:
            print("Too low!")
        elif guess > random_number:
            print("Too high!")
        else:
            print("Congratulations! You guessed the correct number.")
            break

# Run the game
if __name__ == "__main__":
    main()
