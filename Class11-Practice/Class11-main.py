# Generate a random number between 1 and 9 (including 1 and 9).
# Ask the user to guess the number, then tell them whether they guessed too low,
# too high, or exactly right. When they guess right we will tell them how many times they guessed
from Game1 import *

def userGuessGame():
    game = Game()
    while True:
        user_guess = input("Guess a number between 1 and 9 (exit to exit): ")
        if user_guess == "exit":
            break
        else:
            try:
                game.guess(int(user_guess))
            except ValueError:
                print("Invalid input. Try again.")

#Create a version of the game where you guess a number between 1 and 100 and have
# the computer guess. You will provide feedback if it was too high, too low,
# or correct. The computer will then tell you how many tries it took.
def compGuessGame():
    game = Game_2()
    low = 1
    high =100
    found=False
    while True:
        try:
            targetNumber = (int)(input("Input the target number between 1 and 100: "))
        except ValueError:
            print("Invalid input. End game.")
            break

        if targetNumber > 100 or targetNumber < 1:
            continue
        
        while True:
            if(low>high):
                break
            guess = game.guess(low, high)
            c = input(f'Is it correct? Too low (L) or too High (H)??...')
            if(c.upper()  == 'H'):
                high=guess-1
            elif (c.upper() == 'L'):
                low=guess+1
            else:                
                game.reset() 
                found=True 
                break 

        if (found==True)  : 
            print(f'That took me {game.getTries()} tries.') 
        else :
            print(f'Something is wrong in your answers') 
compGuessGame()