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

#agent ���������ε�transģ�鷢�Ͳɼ����ļ������,����ǿ����õ�trans ��ַ��list
trans_list01=['localhost:50000']

class porterThread(threading.Thread):
    def __init__(self,name,q,que_lock=None,interval=None):
        """init data """
        threading.Thread.__init__(self)
        self.name=name 
        self.q=q 
        self.interval=interval
        self.sock_l=[None]
    
    def run(self):
        """name to function 
        collect local monotor data and put data in queue.
        sendjson get data from queque and send to trans by socket.
        """
        if self.name=='collect':
            self.put_data()
        else self.name=='sendjson':
            self.get_data()
    
    def put_data(self):
        """ main function of collect data"""
        m=mon()
        atime=int(time.time())
        while 1 :
            data=m.runAllGet()
            self.q.put(data)
            #����ʱ������Ƶ������
            btime=int(time.time())
            time.sleep(self.interval-( (btime-atime)%self.interval ))
    
    
    def get_data(self):
        while 1:
            print "get"
            if not self.q.empty():
                data=self.q.get()
                print data 
                #debug 
                #pdb.set_trace()
                
                #send monitor data 
                #sendData_mh()
            time.sleep(self.interval)
    
    def startTh(self):
        #init 10 queue ,����10������û�б�����,put����������
        que=Queue.Queue(10)
        que_lock=threading.lock()
        collect=porterThread('collect',que,que_lock,interval=3)
        #start collected thread 
        collect.start()
        
        time.sleep(0.5)
        sendjson=porterThread('sendjson',que,que_lock,interval=3)
        #start send data
        sendjson.start()
        
        collect.join()
        sendjson.join()


if __name__="__main__":
    startTh()



