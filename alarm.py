from mimetypes import init
from unicodedata import name
from pip import main
from playsound import playsound
from tkinter import *
from win10toast import ToastNotifier
import datetime
import time



def alarm(set_alarm):
    toast = ToastNotifier()
    while True:
        time.sleep(1)
        date = datetime.datetime.now()
        now = date.strftime("%H:%M:%S")
        print(now)
        if now == set_alarm:
            print("Here the alarm goes!")
            toast.show_toast("Here the alarm goes!!",duration=5)
            playsound("funny-alarm.mp3")
            exit().alarm("C:")

def getvalue():
    set_alarm = f"{hour.get()}:{min.get()}:{sec.get()}"
    alarm(set_alarm)

root = Tk()
root.geometry("230x130")
info = Label(root,text = "(24)Hour  Min   Sec").place(x = 90)
set_time = Label(root,text = "Enter Time",relief = "solid",font=("Comic Sans MS",10,"bold")).place(x=20,y=28)

# Entry Variables
hour = StringVar()
min = StringVar()
sec = StringVar()

# Entry Widget
hour_E = Entry(root,textvariable = hour,bg = "white",width = 6).place(x=100,y=30)
min_E = Entry(root,textvariable = min,bg = "white",width = 6).place(x=135,y=30)
sec_E = Entry(root,textvariable = sec,bg = "white",width = 6).place(x=170,y=30)

submit = Button(root,text = "Set Alarm",width = 10,command = getvalue).place(x = 80,y=70)

root.mainloop()
