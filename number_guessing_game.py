# generate a new number and guess how long it takes the user to guess the code

import random

# r = random.randrange(-5,11) # generate -4 to 10 or(11)
# print(r)

# r = random.randint(-5,11) # generate to 11
# print(r)
guesses =0  # calculates the number of attempts

top_of_range = input('type a number:  ')

if top_of_range.isdigit():   # checks if the number is adigit and if it is converts it into an integer
   top_of_range = int(top_of_range)
   if top_of_range <= 0:
       print('please type a number larger than 0')
       quit()
else:
    print('please type a number ')
    quit()

random_number = random.randint(0,top_of_range)
# print(random_number)
# let us let the user guess till they get it correct.

while True:
    guesses = guesses + 1
    user_guess = input('guess a number:  ')

    if user_guess.isdigit():
        user_guess = int(user_guess)

    else:
        print('please type a number ')
        continue

    if user_guess == random_number:
        print('you guessed the number')
        break
    elif user_guess > random_number:
         print('you guessed too high')
    else:
        print('you guessed too low')

print('you guessed the number in ',guesses,' guesses')
 # break ends aloop
 # continue  repeats the loop