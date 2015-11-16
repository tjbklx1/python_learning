#!/usr/bin/env python
#coding=utf-8

import Queue
import threading
import time
import json 
import urllib2
import socket
import commands
import pdb 
from moniItems import mon 

import sys,os

#��'..'Ŀ¼����importģ���Ĭ������·����
sys.path.insert(1,os.path.join(sys.path[0],'..'))
#import �������ݵĺ���
#from simpleNet.nbNetFramework import senddata_mh

thread_num=5
intervals=[3,4]

# �޸ĳ�������������ģʽ

#������
class getDataThread(threading.Thread):
    def __init__(self,name,q,que_lock=None,interval=None):
        """init data """
        threading.Thread.__init__(self)
        self.name=name 
        self.q=q 
        self.que_lock=que_lock
        self.interval=interval
        self.sock_l=[None]
    
    def run(self):
        m=mon()
        atime=int(time.time())
        while 1 :
            data=m.runAllGet()
            #data="memory:16G"
            self.que_lock.acquire()
            self.q.put(data)
            print "\n %s get monitor data %s " %(self.name,data)
            self.que_lock.release()
            #����ʱ������Ƶ������
            btime=int(time.time())
            time.sleep(self.interval-( (btime-atime)%self.interval ))
            
#������
class sendDataThread(threading.Thread):
    def __init__(self,name,q,que_lock=None,interval=None):
        """init data """
        threading.Thread.__init__(self)
        self.name=name 
        self.q=q 
        self.que_lock=que_lock
        self.interval=interval
        self.sock_l=[None]
    
    def run(self):
        while 1:
            if not self.q.empty():
                data=self.q.get()
                print "\n           %s send data ... %s " %(self.name,data) 
                #debug 
                #pdb.set_trace()
                #send monitor data 
                #sendData_mh()  
            time.sleep(self.interval)
    
def startTh():
    #init 10 queue ,����10������û�б�����,put����������
    que=Queue.Queue(10)
    que_lock=threading.Lock()
    
    for i in xrange(thread_num):
        collect=getDataThread('collect' + str(i),que,que_lock,interval=intervals[0])
        collect.start()
    
    sendjson=sendDataThread('sendjson',que,que_lock,interval=intervals[1])
    sendjson.start()
    
    #collect.join()
    #sendjson.join()

if __name__=="__main__":
    startTh()

#
#[remote~/z_test]python agent2.py 
#
# collect0 get monitor data {'get': 1447468386} 
#
# collect1 get monitor data {'get': 1447468386} 
#
# collect2 get monitor data {'get': 1447468386} 
#
# collect3 get monitor data {'get': 1447468386} 
#
# collect4 get monitor data {'get': 1447468386} 
#
#           sendjson send data ... {'get': 1447468386} 
#
# collect0 get monitor data {'get': 1447468389} 
#
# collect1 get monitor data {'get': 1447468389} 
#
# collect2 get monitor data {'get': 1447468389} 
#
# collect3 get monitor data {'get': 1447468389} 
#
# collect4 get monitor data {'get': 1447468389} 
#
#           sendjson send data ... {'get': 1447468389} 
#
# collect1 get monitor data {'get': 1447468392} 
#
# collect2 get monitor data {'get': 1447468392} 
#
# collect3 get monitor data {'get': 1447468392} 
#
#           sendjson send data ... {'get': 1447468392} 
#
# collect0 get monitor data {'get': 1447468392} 
#
#           sendjson send data ... {'get': 1447468395} 
#
# collect4 get monitor data {'get': 1447468392} 
#
#           sendjson send data ... {'get': 1447468392} 
#
# collect2 get monitor data {'get': 1447468395} 
#
#           sendjson send data ... {'get': 1447468401} 
#
# collect3 get monitor data {'get': 1447468395} 
#
#           sendjson send data ... {'get': 1447468395} 
#
# collect1 get monitor data {'get': 1447468395} 
#
#           sendjson send data ... {'get': 1447468407} 
#
# collect0 get monitor data {'get': 1447468401} 
#
#           sendjson send data ... {'get': 1447468413} 
#
# collect4 get monitor data {'get': 1447468404} 
#
#           sendjson send data ... {'get': 1447468404} 
#
# collect2 get monitor data {'get': 1447468407} 
#
#           sendjson send data ... {'get': 1447468416} 
#
# collect3 get monitor data {'get': 1447468413} 
#
#           sendjson send data ... {'get': 1447468428} 
#
# collect1 get monitor data {'get': 1447468416} 
#
#           sendjson send data ... {'get': 1447468431} 
#