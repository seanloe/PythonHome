#!/usr/bin/python

from tkinter import *
import numpy as np
import threading,time
import multiprocessing as mp
from functools import partial

def rolldice():
    loopnum = 0
    while np.random.randint(1000) not in [995,996,997,998,999,1000]:
        loopnum += 1
    return loopnum

def buttomcallback(var):
    var.set("")
    list = []
    for i in range(15):
        value = rolldice()
        var.set(var.get()+"共擲了"+ str(value) + "次\n")
        list.append(value)
    var.set(var.get()+'平均擲了 '+str(np.average(list))+' 次')
def update_messagebox(q, lock,var):
    while True:
        time.sleep(1)
        if len(mylist)>0:
            var.set(var.get()+mylist[0])
    
def main():
    root = Tk()
    root.title('My first Window')
    root.geometry("300x300")
    frame1 = Frame(root)
    frame1.pack()
    framebottom = Frame(root)
    framebottom.pack(side = BOTTOM)
    var = StringVar()
    msgbx1 = Message(frame1,textvariable=var, relief=FLAT, fg = "blue", anchor = NW,  bd = 5)
    msgbx1.pack()
    btn1 = Button(framebottom, text="Start", fg="blue", command = partial(buttomcallback,var))
    btn1.pack()
    #lock = threading.Lock()
    #q = mp.Queue()
    #t1 = threading.Thread(target=update_messagebox, args=(q, lock,var)) 
    #t1.start()  #啟動 t1 線程
    #t1.join()  #在 t1線程結束前阻止程式繼續運行

    root.mainloop()

if __name__ == '__main__': main()
