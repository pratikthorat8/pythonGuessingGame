#Guessing game
import random
print('Hello, What is your name buddy ?')
name = input() #User input.
print("Well " + name +  " I am thinking of a number between 0 and 20")
secret_number = random.randint(0,20) # Generates a random number between 0 and 20.

for guesses_taken in range(1,7):
    print('Take a guess')
    guessed_number = int(input())
    if guessed_number > secret_number: #for guess higher than number
        print('Your guess is a bit higher')
    elif guessed_number < secret_number: #for guess lower than number
        print('Your guess is a bit lower')
    else:
        break # this is the condition where guess is correct
if guessed_number == secret_number:
    print('Good job ' + name)
    print('You took ' + str(guesses_taken) + ' guesses')
else:
    print("Nope i was think of " + str(secret_number) + '. Better luck next time')