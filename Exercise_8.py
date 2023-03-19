"""
Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input), compare them, print out a message of congratulations to the winner, and ask if the players want to start a new game)

Remember the rules:

1.Rock beats scissors
2.Scissors beats paper
3.Paper beats rock

https://www.practicepython.org/exercise/2014/03/26/08-rock-paper-scissors.html
"""

print("Welcome to Rock Paper Scissors!!!")
while 1:
    
    print("Enter your choice from rock, paper and scissors")
    player_1=input("Enter for player 1 :")
    player_2=input("Enter for player 2:")
    if player_1==player_2:
        print("Its a tie")
        if input("Do you want to play again? yes/no :")=="yes":
            continue
        else:
            print("Thank you for playing!!!")
            break
    elif player_1=="rock" and player_2=="scissors":
        print("Player 1 wins")
        if input("Do you want to play again? yes/no :")=="yes":
            continue
        else:
            print("Thank you for playing!!!")
            break
    elif player_1=="scissors" and player_2=="paper":
        print("Player 1 wins")
        if input("Do you want to play again? yes/no :")=="yes":
            continue
        else:
            print("Thank you for playing!!!")
            break
    elif player_1=="paper" and player_2=="rock":
        print("Player 1 wins")
        if input("Do you want to play again? yes/no :")=="yes":
            continue
        else:
            print("Thank you for playing!!!")
            break
    elif player_2=="rock" and player_1=="scissors":
        print("Player 2 wins")
        if input("Do you want to play again? yes/no :")=="yes":
            continue
        else:
            print("Thank you for playing!!!")
            break
    elif player_2=="scissors" and player_1=="paper":
        print("Player 2 wins")
        if input("Do you want to play again? yes/no :")=="yes":
            continue
        else:
            print("Thank you for playing!!!")
            break
    elif player_2=="paper" and player_1=="rock":
        print("Player 2 wins")
        if input("Do you want to play again? yes/no :")=="yes":
            continue
        else:
            print("Thank you for playing!!!")
            break
    else:
        print("Invalid Choice")
        



