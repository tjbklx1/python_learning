﻿import string, threading, time
 
def thread_main(a):
    global count, mutex
    # 获得线程名
    threadname = threading.currentThread().getName()
 
    for x in xrange(0, int(a)):
        # 取得锁
        mutex.acquire()
        count = count + 1
        print (">>%s , %d, %d ") % (threadname, x, count)
        # 释放锁
        mutex.release()
        
        time.sleep(1)
 
def main(num):
    global count, mutex
    threads = []
 
    count = 1
    # 创建一个锁
    mutex = threading.Lock()
    # 先创建线程对象
    for x in xrange(0, num):
        threads.append(threading.Thread(target=thread_main, args=(5,)))
    # 启动所有线程
    for t in threads:
        t.start()
    # 主线程中等待所有子线程退出
    for t in threads:
        t.join()  
 
 
if __name__ == '__main__':
    num = 4
    # 创建4个线程
    main(4)