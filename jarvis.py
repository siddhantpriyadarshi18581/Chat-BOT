import pyttsx3
import datetime as dt
import speech_recognition as sr
import wikipedia
# import wikipedia as wiki
# import gtts as tts
import requests

# data = input("enter text which you want ot convert to speech:\n")

engine = pyttsx3.init()


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# speak("This is jarvis AI assisstant")

def weather():
    print("Enter for which city you want to know the weather forcast:")
    speak("Enter for which city you want to know the weather forcast:")
    city = take_command()
    speak('Displaying Weather report for: ')
    speak(city)
    url = 'https://wttr.in/{}'.format(city)
    res = requests.get(url)
    print(res.text)

def aboutyou():
    print("""I am an AI Bot named Anonymous designed by Siddhant Priyadarshi on 22nd December 2022. 
    My major constituting programming language is Python 3.11.1. 
    I can answer your all possible questions. 
    Don't worry I am not as my Siblings Bob and Alice and I am the lover of humanity""")
    speak("""I am an AI Bot named Anonymous designed by Siddhant Priyadarshi on 22nd December 2022. 
    My major constituting programming language is Python 3.11.1. 
    I can answer your all possible questions. 
    Don't worry I am not as my Siblings Bob and Alice and I am the lover of humanity""")

def time():
    Time = dt.datetime.now().strftime("%I:%M:%S")
    speak("The current time is")
    speak(Time)

# time()

def date():
    date = dt.datetime.now().date()
    speak("the current date is")
    speak(date)

# date()
def wishme():
    speak("Welcome back master")
    time()
    speak("and")
    date()
    hour = dt.datetime.now().hour
    if hour>=6 and hour<12:
        speak("Good Morning Sir!")
    elif hour>=12 and hour<=16:
        speak("Good Afternoon Sir!")
    elif hour>16 and hour<21:
        speak("Good Evening Sir!")
    else:
        speak("Good Night Sir!")

    speak("Jarvis at your service. How may I assisst you sir!")

# wishme()
def wikisearch():
    speak("What do you want to be searched?")
    cmd = take_command()
    cmd = cmd.replace("wikipedia", "")
    result = wikipedia.summary(cmd, sentences=2)
    print(result)
    speak("According to wikipedia")
    speak(result)

def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        aud = r.listen(source)

    try:
        print("Recognizing..")
        query = r.recognize_google(aud, language='en-in')
        print(query)
    except Exception as e:
        print(e)
        speak("Please can you say that again. I am not able to recognize")
        take_command()
        return query
    return query

if __name__ == "__main__":
    wishme()
    while True:
        cmd = take_command().lower()

        if 'time' in cmd:
            time()
        elif 'about you' in cmd:
            aboutyou()
        elif 'date' in cmd:
            date()
        elif 'weather' in cmd:
            weather()
        elif 'offline' in cmd:
            speak("Adios")
            quit()
        elif 'search' in cmd:
            wikisearch()
        else:
            speak("I am to learning it sir")
    # speak("भाई")