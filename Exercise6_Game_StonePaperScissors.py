import random  # Importing random
import sys  # Importing sys 
from pygame import mixer  # Importing mixer from pygame

lst = ["S", "P", "X"]  # A list of the options: Stone, Paper and Scissors from which a random generation of choice occurs

attempts = 0  # In the beginning, the number of attempts have to be zero
compu = 0  # In the beginning, the score of computer has to be zero
user = 0  # In the beginning, the score of user has to be zero

print("Stone, Paper or Scissors?")
print("Enter:")

while True:
    attempts = 1
    mixer.init()
    mixer.music.load("Exercise6_Music_StartGame.mp3")
    mixer.music.set_volume(0.7)
    mixer.music.play()

    while attempts <= 10:
        print(11-attempts, "attempts left")

        print(" S for stone\n P for paper \n X for scissors")
        inpChoice = input()

        userChoice = inpChoice.upper()

        choice = random.choice(lst)  # A random option is chosen from Stone, Paper or Scissors from the list

        if userChoice == "S":  # When user chooses Stone
            print(f"You chose {userChoice} and CPU chose {choice}")
            if choice == "P":
                print("You could not win this one.\nBetter luck next time!")
                compu += 1
                mixer.music.load("Exercise6_Music_Lose.mp3")
                mixer.music.set_volume(0.7)
                mixer.music.play()
            elif choice == "S":
                print("Tie!")
            else:
                print("You won!")
                mixer.music.load("Exercise6_Music_Win.mp3")
                mixer.music.set_volume(0.7)
                mixer.music.play()
                user += 1
            print("\n")
            print("\t\t\t---------------------------------")
            print("\t\t\t             SCORE BOARD         |")
            print("\t\t\t---------------------------------")
            print(f"\t\t\tYou:                           {user}|")
            print(f"\t\t\tCPU:                           {compu}|")
            print("\t\t\t---------------------------------")
            print("\n\n\n")

        elif userChoice == "P":  # When user chooses Paper
            print(f"You chose {userChoice} and CPU chose {choice}")
            if choice == "S":
                print("You could not win this one.\nBetter luck next time!")
                compu += 1
                mixer.music.load("Exercise6_Music_Lose.mp3")
                mixer.music.set_volume(0.7)
                mixer.music.play()
            elif choice == "P":
                print("Tie!")
            else:
                print("You won!")
                mixer.music.load("Exercise6_Music_Win.mp3")
                mixer.music.set_volume(0.7)
                mixer.music.play()
                user += 1
            print("\n")
            print("\t\t\t---------------------------------")
            print("\t\t\t             SCORE BOARD         |")
            print("\t\t\t---------------------------------")
            print(f"\t\t\tYou:                           {user}|")
            print(f"\t\t\tCPU:                           {compu}|")
            print("\t\t\t---------------------------------")
            print("\n\n\n")

        elif userChoice == "X":  # When user chooses Scissors
            print(f"You chose {userChoice} and CPU chose {choice}")
            if choice == "S":
                print("You could not win this one.\nBetter luck next time!")
                compu += 1
                mixer.music.load("Exercise6_Music_Lose.mp3")
                mixer.music.set_volume(0.7)
                mixer.music.play()
            elif choice == "X":
                print("Tie!")
            else:
                print("You won!")
                mixer.music.load("Exercise6_Music_Win.mp3")
                mixer.music.set_volume(0.7)
                mixer.music.play()
                user += 1
            print("\n")
            print("\t\t\t---------------------------------")
            print("\t\t\t            SCORE BOARD         |")
            print("\t\t\t---------------------------------")
            print(f"\t\t\tYou:                           {user}|")
            print(f"\t\t\tCPU:                           {compu}|")
            print("\t\t\t---------------------------------")
            print("\n\n\n")
        else: # When user does not choose and enter one among the given letters
            print("Please enter a valid letter and try again!")
        attempts += 1



    if attempts >= 10:  # When all (10) attempts get over
        
        if user > compu:  # When User scores more than Computer/CPU
            print("Congratulations!! \nYou WON!!!!!!")
            mixer.music.load("Exercise6_Music_GameWin.mp3")
            mixer.music.set_volume(0.7)
            mixer.music.play()
        elif compu > user:  # # When Computer/CPU scores more than User
            print("Sorry! \nYou lost the game.\nPlease try again.\n")
        else:
            print("Oh my God! Its a draw!")

        print("Your score      :              ", user)
        print("Computer's score:              ", compu)


        print("Do you want to play again?")  # Prompting User to play again

        print("Press and enter (Y/N)")  # Asking User to input

        again = input()  # Taking User input
        PlayAgain = again.upper()
        
        if PlayAgain == "Y":
            print("OKAY!\nGET READY")

        else:
            print("Bye")
            sys.exit(0)


    else:
        print("Bye")
