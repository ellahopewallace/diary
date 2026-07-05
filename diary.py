import matplotlib.pyplot as plt
import dayplot as dp
import datetime
import random
from statistics import multimode

def saveDiaryEntry():
    with open("diary.txt", "a") as f:
        date = datetime.datetime.now().strftime("%d/%m/%y")
        entry = input("Write your diary entry: ")
        if date in diary:
            diary[date] = diary[date] + "\n" + entry
        else:
            diary[date] = entry
        f.write(date + "\n")
        f.write(entry + "\n")

def loadDiaryEntries():
    diary = {}
    try:
        with open("diary.txt", "r") as f:
            lines = f.readlines()
            for i in range (0, len(lines)-1, 2):
                date = lines[i].strip()
                entry = lines[i+1].strip()
                if date in diary:
                    diary[date] = diary[date] + "\n" + entry
                else:
                    diary[date] = entry

    except FileNotFoundError:
        pass
    return diary

def loadMotivationalMessages():
    messages = {"1":["happy"], "2":["sad"], "3":["frustrated"], "4":["fine"], "5":["stressed"]}
    try:
        with open("quotes.txt", "r") as f:
            lines = f.readlines()
            for i in range (0, len(lines)-1, 2):
                mood = lines[i].strip()
                message = lines[i+1].strip()
                if mood in messages:
                    messages[mood].append(message)
    except FileNotFoundError:
        pass
    return messages

def moodDependingMessage(mood):
    randomNumber = random.randint(1,len(motivationalMessages[mood])-1)
    randomMessage = motivationalMessages[mood][randomNumber]
    return randomMessage

moodConverter = {"1": "Happy", "2": "Sad", "3": "Angry", "4": "Fine", "5": "Stressed"}

def logMood():
    print ("\nKEY:")
    print ("1 -> Happy/good.")
    print ("2 -> Sad/down/disappointed.")
    print ("3 -> Frustrated/angry/annoyed.")
    print ("4 -> Okay/fine/neutral.")
    print ("5 -> Anxious/worried/stressed.")
    mood = input("How are you feeling today?\nType a number from 1 - 5 according to the key: ")
    if mood not in motivationalMessages:
        print("\nPlease only input a number 1-5")
        return logMood()
    else:
        print("\nYou logged a " + motivationalMessages[mood][0] + " mood.\n" + moodDependingMessage(mood)+"\n")
        saveMoodEntry(moodConverter[mood])

def loadMoods():
    moodLogs = {}
    try:
        with open("moodLogs.txt", "r") as f:
            lines = f.readlines()
            for i in range (0, len(lines)-1, 2):
                date = lines[i].strip()
                mood = lines[i+1].strip()
                if date in moodLogs:
                    moodLogs[date].append(mood)
                else:
                    moodLogs[date] = [mood]

    except FileNotFoundError:
        pass
    return moodLogs

def saveMoodEntry(mood):
    with open("moodLogs.txt", "a") as f:
        date = datetime.datetime.now().strftime("%Y-%m-%d")
        if date in moodLogs:
            moodLogs[date].append(mood)
        else:
            moodLogs[date] = [mood]
        f.write(date + "\n")
        f.write(mood + "\n")

def displayCalender():
    fig, ax = plt.subplots(figsize=(16,4))
    dp.calendar(
        dates = list(moodLogs.keys()),
        values = overallMoods(),
        start_date = f"{datetime.datetime.now().year}-01-01",
        end_date = f"{datetime.datetime.now().year}-12-31",
        colors = {
            "Happy": "#FFE66C",
            "Sad": "#4C8CE4",
            "Angry": "#B84747",
            "Fine": "#73B050",
            "Stressed": "#FF97D0",
        },
        month_grid=True,
        legend = True,
        ax = ax,
    )
    ax.set_title("Mood calendar")
    plt.show()

def overallMoods():
    biggestMoods = []
    for day in moodLogs.values():
        biggestMoods.append(multimode(day)[-1]) # most common mood that day, tie breaker falls to most recent
    return biggestMoods


diary = loadDiaryEntries()
motivationalMessages = loadMotivationalMessages()
moodLogs = loadMoods()


print("\nWelcome to your diary! You can...")
print("log your moods, view your mood calender, write a diary entry and read past diary entries by date\n")
nextInput = input("What would you like to do?\nm -> mood log\nc -> view mood calendar\nd -> diary entry\nr -> read diary\nq -> quit\n ")

while nextInput != "q":

    # mood entry
    if nextInput == "m":
        logMood()

    # mood calendar
    elif nextInput == "c":
        displayCalender()

    # diary entry
    elif nextInput == "d":
        saveDiaryEntry()

    # read past diary entry by date
    elif nextInput == "r":
        dayToRead = input("Which day from your diary do you want to read? Please enter a date in the form DD/MM/YY: ")
        if dayToRead in diary:
            print(dayToRead + ":\n" + diary[dayToRead] +"\n")
        else:
            print("No diary entry for this day")

    else:
        print("Please only input m, c, d, r, or q")
        
    nextInput = input("What would you like to do?\nm -> mood log\nc -> view mood calendar\nd -> diary entry\nr -> read diary\nq -> quit\n ")

print("Hope you had a reflective session! Your diary entries and moods are saved for you when you come back.")   