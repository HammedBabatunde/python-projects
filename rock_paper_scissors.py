import random

def play():
    player = input('Please select r -rock, p - paper, s- scissiors: ')
    computer = random.choice(['r', 's', 'p'])

    if player == computer:
        return 'You tied with computer'
    
    if player_win(player, computer):
        return 'You win'

    return 'You lost'

def player_win(player, computer):
    if (player == 'p' and computer == 'r') or (player == 's' and computer == 'p') or (player == 'r' and computer == 's'):
        return True


print(play())