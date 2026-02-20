import random

options = ('rock', 'paper', 'scissors')
playing = True

while playing:
    player = None
    computer = random.choice(options)

    while player not in options:
        player = input('Enter a choice (rock, paper, scissors): ').lower()

    print(f'Player: {player}')
    print(f'Computer: {computer}')

    if player == computer:
        print("It's a tie!")

    elif (player == 'paper' and computer == 'rock') or \
         (player == 'rock' and computer == 'scissors') or \
         (player == 'scissors' and computer == 'paper'):
        print('You win!')

    else:
        print('You lose!')

    play_again = input('Do you want to play again? (y/n): ').lower()

    if play_again == 'n':
        playing = False

print("Thanks for playing!")
