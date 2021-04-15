import os
import time
import playsound
import speech_recognition as sr
from gtts import gTTS
import pyjokes
import webbrowser



def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        said = ""
        try:
            said = r.recognize_google(audio)
            print(said)
        except Exception as e:
            print("Exception" + str(e))
    return said


def main():
    text = get_audio()

    if "hello" in text:
        def speak(text):
            tts = gTTS(text=text, lang="en")
            filename = "hello.mp4"
            tts.save(filename)
            playsound.playsound(filename)
        speak("Hi how are you")
    elif "can you do" in text.lower():
        def speak(text):
            tts = gTTS(text=text, lang="en")
            filename = "work.mp4"
            tts.save(filename)
            playsound.playsound(filename)
        speak("Alot of things.bitch")
    elif "your name" in text:
        def speak(text):
            tts = gTTS(text=text, lang="en")
            filename = "name.mp4"
            tts.save(filename)
            playsound.playsound(filename)
        speak("my name is Trend")
    elif "master" in text:
        def speak(text):
            tts = gTTS(text=text, lang="en")
            filename = "master.mp4"
            tts.save(filename)
            playsound.playsound(filename)
        speak("my master is michael")
    elif "joke" in text:
        def speak(text):
            tts = gTTS(text=text, lang="en")
            filename = "joke.mp4"
            tts.save(filename)
            playsound.playsound(filename)
        m = str(f"{pyjokes.get_joke(language='en')}")
        speak(m)
    elif "chrome" in text.lower():
        try:
            k = "chrome.exe"
            os.startfile(k)
        except:
            def speak(text):
                tts = gTTS(text=text, lang="en")
                filename = "chrome.mp4"
                tts.save(filename)
                playsound.playsound(filename)
            speak("Error occured")
    elif "youtube" in text.lower():
        webbrowser.open("https://youtube.com")
    elif "cmd" in text.lower():
        try:
            k = "cmd.exe"
            os.startfile(k)
        except:
            def speak(text):
                tts = gTTS(text=text, lang="en")
                filename = "cmd.mp4"
                tts.save(filename)
                playsound.playsound(filename)
            speak("Error occured")
    elif "notepad" in text.lower():
        try:
            k = "notepad.exe"
            os.startfile(k)
        except:
            def speak(text):
                tts = gTTS(text=text, lang="en")
                filename = "notepad.mp4"
                tts.save(filename)
                playsound.playsound(filename)
            speak("Error occured")
    elif "logoff" in text.lower():
        os.system("shutdown /l")
    elif "restart" in text.lower():
        os.system("shutdown /o")
    elif "close apps" in text.lower():
        os.system("shutdown /f")
    elif "time" in text.lower():
        def speak(text):
            tts = gTTS(text=text, lang="en")
            filename = "speak.mp4"
            tts.save(filename)
            playsound.playsound(filename)
        speak(time.asctime())
    elif "shutdown" in text.lower():
        os.system("shutdown /p")
    elif "restart" in text.lower():
        os.system("res")
    elif "explorer" in text.lower():
        try:
            os.system("explorer")
        except:
            def speak(text):
                tts = gTTS(text=text, lang="en")
                filename = "explorer.mp4"
                tts.save(filename)
                playsound.playsound(filename)
            speak("Error occured")

    else:
        import random
        import string
        result_str = []

        def get_random_string(length):
            letters = string.ascii_lowercase
            result_str = ''.join(random.choice(letters) for i in range(length))

        get_random_string(4)
        def speak(text):
            tts = gTTS(text=text, lang="en")
            filename = f"{result_str}.mp4"
            tts.save(filename)
            playsound.playsound(filename)
        m = str(f"{pyjokes.get_joke(language='en')}.#error occured")
        speak(m)
while True:
    main()


