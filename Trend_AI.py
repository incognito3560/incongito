from tkinter import *
from time import *
import datetime
import time
import os
import pyttsx3
import speech_recognition as sr
import pyjokes
import webbrowser
from googlesearch import search
import random
import string
from random import randint
import googlesearch
from PIL import ImageTk, Image
import speech_recognition as sr

splash_root = Tk()
splash_root.configure(background="black")
splash_root.title("SPLASH SCRENE")
splash_root.geometry("500x300")
splash_root.iconbitmap("incognito.ico")
splash_root.attributes("-alpha", 9.0)
splash_root.overrideredirect(True)

photo = ImageTk.PhotoImage(Image.open("Incognito1.png"))

splash_label = Label(splash_root, text="WELCOME",fg="cyan", bg="black",image=photo)
splash_label.place(x=0,y=0)

def func_main():
    splash_root.destroy()
    result_str = []

    def get_random_string(length):
        letters = string.ascii_lowercase
        result_str = ''.join(random.choice(letters) for i in range(length))

    get_random_string(4)


    root = Tk()
    root.title("INCOGNITO")
    root.configure(background="black")
    root.geometry("700x300")
    root.iconbitmap("incognito_2.ico")
    root.attributes("-alpha", 0.9)
    root.resizable(width="False", height="False")
    root.config(cursor="arrow")

    def rec(event):
        def speak(text):
            engine = pyttsx3.init('sapi5')
            voices = engine.getProperty('voices')
            engine.setProperty('voice', 'voices[0].id')
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
                    print("Exception" + str(e))

                if "hi" in said.lower():
                    speak("Hello how are you")

                elif "hello" in said.lower():
                    speak("Hello how are you")

                elif "wifi" in said.lower():
                    name_of_router = "OFFLINE"
                    os.system(f'''cmd /c "netsh wlan connect name={name_of_router}"''')

                elif "nickname" in said.lower():
                    list = [
                        "Ace",
                        "Camden",
                        "Colt",
                        "Bowie",
                        "Zane",
                        "Jace",
                        "Jayden",
                        "Rive",
                        "Nova",
                        "Rowan",
                        "Cora"
                    ]
                    n = list[randint(0, 10)]
                    speak(f"should i call you {list[randint(0, 10)]}")
                    if said.lower() == "no":
                        speak(f"Is  {list[randint(0, 10)]} ok with you.")
                    else:
                        speak("Wonder full. ")

                elif "princess" in said.lower():
                    speak("Ooh princess is my best friend")

                elif "best friend" in said.lower():
                    speak("My best friend is you.You are my best friend")

                elif "photo" in said.lower() or "picture" in said.lower():
                    from PIL import ImageGrab
                    img = ImageGrab.grab()
                    img.save(f'{result_str}.png')
                    speak("TAKEN")

                elif "website" in said.lower():
                    webbrowser.open("https://trend0.yolasite.com/")

                elif "beats" in said.lower():
                    webbrowser.open("https://www.youtube.com/results?search_query=beats")

                elif "trend" in said.lower():
                    speak("Yes master, how can i help you.")

                elif "close" in said.lower():
                    m = said.replace("close", "")
                    print(m)
                    os.system(f" TASKKILL /IM {m}.exe")

                elif "can you do" in said.lower():
                    speak("Alot of things.bitch")

                elif "google" in said.lower():
                    webbrowser.open("https://google.com")

                elif "mega" in said.lower():
                    webbrowser.open("https://mega.nz/fm/cfYkUJBR")

                elif "mail" in said.lower():
                    webbrowser.open("https://mail.google.com/mail/u/0/#inbox")

                elif "your name" in said.lower():
                    speak("my name is Trend")

                elif "master" in said.lower():
                    speak("my master is michael")

                elif "stop" in said.lower():
                    speak("OK")
                    text()

                elif "joke" in said.lower():
                    m = str(f"{pyjokes.get_joke(language='en')}")
                    speak(m)

                elif "search for" in said.lower():
                    query = said.replace("search for", "")
                    speak("I found these results.")
                    webbrowser.open(
                        f"https://www.google.com/search?q={query}&source=hp&ei=CI19YL-iG9Cca9L7j5gN&iflsig=AINFCbYAAAAAYH2bGN0Jc1UtQulEx8C49f4zt1msfh5N&oq=diy&gs_lcp=Cgdnd3Mtd2l6EAMyCAguELEDEJMCMggILhCxAxCDATIFCAAQsQMyCAgAELEDEIMBMgUIABCxAzIICC4QsQMQgwEyBQgAELEDMgUIABCxAzIFCAAQsQMyBQguELEDOgoIABDqAhC0AhBDOgoILhDqAhC0AhBDOgIIAFC7JVjNKmDfK2gBcAB4AIAByQKIAcMEkgEFMi0xLjGYAQCgAQGqAQdnd3Mtd2l6sAEK&sclient=gws-wiz&ved=0ahUKEwi_xviJvIrwAhVQzhoKHdL9A9MQ4dUDCAc&uact=5")


                elif "exit" in said.lower():
                    exit()

                elif "create" in said.lower():
                    me = said.replace("create", "")
                    os.system(f"echo #BEST PROGRAMMER > {me}.py")
                    print("DONE")

                elif "chrome" in said.lower():
                    try:
                        k = "chrome.exe"
                        os.startfile(k)
                    except:
                        speak("Error occured")

                elif "youtube" in said.lower():
                    webbrowser.open("https://youtube.com")

                elif "video call" in said.lower() or "duo" in said.lower():
                    webbrowser.open("https://duo.google.com/?web&utm_source=marketing_page_button_main")

                elif "cmd" in said.lower():
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

                elif "settings" in said.lower():
                    os.system("start ms-settings:")

                elif "logoff" in said.lower():
                    os.system("shutdown /l")

                elif "restart" in said.lower():
                    os.system("shutdown /o")

                elif "close apps" in said.lower():
                    os.system("shutdown /f")

                elif "new" in said.lower():
                    googlesearch.search("")

                elif "time" in said.lower():
                    speak(time.asctime())

                elif "shutdown" in said.lower():
                    os.system("shutdown /p")

                elif "restart" in said.lower():
                    os.system("res")

                elif "open" in said.lower():
                    try:
                        m = said.replace("open", "")
                        os.startfile(f"{m}.exe")
                    except:
                        speak("failed.nerrd")

                elif "say" in said.lower():
                    m = third.get().replace("say", "")
                    speak(m)

                elif "explorer" in said.lower():
                    try:
                        os.system("explorer")
                    except:
                        speak("Error occured")


                else:
                    try:
                        speak("I found these results.")
                        webbrowser.open(
                            f"https://www.google.com/search?q={said.lower()}&source=hp&ei=CI19YL-iG9Cca9L7j5gN&iflsig=AINFCbYAAAAAYH2bGN0Jc1UtQulEx8C49f4zt1msfh5N&oq=diy&gs_lcp=Cgdnd3Mtd2l6EAMyCAguELEDEJMCMggILhCxAxCDATIFCAAQsQMyCAgAELEDEIMBMgUIABCxAzIICC4QsQMQgwEyBQgAELEDMgUIABCxAzIFCAAQsQMyBQguELEDOgoIABDqAhC0AhBDOgoILhDqAhC0AhBDOgIIAFC7JVjNKmDfK2gBcAB4AIAByQKIAcMEkgEFMi0xLjGYAQCgAQGqAQdnd3Mtd2l6sAEK&sclient=gws-wiz&ved=0ahUKEwi_xviJvIrwAhVQzhoKHdL9A9MQ4dUDCAc&uact=5")
                    except:
                        speak("Error LOL")

            return said

        while True:
            get_audio()
    def text(event):
        try:
            def speak(text):
                engine = pyttsx3.init('sapi5')
                voices = engine.getProperty('voices')
                engine.setProperty('voice', 'voices[0].id')
                engine.say(text)
                engine.runAndWait()

            def get_audio():
                if "hi" in third.get():
                    speak("Hello how are you")

                elif "hello" in third.get():
                    speak("Hello how are you")

                elif "say" in third.get():
                    m = third.get().replace("say", "")
                    speak(m)

                elif "website" in third.get():
                    webbrowser.open("https://trend0.yolasite.com/")

                elif "nickname" in third.get():
                    list = [
                        "Ace",
                        "Camden",
                        "Colt",
                        "Bowie",
                        "Zane",
                        "Jace",
                        "Jayden",
                        "Rive",
                        "Nova",
                        "Rowan",
                        "Cora"
                    ]
                    n = list[randint(0, 10)]
                    speak(f"should i call you {list[randint(0, 10)]}")

                    if third.get() == "no":
                        speak(f"Is  {list[randint(0, 10)]} ok with you.")
                    else:
                        speak("Wonder full. ")

                elif "princess" in third.get():
                    speak("Ooh princess is my best friend")

                elif "best friend" in third.get():
                    speak("My best friend is you.You are my best friend")

                elif "photo" in third.get() or "picture" in third.get():
                    from PIL import ImageGrab
                    img = ImageGrab.grab()
                    img.save(f'{result_str}.png')
                    speak("TAKEN")

                elif "beats" in third.get():
                    webbrowser.open("https://www.youtube.com/results?search_query=beats")

                elif "trend" in third.get():
                    speak("Yes master, how can i help you.")

                elif "close" in third.get():
                    m = third.get().replace("close", "")
                    print(m)
                    os.system(f" TASKKILL /IM {m}.exe")

                elif "can you do" in third.get():
                    speak("Alot of things.bitch")

                elif "google" in third.get():
                    webbrowser.open("https://google.com")

                elif "mega" in third.get():
                    webbrowser.open("https://mega.nz/fm/cfYkUJBR")

                elif "mail" in third.get():
                    webbrowser.open("https://mail.google.com/mail/u/0/#inbox")

                elif "your name" in third.get():
                    speak("my name is Trend")

                elif "master" in third.get():
                    speak("my master is michael")

                elif "joke" in third.get():
                    m = str(f"{pyjokes.get_joke(language='en')}")
                    speak(m)

                elif "search for" in third.get():
                    query = third.get().replace("search for", "")
                    webbrowser.open(
                        f"https://www.google.com/search?q={query}&source=hp&ei=CI19YL-iG9Cca9L7j5gN&iflsig=AINFCbYAAAAAYH2bGN0Jc1UtQulEx8C49f4zt1msfh5N&oq=diy&gs_lcp=Cgdnd3Mtd2l6EAMyCAguELEDEJMCMggILhCxAxCDATIFCAAQsQMyCAgAELEDEIMBMgUIABCxAzIICC4QsQMQgwEyBQgAELEDMgUIABCxAzIFCAAQsQMyBQguELEDOgoIABDqAhC0AhBDOgoILhDqAhC0AhBDOgIIAFC7JVjNKmDfK2gBcAB4AIAByQKIAcMEkgEFMi0xLjGYAQCgAQGqAQdnd3Mtd2l6sAEK&sclient=gws-wiz&ved=0ahUKEwi_xviJvIrwAhVQzhoKHdL9A9MQ4dUDCAc&uact=5")

                elif "exit" in third.get():
                    root.destroy()

                elif "create" in third.get():
                    me = third.get().replace("create", "")
                    os.system(f"echo #BEST PROGRAMMER > {me}.py")
                    print("DONE")

                elif "chrome" in third.get():
                    try:
                        k = "chrome.exe"
                        os.startfile(k)
                    except:
                        speak("Error occured")

                elif "youtube" in third.get():
                    webbrowser.open("https://youtube.com")

                elif "cmd" in third.get():
                    try:
                        k = "cmd.exe"
                        os.startfile(k)
                    except:
                        speak("Error occured")

                elif "notepad" in third.get():
                    try:
                        k = "notepad.exe"
                        os.startfile(k)
                    except:
                        speak("Error occured")

                elif "settings" in third.get():
                    os.system("start ms-settings:")

                elif "logoff" in third.get():
                    os.system("shutdown /l")

                elif "calculator" in third.get() or "calc" in third.get():
                    cal = Tk()
                    cal.title("CALCULATOR")
                    cal.configure(background="black")
                    cal.geometry("500x300")
                    cal.iconbitmap("incognito_2.ico")
                    cal.attributes("-alpha", 0.9)
                    cal.resizable(width="False", height="False")
                    cal.config(cursor="arrow")

                    def call():
                        if ent2.get() == "+":
                            k = int(ent.get())
                            l = int(ent3.get())
                            m = k + l
                            speak(m)
                        elif ent2.get() == "-":
                            k = int(ent.get())
                            l = int(ent3.get())
                            m = k - l
                            speak(m)
                        elif ent2.get() == "*":
                            k = int(ent.get())
                            l = int(ent3.get())
                            m = k * l
                            speak(m)
                        elif ent2.get() == "/":
                            k = int(ent.get())
                            l = int(ent3.get())
                            m = k / l
                            speak(m)
                        else:
                            speak("Error")


                    first = Label(cal, text="TRENDs CALCILATOR.", fg="cyan", bg="black", font=("DriftType", 22), cursor="star")
                    first.pack()
                    ent = Entry(cal , width=20)
                    ent.place(x=40, y=100)
                    ent2 = Entry(cal, width=10)
                    ent2.place(x=170, y=100)
                    ent3 = Entry(cal, width=20)
                    ent3.place(x=240, y=100)
                    but = Button(cal, text="CALCULATE", command=call)
                    but.place(x=370, y=95)


                    cal.mainloop()

                elif "restart" in third.get():
                    os.system("shutdown /o")

                elif "close apps" in third.get():
                    os.system("shutdown /f")

                elif "new" in third.get():
                    googlesearch.search(third.get())

                elif "video call" in third.get() or "duo" in third.get():
                    webbrowser.open("https://duo.google.com/?web&utm_source=marketing_page_button_main")

                elif "time" in third.get():
                    speak(time.asctime())

                elif "shutdown" in third.get():
                    os.system("shutdown /p")

                elif "restart" in third.get():
                    os.system("res")

                elif "open" in third.get():
                    try:
                        m = third.get().replace("open", "")
                        os.startfile(f"{m}.exe")
                    except:
                        speak("failed.nerrd")

                elif "wifi" in third.get():
                    name_of_router = "OFFLINE"
                    os.system(f'''cmd /c "netsh wlan connect name={name_of_router}"''')

                elif "mike" in third.get():
                    speak("HI mike my name is trend.")

                elif "explorer" in third.get():
                    try:
                        os.system("explorer")
                    except:
                        speak("Error occured")

                else:
                    try:
                        speak("I found these results.")
                        webbrowser.open(
                            f"https://www.google.com/search?q={third.get()}&source=hp&ei=CI19YL-iG9Cca9L7j5gN&iflsig=AINFCbYAAAAAYH2bGN0Jc1UtQulEx8C49f4zt1msfh5N&oq=diy&gs_lcp=Cgdnd3Mtd2l6EAMyCAguELEDEJMCMggILhCxAxCDATIFCAAQsQMyCAgAELEDEIMBMgUIABCxAzIICC4QsQMQgwEyBQgAELEDMgUIABCxAzIFCAAQsQMyBQguELEDOgoIABDqAhC0AhBDOgoILhDqAhC0AhBDOgIIAFC7JVjNKmDfK2gBcAB4AIAByQKIAcMEkgEFMi0xLjGYAQCgAQGqAQdnd3Mtd2l6sAEK&sclient=gws-wiz&ved=0ahUKEwi_xviJvIrwAhVQzhoKHdL9A9MQ4dUDCAc&uact=5")
                    except:
                        speak("Error LOL")

            return get_audio()

            text()
        except:
            print("Invalid name")

    first = Label(root, text="TREND your virtual assiatant.", fg="cyan", bg="black", font=("DriftType", 22), cursor="star")
    second = Button(root, text="SEND", command=text, fg="cyan", bg="black", font="caveat", bd=0,cursor="plus")
    fourth = Button(root, command=rec, fg="cyan", bg="black", text="REC", font="caveat", bd=0,cursor="star")
    third = Entry(root, width=100)
    mic = Label(root, text="o.o", bg="black", fg="cyan", font=("DriftType", 20), cursor="man")
    first.pack()
    second.place(x=605, y=275)
    third.place(x=0, y=285)
    fourth.place(x=660, y=275)
    status = Label(root, text="", bg="black", fg="cyan")
    status.place(x=630, y=260)
    about = Label(root, text="", bg="black", fg="cyan", font=("caveat", 20))
    about.pack(pady=10)
    mic.pack(padx=20)

    def hover(event):
        fourth["fg"] = "white"
        status.config(text="Audio input")
    def left(event):
        fourth["fg"] = "cyan"
        status.config(text="")
    def hover_1(event):
        second["fg"] = "white"
        status.config(text="Text input")
    def left_1(event):
        second["fg"] = "cyan"
        status.config(text="")
    def hover_2(event):
        first["fg"] = "green"
        status.config(text="Welc0.0me")
    def left_2(event):
        first["fg"] = "cyan"
        status.config(text="")
    def hover_3(event):
        first["fg"] = "green"
        about.config(text="TREND was created by Michael.")
    def left_3(event):
        first["fg"] = "cyan"
        about.config(text="")
    def hover_4(event):
        mic["fg"] = "green"
        about.config(text="WELCOME FROM MICHAEL")
    def left_4(event):
        mic["fg"] = "black"
        about.config(text="")

    first.bind("<Enter>", hover_2)
    first.bind("<Leave>", left_2)
    mic.bind("<Enter>", hover_4)
    mic.bind("<Leave>", left_4)
    first.bind("<Enter>", hover_3)
    first.bind("<Leave>", left_3)
    fourth.bind("<Enter>", hover)
    fourth.bind("<Leave>", left)
    fourth.bind("<Return>", rec)
    fourth.bind("<Button-1>", rec)
    second.bind("<Enter>", hover_1)
    second.bind("Leave", left_1)
    second.bind("<Return>", text)
    second.bind("<Button-1>", text)

splash_root.after(3000, func_main)

mainloop()
