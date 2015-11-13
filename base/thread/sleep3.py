#!/usr/bin/env python

# add lock for every thread 

from time import sleep,ctime
import thread

loops=[4,2]

def loop(nloop,nsec,lock):
  print 'start loop ', nloop, ' at:',ctime()
  sleep(nsec)
  print 'loop ', nloop, ' done at:', ctime()
  lock.release()

def main():
  print 'start at:',ctime()
  locks=[]
  nloops=range(len(loops))
  
  # add lock for every thread 
  for i in nloops:  
    lock=thread.allocate_lock()
    lock.acquire()
    locks.append(lock)
  
  #start every thread .
  for i in nloops:  
    thread.start_new_thread(loop,(i,loops[i],locks[i]))

  for i in nloops: 
    while locks[i].locked():
        pass

  print 'all done at:',ctime()

if __name__=='__main__':
  main()

#>python sleep3.py
#start at: Mon Nov 09 14:36:26 2015
#start loop start loop   01   at: at:  Mon Nov 09 14:36:26 2015Mon Nov 09 14:36:2
#
#loop  1  done at: Mon Nov 09 14:36:28 2015
#loop  0  done at: Mon Nov 09 14:36:30 2015
#all done at: Mon Nov 09 14:36:30 2015
#