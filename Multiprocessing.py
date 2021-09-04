from multiprocessing import Process, Value, Array, Lock
from multiprocessing import Queue 
import time
import os
def adduser(x):
    return x+ 1
processes = []
num_processes = os.cpu_count
#create processes
for i in range(num_processes):
    p = Process(target=adduser)
    processes.append(p)
for p in processes:
    p.start()
for p in processes:
    p.join()
def add1(user, lock):
    for i in range(10):
        time.sleep(0.1)
        for i in range(len(user)):
            user[i] += 1
        lock.acquire()
        user.value += 1
        lock.release()
if __name__ == "__main__":
    lock = Lock()
    shared_array = Array('d', [0.0, 100.0, 200.0])
    print('array is', shared_array[:])
    shared_user = Value('i', 0)
    print('First user is', shared_user.value)
    p1 = Process(target=add1, args=(shared_user, shared_array, lock))
    p2 = Process(target=add1, args=(shared_user, shared_array, lock))
    p1.start()
    p2.start()
    p1.join() 
    p2.join()
    print('End user is', shared_user.value)
    print('Ending array is', shared_array[:])
def square(numbers, queue):
    for i in numbers:
        queue.put(i*i)
def make_negative(numbers, queue):
    for i in numbers:
        queue.put(-1*i)
if __name__ == "__main__":
    numbers = range(1,6)
    q = Queue()
    p1 = Process(target=square, args=(numbers, q))
    p2 = Process(target=make_negative, args=(numbers, q))
    p1.start()
    p2.start()
    p1.join()
    p2.join()