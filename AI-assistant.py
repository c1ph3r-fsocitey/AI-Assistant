from email.mime import audio
from lib2to3.refactor import MultiprocessRefactoringTool
from logging import exception
from logging.handlers import QueueListener
import mailbox
from pkgutil import ImpImporter
from re import S
from sqlite3 import DateFromTicks
from tkinter import N
import turtle
from unittest import result
from winreg import QueryInfoKey
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[1].id)
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    
    if hour>=0 and hour <=12:
        speak("Good Morning!")
        
    elif hour>=12 and hour<18:
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
        #print(e)
        
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
            webbrowser.open('youtube.com')
            
        elif 'open google' in query:
            webbrowser.open('google.com')
            
        elif 'open 7 cups' in query:
            webbrowser.open('7cups.com')
            
        elif 'open stack overflow' in query:
            webbrowser.open('stackoverflow.com')
            
        elif 'open gmail' in query:
            webbrowser.open('gmail.com')
            
        elif 'play  music' in query:
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
        
        elif 'stop' in query:
            break
        
        elif 'break' in query:
            break
        
        elif 'shut the f*** up' in query:
            break
