from __future__ import print_function
import datetime
import pickle
import os.path
import os
import time
import pyttsx3
import speech_recognition as sr
import subprocess
import pyjokes
import webbrowser
from googlesearch import search

def speak(text):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.say(text)
    engine.runAndWait()


def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        said = ""

        try:
            said = r.recognize_google(audio)
            print(said)
        except Exception as e:
            print("Exception: " + str(e))

        if "hi" in said.lower():
            speak("Hello how are you")
        elif "hello"  in said.lower():
            speak("Hello how are you")
        elif "princess" in said.lower():
            speak("Ooh princess is my best friend")
        elif "best friend" in said.lower():
            speak("My best friend is you are my best friend")
        elif "trend" in said.lower():
            speak("Yes master, how can i help you.")
        elif "close" in said.lower():
            m = said.replace("close", "")
            print(m)
            os.system(f" TASKKILL /IM {m}.exe")
        elif "can you do" in  said.lower():
            speak("Alot of things.bitch")
        elif "google" in said.lower():
            webbrowser.open("https://google.com")
        elif "mega" in said.lower():
            webbrowser.open("https://mega.nz/fm/cfYkUJBR")
        elif "mail" in said.lower():
            webbrowser.open("https://mail.google.com/mail/u/0/#inbox")
        elif "your name" in  said.lower():
            speak("my name is Trend")
        elif "master" in  said.lower():
            speak("my master is michael")
        elif "joke" in  said.lower():
            m = str(f"{pyjokes.get_joke(language='en')}")
            speak(m)
        elif "search for" in said.lower():
            query = said.replace("search for", "")
            for i in search(query, tld="co.in", num=10, stop=10, pause=2):
                print(i)
        elif "exit" in said.lower():
            exit()
        elif "create" in said.lower():
            me = said.replace("create", "")
            os.system(f"echo #BEST PROGRAMMER > {me}.py")
            print("DONE")
        elif "chrome" in  said.lower():
            try:
                k = "chrome.exe"
                os.startfile(k)
            except:
                speak("Error occured")
        elif "youtube" in  said.lower():
            webbrowser.open("https://youtube.com")
        elif "cmd" in  said.lower():
            try:
                k = "cmd.exe"
                os.startfile(k)
            except:
                speak("Error occured")
        elif "notepad" in said.lower():
            try:
                k = "notepad.exe"
                os.startfile(k)
            except:
                speak("Error occured")
        elif "logoff" in  said.lower():
            os.system("shutdown /l")
        elif "restart" in  said.lower():
            os.system("shutdown /o")
        elif "close apps" in said.lower():
            os.system("shutdown /f")
        elif "time" in said.lower():
            speak(time.asctime())
        elif "shutdown" in  said.lower():
            os.system("shutdown /p")
        elif "restart" in  said.lower():
            os.system("res")
        elif "explorer" in  said.lower():
            try:
                os.system("explorer")
            except:
                speak("Error occured")
        else:
            m = str(f"{pyjokes.get_joke(language='en')}.LOL")
            speak(m)


    return said


while True:
    get_audio()



