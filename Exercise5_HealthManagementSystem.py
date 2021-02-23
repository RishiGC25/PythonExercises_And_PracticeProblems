"""

Exercise 5: Health Management System
Exercise#5
The task is to create a "Health Management System." Suppose you are a fitness trainer and nutritionist. You have to deal
 with three clients, i.e., (Harry, Rohan, Hammad). For each client, you have to design their exercise and diet plan.

Instructions:
Create a food log file for each client
Create an exercise log file for each client.
Ask the user whether they want to log or retrieve client data.
Write a function that takes the user input of the client's name. After the client's name is entered, it will display a
message as "What you want to log- Diet or Exercise".

Use function
def getdate():
           import datetime
           return datetime.datetime.now()
The purpose of this function is to give time with every record of food or exercise added in the file.
Write a function to retrieve exercise or food file records for any client.


"""

import sys

def getdate():
    import datetime
    return datetime.datetime.now()


print("Do you want to log client data or retrieve client data?")

print("For logging press 1 and retrieving press 2")

try:
    LogOrRetrieve = int(input())
except Exception as e:
    print("A non-integer was entered. ERROR!!")
    sys.exit(0)

if LogOrRetrieve == 1:

    print("You have chosen to LOG CLIENT DATA.")
    print("For Client name: \nHarry: Press 1 \nRohan: Press 2 \nHammad: Press 3 \nPress enter!")
    ClientName = int(input())

    print("What do want to log - Diet or Exercise?")
    print("\nEnter 1 for diet.\nEnter 2 for exercise.")
    DietOrExercise = int(input())

    if DietOrExercise == 1:
        if ClientName == 1:
            print("Harry")
            f = open("Exercise5_Harry1.txt", "a")
            date = "[" + str(getdate()) + "]"
            f.write(date)
            print("Enter what food has been consumed.")
            food = input()
            f.write(food+"\n")
            f.close()
        elif ClientName == 2:
            print("Rohan")
            f = open("Exercise5_Rohan1.txt", "a")
            date = "[" + str(getdate()) + "]"
            f.write(date)
            print("Enter what food has been consumed.")
            food = input()
            f.write(food + "\n")
            f.close()
        elif ClientName == 3:
            print("Hammad")
            f = open("Exercise5_Hammad1.txt", "a")
            date = "[" + str(getdate()) + "]"
            f.write(date)
            print("Enter what food has been consumed.")
            food = input()
            f.write(food + "\n")
            f.close()
    if DietOrExercise == 2:
        if ClientName == 1:
            print("Harry")
            f = open("Exercise5_Harry2.txt", "a")
            date = "[" + str(getdate()) + "]"
            f.write(date)
            print("Enter the name of the workout done.")
            workout = input()
            f.write(workout + "\n")
            f.close()
        elif ClientName == 2:
            print("Rohan")
            f = open("Exercise5_Rohan2.txt", "a")
            date = "[" + str(getdate()) + "]"
            f.write(date)
            print("Enter the name of the workout done.")
            workout = input()
            f.write(workout + "\n")
            f.close()
        elif ClientName == 3:
            print("Hammad")
            f = open("Exercise5_Hammad2.txt", "a")
            date = "[" + str(getdate()) + "]"
            f.write(date)
            print("Enter the name of the workout done.")
            workout = input()
            f.write(workout + "\n")
            f.close()

elif LogOrRetrieve == 2:

    print("You have chosen to RETRIEVE CLIENT DATA.")
    print("For Client name: \nHarry: Press 1 \nRohan: Press 2 \nHammad: Press 3 \nPress enter!")
    ClientName = int(input())

    print("What do want to retrieve - Diet or Exercise?")
    print("\nEnter 1 for diet.\nEnter 2 for exercise.")
    DietOrExercise = int(input())

    if DietOrExercise == 1:
        if ClientName == 1:
            print("Harry")
            with open("Exercise5_Harry1.txt") as f:
                a = f.read()
                print(a)
        elif ClientName == 2:
            print("Rohan")
            with open("Exercise5_Rohan1.txt") as f:
                a = f.read()
                print(a)
        elif ClientName == 3:
            print("Hammad")
            with open("Exercise5_Hammad1.txt") as f:
                a = f.read()
                print(a)

    if DietOrExercise == 2:
        if ClientName == 1:
            print("Harry")
            with open("Exercise5_Harry2.txt") as f:
                a = f.read()
                print(a)
        elif ClientName == 2:
            print("Rohan")
            with open("Exercise5_Rohan2.txt") as f:
                a = f.read()
                print(a)
        elif ClientName == 3:
            print("Hammad")
            with open("Exercise5_Hammad2.txt") as f:
                a = f.read()
                print(a)

else:
    print("Oops!!\n"
          "Something went wrong\n"
          "Please recheck the value you have input!\n"
          "Thank you!\n")

