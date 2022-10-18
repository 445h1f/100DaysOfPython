from game_data import data
from art import logo, vs
from random import randint
import os

def clearScreen():
    os.system('cls')

def randomComparisonObject(previousIndex):
    """Returns a random unique item from the list. Takes previous index of previous item to tackle duplicating of item."""
    # generate a random number for getting random item data list
    randomIndex = randint(0, len(data)-1)

    # keeps generating random index while index is equal to preivous item index so that both comparison obhject will be different always
    while randomIndex == previousIndex:
        randomIndex = randint(0, len(data)-1)

    # gets data item on that index
    randomObject = data[randomIndex]

    # assign index key with item index in data so that it can be used again to get different item from data list
    randomObject['index'] = randomIndex
    return randomObject

def compareFollowers(itemAIndex, itemBIndex):
    """Compares the followers of two given item index from data. Returns True if a item is greater else False"""
    itemAFollowers = data[itemAIndex]['followers']
    itemBFollowers = data[itemBIndex]['followers']
    if itemAFollowers > itemBFollowers:
        return True
    else:
        return False


def higherLowerStart():
    """Starts the higher lower game."""

    # flag var for while loop to keep running while game is not over
    gameOver = False

    # variable to store user score
    userScore = 0

    # generate a random index to get a random object from data to start.
    itemAIndex = randint(0, len(data)-1)
    # getting Item A details
    itemA = data[itemAIndex]
    itemAName = itemA['name']
    itemADescription = itemA['description']
    itemAFollowers = itemA['follower_count']
    itemACountry = itemA['country']

    while not gameOver:
        # print the beautiful ASCII Art of Higher Lower Game
        print(logo)
        if userScore != 0:
            print(f'Correct! Your new score is {userScore}.')
        print(f'Compare A: {itemAName}, a {itemADescription}, from {itemACountry}')
        # getting item b for comparison
        itemB = randomComparisonObject(itemAIndex)
        itemBIndex = itemB['index']
        itemBName = itemB['name']
        itemBDescription = itemB['description']
        itemBFollowers = itemB['follower_count']
        itemBCountry = itemB['country']
        # print vs logo
        print(vs)
        print(f'Compare B: {itemBName}, a {itemBDescription}, from {itemBCountry}')
        userChoice = input(f'Who has more followers? Type \'A\' or \'B\'?: ').lower()
        if userChoice == 'a':
            if itemAFollowers > itemBFollowers:
                userScore += 1
            else:
                gameOver = True
        else:
            if itemBFollowers > itemAFollowers:
                userScore += 1
            else:
                gameOver = True

        if gameOver:
            clearScreen()
            print(logo)
            print(f'Game over! Your final score is {userScore}.')
        else:
            itemAIndex = itemBIndex
            itemAFollowers = itemBFollowers
            itemAName = itemBName
            itemADescription = itemBDescription
            itemACountry = itemBIndex
            clearScreen()

higherLowerStart()