
#! /usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np
import threading,time, copy
from queue import Queue

class Myclass:
    species = 'human'
    def __init__(self, name, gender,age):
        self.name = name
        self.gender = gender
        self.age = age

    def run(self):
        print(self.name, ' is running')

    def eat(self, food):
        print(self.name, ' is eating ', food)

        
        
class Man(Myclass):
    def fastrun(self):
        self.run()
        print('This time run very fast')

#test to build a 3D matrix 4X4X3 matrix
S_list=[[[x, x**2, 3*x] for x in np.random.randint(0,100,4)] for num in range(4)]

def thread_job(lock, list,q):
    while len(list)>0:
        #time.sleep(1)
        lock.acquire()
        try:
            i = list.pop()
            #print(time.asctime(time.localtime()), threading.current_thread(), 'get %d'%i)
            q.put(i**5)
        except Exception as e:
            print("Error!",e)
        lock.release()

def multi_thread(lock, l,q):
    threadlist = []
    for i in range(8):
        thread = threading.Thread(target = thread_job, name= 'T'+str(i), args =(lock,l,q))
        thread.start()
        threadlist.append(thread)
    for t in threadlist:
        t.join()
def normal_run(lock,list,q):
    while len(list)>0:
        #time.sleep(1)
        lock.acquire()
        try:
            i = list.pop()
            #print(time.asctime(time.localtime()), threading.current_thread(), 'get %d'%i)
            q.put(i**5)
        except Exception as e:
            print("Error!",e)
        lock.release()    
    
def main():
    lock = threading.Lock()
    a = np.arange(1,10000,1)
    mylist = a.tolist()
    mylist2 = copy.deepcopy(mylist)
    q = Queue()
    t_start = time.time()
    multi_thread(lock,mylist,q)
    t_finish = time.time()
    #print(threading.active_count())
    #print(threading.enumerate())
    print("Total thread execution time:", t_finish-t_start)
    result = 0
    for _ in range(q.qsize()):
        result += q.get()
    print(result)
    print('Now normal run')
    t_start = time.time()
    normal_run(lock,mylist2,q)
    t_finish = time.time()
    result = 0
    print('Now normal run execution time:',t_finish-t_start)
    for _ in range(q.qsize()):
        result += q.get()
    print(result)  
    
if __name__ == '__main__':
    main()
