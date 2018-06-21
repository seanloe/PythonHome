#! python3
import urllib.request
from tkinter import *
from functools import partial
import csv, os

with urllib.request.urlopen('http://www.twse.com.tw/exchangeReport/STOCK_DAY_ALL?response=open_data') as urlfile:
    with open('temp.csv','wb+') as filehandle:
        filehandle.write(urlfile.read())
    #reader = csv.reader(urlfile.read().decode('utf-8'),delimiter=',')

with open('temp.csv', "r", encoding = 'utf-8') as f:
    reader = csv.reader(f)
    mylist = list(reader)
    f.close()
    os.remove('temp.csv')
    root = Tk()
    frame1 = Frame(root)
    frame1.pack()
    var = StringVar()
    msgbx1 = Message(frame1,textvariable=var, relief=FLAT, fg = "blue", anchor = NW,  bd = 5)
    msgbx1.pack()
    for num, line in enumerate(mylist):
        #print(line)
        if num <100:
            var.set(var.get()+str(line)+'\n')
    root.mainloop()
