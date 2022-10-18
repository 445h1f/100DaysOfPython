import os

def clear():
    os.system('cls')

logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
print(f'{logo}\nWelcome to the secret auction program.')

auctionData = {}
loop = True
while loop:
    name = input('What is your name? ')
    bid = int(input('What\'s your bid? $'))
    auctionData[name] = bid
    continueBid = input('Are there any other bidders? Type \'yes\' or \'no\'. ')
    if continueBid == 'yes':
        clear()
    else:
        maxBid = -1
        for i in auctionData:
            bid = auctionData[i]
            if bid > maxBid:
                maxBid = bid
                winner = i
        clear()
        print(f'The winner is {winner} with a bid of ${bid}.')
        loop = False
        break
