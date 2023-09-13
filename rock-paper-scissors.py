#creating a game.
import random

computer_choice= random.choice(['rock', 'paper', 'scissors']) #This code helps generate random values.
user_choice = input('Pick rock, paper, or scissors? ')

print('Computer choice:', computer_choice) # this prints the computer choice so we can see what the computer choices.


if computer_choice == user_choice:
    print('Tie.')
elif user_choice == 'rock' and computer_choice == 'scissors':
    print('You win!')
elif user_choice == 'paper' and computer_choice == 'rock':
    print('You win!')
elif user_choice == 'scissors' and computer_choice == 'paper':
    print('You win!')
else:
    print('You lose, Computer win!')