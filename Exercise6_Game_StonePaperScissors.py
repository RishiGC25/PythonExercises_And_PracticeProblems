import random
import sys
lst = ["S", "P", "X"]
attempts = 0
compu = 0
user = 0
print("Stone, Paper or Scissors?")
print("Enter:")

while True:
    attempts = 1

    while attempts <= 10:
        print(11-attempts, "attempts left")

        print(" S for stone\n P for paper \n X for scissors")
        inpChoice = input()

        userChoice = inpChoice.upper()

        choice = random.choice(lst)
        print(f"You chose {userChoice} and CPU chose {choice}")

        if userChoice == "S":
            if choice == "P":
                print("You could not win this one.\nBetter luck next time!")
                compu += 1
            elif choice == "S":
                print("Tie!")
            else:
                print("You won!")
                user += 1
            print("\n")
            print("             SCORE BOARD")
            print("---------------------------------")
            print(f"You:                           {user}")
            print(f"CPU:                           {compu}")
            print("\n")
        elif userChoice == "P":
            if choice == "S":
                print("You could not win this one.\nBetter luck next time!")
                compu += 1
            elif choice == "P":
                print("Tie!")
            else:
                print("You won!")
                user += 1
            print("\n")
            print("             SCORE BOARD")
            print("---------------------------------")
            print(f"You:                           {user}")
            print(f"CPU:                           {compu}")
            print("\n")
        elif userChoice == "X":
            if choice == "S":
                print("You could not win this one.\nBetter luck next time!")
                compu += 1
            elif choice == "X":
                print("Tie!")
            else:
                print("You won!")
                user += 1
            print("\n")
            print("            SCORE BOARD")
            print("---------------------------------")
            print(f"You:                           {user}")
            print(f"CPU:                           {compu}")
            print("\n")
        else:
            print("Please enter valid letter and try again!")
        attempts += 1

    if attempts >= 10:
        if user > compu:
            print("Congratulations!! \nYou WON!!!!!!")
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
