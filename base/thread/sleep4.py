#!/usr/bin/env python

from time import sleep,ctime
import threading

loops=[4,2]

def loop(nloop,nsec):
  print 'start loop ', nloop, ' at:',ctime()
  sleep(nsec)
  print 'loop ', nloop, ' done at:', ctime()

def main():
  print 'start at:',ctime()
  threads=[]
  nloops=range(len(loops))
  
  # create all thread 
  for i in nloops:  
    t=threading.Thread(target=loop,args=(i,loops[i]))
    threads.append(t)
  
  #start all thread 
  for i in nloops:  
    threads[i].start()

  for i in nloops: 
    threads[i].join()       #  wait for all threads to finish

  print 'all done at:',ctime()

if __name__=='__main__':
  main()


#>python sleep4.py
#start at: Mon Nov 09 14:36:35 2015
#start loop  0start loop   at: 1  at:  Mon Nov 09 14:36:35 2015
#Mon Nov 09 14:36:35 2015
#loop  1  done at: Mon Nov 09 14:36:37 2015
#loop  0  done at: Mon Nov 09 14:36:39 2015
#all done at: Mon Nov 09 14:36:39 2015
#