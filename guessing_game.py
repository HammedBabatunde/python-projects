import random

def guess(x):
    random_number = random.randint(1, x)

    guess = 0

    while(guess != random_number):
        try:
            guess = int(input(f'Guess input a number between 1 and {x}: '))
        except ValueError:
            print('Please enter a Valid Number')
        else:
            if guess < random_number:
                print('Sorry, guessed number is too low, try again')
            elif guess > random_number:
                print('Sorry, guessed number is too high, try again')

    print(f"Yay, you have correctly guessed {random_number}") 
