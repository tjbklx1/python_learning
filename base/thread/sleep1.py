#!/usr/bin/env python

from time import sleep,ctime

def loop0():
  print 'start loop 0 at:',ctime()
  sleep(4)
  print 'loop 0 done at:',ctime()

def loop1():
  print 'start loop 1 at:',ctime()
  sleep(2)
  print 'loop 1 done at:',ctime()

def main():
  print 'start at:',ctime()
  loop0()
  loop1()
  print 'all done at:',ctime()

if __name__=='__main__':
  main()


#>python sleep1.py
#start at: Mon Nov 09 14:36:06 2015
#start loop 0 at: Mon Nov 09 14:36:06 2015
#loop 0 done at: Mon Nov 09 14:36:10 2015
#start loop 1 at: Mon Nov 09 14:36:10 2015
#loop 1 done at: Mon Nov 09 14:36:12 2015
#all done at: Mon Nov 09 14:36:12 2015
#

