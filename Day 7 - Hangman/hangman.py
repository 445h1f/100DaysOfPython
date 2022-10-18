import random
import hangman_art
import hangman_words

print(hangman_art.logo)

wordList = hangman_words.words
chosenWord = random.choice(wordList).lower()
blankWordList = []
for i in chosenWord:
    blankWordList.append('_')
# print(chosenWord)

gameOver = False
leftLivesStrList = []
guessedWords = []

stages = hangman_art.stages

lives = 6
print(f'Game Started!\n')
while not gameOver:
    userGuess = input('Guess a letter: ').lower()
    if len(userGuess) != 1 or not userGuess.isalpha():
        print(f'Enter only single alphabet!')
        continue
    elif userGuess in guessedWords:
        print(f'You already guessed the letter {userGuess}')
        continue
    if userGuess in chosenWord:
        index = 0
        for i in chosenWord:
            if i == userGuess:
                blankWordList[index] = i
            index += 1
        if '_' not in blankWordList:
            print(f'Congratulations! You did it. The word was {chosenWord}')
            gameOver = True
        else:
            print(' '.join(blankWordList))
    else:
        lives -= 1
        print(f'You guessed a letter that\'s not in word. You lose a life!')
        print(stages[lives])
        if lives == 0:
            print(f'Oops! You failed to save the man from hanging😥')
            gameOver = True
    guessedWords.append(userGuess)
    if not gameOver and len(guessedWords) > 0:
        print(f'Guesed Letters: {", ".join(guessedWords)}')

