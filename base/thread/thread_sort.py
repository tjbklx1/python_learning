import threading,time  
  
thread_count=4
t_l=[-1]*4

class TestThread(threading.Thread):  
    def __init__(self,thread_name):  
        threading.Thread.__init__(self)  
        self.setName(thread_name)

    def run(self):
        name=self.getName()
        i_name=int(name)        
        while True:
            threadLock.acquire()
            if min(t_l)==4:
                threadLock.release()
                return 0
            elif t_l[i_name] ==min(t_l):
                t_l[i_name] +=1
                print "thread %s print %s " %(name,str(t_l[i_name] ))
                threadLock.release()
            else:
                threadLock.release()
                time.sleep(1)

if __name__ == '__main__':  
    threadLock=threading.Lock()
    for i in xrange(thread_count):
        t= TestThread(str(i) )   
        t.start()

#thread 0 print 0
#thread 1 print 0
#thread 2 print 0
#thread 3 print 0
#thread 3 print 1
#thread 2 print 1
#thread 1 print 1
#thread 0 print 1
#thread 3 print 2
#thread 2 print 2
#thread 1 print 2
#thread 0 print 2
#thread 3 print 3
#thread 2 print 3
#thread 1 print 3
#thread 0 print 3
#thread 3 print 4
#thread 2 print 4
#thread 1 print 4
#thread 0 print 4