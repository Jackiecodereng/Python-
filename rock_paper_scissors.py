import random



user_wins = 0
computer_wins = 0
options =['rock','paper','scissors']

while True:
    user_input = input(" Type Rock/Paper/Scissors? or Q to quit: ").lower()
    if user_input == 'q':
       break

    if user_input not in options:
        continue

    random_number =random.randint(0,2)
    #rock=0,paper=1,scissors=2
    computer_player = options[random_number]
    print('computer picked',computer_player + ',')

    if user_input == 'rock' and computer_player == 'scissors':
        print('you won')
        user_wins+=1
        continue

    elif user_input == 'paper' and computer_player == 'rock':
        print('you won')
        user_wins += 1
        continue

    elif user_input == 'scissors' and computer_player == 'paper':
        print('you won')
        user_wins += 1
        continue

    elif user_input == computer_player :
        print('try again')
        continue
    else:
        print('you lost')
        computer_wins+=1
print('you won',user_wins,'times')
print('the computer won',computer_wins,'times')
print('goodbye')