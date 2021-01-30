"""
Exercise7 The Healthy Coder

Assume that a coder works at the office from 9am-5pm. We have to remind him about three things,

To drink a total of 4 liters of water between 9am-5pm.
To do an eye exercise after every 30 minutes.
To perform physical activity after every 45 minutes.

For Water, the user should enter “Drank”
For Eye Exercise, the user should enter “EyDone”
For Physical Exercise, the user should enter “ExDone”
After the user enters the input, a file should be created for every task separately, which contains the details about
the time when the user performed a certain task.

"""



from pygame import mixer

import datetime


now = datetime.datetime.now()
TimeNow = now.strftime("%H:%M:%S")

TimeElapsedSince9AM = ( (int(TimeNow[0:2]) - 9)*3600 + (60*(int(TimeNow[3:5]))) + (int(TimeNow[6:8])) )

TimesMissedWaterEye = TimeElapsedSince9AM//1800
TimesMissedWorkout = TimeElapsedSince9AM//2700

if (TimeElapsedSince9AM>1800):

    print("\nREMINDERS HAVE BEEN MISSED!!\n\n")

    print(f"You are supposed to drink {TimesMissedWaterEye} dose(s)(1 dose=250 ml) of water\n") 
    print(f"You are supposed to do {TimesMissedWaterEye} round(s) of your eye exercise\n")

    if (TimeElapsedSince9AM>2700):
        print(f"You are supposed to do {TimesMissedWorkout} round(s) of your workout\n")

WaterDose, EyDose, ExDose = 0,0,0


while True:

    now = datetime.datetime.now()
    TimeNow = now.strftime("%H:%M:%S")

    TimeElapsedSince9AM = ( (int(TimeNow[0:2]) - 9)*3600 + (60*(int(TimeNow[3:5]))) + (int(TimeNow[6:8])) )
    
    if TimeElapsedSince9AM%1800 == 0: # Since 9am, every thirty minutes:
        
        mixer.init()
        mixer.music.load("Exercise7_Song_DrinkMoreWater.mp3")
        mixer.music.set_volume(0.7)
        mixer.music.play()

        print("\nKindly drink 250 ML of water.")

        while True:
            Water = input('Say "Drank" to end the embarrassing music :)')
            WaterQuery = Water.upper()

            now = datetime.datetime.now()
            TimeNow = now.strftime("%H:%M:%S")

            if WaterQuery == 'DRANK':
                mixer.music.stop()
                WaterDose += 1
                f = open("Exercise7_WaterDose.txt","a")
                appendIt = "Time"+str(WaterDose) + ":" + "[" + TimeNow + "]"
                f.write(appendIt)     
                break
            else:
                continue

        print("You have drunk water. Great!")


        now = datetime.datetime.now()
        TimeNow = now.strftime("%H:%M:%S")

        mixer.init()
        mixer.music.load("Exercise7_Song_TheEyeSong.mp3")
        mixer.music.set_volume(0.7)
        mixer.music.play()

        print("\nKindly do your eye exercise.")


        while True:
            Eye = input('Say "EyDone" to end the embarrassing music :)')
            EyeQuery = Eye.upper()

            now = datetime.datetime.now()
            TimeNow = now.strftime("%H:%M:%S")

            if EyeQuery == 'EYDONE':
                mixer.music.stop() 
                EyDose += 1
                f = open("Exercise7_EyeDose.txt","a")
                appendIt = "Time"+str(EyDose) + ":" + "[" + TimeNow + "]"
                f.write(appendIt)
                break
            else:
                continue
        

    now = datetime.datetime.now()
    TimeNow = now.strftime("%H:%M:%S")


    TimeElapsedSince9AM = ( (int(TimeNow[0:2]) - 9)*3600 + (60*(int(TimeNow[3:5]))) + (int(TimeNow[6:8])) )
    print(TimeElapsedSince9AM)

    if TimeElapsedSince9AM % 2700 == 0: # Since 9am, every 45 minutes


        mixer.init()
        mixer.music.load("Exercise7_Song_TheExerciseSong.mp3")
        mixer.music.set_volume(0.7)
        mixer.music.play()

        print("\nKindly do your exercise.")

        while True:
                
            Exercise = input('Say "ExDone" to end the embarrassing music :)')
            ExerciseQuery = Exercise.upper()
            now = datetime.datetime.now()
            TimeNow = now.strftime("%H:%M:%S")

            if ExerciseQuery == 'EXDONE':
                mixer.music.stop()
                ExDose += 1 
                f = open("Exercise7_ExerciseDose.txt","a")
                appendIt = "Time"+str(ExDose) + ":"+ "[" + TimeNow + "]"
                f.write(appendIt) 
                break
            else:
                continue
    
    now = datetime.datetime.now()
    TimeNow = now.strftime("%H:%M:%S")