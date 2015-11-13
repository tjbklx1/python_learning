#!/usr/bin/env python

from random import randint
from time import sleep
from Queue import Queue
from MyThread import MyThread
    
def writeQ(queue):
    queue.put('xxx',1)
    print 'producing object for Q... size now : %d' % (queue.qsize())
    
def readQ(queue):
    val=queue.get(1)
    print '\nconsumed object from Q... size now %d.' %(queue.qsize())

def writer(queue,loops):
    for i in range(loops):
        writeQ(queue)
        sleep(randint(1,3))

def reader(queue,loops):
    for i in range(loops):
        readQ(queue)
        sleep(randint(2,5))

funcs=[writer,reader]
nfuncs=range(len(funcs))

def main():
    nloops=randint(2,5)
    q=Queue(32)
    threads=[]

    # create all thread 
    for i in nfuncs:  
        t=MyThread( funcs[i], (q,nloops), funcs[i].__name__ )
        threads.append(t)

    #start all thread 
    for i in nfuncs:  
        threads[i].start()

    for i in nfuncs: 
        threads[i].join()       # wait for all threads to finish

    print 'all done '

if __name__=='__main__':
    main()

#
#start loop writer at : Fri Nov 13 16:43:38 2015
#start loop reader at : Fri Nov 13 16:43:38 2015
#
#producing object for Q... size now : 1
#consumed object from Q... size now 0.
#
#producing object for Q... size now : 1
#producing object for Q... size now : 2
#producing object for Q... size now : 3
#
#consumed object from Q... size now 2.
#writer finish at: Fri Nov 13 16:43:43 2015
#
#consumed object from Q... size now 1.
#
#consumed object from Q... size now 0.
#reader finish at: Fri Nov 13 16:43:54 2015
#all done




