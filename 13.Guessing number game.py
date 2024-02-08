# import requirements (modules)
import random

#Take Name of user as input
name = str(input('Hello what is your name? '))
print('Well '+name+', I am thinking of a number between 1 and 20')
secretNumber = random.randint(1, 20)

#Ask the user for their guess
for guessesTaken in range(1, 7):
    print('Take a guess.')
    guess = int(input())

    #Check if the guess is too high or too low
    if guess < secretNumber:
        print('Your guess is too low.')
    elif guess > secretNumber:
        print('Your guess is too high.')
    else:
        break

# Print out the number of guesses it took to get the correct answer
if guess == secretNumber:
    print('Good job. '+name+'! you guessed my number in '+str(guessesTaken)+' guesses.')
else:
    print('Nope. The number I was thinking of was '+str(secretNumber))