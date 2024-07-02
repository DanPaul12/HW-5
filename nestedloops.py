import random

moods = ["groovy", "sporty", "lowkey", "doofy", "chunky", "aloof"]
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
timeofday = ["morning", "afternoon", "night"]

for i in range(len(days)):
    for time in timeofday:
        day = days[i]
        mood = random.choice(moods)
        print("On " + day + " " + time + " you were feeling " + mood)