
import random

secrate_number = random.randint(1,100)
attempt = 1
guess_number = int(input("Guess The Number:- "))
while True:

    if guess_number < secrate_number:
        guess_number = int(input("Too Low:- "))
        attempt += 1

    if guess_number >secrate_number :
        guess_number = int(input("Too High:- "))
        attempt += 1
    
    else:
        print("You Got it, in ",attempt," attempts")
        print("Gave Over!")
        break
    


