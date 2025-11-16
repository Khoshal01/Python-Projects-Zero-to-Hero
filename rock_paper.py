
import random 


choice= ["rock","paper","scissors"]

def game(user_choice):
    computer_choice = random.choice(choice)

    if computer_choice == user_choice:
        print("Draw")
    
    elif (user_choice == "rock" and computer_choice == "scissors") or \
     (user_choice == "paper" and computer_choice == "rock") or \
     (user_choice == "scissors" and computer_choice == "paper"):
        print("You win!")
    
    else:
        print("Computer Win!")


user_choice = input("Rock , Paper , Scisoors :- ").lower()
game(user_choice)
while True:
   

    play = input("Try Again (Y/N)").lower()
    if play == 'y':
        user_choice = input("Rock , Paper , Scisoors :- ").lower()
        game(user_choice)
    else:

        break
