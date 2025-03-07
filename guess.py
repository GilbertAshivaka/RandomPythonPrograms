#A guessing game 
from random import randint
secret_num = randint(1,100)
num_guesses = 0
guess = 0
while guess != secret_num and num_guesses <=4:
    guess =eval(input("Enter your guess  "))
    num_guesses+=1
    if guess < secret_num:
        print("HGHER.",5 - num_guesses,"guesses left.")
    elif guess > secret_num:
        print("LOWER.",5 - num_guesses,"guesses left")
    else:
        print("You got it!")
    
if num_guesses == 5 and guess != secret_num:
    print("You loose. The correct number is", secret_num,end=".")
 