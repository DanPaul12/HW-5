import random

moods = ["groovy", "sporty", "lowkey", "doofy", "chunky", "aloof", "spent"]
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]


for i in range(len(days)):
        day = days[i]
        mood = random.choice(moods)
        print("On " + day + " you were feeling " + mood)
