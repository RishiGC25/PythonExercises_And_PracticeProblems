"""

Python Exercise 3 - Guess The Number
You have to build a "Number Guessing Game," in which a winning number is
set to some integer value. The Program should take input from the user,
and if the entered number is less than the winning number, a message
should display that the number is smaller and the appropriate message if it is larger.


Instructions:
The number of guesses should be limited, i.e (5 or 9).
Print the number of guesses left.
Print the number of guesses he took to win the game.
“Game Over” message should display if the number of guesses becomes
equal to 0.
"""

n = 18
g = 0
f = 0
while g < 5:
    print("Enter number")
    x = int(input())
    g = g + 1
    if x == n:
        print("You won!!!")
        print("You took", g, "guesses!")
        f = 1
        break
    elif x > n:
        print("Your attempt is greater than the number")
        print((5-g), "guesses left.")
    else:
        print("Your attempt is lesser than the number")
        print((5-g), "guesses left.")


if f == 0:
    print("Game Over!")

