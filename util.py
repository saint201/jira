import mss
import tkinter as tk
from tkinter import *
from cv2 import *
import cv2
import time
def scrt():
    with mss.mss() as sct:
        filename = sct.shot(output="mon-{mon}.png")
        print(filename)
    return(True)

def msgwindow(msg):
    root = Tk()
    l = Label(root, text = msg)
    root.title("message")
    l.config(font =("Courier", 14))
    l.pack()
    mainloop()
    return(True)

def msgwindowAns(msg):
    def get_data():
        global password
        password=passw_var.get()
        master.destroy()
    master = Tk()
    passw_var=tk.StringVar()
    master.title("message")
    Label(master, text=msg).pack()
    e1 = Entry(master,textvariable = passw_var)
    e1.pack() 
    button = tk.Button(master, text='send' , width=10, command=get_data)
    button.pack() 
    mainloop()
    return(password)

def camUnit():
    cam = cv2.VideoCapture(0) 
    time. sleep(1)
    result, image = cam.read() 
    time. sleep(1)
    result, image = cam.read() 
    if result: 
        cv2.imshow("wc", image) 
        cv2.imwrite("wc.png", image) 
        cv2.waitKey(0) 
        cv2.destroyWindow("wc") 
        return(image)
    else: 
        print("No image detected. Please! try again") 
        return(False)
camUnit()