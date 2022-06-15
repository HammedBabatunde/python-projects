import string 
import random 

words = ['monkeypox', 'daniel-dgg']

# function to get valid word without '-', or ' '
def get_valid_word(words):
    word = random.choice(words) 

    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word.upper()

def hangman():
    word = get_valid_word(words)
    word_letters  = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()
    lives = 6

    while len(word_letters) > 0 and lives > 0:
        
        print(f'You have {lives} lives and you have used these letters: ', ' '.join(used_letters))

        #what current word is (i.e W - R D)
        # for letter in word:
        #     if letter in used_letters:
        #         word_list = [letter]
        #     else:
        #         word.list = ['-']

        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Current word: ', ''.join(word_list))

        user_letter = input('Please select a Character: ').upper()

        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)

            else: 
                lives -= 1
        
        elif user_letter in used_letters:
            print('This letter has been used. Please select another Character')
        
        else:
            lives -= 1
            print('Invalid character')

    if lives > 0:
        print(f"Congratulation, You have successfully guessed the word '{word}'")
    else:
        print(f'The correct word is {word}')
     
    if lives == 0:
        print(f'You died, sorry. The word was {word}')
    else:
        print(f'You have correctly guessed the letters of {word}')

    # if len(word_letters) <=0:
    #     print(f'You have correctly guessed the letters of {word}')

def play_hangman():
    user_input = input('Do you want to play hangman')
    continue_gaming = 'Yes'

    while True:
        if (user_input == 'Yes' and continue_gaming == 'Yes'):
            hangman()
            continue_gaming = input('Do you want to continue playing hangman')
            continue
        
        elif (user_input == 'No' or continue_gaming == 'No'):
            print('Thanks for playing my game')
            break
    
    # elif continue_gaming == 'Yes':
    #     hangman()
    
  
play_hangman()

