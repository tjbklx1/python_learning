#!/usr/bin/env python

from time import sleep,ctime
from MyThread import MyThread
    
def fib(x):
    sleep(0.005)
    if x<2:
        return 1 
    return ( fib(x-2) + fib(x-1) )

def fac(x):
    sleep(0.1)
    if x<2:
        return 1 
    return ( x*fib(x-1) )

def sum(x):
    sleep(0.1)
    if x<2:
        return 1 
    return (x+sum(x-1))
    
funcs=[fib,fac,sum]
n=12

def main():
    nfuncs=range(len(funcs))
    
    print '**** single thread ****'
    for i in nfuncs:
        print 'starting %s at: %s' % (funcs[i].__name__,ctime() )
        print funcs[i](n)
        print '%s finished at: %s' % (funcs[i].__name__,ctime() )
    
    print '\n**** MULTIPLE THREADS ****'
    threads=[]
    for i in nfuncs:
        t=MyThread( funcs[i], (n,), funcs[i].__name__ )
        threads.append(t)
        
    #start all thread 
    for i in nfuncs:  
        threads[i].start()

    for i in nfuncs: 
        threads[i].join()            # wait for all threads to finish
        print threads[i].getResult()

    print 'all done at:',ctime()        
    

if __name__=='__main__':
    main()


#**** single thread ****
#starting fib at: Fri Nov 13 15:23:01 2015
#233
#fib finished at: Fri Nov 13 15:23:08 2015
#starting fac at: Fri Nov 13 15:23:08 2015
#1728
#fac finished at: Fri Nov 13 15:23:13 2015
#starting sum at: Fri Nov 13 15:23:13 2015
#78
#sum finished at: Fri Nov 13 15:23:14 2015
#
#**** MULTIPLE THREADS ****
#start loop  fibstart loop    at :facstart loop   Fri Nov 13 15:23:14 2015 sum  at :   at :Fri Nov 13 15:23:14 2015
# Fri Nov 13 15:23:14 2015
#sum finish at:  Fri Nov 13 15:23:15 2015
#fac finish at:  Fri Nov 13 15:23:19 2015
#fib finish at:  Fri Nov 13 15:23:21 2015
#233
#1728
#78
#all done at: Fri Nov 13 15:23:21 2015







