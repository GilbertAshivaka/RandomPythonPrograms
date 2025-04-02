print("============================================================")

from random import randint

attempts_list = []

def show_score():
    if not attempts_list:
        print("There are currently no high scores, it\'s your\'s for the taking!")

    else: print(f"The curreny high score is {max(attempts_list)} attempts.")


def start_game():
    attempts = 0
    secret_num = randint(1, 10)
    print("Hello traveller, welcome to the game of guesses.")
    player_name = input("What is your name?  ")
    wanna_play = input(f"Hi {player_name}, would you like to play the guessing game? Enter(Yes/No)  ")

    if wanna_play.lower() != "yes":
        print("Well, that\'s cool. Thanks")
        exit()
    
    else:
        show_score()

    while wanna_play.lower() == "yes":
        try:
            guess = eval(input("Choose a number between 1 and 10:  "))
            if 1<guess>10:
                raise ValueError("Please guess a number within the given range.")
            

            attempts += 1
            attempts_list.append(attempts)

            if secret_num == guess:
                print("You got it right!")
                print(f"It took you {attempts} attempts.")
                wanna_play = input("Would you like to play again? Enter(Yes/No)")

                if wanna_play.lower() != "yes":
                    print("That\'s cool. Have a good one.")
                    break
                
                else: 
                    attempts = 0
                    secret_num = randint(1, 10)
                    show_score()
                    continue

            else:
                if guess > secret_num:
                    print("Lower than that.")
                else:
                    print("Higher than that.")
            
        except ValueError as err:
            print("Oh no! That\'s not a valid value. Please try again")
            print(err)

if __name__ == "__main__":
    start_game()

