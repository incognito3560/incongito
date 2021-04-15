#THANK YOU FOR DOWLOADING THIS EXCELLENT TOOL
#THIS TOOL IS ESSPECIALY MADE FOR AUTOMATION PURPOSES AND NOT ANY MALICIOUS ACTIVITY (0_-)
#FEAL FREE TO CONTRIBUTE TO MAKE THIS TOOL BETTER


'The error message keeps popping with non apps opening EG:Time function'

'I imported the modules that run the app'
from os import *
from tkinter import *
from tkinter import filedialog
from time import *
import webbrowser
from gtts import gTTS
import speech_recognition as sr
import pyaudio



'This is the main window'
root = Tk()
root.iconbitmap("iconfinder_ArtificialIntelligence23_2890589.ico")
root.configure(background="black")
root.title("SOFTWARE OPENER")
root.geometry("500x500")
root.attributes("-alpha", 0.9)
root.resizable(width="false", height="false")


'Audio input'
try:
    def sound():
        filename = "ace-by-user144529-on-2020-08-30t162459119690z.wav"
        playsound.playsound(filename)


    sound()
except:
    pass

'This is the function for running the users input'

def all():
    def opn(event):
        try:
            'these are the functions that run the search engine and etc'
            mike = entry.get()
            if entry.get() == "hacking":
                os = startfile("vmware")
                os = startfile("cmd")

            elif entry.get() == "commands":
                coo = Tk()
                coo.iconbitmap("iconfinder_ArtificialIntelligence23_2890589.ico")
                coo.configure(background="black")
                coo.title("KALI COMMANDS")
                coo.attributes("-alpha", 0.9)
                coo.resizable(width="false", height="false")

                coo_label = Label(coo, text="Hello this are my favorite commands:", bg="black", fg="white")
                coo_label.pack()
                coo_label2 = Label(coo, text="1: anonsurf start 2: msfconsole 3: whois 4: python 5: sudo su\n6: nmap 7: ping 8: tracert 9: ifconfig 10: proxychains\n11: cd 12: ls 13: cat 14: nano 15: rm <<'for deliting files'", fg="red", bg="black")
                coo_label2.pack(pady=10)
                coo_label3 = Label(coo, text="My favorite tools:", bg="black", fg="white")
                coo_label3.pack(pady=10)
                coo_label4 = Label(coo, text="1: NMAP 2: Metasploit 3: Kage << 'metasploit gui' 4: social engeniering toolkit 5: hydra\n6: CMD 7: ZAP 8: Nikto 9: sqlmap 10: metaploitable << 'practicing pentesting'", fg="red", bg="black")
                coo_label4.pack(pady=10)

            elif entry.get() == "time":
                time = Label(root, text=asctime(), bg="black", fg="white")
                time.pack()

            elif entry.get() == "search":
                web = Tk()
                web.iconbitmap("iconfinder_ArtificialIntelligence23_2890589.ico")
                web.configure(background="black")
                web.title("SEARCH")
                web.attributes("-alpha", 0.9)
                web.geometry("200x200")
                web.resizable(width="false", height="false")

                def done():
                    webbrowser.open("http://" + str(gs.get()))

                inpu = Label(web, text="Enter website name: ", bg="black", fg="white")
                inpu.pack()
                gs = Entry(web, width=20)
                gs.pack(pady=10)
                but = Button(web, text="ENTER", bg="black", fg="white", command=done)
                but.pack(pady=10)

            elif entry.get() == "close":
                'this is the second window'
                window = Tk()
                window.iconbitmap("iconfinder_ArtificialIntelligence23_2890589.ico")
                window.configure(background="black")
                window.title("SOFTWARE CLOSER")
                window.geometry("300x300")
                window.attributes("-alpha", 0.9)
                window.resizable(width="false", height="false")

                def click(event):
                    try:
                        'this is a funstion for closing apps'
                        os = system("TASKKILL /IM " + str(la.get()) + ".exe /F")
                        if la.get() == "help":
                            os = system("taskmgr")
                        else:
                            window.destroy()
                    except:
                        er = Label(window, text="INVALID NAME TRY AGAIN OR TYPE HELP")

                lable = Label(window, text="Enter name of app you want to close: ", bg="black", fg="white")
                lable.pack()
                la = Entry(window, width=20)
                la.pack(pady=3)
                ent = Button(window, text="ENTER", bg="black", fg="white", command=click)
                ent.pack(pady=10)
                ent.bind("<Return>", click)
                ent.bind("<Button-1>", click)

            elif entry.get() == "photo editing":
                os = startfile("photoshop")

            elif entry.get() == "av":
                os = startfile("AvastUI.exe")

            elif entry.get() == "about":
                status = Tk()
                status.iconbitmap("iconfinder_ArtificialIntelligence23_2890589.ico")
                status.configure(background="black")
                status.title("ABOUT")
                status.attributes("-alpha", 0.9)
                status.resizable(width="false", height="false")

                def dest():
                    status.destroy()

                about_label = Label(status,
                                    text="THANKS FOR DOWLOADING THIS AWESOME APP\nThis app was devoped by tenage boy by the name 'MICHAEL'\nHe has a huge love for coding and so he decide to make his own,\nand by making this app his dream came true.(0.0)",
                                    bg="black", fg="white")
                about_label.pack()

                about_button = Button(status, command=dest, text="EXIT", bg="black", fg="white")
                about_button.pack()

            elif entry.get() == "files":
                os = startfile("C:")

            elif entry.get() == "cain":
                os = startfile("C:\Program Files (x86)\Cain\Cain.exe")

            elif entry.get() == "vpn":
                os = startfile("NordVPN.exe")

            elif entry.get() == "video editing":
                os = startfile("premire pro")

            elif entry.get() == "browsing":
                os = startfile("chrome.exe")

            elif entry.get() == "3d":
                os = startfile("cinema 4d")

            elif entry.get() == "coding":
                os = startfile("pycharm")

            elif entry.get() == "shutdown":
                os = system("shutdown /p")

            elif entry.get() == "help":
                'this is the help window'
                second = Tk()
                second.iconbitmap("iconfinder_ArtificialIntelligence23_2890589.ico")
                second.configure(background="black")
                second.title("HELP DIALOG")
                second.geometry("300x300")
                second.attributes("-alpha", 0.9)

                def close():
                    second.destroy()

                second.resizable(width="false", height="false")
                lam = Label(second,
                            text="THE FOLLOWING OPTIONS ARE AVILABLE:\n>>hacking<<,>>photo editing<<\n>>video editing<<\n>>3d<<,>>dialog<<\n>>browser<<,>>close<<\n>>time<<,>>av<<\n>>vpn<<,>>files<<\n>>about<<,>>cain<<\n>>commands<<,>>search<<\n",
                            fg="white", bg="black")
                lam.pack()
                exit = Button(second, text="CLICK TO EXIT", command=close, fg="white", bg="black")
                exit.pack(pady=20)

            elif entry.get() == "dialog":
                def open():
                    'this is a function for open a dialog box'
                    root.filename = filedialog.askopenfilename(initialdir="C:\ ", title="Enter file name: ",
                                                               filetypes=(("all files", "*.*"), ("exe files", ".*exe")))
                    warning = Label(root, text="WARNING!!DOES NOT SUPPORT >> .ico << FILES", fg="white", bg="black")
                    os = startfile(root.filename)

                open()

            os = startfile(mike)
            os = system(mike)
            os = stat(mike)
        except:
            'this is the error message'
            err = Label(root,
                        text="INVALID INPUT (0_0) Please try >>help<<",
                        bg="black", fg="white")
            err.pack()

    'this is the main user interface'
    label = Label(root, text="HELLOW Dear user welcome to application opener", bg="black", fg="white",
                  font=("Warmesty", 15))
    label.pack()

    label2 = Label(root, text="(0_-)~Type the task you want to automate opening~: ", bg="black", fg="white")
    label2.pack(pady=10)

    def clear():
        os = startfile("automation.exe")
        root.destroy()


    entry = Entry(root, width=20)
    entry.pack(pady=0)

    button = Button(root, text="ENTER", bg="black", fg="white", command=opn)
    button.pack(pady=5)

    close_button = Button(root, text="CLEAR SCREEN", command=clear, bg="black", fg="white", bd=0)
    close_button.place(x=0, y=480)

    button.bind("<Return>", opn)
    button.bind("<Button-1>", opn)

if __name__ == '__main__':
    all()

mainloop()
