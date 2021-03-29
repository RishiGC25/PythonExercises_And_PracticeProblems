import random
import sys
from pygame import mixer

lst = ["S", "P", "X"]
attempts = 0
compu = 0
user = 0
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

        choice = random.choice(lst)

        if userChoice == "S":
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
            print("\t\t\t             SCORE BOARD")
            print("\t\t\t---------------------------------")
            print(f"\t\t\tYou:                           {user}")
            print(f"\t\t\tCPU:                           {compu}")
            print("\n\n\n")

        elif userChoice == "P":
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
            print("\t\t\t             SCORE BOARD")
            print("\t\t\t---------------------------------")
            print(f"\t\t\tYou:                           {user}")
            print(f"\t\t\tCPU:                           {compu}")
            print("\n\n\n")

        elif userChoice == "X":
            print(f"You chose {userChoice} and CPU chose {choice}")
            if choice == "S":
                print("You could not win this one.\nBetter luck next time!")
                compu += 1
                mixer.init()
                mixer.music.load("Exercise6_Music_Lose.mp3")
                mixer.music.set_volume(0.7)
                mixer.music.play()
            elif choice == "X":
                print("Tie!")
            else:
                print("You won!")
                mixer.init()
                mixer.music.load("Exercise6_Music_Win.mp3")
                mixer.music.set_volume(0.7)
                mixer.music.play()
                user += 1
            print("\n")
            print("\t\t\t            SCORE BOARD")
            print("\t\t\t---------------------------------")
            print(f"\t\t\tYou:                           {user}")
            print(f"\t\t\tCPU:                           {compu}")
            print("\n\n\n")
        else:
            print("Please enter a valid letter and try again!")
        attempts += 1

    if attempts >= 10:
        
        if user > compu:
            print("Congratulations!! \nYou WON!!!!!!")
            mixer.init()
            mixer.music.load("Exercise6_Music_GameWin.mp3")
            mixer.music.set_volume(0.7)
            mixer.music.play()
        elif compu > user:
            print("Sorry! \nYou lost the game.\nPlease try again.\n")
        else:
            print("Oh my God! Its a draw!")

        print("Your score      :              ", user)
        print("Computer's score:              ", compu)

        print("Do you want to play again?")

        print("Press and enter (Y/N)")

        again = input()
        PlayAgain = again.upper()
        if PlayAgain == "Y":
            print("OKAY!\nGET READY")
        else:
            print("Bye")
            sys.exit(0)
    else:
        print("Bye")
