#!/bin/python3

'''
Create a game of guess the number :
    1. Create a script that will ask the user how many games they would like to play
    2. For every game, ask the player to select a random number between 1 - 25
    3. Inform player if the number is higher or lower
    4. Build a loop statement that will iterate number of games and numbers picked
    5. When user guesses right, tell them how many guesses it took.
'''

import random
import datetime

def get_int(message):
    '''
    Handle errors while trying to get an integer from user
    '''
    print(message)
    try:
        user_input = int(input())
        return user_input
    except ValueError:
        print("Please only answer with an integer.")
    return False


def game_round(game):
    '''
    Run through a round with the user
    '''
    print(f'Playing round: {game}')
    # Pick random number
    print("Picking a random number between 1 and 25 (inclusive)...")
    secret = random.randint(1, 25)
    guess = False
    guess_count = 0
    while not guess:
        guess_count += 1
        user_guess = get_int("\tPlease provide a guess:")
        if not user_guess:
            print("\tEnding round due to issue with last input.")
            break
        if user_guess < secret:
            print("\t\tYou need to guess higher.")
        if user_guess == secret:
            print(f'\tCongratulations, you guessed it in {guess_count} tries!')
            guess = True
        if user_guess > secret:
            print("\t\tYou need to guess lower.")

def main():
    '''
    Get round count and call game_round()
    '''
    random.seed(datetime.datetime.now())
    # Ask for game count
    game_count = get_int("How many games would you like to play? [integer]")
    # Play user provided count fo rounds
    for game in range(1, game_count+1):
        game_round(game)

if __name__ == "__main__":
    main()
