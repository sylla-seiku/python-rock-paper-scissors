import random

def play_game():
    while True:
        play_again = input('Do you want to play? Enter "y" Otherwise press <Enter> to quit:')
        if play_again != 'y':
            break  # Exit the loop if the user doesn't enter 'y'

        computer_choice = random.choice(['rock', 'paper', 'scissors'])
        user_choice = input('Pick rock, paper, or scissors: ')

        print('Computer choice:', computer_choice)

        if computer_choice == user_choice:
            print('Tie.')
        elif user_choice == 'rock' and computer_choice == 'scissors':
            print('You win!')
        elif user_choice == 'paper' and computer_choice == 'rock':
            print('You win!')
        elif user_choice == 'scissors' and computer_choice == 'paper':
            print('You win!')
        else:
            print('You lose. Computer wins!')

# Call the play_game function to start the game

play_game()




'''
#creating a game.
import random

play_game = input('Do you want to play "y" to play <enter> to quit '):


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

    '''