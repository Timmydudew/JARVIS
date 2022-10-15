import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser as wb
import os
import smtplib
import requests
from pprint import pprint
from selenium import webdriver

 engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice',voices[0].id)
 def speak(audio): 
     engine.say(audio) 
     engine.runAndWait() 

def wishMe(): 
    speak("Welcome back sir") 
    hour = int(datetime.datetime.now().hour) 
    print(hour)
    year = int(datetime.datetime.now().year) 
    month = int(datetime.datetime.now().month) 
    date = int(datetime.datetime.now().day) 
    Time = datetime.datetime.now().strftime("%I:%M:%S") 
    print(Time)
    print(date) 
    print(month) 
    print(year) 
    speak("the current Time is") 
    speak(Time) 
    speak("the current Date is") 
    speak(date) 
    speak(month)
    speak(year) 
    if hour>=6 and hour<12: 
      speak("Good Morning Sir!") 

    elif hour>=12 and hour<18: 
      speak("Good Afternoon Sir!")

    elif hour>=18 and hour<24: 
      speak("Good Evening Sir") 

    else: speak("Good Night Sir!") 

    speak("Jarvis at your Service. Please tell me how can I help You ")
   #wishMe()

def takeCommand():
    r = sr.Recognizer() 
    with sr.Microphone() as source: 
    print("i am Listening...") 
    r.pause_threshold = 1 
    audio = r.listen(source) 
    try: print("Recognizing...") 
    query = r.recognize_google(audio, language='en-in') 
    print(f"Sir you Said:{query}\n") 
    except Exception as e: 
    print(e) 
    print("Say that again Please...") 
    speak("Say that again Please...") 
    return "None" 
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587) 
    server.ehlo() 
    server.starttls() 
    server.login('Senderemail@gmail.com', 'Password') 
    server.sendmail('Senderemail@gmail.com', to, content) 
    server.close() 

def lighton(): 
    driver = webdriver.Chrome('C:/Users/Username/Downloads/chromedriver.exe') 
    add the location of the chrome Drivers driver.get("https://Add here.000webhostapp.com/main.html")
    Add the webhost name elem1 = driver.find_element_by_id("S1off") 
    elem1.click()
 
def lightoff(): 
    driver = webdriver.Chrome('C:/Users/timifresh101/Downloads/chromedriver.exe') 
    driver.get("https://Add here.000webhostapp.com/main.html")
    Add the webhost name elem1 = driver.find_element_by_id("S1on") 
    elem1.click() 
    if __name__ == "__main__": 
    wishMe() 
    while True:
   query = takeCommand().lower() if 'wikipedia' in query:
