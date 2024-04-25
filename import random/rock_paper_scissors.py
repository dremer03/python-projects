import random

user_wins = 0
computer_wins = 0

options = {
    '1': 'rock',
    '2': 'paper',
    '3': 'scissors'}

print('Go play a game!')

while True:
    user_choose = input('Choose Paper/Rock/Scissors or q to leave: ').lower()
    if user_choose == 'q':
        break
    if user_choose not in options.values():
        continue

    random_number = random.choice(list(options.keys()))
    computer_choose = options[str(random_number)]

    if user_choose == 'paper' and computer_choose == 'rock':
        print('You won')
        user_wins += 1
    elif user_choose == 'rock' and computer_choose == 'scissors':
        print('You won')
        user_wins += 1
    elif user_choose == 'scissors' and computer_choose == 'paper':
        print('You win')
        user_wins += 1
    else:
        print('You lose')
        computer_wins += 1

print(f"Your wins = {user_wins}, computer wins = {computer_wins}")
print('Goodbye!')



