print('Welcome to my computer quiz game!')
  #ask user if they want to play
playing = input('Do you want to play ?  ')

# check if user saide yes or no if no exit
if playing .lower() != 'yes':  #!= means no equal while == means equal to  ,the .lower helps the user even they typed their answer in different cases its still converted to lower case or .upper()
    quit()
print('okay! lets play :)')
score = 0     # this counts how many questions the user got correct.

answer =input('what does cpu stand for? ')
if answer.lower() == 'central processing unit':
    print('the answer is correct :)')
    score = score + 1
else:
    print('the answer is incorrect :(')

answer =input('what does gpu stand for? ')
if answer.lower() == 'graphics processing unit':
    print('the answer is correct :)')
    score = score + 1
else:
    print('the answer is incorrect :(')

answer =input('what does RAM stand for? ')
if answer.lower() == 'random access memory':
    print('the answer is correct :)')
    score = score + 1
else:
    print('the answer is incorrect :(')

answer =input('what does ROM stand for? ')
if answer .lower() == 'read only memory':
    print('the answer is correct :)')
    score = score + 1
else:
    print('the answer is incorrect :(')


print('you got '+ str(score) + ' questions correct!')
print('you got '+ str((score/4) *100) + ' %')  # GIVES  a percentage 4 is the no of questions