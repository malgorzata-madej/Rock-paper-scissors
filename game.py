#Rock paper scissors

import random

winner = ''
games = int(input("How many times do you want to play? "))

choices = ['ROCK', 'PAPER', 'SCISSORS']

for i in range (0, games):

    choice = random.choice(choices)
    
    user = ''
    while (user.upper() != 'ROCK' and
           user.upper() != 'PAPER' and
           user.upper() != 'SCISSORS'):
        user = input("What do you play? ")

    print('Your choice:', user, " Computer's choice:", choice)

    if choice == user.upper():
        winner = "Tie"
    elif choice == 'ROCK' and user.upper() == 'SCISSORS':
        winner = 'You lose'
    elif choice == 'PAPER' and user.upper() == 'ROCK':
        winner = 'You lose'
    elif choice == 'SCISSORS' and user.upper() == 'PAPER':
        winner = 'You lose'
    else:
        winner = 'You win'

    print(winner)
