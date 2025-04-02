import os
from random import randint
import time 


def num_dice():
    while True:
        try:
            num_dice = input('Number of dice: ')
            valid_responces = ['1', 'two', '2', 'two']
            if num_dice not in valid_responces:
                raise ValueError('1 or 2 only')
            else: 
                return num_dice
        except ValueError as err:
            print(err)

def roll_dice():
    min_value = 1
    max_value = 6
    roll_again = 'y'

    while roll_again.lower() == 'y' or roll_again.lower() == 'yes':
        os.system('cls' if os.name == 'nt' else 'clear')
        amount = num_dice()

        if amount == '2' or amount == 'two':
            print('Rolling dice...')
            time.sleep(4)
            dice_1 = randint(min_value, max_value)
            dice_2 = randint(min_value, max_value)

            print('The values are:')
            time.sleep(2)
            print('Die one:',dice_1)
            time.sleep(2)
            print('Die two:',dice_2)
            time.sleep(2)
            print('Total:', dice_1+dice_2)
            time.sleep(2)
            roll_again = input('Roll again? ')

        else:
            print('Rolling the die...')
            dice_1= randint(min_value, max_value)
            print(f'The value is {dice_1}')

            roll_again = input('Roll again?')

if __name__ == '__main__':
    roll_dice()

    

