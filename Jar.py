import pyttsx3
import speech_recognition as sr
import webbrowser 
import datetime
import wikipedia

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source: 
       print('Listening')
    r.pause_threshold = 0.7 
    audio = r.listen(source)
    try: 
       print("Recognizing")
       Query = r.recognize_google(audio, language='en-in')
       print("You=", Query)
   except Exception as e: 
         print(e) 
         print("Say that again sir") 
         return "None"
   
       return Query

def speak(audio):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    #1 for female voice
    engine.setProperty('voice', voices[0].id)
    engine.say(audio)

def Take_query():
    while(True):
        query = takeCommand().lower()
    if "hello" in query:
       speak("hello sir I am JARVIS an Ai programmed by Timmy")
    elif "who are you" in query:
         speak("I am an Jarvis sir")
