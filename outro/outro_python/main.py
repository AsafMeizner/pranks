import tkinter
import playsound
import os
from random import randint
from time import sleep
import sys
from threading import Thread
import keyboard
import win32con
import win32api
import time
from time import sleep
import ctypes
from tkinter import *
from tkinter import messagebox
from importlib import import_module
from PIL import Image, ImageTk

time_to_wait = 10
volume = False

def emergency_exit():
    while True:
        if keyboard.is_pressed('ENTER'):
            os._exit(0)

exitThread = Thread(target = emergency_exit)
exitThread.start()


keyboard.press('f11')


def changeVolume(arg):
    i = 0
    while i < 100 / 2:
        win32api.keybd_event(win32con.VK_VOLUME_UP, 0)
        win32api.keybd_event(win32con.VK_VOLUME_UP, 0, win32con.KEYEVENTF_KEYUP)
        time.sleep(0.1)
        i = i + 1

if changeVolume == True:
    volumeThread = Thread(target = changeVolume, args = (10, ))
    volumeThread.start()


def musicThreading(arg):
    outro_path = str(f'{os.path.dirname(__file__)}\Outro-Music.mp3')
    playsound.playsound(outro_path)

musicThread = Thread(target = musicThreading, args = (10, ))
musicThread.start()

sleep(0.1)

def timerThreading():
    i = time_to_wait
    while i > 0:
        def window1(i):
            print('Deleting system 32 in ' + str(i))
            messagebox.showerror('Error', 'Error: Deleting system 32 in ' + str(i))
            ctypes.windll.user32.MessageBoxW(0, u"Deleting system 32 in " + str(i), u"Error" + str(i), 0)
            messagebox.showerror('Error', 'Error: Deleting system 32 in ' + str(i))
            ctypes.windll.user32.MessageBoxW(0, u"Deleting system 32 in " + str(i), u"Error" + str(i), 0)
            messagebox.showerror('Error', 'Error: Deleting system 32 in ' + str(i))
            ctypes.windll.user32.MessageBoxW(0, u"Deleting system 32 in " + str(i), u"Error" + str(i), 0)

        windowThread = Thread(target = window1, args = (i, ))
        windowThread.start()


        def window2(i):
            ctypes.windll.user32.MessageBoxW(0, u"Deleting system 32 in " + str(i), u"Error" + str(i), 0)
            messagebox.showerror('Error', 'Error: Deleting system 32 in ' + str(i))
            messagebox.showerror('Error', 'Error: Deleting system 32 in ' + str(i))
            ctypes.windll.user32.MessageBoxW(0, u"Deleting system 32 in " + str(i), u"Error" + str(i), 0)
            messagebox.showerror('Error', 'Error: Deleting system 32 in ' + str(i))
            ctypes.windll.user32.MessageBoxW(0, u"Deleting system 32 in " + str(i), u"Error" + str(i), 0)

        windowThread = Thread(target = window2, args = (i, ))
        windowThread.start()


        sleep(0.9)
        i = i - 1

countdownThread = Thread(target = timerThreading)
countdownThread.start()


sleep(10)


print("Goodbye :)")

sleep(0.5)

def showPIL(pilImage):
    root = tkinter.Tk()
    w, h = root.winfo_screenwidth(), root.winfo_screenheight()
    root.overrideredirect(1)
    root.geometry("%dx%d+0+0" % (w, h))
    root.focus_set()    
    root.bind("<Escape>", lambda e: (e.widget.withdraw(), e.widget.quit()))
    canvas = tkinter.Canvas(root,width=w,height=h)
    canvas.pack()
    canvas.configure(background='black')
    imgWidth, imgHeight = pilImage.size
    if imgWidth > w or imgHeight > h:
        ratio = min(w/imgWidth, h/imgHeight)
        imgWidth = int(imgWidth*ratio)
        imgHeight = int(imgHeight*ratio)
        pilImage = pilImage.resize((imgWidth,imgHeight), Image.ANTIALIAS)
    image = ImageTk.PhotoImage(pilImage)
    imagesprite = canvas.create_image(w/2,h/2,image=image)
    root.mainloop()

bsod_path = str(f"{os.path.dirname(__file__)}\\bsod.png")
pilImage = Image.open(bsod_path)

def bsod():
    showPIL(pilImage)
    while True:
        if keyboard.is_pressed('ENTER'):
            os._exit(0)

#bsod section \/
if sys.platform == "win32":
    os.chdir(os.path.dirname(__file__))

    volume = False

    try:
        range_repeat = randint(1, 3)
        for i in range(range_repeat):
            print("ERROR CANT FIND CURRENT WORKING DIRECTORY")
            keyboard.press_and_release("F11")
            keyboard.press_and_release("F11")
            keyboard.press_and_release("F11")
            keyboard.press_and_release("F11")
            keyboard.press_and_release("F11")
            sleep(0.01)
            keyboard.press_and_release("F11")
            keyboard.press_and_release("F11")
            keyboard.press_and_release("F11")
            keyboard.press_and_release("F11")

        bsod()


    except:
        input("Sorry something went wrong in the installation process. Please turn on internet and try again.")

else:
    input("Sorry, this program is only compatible with Windows.")
