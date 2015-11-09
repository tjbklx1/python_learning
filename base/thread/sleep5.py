#!/usr/bin/env python

from time import sleep,ctime
import threading

loops=[4,2]

class ThreadFunc(object):
  def __init__(self,func,args,name=''):
    self.name=name
    self.func=func
    self.args=args
  
  def __call__(self):
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
    t=threading.Thread(
    target= ThreadFunc(loop,(i,loops[i]),loop.__name__))
    threads.append(t)
  
  for i in nloops:  
    threads[i].start()

  for i in nloops:          # wait for all
    threads[i].join()       # threads to finish

  print 'all done at:',ctime()

if __name__=='__main__':
  main()


#>python sleep5.py
#start at: Mon Nov 09 14:36:46 2015
#start loop  0start loop    at:1  Mon Nov 09 14:36:46 2015 at:
# Mon Nov 09 14:36:46 2015
#loop  1  done at: Mon Nov 09 14:36:48 2015
#loop  0  done at: Mon Nov 09 14:36:50 2015
#all done at: Mon Nov 09 14:36:50 2015