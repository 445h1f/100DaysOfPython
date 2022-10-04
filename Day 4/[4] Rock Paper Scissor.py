import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
things = [rock, paper, scissors]

userInput = input(
    "What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. ")

if int(userInput) > 2 or int(userInput) < 0:
    print(f'It\'s not a valid number. You lose')
else:
    userChoice = things[int(userInput)]

    computerChoice = random.choice(things)

    print(f'You chose:\n{userChoice}')
    print(f'Computer chose:\n{computerChoice}')
    if userChoice == computerChoice:
        print(f'It\'s Draw')
    else:
        if userChoice == rock and computerChoice == scissors or userChoice == scissors and computerChoice == paper or userChoice == paper and computerChoice == rock:
            print('You win')
        else:
            print('You lose')