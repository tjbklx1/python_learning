#!/usr/bin/env python

from time import sleep,ctime
import thread

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
  thread.start_new_thread(loop0,())
  thread.start_new_thread(loop1,())
  sleep(6)  # wait two thread end.
  print 'all done at:',ctime()

if __name__=='__main__':
  main()

#>python sleep2.py
#start at: Mon Nov 09 14:36:16 2015
#start loop 0 at:start loop 1 at:  Mon Nov 09 14:36:16 2015Mon Nov 09 14:36:16 20
#
#loop 1 done at: Mon Nov 09 14:36:18 2015
#loop 0 done at: Mon Nov 09 14:36:20 2015
#all done at: Mon Nov 09 14:36:22 2015
#




# donot wait two thread end
# #sleep(6)  # wait two thread end.


#start at: Fri Nov 13 10:42:14 2015
#all done at:start loop 0 at:start loop 1 at:  Fri Nov 13 10:42:14 2015 Fri Nov 1
#Fri Nov 13 10:42:14 2015