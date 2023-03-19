"""
Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number, 
then tell them whether they guessed too low, too high, or exactly right. (Hint: remember to use 
the user input lessons from the very first exercise)

Extras:

Keep the game going until the user types “exit”
Keep track of how many guesses the user has taken, and when the game ends, print this out.

https://www.practicepython.org/exercise/2014/04/02/09-guessing-game-one.html
"""

import random
a=random.randint(1,9)

c=0
while 1:
    num = input("Guess a number between 1 and 9, type exit to exit the game : ")
    if num.lower()=="exit":
        print("Thank you for playing, have a great day!!!")
        break
    num=int(num)
    c+=1
    if num<a:
        print("Oops you've guessed too low")
       
    elif num>a:
        print("Oops you've guessed too high")
        
    elif num==a:
        print(f"Congratulations!!! You've guessed it right, you've made {c} guesses")

#Alternate solutions : https://www.practicepython.org/solution/2014/04/10/09-guessing-game-one-solutions.html