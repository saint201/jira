import mss
import tkinter as tk
from tkinter import *
from cv2 import *
import pyautogui as pyg
import cv2
import time
import requests
from datetime import datetime
import json
import os
import numpy

def setToken(newToken):
    f = open('config.json')
    data = json.load(f)
    data['TOKEN']=newToken
    with open('config.json', 'w') as f:
        json.dump(data, f,indent=2)

def setStartState(state):
    f = open('config.json')
    data = json.load(f)
    data['startWithWindows']=state
    with open('config.json', 'w') as f:
        json.dump(data, f,indent=2)

def getStartState():
    f = open('config.json')
    data = json.load(f)
    state = data['startWithWindows']
    with open('config.json', 'w') as f:
        json.dump(data, f,indent=2)
    return(state)

def getToken():
    f = open('config.json')
    data = json.load(f)
    TOKEN = data['TOKEN']
    with open('config.json', 'w') as f:
        json.dump(data, f,indent=2)
    return(TOKEN)

def readhistory():
    f = open('config.json')
    data = json.load(f)
    with open('config.json', 'w') as f:
        json.dump(data, f,indent=2)
    return(data["history"])

async def addhistory(id,text,user):
    now = datetime.now()
    dt_string = now.strftime("%b/%d/%Y %H:%M:%S")
    f = open('config.json')
    data = json.load(f)
    data["history"].insert(0,"ID "+str(id)+" | "+dt_string+" | USER @"+user+" | ACTION: "+text)
    with open('config.json', 'w') as f:
        json.dump(data, f,indent=2)

def scrt():
    with mss.mss() as sct:
        filename = sct.shot(output="files/mon.png")
    return(filename)

def clickByPhoto():
    imagerz = cv2.imread('files/gotDot.png')
    imgfindgray = numpy.array(imagerz)
    hsv_min = numpy.array((1, 80, 80), numpy.uint8)
    hsv_max = numpy.array((20,250,250), numpy.uint8)
    hsv = cv2.cvtColor(imgfindgray, cv2.COLOR_BGR2HSV)
    thresh = cv2.inRange(hsv, hsv_min, hsv_max)
    moments = cv2.moments(thresh, 1)
    dM01 = moments['m01']
    dM10 = moments['m10']
    dArea = moments['m00']
    x = int(dM10 / dArea)
    y = int(dM01 / dArea)
    pyg.click(x * 1.5, y * 1.5)
    os.remove('files/gotDot.png')

def sendingGrayScale():
    with mss.mss() as sct:
        filename = sct.shot(output="files/mon.png")
    image = cv2.imread('files/mon.png')
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cv2.imwrite("files/mon.png", gray_image)
    return(filename)

def msgwindow(msg):
    root = Tk()
    l = Label(root, text = msg)
    root.title("message")
    l.config(font =("Courier", 14))
    l.pack()
    mainloop()
    
def doubleClick():
    pyg.doubleClick()

def rightClick():
    pyg.rightClick()

def pressButton(but):
    pyg.keyDown(but)
    pyg.keyUp(but)

def getRegistredUsers():
    f = open('config.json')
    data = json.load(f)
    with open('config.json', 'w') as f:
        json.dump(data, f,indent=2)
    return(data["registred_users"])
def botOnlineAllert():
    for i in getRegistredUsers():
        botSendMessage(i,"bot is online /start - to use")

def botSendMessage(id,text):
    TOKEN = getToken()
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={id}&text={text}"
    requests.get(url)

def msgwindowAns(id,msg):
    def get_data():
        global mesg
        mesg=passw_var.get()
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
    botSendMessage(id,mesg)

def camUnit():
    cam = cv2.VideoCapture(0) 
    time. sleep(1)
    result, image = cam.read() 
    time. sleep(1)
    result, image = cam.read() 
    if result: 
        cv2.imshow("wc", image) 
        cv2.imwrite("files/wc.png", image) 
        cv2.waitKey(0) 
        cv2.destroyWindow("wc") 
        return(image)
    else: 
        print("No image detected. Please! try again") 
        return(False)
