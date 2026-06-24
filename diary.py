import datetime
import random

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


diary = loadDiaryEntries()
motivationalMessages = loadMotivationalMessages()

print("\nWelcome to your diary! You can...")
print("write a diary entry and read past diary entries by date\n")
nextInput = input("What would you like to do?\nm -> log mood\nd -> diary entry\nr -> read diary\nq -> quit\n ")

while nextInput != "q":

    # mood entry
    if nextInput == "m":
        logMood()

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
        print("Please only input d, r, or q")
        
    nextInput = input("What would you like to do?\nm -> log mood\nd -> diary entry\nr -> read diary\nq -> quit\n ")

print("Hope you had a reflective session! Your diary entries are saved for you when you come back.")





    

