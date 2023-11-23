import subprocess
import os
import playsound
from random import randint
from time import sleep
from tkinter import *
from tkinter import messagebox
import sys
from threading import Thread
import keyboard
import win32con
import ctypes
import win32api
# import pynput

def bsod():
    if sys.version_info[0] == 2:  # the tkinter library changed it's name from Python 2 to 3.
        import Tkinter
        tkinter = Tkinter #I decided to use a library reference to avoid potential naming conflicts with people's programs.
    else:
        import tkinter
    from PIL import Image, ImageTk

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



def emergency_exit():
    while True:
        if keyboard.is_pressed('ENTER'):
            os._exit(0)

exitThread = Thread(target = emergency_exit)
exitThread.start()


keyboard.press('f11')


volume = True
def changeVolume(arg):
    i = 0
    # while i < volume / 2:
    #     win32api.keybd_event(win32con.VK_VOLUME_UP, 0)
    #     win32api.keybd_event(win32con.VK_VOLUME_UP, 0, win32con.KEYEVENTF_KEYUP)
    #     sleep(0.1)
    #     i = i + 1


volumeThread = Thread(target = changeVolume, args = (10, ))
volumeThread.start()


def musicThreading(arg):
    print("you messed up")
    outro_path = str(f'{os.path.dirname(__file__)}\Outro-Music.mp3')
    playsound.playsound(outro_path)

musicThread = Thread(target = musicThreading, args = (10, ))
musicThread.start()


sleep(0.1)


def countdown(timer):
    i = timer
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


countdownThread = Thread(target = countdown, args = (10, ))
countdownThread.start()


sleep(10)


print("Goodbye :)")

sleep(0.5)


#bsod section \/
if sys.platform == "win32":
    os.chdir(os.path.dirname(__file__))

    volume = False

    # pip_file_path = str(f"{os.path.dirname(__file__)}/bat/pip.bat")
    # subprocess.call([pip_file_path])

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


        # bat_file_path = str(f"{os.path.dirname(__file__)}/bsod.bat")
        # subprocess.call([bat_file_path])
        bsod()
        # pycache_path = str(f"{os.path.dirname(__file__)}/__pycache__/volume.cpython-310.pyc")
        # os.remove(pycache_path)


    except:
        input("Sorry something went wrong in the installation process. Please turn on internet and try again.")

else:
    input("Sorry, this program is only compatible with Windows.")


# volume = False


# range_repeat = randint(1, 3)
# for i in range(range_repeat):
#     print("ERROR CANT FIND CURRENT WORKING DIRECTORY")
#     keyboard.press_and_release("F11")
#     keyboard.press_and_release("F11")
#     keyboard.press_and_release("F11")
#     keyboard.press_and_release("F11")
#     keyboard.press_and_release("F11")
#     sleep(0.01)
#     keyboard.press_and_release("F11")
#     keyboard.press_and_release("F11")
#     keyboard.press_and_release("F11")
#     keyboard.press_and_release("F11")


# # bat_file_path = str(f"{os.path.dirname(__file__)}/bsod.bat")
# # subprocess.call([bat_file_path])
# bsod()
