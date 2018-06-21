#!python3
import multiprocessing as mp
import numpy as np
import time, functools

def mp_job(x):
    return x**2

def var_job(lock,var, target_value):
    lock.acquire()
    for _ in range(10):
        time.sleep(0.1)
        var.value = target_value
        print('Current value =',var.value)
    lock.release()
def main():
    pool = mp.Pool(processes = 4)
    myarray = np.arange(1,100,1)
    mylist = myarray.tolist()
    result = pool.map(mp_job, mylist)
    print(np.sum(result))
    multi_result = [pool.apply_async(mp_job, (i,)) for i in range(100)]
    print("async result:",np.sum([result.get() for result in multi_result]))

def test_var():
    print('Start running test_var')
    #m = mp.Manager()
    lock = mp.Lock()
    #func1 = functools.partial(var_job, lock)
    myvar = mp.Value('i',0)
    #pool = mp.Pool()
    #pool.map(func1, [(myvar,1),(myvar,3)])
    p1 = mp.Process(target = var_job, args = (lock,myvar,1))
    #print(res.get())
    #res = pool.Apply_async(func1, (myvar,3))
    p2 = mp.Process(target = var_job, args = (lock,myvar,3))
    #print(res.get())
    p1.start()
    p2.start()
if __name__ == '__main__':
    main()
    test_var()
