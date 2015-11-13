#!/usr/bin/env python

from time import sleep,ctime
import threading

loops=(4,2)

class MyThread(threading.Thread):
    def __init__(self,func,args,name=''):
        threading.Thread.__init__(self)
        self.name=name
        self.func=func
        self.args=args

    def run(self):
        apply(self.func,self.args)

def loop(nloop,nsec):
    print 'start loop ', nloop, ' at:',ctime()
    sleep(nsec)
    print 'loop ', nloop, ' done at:', ctime()

def main():
    print 'start at:',ctime()
    threads=[]
    nloops=range(len(loops))

    for i in nloops:  
        t=MyThread(loop, (i,loops[i]), loop.__name__)
        threads.append(t)

    for i in nloops:  
        threads[i].start()

    for i in nloops:
        threads[i].join()       # wait for all threads to finish

    print 'all done at:',ctime()

if __name__=='__main__':
    main()

#start at: Fri Nov 13 12:15:02 2015
#start loop  start loop 0  1 at:   at:Fri Nov 13 12:15:02 2015
#Fri Nov 13 12:15:02 2015
#loop  1  done at: Fri Nov 13 12:15:04 2015
#loop  0  done at: Fri Nov 13 12:15:06 2015
#all done at: Fri Nov 13 12:15:06 2015