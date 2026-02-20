import random

low = 1
high = 100

number = random.randint(low, high)
guesses = 0   

while True:
    guess = int(input(f'Enter a number between {low} - {high}: '))
    
    guesses += 1

    if guess < number:
        print(f'{guess} is too low')

    elif guess > number:
        print(f'{guess} is too high')

    else:
        print(f'{guess} is correct!')
        print(f'This round took you {guesses} guesses.')
        break  
     
