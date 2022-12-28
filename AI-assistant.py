import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random

jokes = ['what comes after 69? mouthwash', 'what do you call an terrorist who likes to swim? A bath bomb', 'how do stars die? mostly Overdose', 'what is the differnece between usain bolt and adolf hitler? usain bolt can actually finish a race! ' ] 

joke = random.choice(jokes)

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[1].id)
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishme():
    hour = int(datetime.datetime.now().hour)

    if hour >= 0 and hour <= 12:
        speak("Good Morning!")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("welcome CIPHER!")
    speak("I am your artificial assistant! How can i help you?")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}\n")

    except Exception as e:
        # print(e)

        print("could you please say that again?")
        return "none"
    return query


if __name__ == "__main__":
    wishme()
    while True:

        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak('searching wikipedia...')
            query = query.replace("wikipedia", "")
            result = wikipedia.summary(query, sentences=2)
            speak("according to wikipedia")
            print(result)
            speak(result)

        elif 'open youtube' in query:
            speak ("opening youtube")
            webbrowser.open('youtube.com')

        elif 'open google' in query:
            speak ("opening Google")
            webbrowser.open('google.com')

        elif 'open 7 cups' in query:
            speak("opening 7 Cups")
            webbrowser.open('7cups.com')

        elif 'open stack overflow' in query:
            spead("opening stack overflow")
            webbrowser.open('stackoverflow.com')

        elif 'open gmail' in query:
            speak("opening Gmail")
            webbrowser.open('gmail.com')

        elif 'play  music' in query:
            speak ("playing music")
            music_dir = 'C:\\music'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[1]))

        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak('the time is')
            print(strTime)
            speak(strTime)

        elif 'open visual studio' in query:
            codePath = "(put .exe path here)"
            os.startfile(codePath)

        elif 'joke' in query:
            speak(joke)
        
        elif 'stop' in query:
            break

        elif 'break' in query:
            break
        
        elif 'shut up' in query:
            speak("I am really sorry master")
            break

        elif 'fuck' in query:
            speak("i am really sorry master!")
            break
