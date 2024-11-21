name =input('type your name?')
print('welcome',name,'to this adventure!')

answer = input(
    'you are on a dirt road,it has come to an end you can go right or left(right/left):').lower()

if answer == 'left':
    answer = input('you come to a river and u can walk around it or swim across it')
    if answer =='swim':
        print('you swam and was eaten by a crocodile')
    elif answer =='walk':
        print('you walk for many  days and died ')
    else:
        print('not a valid option .you lose')
elif answer == 'right':
    answer = input('you come to a bridge do you wish to cross or head back(cross/back):')
    if answer =='back':
        print('you go back to the main road')
    elif answer =='cross':
         answer =  input('you cross the bridge and meet a stranger do yo tealk to them(yes/no)?')

    if answer =='yes':
         print('you talk to the stranger and they show you home .you win')
    elif answer =='no':
        print('you turn off the stranger and die.you lose')

    else:
       print('not a valid option .you lose.')
print('thankyou for playing')