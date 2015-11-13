﻿#!/usr/bin/env python

from time import sleep,ctime
import threading

class MyThread(threading.Thread):
    def __init__(self,func,args,name=''):
        threading.Thread.__init__(self)
        self.name=name
        self.func=func
        self.args=args

    def getResult(self):
        return self.res

    def run(self):
        print 'start loop ', self.name, ' at :',ctime()
        self.res=apply(self.func,self.args)
        print self.name,'finish at: ', ctime()
