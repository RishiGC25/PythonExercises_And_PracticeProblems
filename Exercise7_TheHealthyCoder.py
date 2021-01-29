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
TimeNow = now.strftime("%H:%M")
TimeElapsedSince9AM = ( (int(TimeNow[0:2]) - 9)*60 + int(TimeNow[3:5]) )
TimesMissed = TimeElapsedSince9AM//30
if (TimeElapsedSince9AM>30):
    print(f"You are supposed to drink {TimesMissed} dose(s)(1 dose = 250 ml) of water and {TimesMissed} round(s) of your workout")

WaterDose, EyDose, ExDose = 0,0,0

while True:

    now = datetime.datetime.now()
    TimeNow = now.strftime("%H:%M")
    TimeElapsedSince9AM = ( (int(TimeNow[0:2]) - 9)*60 + int(TimeNow[3:5]) )  # Gives time elapsed in minutes since 9 AM

    if TimeElapsedSince9AM%30 == 0: # Since 9am, every thirty minutes:
        
        mixer.init()
        mixer.music.load("Exercise7_Song_DrinkMoreWater.mp3")
        mixer.music.set_volume(0.7)
        mixer.music.play()
        print("Kindly drink 250 ML of water.")

        while True:
            Water = input('Say "Drank" to end the embarrassing music :)')
            WaterQuery = Water.upper()

            if WaterQuery == 'DRANK':
                mixer.music.stop()
                WaterDose += 1 
                break
            else:
                continue

        print("You have drunk water. Great!")

        now = datetime.datetime.now()
        TimeNow = now.strftime("%H:%M")

        mixer.init()
        mixer.music.load("Exercise7_Song_TheEyeSong.mp3")
        mixer.music.set_volume(0.7)
        mixer.music.play()
        print("Kindly do your eye exercise.")

        while True:
            Eye = input('Say "EyDone" to end the embarrassing music :)')
            EyeQuery = Eye.upper()

            if EyeQuery == 'EYDONE':
                mixer.music.stop() 
                EyDose += 1
                break
            else:
                continue
        
        now = datetime.datetime.now()
        TimeNow = now.strftime("%H:%M")

    TimeElapsedSince9AM = ( (int(TimeNow[0:2]) - 9)*60 + int(TimeNow[3:5]) )

    if TimeElapsedSince9AM % 45 == 0: # Since 9am, every 45 minutes
        mixer.init()
        mixer.music.load("Exercise7_Song_TheExerciseSong.mp3")
        mixer.music.set_volume(0.7)
        mixer.music.play()
        while True:
            print("Kindly do your exercise.")
            Exercise = input('Say "ExDone" to end the embarrassing music :)')
            ExerciseQuery = Exercise.upper()
            if ExerciseQuery == 'EXDONE':
                mixer.music.stop()
                ExDose += 1 
                break
            else:
                continue
        
        now = datetime.datetime.now()
        TimeNow = now.strftime("%H:%M")