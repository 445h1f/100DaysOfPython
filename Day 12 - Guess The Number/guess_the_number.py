from art import logo
import random

def playGame():
    """Plays guess the number game"""
    print(logo)
    print('Welcome to the Number Guessing Game!\nI\'m thinking of a number between 1 and 100.')
    correctNumber = random.randint(1, 100)
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if difficulty == 'easy':
        attemptsLeft = 10
    else:
        attemptsLeft = 5
    while attemptsLeft != 0:
        print(f'You have {attemptsLeft} attempts remaining to guess the number.')
        guess = int(input('Make a guess: '))
        if guess != correctNumber:
            if guess > correctNumber:
                print('Too high.')
                attemptsLeft -= 1
            elif guess < correctNumber:
                print('Too low.')
                attemptsLeft -= 1
            if attemptsLeft == 0:
                print('You\'d ran out of guesses, you lose.')
            else:
                print('Guess again.')
        else:
            print(f'You got it! The answer was {guess}.')
            attemptsLeft = 0

playGame()
