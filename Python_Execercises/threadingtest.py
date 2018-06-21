#! /usr/bin/env python
# -*- coding: utf-8 -*-
import threading as td
import time

def func1(num,lock):
    for loop in range(50):
        time.sleep(1)
        lock.acquire()
        print('Now func1 loop %d'%(loop))
        lock.release()
        
def func2(num,lock):
    for loop in range(50):
        time.sleep(1)
        lock.acquire()
        print('Now func2 loop %d'%(loop))
        lock.release()
        
def main():
    lock = td.Lock()
    td1 = td.Thread(target =func1, args=(8,lock))
    td2 = td.Thread(target =func2, args=(8,lock))
    td1.start()
    td2.start()
    #td1.join()
    #td2.join()


if __name__ == '__main__': main()